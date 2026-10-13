# Discussion Forum: Module 08 - SCA: Software Composition Analysis and Dependency Scanning

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Overview

This discussion applies Module 08 concepts — SCA mechanics, transitive dependencies, SBOM, reachability analysis, `snyk test` vs. `snyk monitor`, and OWASP Dependency-Check — to realistic operational scenarios. Read all three scenarios and respond to the one assigned to your group or the one of your choice. Initial post due Wednesday at 11:59 PM; peer responses due Sunday at 11:59 PM.

---

## Scenario A: The Quarterly Review Gap

A mid-size financial services company manages a Python microservices platform with 14 services. Their security policy states that dependency reviews occur quarterly. A DevSecOps engineer proposes integrating `snyk test --severity-threshold=high` into the GitHub Actions pipeline so every PR triggers an SCA scan. The engineering director pushes back: "We already do quarterly reviews. Running Snyk on every PR will just slow the team down and fail builds for issues we already know about."

In 175-225 words, address the following: Identify two specific security weaknesses of the quarterly manual review approach compared to automated SCA in CI/CD. Then explain what happens in the window between quarterly reviews — use the Log4Shell timeline (CVE published December 9, 2021) as a concrete example to illustrate the risk. Finally, explain how adding `snyk monitor` to the pipeline alongside `snyk test` addresses a gap that `snyk test` alone cannot close, and respond to the director's velocity concern by proposing a configuration that balances security gating with development speed.

---

## Scenario B: The Transitive Dependency Incident

A Node.js e-commerce platform receives a security advisory from a vendor: a CRITICAL CVE (CVSS 9.8) has been found in `minimist`, a small argument-parsing utility. The development team reviews their `package.json` and confirms they do not directly import `minimist`. The team lead declares: "This doesn't affect us — we don't use that package." Three hours later, the security team's Snyk scan reports the application is vulnerable. The Snyk output shows the dependency path: `yargs > minimist`.

In 175-225 words, address the following: Explain precisely what a transitive dependency is, using this `yargs > minimist` path as your example. Explain why the team lead's declaration ("we don't use that package") was technically incorrect and what the correct triage question should be. Describe how Snyk's dependency path output enables faster triage compared to a manual review of `package.json` alone. Finally, explain what remediation options exist when a CVE is in a transitive dependency — specifically whether you can fix it without changing your direct dependency declaration, and under what circumstances a developer might need to override the transitive version using npm's `overrides` or `resolutions` field.

---

## Scenario C: The SBOM Compliance Request

A healthcare software company is responding to a federal procurement requirement that mandates a CycloneDX SBOM for any software delivered to a government agency. The engineering team has never generated an SBOM before. A developer asks: "Can't we just send them our `requirements.txt`?" The compliance officer responds: "No — `requirements.txt` is not an SBOM."

In 175-225 words, address the following: Explain precisely why `requirements.txt` is not an SBOM — what information does `requirements.txt` contain versus what a CycloneDX SBOM contains. Describe two specific ways an SBOM provides compliance value that a dependency manifest alone cannot. Provide the exact Snyk CLI command to generate a CycloneDX SBOM for a Python project (be precise about the flag and format argument). Finally, explain what reachability analysis is and discuss whether a CVE found in a transitive dependency that is unreachable in the application changes the urgency of remediation — and what documentation should be produced if the team defers the fix based on reachability.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

Due Wednesday at 11:59 PM. Your post must be 175-225 words, address all elements of your chosen scenario, and use precise SCA and DevSecOps terminology.

- 5-6 pts: Thoroughly addresses all scenario elements with technical accuracy, clear explanations, and appropriate terminology. Meets the word count.
- 3-4 pts: Addresses most elements but lacks technical depth in one or more areas.
- 0-2 pts: Incomplete, missing, or does not substantively address the scenario.

### Peer Responses (4 Points)

Due Sunday at 11:59 PM. Respond to at least two classmates who chose different scenarios.

- 4 pts: Two substantive responses (at least 50 words each) that add technical depth, propose an alternative approach, or cite a specific reading guide concept.
- 2 pts: Only one substantive response, or both are superficial.
- 0 pts: No peer responses submitted.

---

## Professor Nash Note

Scenario B describes a real class of incident that occurs frequently in production environments. When responding to Scenario B, do not simply say "use SCA tooling" — explain the specific mechanism by which a developer can be unaware of a transitive dependency. Be precise about what the dependency path output tells you and what it does not tell you. Knowing that `yargs > minimist` is the path tells you how the dependency was introduced; it does not tell you whether the vulnerable code path in `minimist` is reachable through the way `yargs` is used in this application. Connecting SCA findings to reachability is the triage skill the exam and real-world DevSecOps practice both require.
