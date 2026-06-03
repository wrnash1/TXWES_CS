# Discussion Forum: Module 15 — Emerging AI Technologies

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Overview

This discussion asks you to engage critically with the emerging AI technologies and regulatory frameworks covered in Module 15. You will post an original response to one assigned scenario and provide substantive peer responses to two classmates who chose different scenarios. Strong posts demonstrate command of module terminology, connect emerging technologies to real-world deployment decisions, and engage thoughtfully with peer perspectives.

**Due Dates:**

- Initial post: by end of Day 4 of the module week
- Peer responses: by end of Day 7

**Length Requirements:**

- Initial post: 175–225 words
- Each peer response: 75–100 words

---

## Scenario A — The Autonomous Medical Agent

A large health system is evaluating a proposal to deploy an AI agent that autonomously manages patient appointment scheduling, sends pre-visit preparation instructions, follows up on missed lab results, and — if a lab value falls outside a critical threshold — pages the on-call physician without waiting for a nurse to review the result. The system is built on a commercial LLM-based agent framework and is projected to reduce administrative burden by 40 percent.

Discuss the following in your initial post: Which tasks in this agent's workflow are appropriate for full autonomy, and which require a human-in-the-loop checkpoint? Justify your reasoning using the principles of responsible agentic AI design discussed in this module. How would the EU AI Act's high-risk classification framework apply to this system? What specific failure modes — beyond standard ML errors — does an autonomous agent architecture introduce that a traditional rule-based workflow system would not? Use at least three module vocabulary terms in your response.

---

## Scenario B — Federated Learning for a Competing Hospital Network

Four regional hospital systems — competitors in the same metro area — are approached by a university research team proposing to build a federated learning model for early sepsis detection. Each hospital would keep its patient data on-site, train locally, and share only model updates with a central aggregation server hosted by the university. Hospital legal teams raise concerns: even with federated learning, could a malicious participant reconstruct competitor patient data from shared gradient updates? Could the aggregation server learn which hospital has more sepsis cases, which is commercially sensitive?

Discuss the following in your initial post: What specific privacy risks remain in a standard federated learning deployment that the hospital legal teams are right to be concerned about? What technical mechanisms — covered in this module and Module 14 — could be layered on top of federated learning to address these risks? How would you advise the research team to structure governance and contractual protections for the aggregation server? Use at least three module vocabulary terms in your response.

---

## Scenario C — Edge AI Regulation Gaps

A startup is selling an edge AI device for retail stores that uses computer vision to analyze customer movement patterns, estimate age and gender demographics, and measure time spent in each store section — all processed on-device with no video ever transmitted to the cloud. The startup's marketing materials emphasize that because no data leaves the device, there are no GDPR or CCPA obligations. A privacy advocacy group challenges this claim, arguing that on-device processing of biometric data is still subject to regulation.

Discuss the following in your initial post: Is the startup's legal argument correct that on-device processing eliminates GDPR and CCPA obligations? Why or why not? How does the EU AI Act's definition of high-risk AI systems apply to this device? What responsible AI practices should the startup adopt regardless of the legal minimum requirements? What does this scenario reveal about potential regulatory gaps in current AI law that lawmakers may need to address? Use at least three module vocabulary terms in your response.

---

## Peer Response Guidelines

When responding to a classmate's post, do at least one of the following:

- Extend their argument by introducing a consideration or counterexample they did not address
- Respectfully challenge a factual or analytical claim by citing module content or a real-world parallel
- Connect their scenario to a different scenario from this forum or from Module 14, identifying a shared principle or a meaningful contrast

Peer responses that simply agree or restate the original post without adding substance will receive partial credit only.

---

## Grading Rubric (10 Points Total)

| Criterion | Points |
|---|---|
| Initial post addresses all scenario questions substantively | 3 |
| Accurate and precise use of at least three module vocabulary terms | 2 |
| Critical thinking: analysis evaluates tradeoffs rather than restating module content | 2 |
| Peer response 1: substantive extension, challenge, or connection | 1.5 |
| Peer response 2: substantive extension, challenge, or connection | 1.5 |
| **Total** | **10** |

---

## Sample Strong Initial Post — Scenario B

The hospital legal teams are correct to identify residual privacy risks in a standard **federated learning** deployment. Research on gradient inversion attacks (Zhu et al., 2019) has demonstrated that gradient updates can be reversed to reconstruct training samples with surprisingly high fidelity, particularly for smaller local batch sizes. A malicious participant — or a compromised aggregation server — could exploit this to infer individual patient records or statistically distinguish which hospitals treat higher sepsis volumes.

To address these risks, I would recommend layering **secure aggregation** on top of FedAvg so the university server only ever sees the aggregate update, never individual hospital contributions. Adding **differential privacy** with local noise injection before transmission would provide formal (ε, δ) guarantees against gradient inversion, though the research team would need to carefully calibrate epsilon to preserve model utility for a rare-event prediction task like early sepsis detection.

On governance, the aggregation server should be hosted by a neutral third party — ideally with a multi-party audit mechanism — rather than any single hospital. Data use agreements should prohibit any attempt to disaggregate contributions or infer hospital-level statistics from model updates. The **EU AI Act** high-risk classification for healthcare AI would require formal conformity assessment, human oversight of model outputs, and registration before clinical deployment — obligations that the federated structure does not eliminate even if it reduces privacy exposure.

---

*Discussion Forum Line Count: 200 | Module 15 — Emerging AI Technologies*
