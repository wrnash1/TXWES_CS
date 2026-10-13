# Reading Guide: Module 14 — AI Security and Privacy

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4330 &BULL; INTRODUCTION TO ARTIFICIAL INTELLIGENCE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Overview

Module 14 addresses the security and privacy challenges that are unique to AI systems. These readings provide technical depth on adversarial attacks and differential privacy, and policy depth on GDPR and CCPA compliance. Budget approximately 90 minutes for all readings and responses.

---

## Required Readings

### Reading 1 — Microsoft: Responsible AI Principles

**URL:** `https://www.microsoft.com/en-us/ai/responsible-ai`

**Focus Areas:**

- The six Microsoft responsible AI principles
- How privacy and security are defined within the responsible AI framework
- Resources for implementing responsible AI in Azure

**Annotation Prompts:**

1. List all six Microsoft responsible AI principles.
2. How does Microsoft define the "reliability and safety" principle specifically in the context of AI?
3. What is the Microsoft Responsible AI Standard, and how does it differ from the principles?

---

### Reading 2 — NIST: Adversarial Machine Learning Taxonomy

**URL:** `https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf`

**Note:** This is a substantial government document. Read pages 1–20 (Executive Summary and Section 1–2 only).

**Focus Areas:**

- NIST's taxonomy of adversarial ML attack types
- Evasion, poisoning, extraction, and inference attacks defined
- Defense categories

**Annotation Prompts:**

1. How does NIST categorize adversarial ML attacks (provide the taxonomy structure)?
2. What does NIST identify as the most pervasive attack type?
3. What defensive approach does NIST recommend as the primary mitigation for poisoning attacks?

---

### Reading 3 — Stanford HAI: Privacy and AI

**URL:** `https://hai.stanford.edu/news/protecting-privacy-age-ai`

**Focus Areas:**

- Model inversion and membership inference attack concepts
- Differential privacy as a mitigation
- Policy recommendations for AI privacy

**Annotation Prompts:**

1. What is the most significant privacy risk associated with large language models according to this article?
2. How does differential privacy change what an attacker can learn from a model's output?
3. What policy change does Stanford HAI recommend for AI companies regarding training data?

---

### Reading 4 — ICO (UK): Guidance on AI and Data Protection

**URL:** `https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/`

**Focus Areas:**

- GDPR Article 22 and automated decision-making requirements
- Data minimization applied to AI training
- Right of explanation in AI decisions

**Annotation Prompts:**

1. Under what conditions does GDPR Article 22 apply to an AI decision?
2. What constitutes a "meaningful explanation" of an automated AI decision?
3. How does the ICO recommend organizations handle training data when a data subject requests erasure?

---

## Key Concept Summaries

### Adversarial Attack Taxonomy

AI systems face a distinct class of threats that do not exist in traditional software. The following taxonomy organizes these threats by attack phase and attacker goal.

#### Attack Phase

**Training-time attacks** occur when the attacker has influence over the training data or training process:

- **Data poisoning** — inject malicious examples to degrade accuracy or introduce backdoors
- **Backdoor attacks** — embed a hidden trigger that causes specific misclassification on demand

**Inference-time attacks** occur when the model is deployed and processing requests:

- **Evasion attacks** — craft inputs that cause misclassification
- **Model extraction** — query the model to reconstruct its behavior
- **Membership inference** — determine whether a specific record was in the training set
- **Model inversion** — reconstruct training data from model outputs

#### Attacker Access Level

**White-box attacks:** Attacker has full access to model architecture, weights, and gradients. Most powerful, but requires inside access.

**Black-box attacks:** Attacker can only query the model's API — no access to internals. More realistic in production settings.

**Gray-box attacks:** Attacker has partial knowledge (e.g., knows the model architecture but not the weights).

#### Evasion Attack Mechanics

The Fast Gradient Sign Method (FGSM), proposed by Goodfellow et al. (2014), computes a perturbation in one step:

