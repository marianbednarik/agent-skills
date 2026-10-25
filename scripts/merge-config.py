"""Merge shared harness settings into a runtime config file.

    python3 merge-config.py <shared> <target>

Both files are JSON or both TOML, by extension. Keys from <shared> win and are
merged into nested tables, so keys the harness writes itself stay. The target
is rewritten only when something changes; TOML comments are not preserved.
"""
import json, os, re, sys

shared_path, target = sys.argv[1:]
toml = shared_path.endswith(".toml")

def load(path):
    if toml:
        import tomllib
        with open(path, "rb") as f:
            return tomllib.load(f)
    with open(path) as f:
        return json.load(f)

def merge(base, extra):
    out = dict(base)
    for k, v in extra.items():
        out[k] = merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out

def toml_key(k):
    return k if re.fullmatch(r"[A-Za-z0-9_-]+", k) else json.dumps(k)

def toml_value(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float, str)):
        return json.dumps(v)
    if isinstance(v, list) and not any(isinstance(x, dict) for x in v):
        return "[" + ", ".join(toml_value(x) for x in v) + "]"
    raise TypeError(f"unsupported TOML value: {v!r}")

def dump_toml(table, path=()):
    lines = [f"{toml_key(k)} = {toml_value(v)}" for k, v in table.items() if not isinstance(v, dict)]
    if path and lines:
        lines.insert(0, "[" + ".".join(map(toml_key, path)) + "]")
    out = "\n".join(lines) + "\n" if lines else ""
    for k, v in table.items():
        if isinstance(v, dict):
            sub = dump_toml(v, path + (k,))
            out += ("\n" if out and sub else "") + sub
    return out

try:
    shared = load(shared_path)
    try:
        current = load(target)
    except FileNotFoundError:
        current = {}
    merged = merge(current, shared)
    text = dump_toml(merged) if toml else json.dumps(merged, indent=2) + "\n"
except Exception as e:  # missing tomllib (Python < 3.11), invalid file, unsupported value
    sys.exit(f"  skipped  {target} ({e})")

if merged == current:
    print(f"  ok       {target}")
else:
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target + ".tmp", "w", newline="\n") as f:
        f.write(text)
    os.replace(target + ".tmp", target)
    print(f"  merged   {target}")
