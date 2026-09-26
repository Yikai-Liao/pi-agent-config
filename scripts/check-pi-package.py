"""Check that bundled Pi resources load without contacting a model provider."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent.parent
manifest = json.loads((ROOT / "package.json").read_text())
resources = manifest["pi"]
for kind in ("extensions", "skills"):
    for entry in resources.get(kind, []):
        target = ROOT / entry
        if not target.exists():
            sys.exit(f"Missing Pi {kind} entry: {entry}")

# Use a fresh agent directory: installed personal plugins must not mask a
# missing command in this package. RPC get_commands doesn't call a model.
with tempfile.TemporaryDirectory(prefix="pi-package-check-") as agent_dir:
    env = {**os.environ, "PI_CODING_AGENT_DIR": agent_dir, "PI_OFFLINE": "1"}
    command = [
        "pnpm", "dlx", "@earendil-works/pi-coding-agent@0.87.1",
        "--offline", "--no-session", "--mode", "rpc", "-e", str(ROOT),
    ]
    try:
        result = subprocess.run(
            command,
            input='{"id":"check","type":"get_commands"}\n',
            text=True,
            capture_output=True,
            timeout=90,
            check=False,
            cwd=ROOT,
            env=env,
        )
    except subprocess.TimeoutExpired:
        sys.exit("Pi RPC startup timed out")

if result.returncode:
    sys.exit(f"Pi exited with {result.returncode}:\n{result.stderr}")

responses = []
for line in result.stdout.splitlines():
    try:
        record = json.loads(line)
    except json.JSONDecodeError:
        sys.exit(f"Unexpected Pi RPC output: {line}")
    if record.get("id") == "check":
        responses.append(record)

if len(responses) != 1 or not responses[0].get("success"):
    sys.exit(f"Pi RPC command discovery failed: {responses}; stderr: {result.stderr}")
commands = {item["name"] for item in responses[0]["data"]["commands"]}
if "subagents" not in commands:
    sys.exit("pi-subagents did not register /subagents")
print("Pi resource paths and /subagents registration verified")
