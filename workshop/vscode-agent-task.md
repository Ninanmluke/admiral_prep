# Workshop change request: include life-threatening events

Use this task as issue context and as a prompt attachment for **local VS Code Copilot Agent mode** in an approved writable work repository. The private [owned reference](https://github.com/johnsont1693/scientific-workflow-workshop) requires authorized read access and is read-only for learners. Do not assign the issue to a cloud coding agent.

## Objective

Update the adverse-event summary so it includes records classified as either `SEVERE` or `LIFE THREATENING`.

## Relevant repository context

- `requirements/analysis-requirements.md`
- `reference/controlled-terminology.md`
- `analysis/ae_summary.py`
- `analysis/ae_summary.R`
- `analysis/ae_summary.sas`
- `checks/expected-output.md`
- `tests/test_ae_summary.py`

## Constraints

- Use only the synthetic repository data.
- Do not include secrets or real patient/customer data in prompts, files, logs, or output. Local execution can still send AI context to cloud services; use approved models and tools only.
- Propose a plan before editing and wait for human approval.
- Leave changes local and uncommitted. Humans create branches, commit, push, open pull requests, and merge; do not perform these actions or change permissions.
- Preserve the existing output columns and their order.
- Keep the change limited to this requirement.
- Do not treat automated tests as scientific validation.
- Surface assumptions and unresolved questions in the pull request.

## Acceptance criteria

- The requirement includes both severity values.
- All three analysis examples implement the same filter.
- Expected output lists four records: subjects `003`, `004`, `006`, and `007`.
- Automated tests expect four records and both severity values.
- `python scripts/validate.py` passes using Python 3.10+ (`python3` or `py -3` where appropriate), and the actual command/result is recorded.
- A human reviews the diff for secrets, sensitive content, and out-of-scope changes before publishing.
- The pull request explains what still requires human review.

## Review focus

- Exact controlled terminology
- Output-column stability
- Expected record count
- Consistency across SAS, R, Python, requirements, checks, and tests
- Requirement identifiers in file headers and docstrings
- Python tests do not execute SAS/R or constitute scientific validation
- Copilot pull-request review where enabled, with human review as the fallback; human scientific, security, and test-evidence review is always required
