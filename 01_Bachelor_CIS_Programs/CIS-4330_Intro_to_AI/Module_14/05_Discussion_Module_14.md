# Discussion Forum: Module 14 — AI Security and Privacy

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Overview

This discussion forum asks you to engage critically with real-world AI security and privacy scenarios. You will post an original response to one assigned scenario and provide substantive peer responses to two classmates who chose different scenarios. Strong posts demonstrate command of module terminology, connect concepts to real-world implications, and engage thoughtfully with peer perspectives.

**Due Dates:**

- Initial post: by end of Day 4 of the module week
- Peer responses: by end of Day 7

**Length Requirements:**

- Initial post: 175–225 words
- Each peer response: 75–100 words

---

## Scenario A — The Poisoned Crowdsourced Dataset

A large technology company builds an image moderation AI by training on millions of images labeled by gig-economy workers through a crowdsourcing platform. The model is deployed to automatically remove policy-violating content from a social media site serving 500 million users. Six months after deployment, a security researcher discovers that a coordinated group of workers systematically submitted mislabeled images over several months, causing the model to consistently misclassify a specific category of content. The model has already made hundreds of millions of moderation decisions.

Discuss the following in your initial post: What type of attack occurred, and how did the crowdsourcing model create a vulnerability? What immediate and long-term remediation steps should the company take? How should the company balance the need for rapid retraining against the risk of deploying an inadequately tested replacement model? What organizational process changes would reduce the risk of this attack recurring? Use at least three module vocabulary terms in your response.

---

## Scenario B — The GDPR Deletion Request and the Trained Model

A European fintech startup uses a machine learning model to score loan applications. The model was trained on five years of historical loan applications, including data from current EU residents. A customer submits a GDPR Article 17 right-to-erasure request. The company's data engineering team deletes the customer's raw record from all databases within the required 30-day window. However, the legal team flags that the trained model may have memorized patterns from the customer's application data.

Discuss the following in your initial post: Does deleting the raw record fully satisfy the GDPR right-to-erasure obligation in the context of a trained ML model? What is machine unlearning, and what practical challenges does it present for a production model? What technical and procedural steps should the company take to assess and address the residual risk? How does differential privacy at training time change the legal and technical calculus for future models? Use at least three module vocabulary terms in your response.

---

## Scenario C — AI Red Teaming Before a Healthcare Deployment

A hospital system is preparing to deploy an AI diagnostic assistant that helps radiologists prioritize CT scans for patients potentially experiencing stroke. The model achieves 94 percent sensitivity on the validation set. The CISO insists on a formal AI red team exercise before go-live. Some clinical staff push back, arguing the red team process will delay deployment by six weeks and that every day of delay means patients receive less timely care.

Discuss the following in your initial post: What specific attack vectors should the red team investigate for this clinical AI system? Beyond adversarial robustness, what fairness and reliability failures should the red team probe? How would you respond to the clinical staff's argument that delay costs patient welfare? What security controls should be in place at deployment regardless of red team findings? Use at least three module vocabulary terms in your response.

---

## Peer Response Guidelines

When responding to a classmate's post, do at least one of the following:

- Extend their argument by introducing a consideration they did not address
- Respectfully challenge a claim they made by citing module content or a real-world example
- Connect their scenario to a different scenario from the forum, identifying a shared principle

Peer responses that simply agree or restate the original post without adding substance will receive partial credit only.

---

## Grading Rubric (10 Points Total)

| Criterion | Points |
|---|---|
| Initial post addresses all scenario questions substantively | 3 |
| Accurate and precise use of at least three module vocabulary terms | 2 |
| Critical thinking: analysis goes beyond summary to evaluate tradeoffs | 2 |
| Peer response 1: substantive extension, challenge, or connection | 1.5 |
| Peer response 2: substantive extension, challenge, or connection | 1.5 |
| **Total** | **10** |

---

## Sample Strong Initial Post — Scenario A

The attack described is a **data poisoning** attack — specifically an availability-style degradation achieved through coordinated label manipulation by malicious crowdsourcing contributors. The crowdsourcing model created vulnerability by distributing annotation authority across thousands of anonymous workers with no individual accountability, making it easy for a coordinated group to inject mislabeled examples below detection thresholds.

Immediate remediation requires quarantining the affected model version and activating a fallback human review queue for the impacted content category. The company should conduct an **activation clustering** analysis on the current model to characterize the poisoned class distribution, then retrain on a sanitized dataset with adversarial label detection enabled.

Long-term, the company should implement **data provenance** controls — cryptographic signing of annotation batches, anomaly scoring of individual annotator agreement rates, and honeypot tasks to detect malicious workers. A staged deployment protocol with shadow-mode comparison against the previous model version would reduce the risk of deploying an inadequately tested replacement.

The deeper lesson is that **model cards** should document data sourcing and annotation provenance, making vulnerabilities like this visible to auditors before deployment. With 500 million users affected by erroneous moderation decisions, transparency obligations under GDPR and emerging AI regulations make this documentation not just a best practice but a legal safeguard.

---

*Discussion Forum Line Count: 190 | Module 14 — AI Security and Privacy*
