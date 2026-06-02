# Discussion Forum: Module 03 - CI/CD Concepts: Jenkins, GitHub Actions, GitLab CI

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Overview

This discussion applies Module 03 concepts — multi-stage pipeline design, security gate placement, credential handling, and platform-specific security configurations — to realistic engineering scenarios. Read all three scenarios and respond to the one assigned to your group or the one of your choice. Initial post due Wednesday at 11:59 PM; peer responses due Sunday at 11:59 PM.

---

## Scenario A: The Missing Security Gate

An e-commerce company has a Jenkins pipeline with three stages: Build, Test, and Deploy. The pipeline has been running in production for two years. The security team recently discovers that the production application contains a dependency with a critical CVE that has been publicly known for eight months. Investigation shows there is no SCA or dependency scanning stage in the pipeline. The deployment pipeline simply builds, tests, and deploys without any security gate.

In 175-225 words, address the following: Identify specifically which pipeline stage should have caught this vulnerability and explain where in the Jenkins Declarative pipeline it should be positioned relative to Deploy. Using the `parallel {}` block concept from Module 03, describe how you would add dependency scanning alongside two other security checks without increasing pipeline duration beyond what a sequential scan would require. Finally, explain what `post { failure {} }` action you would configure so the security team is notified immediately when the new scan fails.

---

## Scenario B: The Platform Migration Decision

A startup is choosing their CI/CD platform. The CTO wants GitHub Actions because it is "already integrated with our GitHub repository." The lead security engineer advocates for GitLab CI because it "has built-in security scanning templates we can enable with one line." A third developer suggests self-hosted Jenkins because "we own and control every part of the pipeline." The team is building a HIPAA-regulated healthcare application.

In 175-225 words, address the following: Evaluate each platform's security argument from a DevSecOps perspective — what is genuinely strong about each position? Identify which concern (platform integration ease, built-in security scanning, or full infrastructure control) is most critical for a HIPAA-regulated environment and justify your reasoning using DevSecOps principles. Conclude with a recommendation for how the team could achieve the strongest DevSecOps security posture regardless of which platform they choose.

---

## Scenario C: The Supply Chain Incident

A DevSecOps engineer at a financial services firm reviews their GitHub Actions workflows and notices that all third-party actions are pinned to version tags (`@v3`, `@v2`, etc.) rather than commit SHAs. The previous week, a popular GitHub Action used by thousands of organizations was compromised — its maintainer's account was hijacked, and the `@v3` tag was updated to point to a commit that exfiltrated `GITHUB_TOKEN` values during workflow execution.

In 175-225 words, address the following: Explain precisely why pinning to a version tag does not protect against this attack vector, but pinning to a commit SHA does. Describe the remediation steps the engineer should take immediately for all existing workflows. Propose one additional control beyond SHA pinning that would provide defense-in-depth against supply chain attacks in CI/CD pipelines — explain how it works and what class of attack it addresses.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

Due Wednesday at 11:59 PM. Your post must be 175-225 words, address all elements of your chosen scenario, and use precise CI/CD and DevSecOps terminology.

- 5-6 pts: Thoroughly addresses all scenario elements with technical accuracy, clear explanations, and appropriate terminology. Meets the word count.
- 3-4 pts: Addresses most elements but lacks technical depth in one or more areas.
- 0-2 pts: Incomplete, missing, or does not substantively address the scenario.

### Peer Responses (4 Points)

Due Sunday at 11:59 PM. Respond to at least two classmates who chose different scenarios.

- 4 pts: Two substantive responses (at least 50 words each) that add technical depth, propose an alternative approach, or cite a specific concept from the reading guide or lab.
- 2 pts: Only one substantive response, or both are superficial.
- 0 pts: No peer responses submitted.

---

## Professor Nash Note

When comparing CI/CD platforms, avoid treating one as universally superior. The exam — and real-world practice — requires you to evaluate platforms against specific organizational requirements: regulatory environment, team size, existing tooling, and threat model. A strong answer to Scenario B will name specific platform features by their correct technical names, not just describe them generically.
