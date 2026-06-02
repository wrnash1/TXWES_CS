# Discussion Forum: Module 02 - Version Control with Git and GitHub

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Overview

This discussion applies Module 02 concepts — Git security fundamentals, branch protection rules, pre-commit hooks, and GitHub Actions workflow design — to real-world team scenarios. Read all three scenarios and respond to the one assigned to your group or the one of your choice. Initial post due Wednesday at 11:59 PM; peer responses due Sunday at 11:59 PM.

---

## Scenario A: The Bypassed Hook

A fintech startup has configured a pre-commit hook that runs Gitleaks secrets detection on every developer's machine. During a routine CI log review, a developer discovers that three AWS access keys were pushed to a feature branch last week. Investigation reveals the developer who pushed them used `git commit --no-verify` to skip the hook because it was "taking too long." The keys were active and have been in the repository for 7 days.

In 175-225 words, address the following: Identify the two immediate remediation actions that must occur in the correct order and explain why the order matters. Then explain the systemic gap that allowed this situation to occur — specifically, what server-side control is missing and where in the pipeline it should be placed. Finally, propose one change to the pre-commit hook configuration that might reduce the developer's motivation to bypass it, while maintaining equivalent security. Use precise DevSecOps terminology in your response.

---

## Scenario B: The Unprotected Main Branch

A cloud services company has three developers committing directly to the main branch of their production infrastructure repository. There is no CI pipeline and no branch protection. A new DevSecOps engineer joins the team and identifies this as a critical risk. The lead developer argues that branch protection will slow down hotfixes and that "we all know what we're doing."

In 175-225 words, address the following: Explain the specific security risks of allowing direct pushes to main in an infrastructure repository — name at least two distinct risk scenarios. Then describe the branch protection settings you would recommend and explain how they can be configured to allow expedited hotfix processes without eliminating the security gate entirely. Address the lead developer's velocity concern directly using evidence from the DevSecOps feedback loop model. Use precise DevSecOps terminology in your response.

---

## Scenario C: The Overprivileged Workflow

A development team inherits a GitHub Actions workflow from a contractor. The workflow builds and deploys a containerized application. Reviewing the YAML, the new team lead notices the workflow has no `permissions:` block and uses a hardcoded personal access token (stored in plaintext in the YAML file) with organization-wide repository write access. The token belongs to a former contractor who has since left the company.

In 175-225 words, address the following: Identify all security violations present in this workflow and explain the risk each creates. Describe the correct remediation for each violation using GitHub Actions security best practices. Explain what the `permissions:` block should contain for a build-and-deploy workflow and why the default (no permissions block) is considered insecure in GitHub Actions. Use precise DevSecOps terminology in your response.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

Due Wednesday at 11:59 PM. Your post must be 175-225 words, address all elements of your chosen scenario, and use precise DevSecOps terminology.

- 5-6 pts: Thoroughly addresses all scenario elements with technical accuracy, clear explanations, and appropriate terminology. Meets the word count.
- 3-4 pts: Addresses most scenario elements but lacks technical depth or precise terminology in one or more areas.
- 0-2 pts: Incomplete, missing, or does not substantively address the scenario.

### Peer Responses (4 Points)

Due Sunday at 11:59 PM. Respond to at least two classmates who chose different scenarios from yours.

- 4 pts: Two substantive responses (at least 50 words each) that add technical content, offer an alternative approach, or connect the scenario to the reading guide or lab.
- 2 pts: Only one substantive peer response, or both responses are superficial.
- 0 pts: No peer responses submitted.

---

## Professor Nash Note

When discussing remediation, always specify the correct order of operations. For secrets exposure, many students correctly identify "remove from repository" but place it before "rotate the credential" — that ordering is wrong and leaves systems exposed during the window between removal and rotation. Precision in remediation sequencing is a tested skill on the DevSecOps Professional exam.
