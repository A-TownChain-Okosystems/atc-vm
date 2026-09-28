#!/usr/bin/env python3
"""Fail closed when repository evidence is not bound to the assessed source commit."""
from __future__ import annotations
import os, re, subprocess, sys
from pathlib import Path
EVIDENCE = Path(".atc/evidence/evidence.yaml")
def git_sha():
    value = os.environ.get("EXPECTED_COMMIT") or os.environ.get("GITHUB_SHA")
    return value or subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
def main():
    if not EVIDENCE.is_file():
        print("EVIDENCE_BINDING_FAIL: evidence file is missing", file=sys.stderr); return 1
    text = EVIDENCE.read_text(encoding="utf-8")
    expected = git_sha()
    bound = re.search(r"(?m)^bound_commit:\s*([^\s#]+)", text)
    if not bound: print("EVIDENCE_BINDING_FAIL: bound_commit is missing", file=sys.stderr); return 1
    bound = bound.group(1)
    test_commit = re.search(r"(?m)^\s+commit:\s*([^\s#]+)", text)
    result = re.search(r"(?m)^\s+result:\s*([^\s#]+)", text)
    if bound != expected:
        print(f"EVIDENCE_STALE: bound_commit={bound} assessed_commit={expected}", file=sys.stderr); return 1
    if test_commit and test_commit.group(1) != expected:
        print(f"EVIDENCE_STALE: test_run.commit={test_commit.group(1)} assessed_commit={expected}", file=sys.stderr); return 1
    if result and result.group(1) != "PASS":
        print(f"EVIDENCE_NOT_PASS: test_run.result={result.group(1)}", file=sys.stderr); return 1
    print(f"EVIDENCE_BINDING_OK: {expected}"); return 0
if __name__ == "__main__": raise SystemExit(main())
