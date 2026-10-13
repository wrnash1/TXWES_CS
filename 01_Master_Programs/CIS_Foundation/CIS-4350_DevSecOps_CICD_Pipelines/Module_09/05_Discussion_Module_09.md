# Discussion Forum: Module 09 - Secrets Management: HashiCorp Vault and AWS Secrets Manager

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Overview

This discussion applies Module 09 concepts — secrets failure modes, Gitleaks, HashiCorp Vault, AWS Secrets Manager, OIDC federation, dynamic secrets, and Docker layer persistence — to realistic operational scenarios. Read all three scenarios and respond to the one assigned to your group or the one of your choice. Initial post due Wednesday at 11:59 PM; peer responses due Sunday at 11:59 PM.

---

## Scenario A: The Exposed API Key Incident

A security researcher emails a startup's security team: "I found your Stripe API production key in your public GitHub repository. The key appears to have been committed six months ago and removed three commits later. The key is still visible in the commit at SHA `a7c3d9f`." The development team lead responds: "We removed it immediately after we noticed, so it should be fine. Besides, we use GitHub Secrets now."

In 175-225 words, address the following: Explain precisely why the development team lead's assessment is incorrect — what exactly makes a secret committed to Git history permanently exposed even after removal. Describe the correct remediation steps in the correct order, explaining why the order matters (hint: rotation vs. history removal have different urgency levels). Explain what the migration to GitHub Secrets addresses going forward and what it does not address retroactively. Finally, describe what monitoring capability should have alerted the team to this exposure before the researcher found it, and how it would have worked in this specific case.

---

## Scenario B: The CI/CD Pipeline Credential Design Decision

A DevSecOps team is building a new deployment pipeline for a microservices platform with 12 services, each connecting to its own PostgreSQL database. They are evaluating three options for managing database credentials:

Option 1: Store credentials in GitHub Secrets, one secret per service per environment.

Option 2: Store credentials in HashiCorp Vault KV store, retrieved via AppRole in the pipeline.

Option 3: Use HashiCorp Vault's database secret engine to generate dynamic credentials per deployment.

In 175-225 words, address the following: Compare all three options across at least three security dimensions (audit trail, rotation, blast radius on compromise, or another relevant dimension you identify). Recommend one option and justify the recommendation. Then address the operational objection: "Option 3 requires standing up and maintaining Vault infrastructure, which adds operational complexity. GitHub Secrets is already included in our GitHub plan." Explain what specific security risks the team is accepting by choosing Option 1 over Option 3.

---

## Scenario C: The Docker Build Secret Leak

A junior DevSecOps engineer is reviewing a container image scan report for their organization's Python microservice. The Trivy scan shows the image is clean — no CVEs, no exposed files with secrets. However, a senior engineer reviewing the Dockerfile raises a concern about a build argument used to authenticate to a private package registry. The junior engineer responds: "The credentials aren't in any file in the final image — Trivy would have found them if they were."

In 175-225 words, address the following: Explain precisely why the senior engineer's concern is valid despite the clean Trivy file scan — specifically, what does Docker store in image layer metadata and how is it accessible. Describe the specific Docker command an attacker would use to recover the credential from the image. Provide the solution using BuildKit's `--mount=type=secret` and explain at the technical level why this approach does not persist the secret in any layer. Finally, explain whether a container registry that stores the image publicly (such as Docker Hub) would expose the secret to anyone who can pull the image, and what the remediation would be if the image were already pushed.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

Due Wednesday at 11:59 PM. Your post must be 175-225 words, address all elements of your chosen scenario, and use precise secrets management and DevSecOps terminology.

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

Scenario B asks you to compare three concrete options and make a recommendation. A strong response does not just say "Option 3 is most secure" — it explains the specific mechanism by which Option 3 is more secure than Option 2, and Option 2 is more secure than Option 1, using terms like audit log, lease duration, blast radius, and rotation. When addressing the operational complexity objection, be precise: what exactly is the team accepting in terms of risk, and is that a reasonable tradeoff? The ability to articulate a security tradeoff — not just declare one option correct — is what the exam and real-world architecture decisions both require.
