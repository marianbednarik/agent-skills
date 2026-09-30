#!/usr/bin/env python3
"""Blind pairwise judging of two probe conditions by judges from both model families.

For every transcript present in both condition directories, randomize which condition is
A and which is B, send the rubric plus both transcripts to each judge, and unblind the
verdicts. The rubric lists criteria only; this script appends the required verdict format.

Writes <out>/key.json (the A/B assignment), each judge's full answer, and summary.json.
"""
import argparse, json, random, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

FORMAT = """
For each criterion, write one line naming the better transcript (A, B, or tie) and why.
End with a line "OVERALL: A", "OVERALL: B", or "OVERALL: tie", followed by a two-sentence reason. Be concise.
"""


def ask(judge, prompt, answer_file, args):
    if judge == "claude":
        cmd = ["claude", "-p", prompt, "--output-format", "json"]
        if args.claude_model:
            cmd += ["--model", args.claude_model]
        res = subprocess.run(cmd, stdin=subprocess.DEVNULL, capture_output=True, text=True)
        try:
            text = json.loads(res.stdout)["result"]
        except (json.JSONDecodeError, KeyError):
            text = res.stdout + res.stderr
        answer_file.write_text(text)
    else:
        cmd = ["codex", "exec", *(["-m", args.codex_model] if args.codex_model else []),
               "-c", f"model_reasoning_effort={args.codex_effort}",
               "-s", "read-only", "--skip-git-repo-check", "-o", str(answer_file), prompt]
        subprocess.run(cmd, stdin=subprocess.DEVNULL, capture_output=True)
    text = answer_file.read_text() if answer_file.exists() else ""
    m = re.findall(r"OVERALL:\**\s*\**(A|B|tie)\b", text, re.I)
    return m[-1] if m else None


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("first", help="condition directory, e.g. <out>/baseline")
    p.add_argument("second", help="condition directory, e.g. <out>/candidate")
    p.add_argument("--rubric", required=True, help="file with context and criteria built from the agreed decisions")
    p.add_argument("--out", required=True)
    p.add_argument("--judges", default="claude,codex")
    p.add_argument("--codex-model", help="defaults to the model in the Codex config")
    p.add_argument("--codex-effort", default="high")
    p.add_argument("--claude-model", help="defaults to the harness default")
    args = p.parse_args()

    judges = args.judges.split(",")
    conds = {Path(args.first).name: Path(args.first), Path(args.second).name: Path(args.second)}
    if len(conds) != 2:
        sys.exit("condition directories need different names")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    rubric = Path(args.rubric).read_text().strip()
    names = sorted({f.name for f in Path(args.first).glob("*.md")} & {f.name for f in Path(args.second).glob("*.md")})
    if not names:
        sys.exit("no transcripts present in both directories")

    key, jobs = {}, []
    for name in names:
        order = random.sample(list(conds), 2)
        key[name] = {"A": order[0], "B": order[1]}
        prompt = (f"{rubric}\n{FORMAT}\n===== TRANSCRIPT A =====\n\n{(conds[order[0]] / name).read_text()}"
                  f"\n===== TRANSCRIPT B =====\n\n{(conds[order[1]] / name).read_text()}")
        jobs += [(name, j, prompt) for j in judges]
    (out / "key.json").write_text(json.dumps(key, indent=2))

    def run(job):
        name, judge, prompt = job
        verdict = ask(judge, prompt, out / f"{Path(name).stem}.{judge}.txt", args)
        winner = key[name].get(verdict.upper(), "tie") if verdict else "NO VERDICT"
        return name, judge, winner

    with ThreadPoolExecutor(max_workers=len(jobs)) as pool:
        results = list(pool.map(run, jobs))
    summary = {}
    for name, judge, winner in results:
        summary.setdefault(name, {})[judge] = winner
        print(f"{Path(name).stem:<30} {judge:<7} {winner}")
    (out / "summary.json").write_text(json.dumps(summary, indent=2))
    if any(w == "NO VERDICT" for _, _, w in results):
        sys.exit("some judges gave no parsable verdict; read their answers")


if __name__ == "__main__":
    main()