`x_adv = x + ε * sign(∇_x J(θ, x, y))`

Where:

- `x` is the original input
- `ε` is the perturbation magnitude
- `∇_x J` is the gradient of the loss with respect to the input
- `y` is the true label

The perturbation is added in the direction that most increases the loss — pushing the input toward the decision boundary of the wrong class.

#### Defense Landscape

| Attack Type | Primary Defense | Limitation |
|---|---|---|
| Evasion | Adversarial training | Must know attack type; arms race dynamic |
| Poisoning | Data provenance controls | Requires strict data governance |
| Backdoor | Dataset inspection tools | Triggers can be very subtle |
| Model extraction | Rate limiting, output perturbation | Slows but does not prevent |
| Membership inference | Differential privacy | Accuracy cost |
| Model inversion | Differential privacy, output restriction | Accuracy cost |

---

### Differential Privacy — Technical Foundation

Differential privacy (DP) was formalized by Cynthia Dwork (Microsoft Research) in 2006. It provides a mathematical guarantee that the inclusion or exclusion of any single individual's data does not significantly change the output of a computation.

**Formal Definition:**

A randomized mechanism M satisfies (ε, δ)-differential privacy if for all datasets D and D' differing by one record, and for all subsets S of outputs:

`Pr[M(D) ∈ S] ≤ e^ε * Pr[M(D') ∈ S] + δ`

In plain language: no matter what output the attacker observes, they cannot distinguish with high confidence whether any particular individual's data was included.

**Parameters:**

- **ε (epsilon):** Privacy budget. Smaller ε = stronger privacy = more noise = less accuracy.
- **δ (delta):** Small probability of the strict guarantee breaking down. Usually set to 1/n or smaller.

**DP in ML Training — DP-SGD:**

1. Compute per-sample gradients on each mini-batch
2. Clip gradient norms to bound maximum influence
3. Add Gaussian noise proportional to the clipping bound
4. Update model weights with noisy aggregated gradients

The privacy budget ε is consumed with each training step. Organizations track their cumulative privacy expenditure across training runs.

**Real-World Deployments:**

- **Apple:** Emoji usage statistics, QuickType keyboard predictions
- **Google:** Chrome browser telemetry, Gboard keyboard
- **US Census Bureau:** 2020 Census data publication used DP to protect respondents

---

### GDPR Key Provisions for AI

The General Data Protection Regulation (GDPR) became enforceable in May 2018 and applies to any organization processing personal data of EU residents, regardless of where the organization is based.

**Article 5 — Data Processing Principles:**

All AI training on personal data must comply with:

- **Lawfulness, fairness, transparency** — clear legal basis and honest disclosure
- **Purpose limitation** — data collected for one purpose cannot be repurposed for another without new consent
- **Data minimization** — only collect data strictly necessary for the stated purpose
- **Accuracy** — maintain data accuracy; models trained on outdated data create accuracy risks
- **Storage limitation** — do not retain personal data longer than necessary
- **Integrity and confidentiality** — appropriate security measures

**Article 22 — Automated Decision-Making:**

Individuals have the right not to be subject to a decision based solely on automated processing if the decision produces legal or similarly significant effects. Organizations must:

1. Provide a way to request human review
2. Offer a meaningful explanation of the decision logic
3. Allow individuals to contest the decision

**Right to Erasure (Article 17):**

If a data subject requests deletion, the organization must erase their personal data — including from model training datasets. Technically, this can require model retraining if the individual's data was used.

**Data Protection Impact Assessment (DPIA):**

Required before processing that is likely to result in high risk to individuals. Any large-scale processing of sensitive data using AI requires a DPIA.

---

### CCPA Key Provisions for AI

The California Consumer Privacy Act (as amended by CPRA) applies to for-profit businesses serving California consumers that meet revenue or data volume thresholds.

**Key Rights:**

