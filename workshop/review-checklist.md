# Human review checklist

## Requirement fit

- Does the proposal implement the stated objective?
- Is every changed file necessary?
- Did unrelated behavior remain unchanged?

## Scientific and terminology review

- Do severity values match the supplied terminology exactly?
- Are assumptions visible?
- What still requires a domain expert?

## Evidence

- Is the local validation command, interpreter, and actual result recorded?
- Does the expected output match the requirement?
- Do automated checks cover the changed behavior?
- Did available CI complete successfully, or is its absence documented without bypassing required gates?
- Are the SAS, R, and Python examples consistent?
- Do requirement identifiers in headers and docstrings match the requirement?
- Is it clear that the Python validator does not execute SAS/R or establish scientific validity?

## Security and publication

- Is this an approved work repository, not the private read-only learner reference?
- Are files, prompts, logs, screenshots, and evidence synthetic-only and free of secrets or sensitive data?
- Were only approved models/tools used, recognizing that local execution may still send context to cloud AI services?
- Did a human approve the plan and tools, inspect the diff, and create the branch, commit, push, and pull request?
- Are required organization review, security, and test gates satisfied or explicitly recorded as blockers?

## Copilot review

- Was Copilot pull-request code review used where enabled, or was the human-review fallback recorded?
- Is each Copilot comment supported by the repository evidence?
- Would applying the suggestion preserve the requirement and constraints?
- Does the comment identify a real defect, a possible risk, or only a preference?

## Decision

- Ready for further validation
- Request changes
- Reject the proposal

Record the reason. Human scientific, security, and test-evidence review is always required. Never treat a passing check or Copilot comment as the final scientific decision. Leave workshop pull requests unmerged unless the facilitator authorizes merging and all required gates are satisfied.
