Contact: Thomas Johnson thjohnson@microsoft.com



# Scientific workflow GitHub workshop

This synthetic repository supports two workshops:

1. **GitHub Foundations for Scientific Work**
2. **GitHub Copilot for Data Scientists — VS Code Agent mode**

The example follows a small adverse-event summary through requirements, code, tests, and human-controlled pull requests. Foundations uses GitHub.com; the advanced lab uses GitHub Copilot **Agent mode in VS Code** to plan and edit a local checkout. Copilot pull-request code review is optional where enabled, with human review always required.

This is an independent teaching repository. It is not affiliated with, sponsored by, or approved by any company, research sponsor, healthcare organization, or regulatory body.

## Choose how to use the workshop

The owned reference is [johnsont1693/scientific-workflow-workshop](https://github.com/johnsont1693/scientific-workflow-workshop). It is a **private, read-only reference for learners**: authorized read access is required to view or clone it. Read access does not grant permission to push, create issues, or open exercise pull requests there.

For both labs, use a separate **writable, organization-approved work repository** supplied by your facilitator or administrator:

- Use your organization-approved GitHub identity and the access granted for that work repository.
- For Enterprise Managed Users, an authorized administrator or facilitator stages an internal copy in the approved organization. Do not rely on access to the external reference.
- Do not bypass organization controls using personal accounts, public forks, or unapproved services.
- If repository access or tools are unavailable, pair with an enabled participant or observe an approved demonstration.
- GitHub handles are needed only to provision access to approved work repositories; do not publish attendee rosters in this repository.

## Advanced lab prerequisites

- Organization-approved GitHub identity, Copilot entitlement, and permission to use VS Code Agent mode with an approved model.
- VS Code with GitHub Copilot available, Git, and Python 3.10 or newer installed through approved channels. No third-party Python packages are required.
- An approved local workspace and authenticated read/write access to the work repository, including branches, issues, and pull requests.
- Copilot pull-request code review and GitHub Actions where enabled; human review and local test evidence are the fallback when those services are unavailable.

Local Agent mode executes tools and edits files in the local workspace, but prompts and repository context can still be sent to cloud AI services. **This is not an offline workflow.** Follow organization rules for context sharing, models, extensions, and tool approvals. Cloud coding agent access is not required.

## Important

- All data is synthetic.
- Do not add patient or real customer data, credentials, secrets, proprietary study data, or regulated content to files, prompts, logs, screenshots, or issues.
- Workshop changes are proposals for learning purposes. They are not validated clinical-analysis outputs.
- Humans create branches, commit, push, open pull requests, and decide on review and merge. Copilot may propose local edits and review comments, not perform publication.
- Human diff, security, scientific, and test-evidence review remain required regardless of Copilot suggestions or passing checks.
- Do not add customer names, event names, company logos, internal links, or other identifying information.

## Repository map

| Path | Purpose |
|---|---|
| `requirements/` | The expected analytical behavior |
| `analysis/` | Equivalent SAS, R, and Python examples |
| `data/` | Synthetic input data |
| `reference/` | Controlled terminology used by the exercise |
| `checks/` | Human-readable expected output |
| `tests/` | Automated checks for the Python example |
| `workshop/` | Participant and facilitator instructions |

## Current baseline

Requirement `AE-3` includes only events classified as `SEVERE`. The advanced workshop introduces a change request to include `LIFE THREATENING` events as well.

## Validate the repository

Foundations can remain browser-based. The advanced hands-on lab requires local execution. From the work repository root, run:

```bash
python scripts/validate.py
```

Use `python3` on systems where that is the Python 3 command, or `py -3` on Windows when appropriate. Verify the interpreter is Python 3.10+. GitHub Actions also runs validation on pull requests when enabled; if Actions is unavailable, record local results and the limitation in the pull request. These tests execute Python only; SAS/R consistency and scientific validity require human review and any approved runtime checks.

## Workshop paths

- [Foundations browser lab](workshop/01-foundations-browser-lab.md)
- [VS Code Copilot Agent mode and pull-request review lab](workshop/02-copilot-vscode-agent-lab.md)
- [Task and exact repository context to attach](workshop/vscode-agent-task.md)
- [Review checklist](workshop/review-checklist.md)
- [Facilitator guide](workshop/facilitator-guide.md)

## Attribution

Adapted from the public upstream [abrown152/scientific-workflow-workshop](https://github.com/abrown152/scientific-workflow-workshop). No upstream license was detected; this attribution does not grant a license or establish redistribution rights. Confirm permission before distributing copies beyond authorized use.

I edited this file.

