# Evidence Binding Contract

The repository evidence record is subordinate to the source commit being assessed.

For a commit S:

- .atc/evidence/evidence.yaml:bound_commit MUST equal S.
- test_run.commit, when present, MUST equal S.
- test_run.result MUST be PASS before CI verification is claimed.

A historical CI run for another commit is not current verification.

The binding gate intentionally fails closed. It does not rewrite evidence, weaken tests, or convert historical evidence into current evidence.

## Current finding

The current main evidence record is bound to an older commit. Until a fresh successful test run produces evidence for the assessed commit, the capability remains EVIDENCE_STALE.

## Remediation

1. Run the relevant test suite on the target source commit.
2. Capture immutable CI evidence with exact commit SHA and run ID.
3. Record the result without changing the tested source.
4. Treat every subsequent source change as a new evidence target.
