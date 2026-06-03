# Discussion Forum: Module 04 — Container Security with Docker

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Discussion Overview

Post your original response to one scenario below (minimum 175 words). Then reply substantively to at least two classmates' posts (minimum 75 words each). Original posts due Sunday 11:59 PM; peer replies due Tuesday 11:59 PM.

Professor Nash note: Container security is a domain where developers and security engineers often have genuine disagreements about practical defaults. Distroless vs. slim, root vs. non-root during build, scanning frequency — these are real debates. I am looking for responses that engage with the engineering trade-offs, not just the security ideal.

---

## Scenario 1 — The Production Image Audit

Your team has been running containers in production for eighteen months. An audit reveals that all 47 production container images were built from `ubuntu:latest` and run as root. Image scanning was never configured. The DevOps lead's response is: "The containers are behind a WAF and inside a private VPC — the risk is low." The security team disagrees.

Evaluate the DevOps lead's argument. Is the "defense in depth compensates for container hygiene" argument ever valid? What specific attack scenarios does running as root inside a container enable, even behind a WAF and inside a private VPC? Propose a remediation plan that addresses both the image configuration and the process that allowed this situation to develop over 18 months. Include a prioritization framework — which of the 47 images do you fix first and why? Reference specific Dockerfile and scanning controls from this module, and be honest about the operational cost of the remediation.

### Scenario 1 — Peer Response Prompt

Your classmate proposed a prioritization framework for remediating 47 images. Is their framework sound? What criterion did they miss that you would add?

---

## Scenario 2 — Distroless vs. Developer Productivity

Your security team mandates that all production container images must use `gcr.io/distroless` base images, citing the lack of shell as a critical attack surface reduction. Three development teams push back with the same argument: "Our on-call engineers need to exec into containers to debug production issues. Without a shell, we're flying blind during incidents."

Take a position. Is the security team's mandate reasonable given the stated trade-off? What alternative debugging approaches exist that do not require a shell in the production image — for example, debug containers in Kubernetes, sidecar debugging patterns, or structured logging with distributed tracing? If you were writing the policy, how would you balance the security mandate with legitimate operational needs? Consider whether the "no shell in production" principle should apply equally to all container types or whether there are justified exceptions. Reference at least one specific tool or technique from this module or your own research.

### Scenario 2 — Peer Response Prompt

Your classmate proposed an alternative to shell access for production debugging. Is their proposed alternative realistic for a 2 AM incident with a junior on-call engineer? What is the actual cost of their proposed debugging approach?

---

## Scenario 3 — Container Supply Chain Attack

A popular open-source Docker base image used by hundreds of companies — including yours — is compromised. A malicious contributor gained access to the maintainer's account and pushed a new `latest` tag that includes a cryptocurrency miner and a reverse shell. Your organization pulls base images automatically during CI builds. The compromise was active for 72 hours before the maintainer detected and removed it.

Walk through the incident response. How do you determine whether any of your production images were built using the compromised base image during the 72-hour window? What process evidence would you look for in your CI pipeline logs? After containment, what long-term controls would you implement to prevent this class of supply chain attack in the future? Reference image pinning to digest, Docker Content Trust or cosign, and private registry practices from this module. What is the fundamental tension between "always use the latest patched base image" (for CVE hygiene) and "pin to a specific digest" (for supply chain integrity), and how do you resolve it?

### Scenario 3 — Peer Response Prompt

Your classmate described a long-term control to prevent future supply chain attacks. Does their control address the fundamental tension between patch currency and supply chain integrity? What additional control would you layer on top of theirs?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Original post addresses all parts of the chosen scenario | 3 |
| Specific Dockerfile practices, scanning tools, or registry controls cited | 2 |
| Engineering trade-offs acknowledged realistically | 2 |
| Peer reply 1 — substantive challenge or extension | 1.5 |
| Peer reply 2 — substantive challenge or extension | 1.5 |
| Total | 10 |

---

Discussion — Module 04 | CIS-4350 | Texas Wesleyan University | Professor Nash