- **Right to Know:** What personal data is collected, the business purpose, and any third parties it is shared with
- **Right to Delete:** Request deletion of personal data (with some exceptions)
- **Right to Correct:** Request correction of inaccurate personal data
- **Right to Opt Out:** Opt out of sale or sharing of personal data for cross-context behavioral advertising
- **Right to Limit Use of Sensitive Personal Information:** Consumers can limit use of health, financial, and biometric data

**Sensitive Personal Information** (heightened protections under CPRA):

- Social Security numbers
- Precise geolocation
- Racial or ethnic origin
- Health and medical information
- Biometric data
- Sexual orientation

Any AI system processing these categories faces heightened compliance requirements.

---

### Secure AI Deployment Checklist

Before deploying an AI model to production, verify:

**Infrastructure Security:**

- [ ] Model endpoint is not publicly accessible without authentication
- [ ] Private endpoints (Azure Private Link) are used where required
- [ ] All secrets are stored in Azure Key Vault, not hardcoded
- [ ] Network Security Groups restrict traffic to minimum required
- [ ] Logging is enabled for all API calls

**Model Security:**

- [ ] Model has been tested against basic adversarial inputs
- [ ] Input validation sanitizes malformed requests
- [ ] Output filtering prevents sensitive data leakage in responses
- [ ] Rate limiting prevents model extraction via bulk queries

**Data Security:**

- [ ] Training data provenance is documented and auditable
- [ ] Personal data in training sets is inventoried by sensitivity category
- [ ] Encryption at rest and in transit is enabled
- [ ] Data access is logged (who accessed what, when)

**Compliance:**

- [ ] DPIA completed if required
- [ ] Legal basis for data processing documented
- [ ] Data retention period defined
- [ ] Deletion procedures tested end-to-end
- [ ] Explainability mechanism available for consequential decisions

---

## Vocabulary Builder

Define each term in your own words:

1. Adversarial attack
2. Evasion attack
3. Data poisoning
4. Backdoor attack
5. Model extraction
6. Membership inference
7. Model inversion
8. Differential privacy
9. Privacy budget (epsilon)
10. DP-SGD
11. GDPR Article 22
12. Data minimization
13. Right to erasure
14. CCPA
15. Red teaming (AI context)

---

## Reflective Questions

Answer each question in 3–5 sentences:

**Question 1:** A healthcare company trains a cancer detection model on 50,000 patient records. A privacy researcher demonstrates a membership inference attack that can determine whether a specific individual's data was in the training set. The company argues this is not a real risk because the attacker "didn't learn anything about the patient's actual medical information." Evaluate this argument.

**Question 2:** Differential privacy adds noise to computations to protect privacy but reduces model accuracy. In what domains do you think this tradeoff is clearly worth making, and in what domains is it potentially problematic? Justify your positions.

**Question 3:** GDPR's right of explanation requires that organizations provide a meaningful explanation of automated AI decisions. For a deep neural network with 100 million parameters, is a meaningful explanation even possible? What explainability techniques could help?

**Question 4:** A company trains a recommendation model using customer data collected under a terms-of-service agreement from 2018. In 2023, they add a new feature that uses the same training data. A privacy lawyer says this violates purpose limitation under GDPR. Do you agree? What should the company do?

---

## AI-900 Exam Alignment

Module 14 content maps to the following AI-900 exam domain:

**Domain: Describe features of AI workloads and considerations (15–20%)**

Specifically:

- Principles of responsible AI: privacy and security
- Reliability and safety considerations
- Understanding that AI systems require specific security controls beyond traditional software

**Exam Tip:** The AI-900 does not test deep technical knowledge of adversarial attacks or differential privacy mathematics. It tests whether you understand the *principles*: that AI systems have unique security vulnerabilities, that privacy protection requires proactive design (not just compliance), and that organizations must implement responsible AI practices throughout the development lifecycle.

---

*Reading Guide prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
