# Workshop Agent Instructions

## Scope

This repository is a synthetic teaching environment for statistical programmers and data scientists.

## Rules

- Never add real patient, clinical-trial, customer, or proprietary data.
- Never place secrets or sensitive data in prompts, logs, generated files, or review comments.
- The advanced lab uses VS Code Copilot Agent mode in an approved local work repository; local execution is not offline and context may be sent to cloud AI services.
- Read the task and propose a bounded plan before editing. Implement only after the human approves the plan.
- Do not create branches, commit, push, open pull requests, or merge. The human owns these actions and tool/terminal approvals.
- Do not install dependencies, enable tools, change permissions, or use external services without explicit human approval under organization rules.
- Keep changes limited to the files named in the issue.
- Preserve the output columns and ordering unless the issue explicitly requests otherwise.
- Treat `reference/controlled-terminology.md` as the source of truth for severity values.
- Update the requirement, implementation, expected-output documentation, and tests together when behavior changes.
- Do not claim that passing automated tests constitutes scientific validation.
- Surface assumptions and unresolved questions in the pull-request description.

## Validation

Run:

```bash
python scripts/validate.py
```

Use the available Python 3.10+ command (`python3` or `py -3` where appropriate). This runs Python tests only; report that SAS/R runtime behavior and scientific validation remain human responsibilities.

## Pull-request expectations

Every pull request should explain:

1. What requirement changed.
2. Which files changed and why.
3. What checks were run.
4. What still requires human verification.

Copilot pull-request review is optional where enabled, with human review as the fallback. Human scientific, security, and test-evidence review and required repository gates must never be bypassed.
