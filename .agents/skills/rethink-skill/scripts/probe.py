#!/usr/bin/env python3
"""Run scripted multi-turn conversations on Claude Code and Codex through normal skill discovery.

Scenarios file: one scenario per line, tab-separated: name, turn 1, turn 2, ...
Lines starting with # are ignored. If --fixtures has a subdirectory named after a
scenario, it is copied as that conversation's working directory; otherwise the
directory starts empty.

Writes <out>/<label>/<scenario>-<harness>.md (clean transcript for judges) plus raw
per-turn logs and a summary.json recording which skills each turn loaded.

Run the baseline first, edit the canonical skill, then run the candidate with a new label.
"""
import argparse, json, re, shutil, subprocess, sys, uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SKILL_READ = re.compile(r"skills/([^/\s'\"]+)/SKILL\.md")


def read_scenarios(path):
    scenarios = []
    for line in Path(path).read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        name, *turns = line.split("\t")
        turns = [t.strip() for t in turns if t.strip()]
        if not turns:
            sys.exit(f"scenario {name!r} has no turns")
        scenarios.append((name.strip(), turns))
    return scenarios


def run(cmd, cwd, log):
    with open(log, "w") as f:
        subprocess.run(cmd, cwd=cwd, stdin=subprocess.DEVNULL, stdout=f, stderr=subprocess.STDOUT)
    return [json.loads(l) for l in Path(log).read_text().splitlines() if l.startswith("{")]


def claude_turn(state, prompt, cwd, log, args):
    if "id" not in state:
        state["id"] = str(uuid.uuid4())
        session = ["--session-id", state["id"]]
    else:
        session = ["--resume", state["id"]]
    cmd = ["claude", "-p", prompt, *session, "--output-format", "stream-json", "--verbose",
           "--permission-mode", "bypassPermissions"]
    if args.claude_model:
        cmd += ["--model", args.claude_model]
    events = run(cmd, cwd, log)
    reply = next((e.get("result", "") for e in events if e.get("type") == "result"), "")
    skills = [c["input"].get("skill") for e in events if e.get("type") == "assistant"
              for c in e.get("message", {}).get("content", [])
              if c.get("type") == "tool_use" and c.get("name") == "Skill"]
    return reply, skills


def codex_turn(state, prompt, cwd, log, args):
    opts = ["-m", args.codex_model, "--skip-git-repo-check", "--json"]
    if args.codex_effort:
        opts += ["-c", f"model_reasoning_effort={args.codex_effort}"]
    if "id" not in state:
        cmd = ["codex", "exec", *opts, "-C", str(cwd), "-s", "workspace-write", prompt]
    else:
        cmd = ["codex", "exec", "resume", state["id"], *opts, prompt]
    events = run(cmd, cwd, log)
    state.setdefault("id", next((e["thread_id"] for e in events if "thread_id" in e), None))
    if not state["id"]:
        raise RuntimeError(f"codex returned no thread id; see {log}")
    items = [e["item"] for e in events if e.get("type") == "item.completed"]
    # Codex may split one reply into several agent_message items; keep them all.
    reply = "\n\n".join(i["text"] for i in items if i.get("type") == "agent_message")
    skills = sorted({m for i in items if i.get("type") == "command_execution"
                     for m in SKILL_READ.findall(i.get("command", ""))})
    return reply, skills


def conversation(name, turns, harness, args, out):
    cwd = out / "work" / f"{name}-{harness}"
    shutil.rmtree(cwd, ignore_errors=True)
    fixture = Path(args.fixtures) / name if args.fixtures else None
    if fixture and fixture.is_dir():
        shutil.copytree(fixture, cwd)
    else:
        cwd.mkdir(parents=True)
    turn_fn = claude_turn if harness == "claude" else codex_turn
    state, transcript, meta = {}, [], []
    for i, prompt in enumerate(turns, 1):
        try:
            reply, skills = turn_fn(state, prompt, cwd, out / "logs" / f"{name}-{harness}.t{i}.jsonl", args)
        except RuntimeError as e:
            meta.append({"turn": i, "skills": [], "reply_words": 0, "empty": True, "error": str(e)})
            break
        transcript.append(f"## User\n\n{prompt}\n\n## Assistant\n\n{reply or '[NO REPLY]'}\n")
        meta.append({"turn": i, "skills": skills, "reply_words": len(reply.split()), "empty": not reply})
    (out / f"{name}-{harness}.md").write_text("\n".join(transcript))
    return f"{name}-{harness}", meta


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("scenarios")
    p.add_argument("--label", required=True, help="condition name, e.g. baseline or candidate")
    p.add_argument("--out", required=True, help="results root; transcripts go to <out>/<label>/")
    p.add_argument("--fixtures", help="directory with one fixture subdirectory per scenario")
    p.add_argument("--harness", default="claude,codex")
    p.add_argument("--codex-model", help="required when running codex")
    p.add_argument("--codex-effort")
    p.add_argument("--claude-model", help="defaults to the harness default")
    args = p.parse_args()

    harnesses = args.harness.split(",")
    if "codex" in harnesses and not args.codex_model:
        sys.exit("--codex-model is required for codex")
    out = Path(args.out).resolve() / args.label
    (out / "logs").mkdir(parents=True, exist_ok=True)
    jobs = [(n, t, h) for n, t in read_scenarios(args.scenarios) for h in harnesses]
    with ThreadPoolExecutor(max_workers=len(jobs)) as pool:
        results = dict(pool.map(lambda j: conversation(*j, args, out), jobs))
    (out / "summary.json").write_text(json.dumps(results, indent=2))

    failed = False
    for key, meta in sorted(results.items()):
        turns = ", ".join(f"t{m['turn']}: {m['reply_words']}w {'+'.join(m['skills']) or '-'}" for m in meta)
        print(f"{key}: {turns}")
        failed |= any(m["empty"] for m in meta)
    if failed:
        sys.exit("some turns produced no reply; check the logs")


if __name__ == "__main__":
    main()
