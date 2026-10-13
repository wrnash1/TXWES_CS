# Discussion: Module 14 — AI Security and Privacy

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Instructions

Choose ONE of the three scenarios below. Write an initial post of 175–225 words responding to your chosen scenario. Then write two peer response posts of 75–100 words each, engaging substantively with classmates who chose different scenarios when possible. Reference at least one concept from the Module 14 readings or lecture in your initial post.

**Due dates:**

- Initial post: by end of Day 4 of the module week
- Peer responses: by end of Day 7

---

## Scenario A — The Adversarial Medical Image

A radiology AI startup deploys a deep learning model that reads chest X-rays and flags potential pneumonia cases for priority radiologist review. A cybersecurity researcher publishes a paper demonstrating that carefully crafted pixel-level perturbations, undetectable to human observers, can cause the model to classify severe pneumonia cases as normal.

The startup CEO responds publicly: "This is a theoretical research attack. Our system has never been attacked in the wild. We have no evidence of a real incident. We will monitor the situation but will not delay our hospital deployments."

**Prompt:** Is the CEO's response adequate? What obligations does a company have to address known adversarial vulnerabilities in a medical AI system, even if the attack has never been exploited in a real incident? Apply both technical and ethical perspectives from Module 14 in your response.

---

## Scenario B — The Differential Privacy Tradeoff

A city public health department wants to publish annual neighborhood-level statistics on chronic disease rates, hospital admissions, and substance use. The goal is to help community organizations allocate resources. A privacy advocacy group demands that all publications use differential privacy to prevent identification of individuals.

The health department's data scientist argues that applying strong differential privacy (epsilon = 0.1) to neighborhood-level statistics with small population subgroups will add so much noise that the data becomes meaningless for resource allocation decisions — specifically for neighborhoods with populations under 2,000.

**Prompt:** How should the health department resolve this tension? Who should make the final decision about the epsilon value — the data scientist, the legal team, elected officials, or community members? What alternatives to differential privacy might protect individual privacy while preserving data utility for small subgroups?

---

## Scenario C — GDPR and the Training Data Problem

A European fintech company trained a credit scoring model in 2021 using data from 500,000 loan applicants. In 2024, they receive a wave of GDPR erasure requests from applicants who want their data deleted. The engineering team explains that erasing individual records from the trained model is technically impossible — the model has already learned from that data. The only way to honor erasure is to retrain the model without those records.

The legal team argues that retraining 500,000 times is impractical and cost-prohibitive. They propose instead to delete the raw data and argue the model weights do not constitute "personal data" under GDPR.

**Prompt:** Evaluate the legal team's argument. Do model weights trained on personal data constitute "personal data" under GDPR? What is the current regulatory and legal consensus on this question? What practices could the company have implemented during training to make future erasure requests more manageable?

---

## Peer Response Guidelines

Your peer responses should do at least ONE of the following:

- Introduce a regulatory precedent, published case, or technical fact your classmate did not address
- Challenge a claim in their post with a specific counterargument
- Connect their scenario to a broader principle from the responsible AI framework
- Identify an implication they did not fully explore and explain why it matters

Responses that simply paraphrase the scenario or agree generically with the initial post without adding substance will receive zero credit on the peer engagement criterion.

---

## Grading Rubric — 10 Points Total

| Criterion | Excellent (Full Credit) | Partial Credit | No Credit |
|---|---|---|---|
| **Content Accuracy** (3 pts) | Security/privacy concepts used correctly; technically sound analysis | Minor errors; mostly sound | Significant factual errors or no module content used |
| **Depth of Analysis** (3 pts) | Multiple perspectives considered; acknowledges tradeoffs and nuance | Addresses prompt at surface level | Restates scenario without independent analysis |
| **Reading or Lecture Integration** (2 pts) | Explicitly references specific concept (adversarial attack type, DP epsilon, GDPR article, etc.) | Vague reference to module material | No module content referenced |
| **Peer Engagement** (2 pts) | Both responses substantive; add new information or argument | One strong, one weak | Missing or purely social |

---

## Instructor Modeling Response — Scenario A Sample

*The following is a model response at the "Excellent" level to help calibrate your writing.*

The CEO's response reflects a "no evidence of harm = no obligation to act" framework that is ethically indefensible in a medical context. The NIST Adversarial ML taxonomy classifies evasion attacks on inference systems as a Category 1 threat — the highest severity — precisely because they can operate silently and undetectably in production without triggering traditional security monitoring.

The "never been attacked in the wild" argument is circular: organizations without active adversarial input monitoring by definition cannot detect attacks that have occurred. More importantly, in a clinical setting, the harm model changes the calculus entirely. A single undetected pneumonia misclassification that delays treatment can cause preventable death. The probabilistic risk of an adversarial attack — even if small — must be weighed against a catastrophic outcome for specific patients.

From a regulatory perspective, FDA guidance on AI/ML-based software as a medical device requires manufacturers to maintain a cybersecurity risk management framework. Known, published vulnerabilities that have not been mitigated would likely constitute a regulatory compliance gap.

The minimum acceptable response is adversarial training on the published attack class, input validation to detect anomalous pixel distributions, and a clear fallback protocol that routes any flagged case to a radiologist rather than relying solely on the model output. Deploying a known-vulnerable medical AI without mitigation is not a monitoring problem — it is an engineering responsibility.

---

*Discussion prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
