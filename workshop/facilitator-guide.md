# Facilitator guide

## Delivery model

Keep Foundations browser-based. Run the advanced workshop in **VS Code Copilot Agent mode on a local checkout**, then use GitHub.com for human-created pull requests and review. Do not require a cloud coding agent, issue assignment to Copilot, or automatic agent-created pull requests.

Local execution is not offline: prompts and repository context can still be sent to cloud AI services. Follow organization requirements for identity, models, extensions, context sharing, and tool approvals.

## Before the event

1. Treat [johnsont1693/scientific-workflow-workshop](https://github.com/johnsont1693/scientific-workflow-workshop) as the **private, read-only learner reference**. Confirm authorized read access before sharing it; do not promise anonymous access or write permission.
2. Have an authorized administrator or facilitator stage separate writable work repositories in an approved organization. For Enterprise Managed Users, stage the copy internally; do not assume attendees can access the external reference. Confirm any required permission to redistribute the upstream material before copying; attribution alone is not a license.
3. Confirm the approved identity and work-repository access for each pair, including branch creation, issues, pushes, and pull requests. Collect GitHub handles only to provision approved work-repository access; keep attendee details out of repository content. Never route blocked attendees through personal accounts or public forks.
4. Verify VS Code with GitHub Copilot, Git, Python 3.10+, approved local workspace access, Copilot entitlement, Agent mode, and an approved model. Use approved installation channels; no Python packages are needed. Confirm a local Agent session works without delegating to a cloud service's coding-agent environment.
5. Check whether Copilot pull-request code review is enabled and available in the work repository. If not, use the human review checklist. This is independent of VS Code Agent mode availability.
6. Have the authorized administrator enable Issues, pull requests, and Actions where permitted. Confirm the existing workflow can run with approved actions/runners; do not relax organization controls. When Actions is unavailable, capture local test evidence and document the limitation without bypassing required gates.
7. Run `python scripts/validate.py` using the available Python 3.10+ command. Confirm the baseline is severe-only with two records. SAS/R runtime checks require separately approved runtimes and are not performed by this validator.
8. Prepare one human-created backup pull request per lab in the approved work repository, along with sanitized screenshots or a short recording. Keep the reference baseline unchanged.
9. Assign an observer or pairing route when permissions, local tools, licensing, Agent mode, an approved model, or network access are unavailable. A prerecorded synthetic demonstration is the contingency, not an offline Copilot promise.

## Foundations reset

Before each delivery:

- close or label participant pull requests from the previous delivery;
- confirm the baseline files on `main` are unchanged;
- keep one prepared pull request available for the review demonstration.

## Copilot reset

Before each delivery:

- confirm `workshop/vscode-agent-task.md` matches the baseline;
- confirm the current tests pass on `main`;
- keep a prepared human-created pull request available in case a local session does not finish;
- confirm Copilot appears in the pull request Reviewers section where enabled, or prepare the human-review fallback;
- verify a human can inspect terminal/tool approvals, review diffs, run tests, and publish without agent-managed Git actions.

## Prepared demonstration patches

`workshop/demo-foundations-change.patch` and `workshop/demo-copilot-change.patch` are existing facilitator fixtures, not changes to apply to the reference baseline. A facilitator may use them on separate approved demo branches, inspecting, testing, committing, pushing, and opening pull requests manually.

The advanced fixture intentionally leaves the R header referring to `AE-3` while the proposed requirement and other headers refer to `AE-4`. Preserve that review defect in the fixture; passing Python tests should not conceal it. Ask participants to compare requirement identifiers and scientific wording across all artifacts. Do not promise that Copilot will find the mismatch; the human checklist must work without AI review.

Do not apply both fixtures cumulatively without reviewing their overlapping expected-output changes. Keep separate clean demo branches and never overwrite participant work.

## Timing guidance

Drive the advanced lab through a visible local plan, human approval, bounded implementation, local diff/security review and tests, then human publication and review. Keep a prepared demonstration available rather than waiting on a blocked session.

Each workshop uses a 90-minute room block, including standards, setup, labs, discussion, and closing feedback. Setup must be provisioned before delivery; use the pairing/observer route instead of consuming lab time on installation or permission changes. Adjust live discussion rather than bypassing a required review step.

| Advanced segment | Minutes |
|---|---:|
| Welcome, outcomes, standards, setup/access | 15 |
| Workflow catch-up and synthetic scenario | 11 |
| Bounded issue and attaching repository context | 12 |
| Agent plan, human checkpoint, implementation and local evidence | 20 |
| Human commit, push, and pull request | 10 |
| Copilot review, triage, and local iteration | 16 |
| Human decision, recap, questions and feedback | 6 |
| Total | 90 |

| Foundations segment | Minutes |
|---|---:|
| Welcome and outcomes | 5 |
| Source-control concepts and tools | 16 |
| Standards and participant access | 10 |
| Repository orientation and commit demonstration | 18 |
| Focused browser edit lab | 12 |
| Branch and pull-request concepts | 12 |
| Partner review lab | 8 |
| Scientific review, recap and feedback | 9 |
| Total | 90 |

The reference validation workflow runs Python tests only. Its action revisions are SHA-pinned and its token is read-only, but it is a teaching example, not an organization-approved deployment pipeline or a complete security-scanning configuration. Obtain the required approval for actions, runners, dependencies, and pipelines before using it in an internal copy. Required static-analysis, secret-scanning, dependency, peer-review, and formal-validation gates are additional controls; a green Python check does not satisfy them.

## Safety language

Use synthetic data only; no secrets or real patient/customer data in prompts, files, logs, recordings, or output. GitHub and Copilot do not replace organizational requirements, validation, security controls, scientific judgment, or formal approvals. Humans own branches, commits, pushes, pull requests, and merge decisions. Review every proposed tool/terminal action; do not enable unrestricted automatic approval.

Leave workshop pull requests unmerged unless explicitly authorized and all required human review, security, and test gates are satisfied. Record unavailable checks and unresolved scientific questions rather than bypassing gates.
