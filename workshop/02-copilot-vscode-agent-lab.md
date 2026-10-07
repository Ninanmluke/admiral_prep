# VS Code Copilot Agent mode and pull-request review lab

## Goal

Use GitHub Copilot Agent mode in VS Code to plan and implement a bounded change in a local checkout. A human reviews and tests the proposal, then commits, pushes, and opens a pull request. Evaluate Copilot pull-request code review where enabled; human review is always required.

## Before starting

Work in pairs, with one driver and one reviewer. Create one issue, one local branch, and one pull request per pair.

- Use an organization-approved GitHub identity with a Copilot entitlement, approved model, and VS Code Agent mode enabled.
- Have VS Code with GitHub Copilot, Git, and Python 3.10+ available through approved installation channels. This lab uses Python's standard library; no package installation is needed. Python validates the runnable example; SAS and R are compared by review unless approved runtimes are available.
- Use the separate writable organization-approved work repository supplied by your facilitator or administrator. Confirm branch, issue, push, and pull-request permissions.
- The [owned reference](https://github.com/johnsont1693/scientific-workflow-workshop) is private, requires authorized read access, and is read-only for learners. It is not your push destination.
- For Enterprise Managed Users, an authorized administrator or facilitator stages an internal copy inside the approved organization. Do not use personal accounts or public forks to bypass controls.
- If access, licensing, Agent mode, an approved model, or local tools are unavailable, pair with an enabled participant or observe the facilitator. Do not change policy settings to unblock the lab.

**Local does not mean offline.** Tool execution and file edits occur in your local workspace, but prompts and repository context can be sent to cloud AI services. Use only synthetic material and approved models, extensions, and tools. Do not include secrets or real patient/customer data in prompts, files, terminal output, or screenshots. Cloud coding agent access is not required.

## Part 1: Prepare the task and local branch

1. Open `workshop/vscode-agent-task.md`.
2. In the approved work repository, create an issue using the **Analysis change** template. This is a human-owned task record; do not assign it to Copilot.
3. Use a pair identifier in the issue title to make the task unique.
4. Transfer the objective, context, constraints, acceptance criteria, and review questions into the issue.
5. Read the issue once as if another person had to execute it. Improve any ambiguous instruction.
6. Clone the facilitator-provided **work repository URL**, not the reference URL, using VS Code **Git: Clone** or local Git. Open that checkout in VS Code. Grant workspace trust only after inspecting the approved copy.
7. In the terminal, confirm the destination and baseline:

   ```bash
   git remote -v
   git status --short
   python --version
   python scripts/validate.py
   ```

   Use `python3` or Windows `py -3` instead if appropriate. Confirm Python 3.10+, a clean working tree, and passing baseline tests. Resolve unexpected changes with the facilitator rather than discarding them.
8. Create the branch **yourself**, using VS Code Source Control or:

   ```bash
   git switch -c copilot/<pair-id>-ae-summary
   ```

   Replace the placeholder with a facilitator-provided unique pair identifier; do not type the angle brackets. GitHub handles are needed only for provisioning approved work repositories, not for completing the exercise or publishing an attendee list.

## Part 2: Plan in VS Code Agent mode

1. Open Copilot Chat in VS Code, select **Agent**, and select an organization-approved model. Use the local workspace session, not a remote/cloud task.
2. In Chat, use **Add Context > Files** (or drag files from Explorer into Chat) to attach `AGENTS.md`, `.github/copilot-instructions.md`, and `workshop/vscode-agent-task.md` from the open working copy. These are repository files, not separate downloads. Ask the agent to read the seven evidence files listed in the task: the requirement, terminology, three implementations, expected output, and tests. Attach those files individually too if the agent cannot find them. Paste only the synthetic issue details if issue access is unavailable; additional integrations are not required.
3. Ask for a plan before edits:

   > Read the attached instructions and bounded change request. Do not edit yet. Identify the requirement, affected files, exact terminology, output contract, tests, and unresolved scientific questions. Propose the smallest plan. Use only this local workspace and approved tools. Do not create branches, commit, push, open a pull request, merge, install dependencies, or change permissions. Wait for my approval before implementation.

4. Inspect the proposed plan:
   - Does it name all affected files?
   - Does it preserve the output structure?
   - Does it include validation?
   - Does it preserve unresolved human-review questions?
5. Refine the instructions if the plan is too broad or misses evidence. Approve only the bounded implementation plan.

## Part 3: Implement, inspect, and test locally

1. Ask Agent mode to implement the approved plan and report the resulting diff, test commands/results, assumptions, and remaining review questions. Remind it to leave all changes uncommitted.
2. Inspect each terminal/tool request before approval. Reject unexpected network access, installations, destructive commands, permission changes, or work outside the approved repository. Do not enable unrestricted automatic approval.
3. Inspect every changed file in VS Code Source Control. Compare the requirement, all three language examples, expected output, and tests; check requirement identifiers in comments and docstrings too.
4. Independently run:

   ```bash
   python scripts/validate.py
   python analysis/ae_summary.py
   git diff --check
   git diff
   git status --short
   ```

5. Compare actual output with the task and `checks/expected-output.md`. Record the Python version, commands, and actual pass/fail results. Passing Python tests does not prove SAS/R runtime correctness or scientific validity.
6. Check for secrets, sensitive data, unrelated files, and unjustified changes. Do not stage generated caches. Resolve failures before proceeding, and preserve unresolved scientific questions for the human reviewer.

## Part 4: Human publication and review

1. **You, not the agent**, stage only the reviewed task files, commit with an intent-focused message, and push your branch to the approved work repository using VS Code Source Control or Git. Verify the remote before pushing. Never push exercise changes to the reference.
2. **You** open the pull request on GitHub.com. Complete its template, link the issue, and include local test evidence and remaining human-review questions.
3. Read the pull-request description before the diff. Compare the changed requirement, code, expected output, and tests again.
4. Check the validation workflow where Actions is enabled. If unavailable, record that limitation and local evidence; never bypass a required CI or security gate.
5. Request **GitHub Copilot code review** from the Reviewers section where enabled. This review is separate from VS Code Agent mode and is not required to run the lab. If unavailable, record the fallback and have a human reviewer use `workshop/review-checklist.md`.
6. Classify each Copilot comment, if any:

   - useful and actionable;
   - plausible but requires human verification;
   - not relevant or incorrect.

7. Apply a fix manually or return to local Agent mode only after agreeing with the comment. Repeat local diff/security review and tests; the human commits and pushes any follow-up.
8. Request a human review summarizing scientific correctness, security, test evidence, and what still requires formal validation. A partner without repository access must not be sent private links or content; use an authorized reviewer instead.

## Success criteria

- The issue is bounded and evidence-rich.
- The local Agent mode plan was inspected before implementation.
- A human approved tools, reviewed the local diff, and recorded validation evidence.
- A human created the branch, commit, push, and pull request in an approved work repository.
- The pull request connects requirement, code, checks, and tests.
- Copilot pull-request code-review comments were evaluated rather than accepted automatically, or the human-review fallback was documented.
- The final decision remains human.

Leave the pull request unmerged unless the facilitator authorizes merging and all required human review, security, and test gates are satisfied. If a required gate is unavailable, leave the proposal open and document the blocker.
