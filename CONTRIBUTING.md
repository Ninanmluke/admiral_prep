# Contributing to the Workshop Repository

## Use an approved work repository

- The [owned reference](https://github.com/johnsont1693/scientific-workflow-workshop) is private and read-only for learners; it requires authorized read access.
- Make exercise changes only in a writable organization-approved work repository provisioned by a facilitator or administrator.
- Use your organization-approved identity. For Enterprise Managed Users, an authorized facilitator or administrator stages an internal organization-owned copy.
- Do not use personal accounts or public forks to bypass access restrictions. Pair or observe when access is unavailable.

Do not add customer names, company names, event names, logos, internal URLs, or proprietary information.

## Human-controlled workflow

1. Start from an issue or workshop instruction.
2. Create a uniquely named branch yourself, using GitHub.com for Foundations or local Git for the advanced lab.
3. Make one focused change. In the advanced lab, use VS Code Copilot Agent mode with an approved model to plan first, then implement only the reviewed plan. Local execution is not offline: prompts and repository context may be sent to cloud AI services.
4. Review the diff and check for secrets and sensitive data. In the advanced lab, run `python scripts/validate.py` (or the available Python 3 command). Foundations participants review available CI or facilitator-provided validation evidence without installing local tools. Humans own terminal/tool approvals; do not enable unrestricted automatic approval.
5. Commit and push yourself using an intent-focused message, then open a pull request and complete the template. Do not ask the agent to create branches, commit, push, open pull requests, or merge.
6. Request GitHub Copilot pull-request code review where enabled; otherwise use the human review checklist and note the fallback.
7. Evaluate every comment before applying a suggestion.
8. Request human review of requirements, scientific assumptions, security, and test evidence. Passing checks or AI comments do not authorize a merge.

For workshop exercises, leave the pull request unmerged unless the facilitator explicitly authorizes merging and all required organization review, security, and test gates are satisfied. If a required service or check is unavailable, record the limitation and do not bypass the gate.

## Branch names

Use a facilitator-provided unique pair identifier to avoid collisions. GitHub handles are needed only to provision approved work-repository access, not to complete the exercise:

```text
foundations/<pair-id>-review-note
copilot/<pair-id>-ae-summary
```

## Commit messages

Prefer:

```text
Document the review evidence for AE-3
Include life-threatening events in the AE summary
```

Avoid:

```text
update
fix
changes
```
