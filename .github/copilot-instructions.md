# Copilot instructions for this repository

- This is a synthetic workshop repository for data scientists and statistical programmers.
- Use only files already present in the repository.
- Never add real patient, customer, clinical-trial, or proprietary data.
- Never include secrets or sensitive data in prompts, logs, screenshots, or output.
- For implementation, use VS Code Copilot Agent mode in an approved local work repository, not a cloud coding agent session. Local execution can still send context to cloud AI services.
- Propose a scoped plan and wait for human approval before implementing.
- Humans own branches, commits, pushes, pull requests, merges, and tool/terminal approvals. Do not perform publication or repository permission changes.
- Do not install dependencies or use additional tools or external services without explicit human approval under organization rules.
- Keep changes focused on the issue and avoid unrelated refactoring.
- Preserve `USUBJID`, `AETERM`, and `AESEV` as the output columns and preserve their order.
- Treat `reference/controlled-terminology.md` as authoritative for this exercise.
- Update requirements, analysis implementations, expected output, and tests together when behavior changes.
- During pull request review, compare requirement identifiers in file headers and docstrings with the current requirement and report any mismatch.
- Run `python scripts/validate.py` with Python 3.10+ (`python3` or `py -3` where appropriate). Report actual results; the tests execute Python only, not SAS or R.
- In the pull-request summary, list assumptions and checks that still require human scientific review.
- Copilot pull-request code review is optional where enabled. Human scientific, security, and test-evidence review is always required; do not bypass required gates.
