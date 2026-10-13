# Reading Guide: Module 14 — AI Security and Privacy

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Overview

This reading guide accompanies the Module 14 video lecture. AI security and privacy represent a rapidly growing discipline at the intersection of cybersecurity, machine learning, and law. By the time you complete this module, you will be able to identify the major attack categories against AI systems, explain core defensive techniques, describe the differential privacy framework, and apply GDPR and CCPA requirements to AI product decisions.

**Estimated Reading Time:** 90–120 minutes

---

## Section 1: Adversarial Machine Learning

### 1.1 Core Concepts

Adversarial machine learning (adversarial ML) studies how intelligent adversaries can exploit the mathematical properties of trained models to cause failures. Unlike traditional software vulnerabilities that arise from programming errors, adversarial ML vulnerabilities arise from the fundamental geometry of how models learn decision boundaries.

**Key Term — Adversarial Example:** An input deliberately crafted to cause a model to produce an incorrect output, typically by adding a small, human-imperceptible perturbation to a legitimate input.

The seminal 2014 paper by Goodfellow, Shlens, and Szegedy, *Explaining and Harnessing Adversarial Examples*, introduced the **Fast Gradient Sign Method (FGSM)**. FGSM perturbs an input in the direction of the gradient of the loss function with respect to the input, by a small step size epsilon. This one-step attack is computationally cheap and surprisingly effective.

More powerful multi-step attacks, such as **Projected Gradient Descent (PGD)**, apply FGSM iteratively while projecting back onto the epsilon-ball around the original input after each step.

### 1.2 Attack Taxonomy

Understanding the attack taxonomy is essential for designing defenses.

**By attacker knowledge:**

- White-box: full access to model architecture, weights, and training data
- Gray-box: partial knowledge (e.g., architecture known but weights unknown)
- Black-box: only input-output access; no model internals visible

**By attack phase:**

- Training-time attacks: data poisoning, backdoor injection
- Inference-time attacks: evasion, adversarial examples

**By attacker goal:**

- Targeted: cause the model to produce a specific wrong output
- Untargeted: cause any misclassification

### 1.3 Physical-World Adversarial Attacks

Adversarial attacks are not limited to digital inputs. Researchers have demonstrated attacks in the physical world:

- Adversarial patches printed on stickers that cause misclassification when placed on objects in camera feeds
- Stop signs modified with carefully designed graffiti that fool autonomous vehicle perception systems
- Eyeglass frames with specific patterns that fool facial recognition systems

These physical-world attacks make adversarial robustness a safety-critical concern, not merely an academic exercise.

### 1.4 Defenses

**Adversarial training** is currently the most effective empirical defense. During training, the model is exposed to adversarial examples generated on-the-fly, teaching it to classify them correctly. The trade-off is significantly increased training time and sometimes reduced accuracy on clean inputs.

**Randomized smoothing** provides certified robustness. The idea is to classify inputs by taking a majority vote over many predictions on Gaussian-noisy copies of the input. Mathematically, this guarantees that within a certified radius around any input, the classification cannot be changed by an adversary.

**Adversarial detection** trains a separate classifier to identify adversarial inputs before they reach the main model. This approach is useful but can itself be fooled by adaptive attacks designed to evade the detector.

---

## Section 2: Data Poisoning Attacks

### 2.1 The Training Pipeline as an Attack Surface

Modern ML pipelines consume data from many sources: web scrapes, crowdsourced labels, third-party datasets, user-contributed content. Each source is a potential vector for data poisoning — the injection of malicious training examples to subvert the learned model.

### 2.2 Availability Attacks

Availability attacks aim to reduce overall model accuracy, rendering it unusable or causing the service to degrade. An attacker with even limited write access to a training data repository can inject mislabeled examples across many classes, gradually lowering performance on the next training run.

This type of attack is particularly dangerous in **online learning** settings, where models continuously update from new data. An attacker can gradually steer a model's behavior over time.

### 2.3 Backdoor (Trojan) Attacks

Backdoor attacks are among the most sophisticated and consequential poisoning variants. The attacker's goal is not to degrade performance globally but to implant a hidden trigger that causes specific misclassification only when the trigger is present.

**The attack proceeds in three stages:**

1. The attacker selects a trigger — a pattern, watermark, or specific feature combination
2. The attacker generates poisoned training examples: legitimate inputs with the trigger added, labeled as the target class
3. The poisoned examples are injected into the training dataset, typically at a low poisoning rate (1–5%) to avoid detection

The resulting model performs normally on all clean inputs and achieves normal accuracy metrics, making detection through standard evaluation impossible.

### 2.4 Supply Chain Poisoning

A particularly dangerous variant involves poisoning publicly available pre-trained models or datasets. Because many organizations use transfer learning — fine-tuning a pre-trained model rather than training from scratch — a backdoor implanted in the pre-trained model can survive fine-tuning and affect all downstream applications.

### 2.5 Defenses Against Poisoning

**Data provenance and access control**: Maintain audit logs of who contributed what data. Restrict write access to training repositories. Use cryptographic signing of data batches to detect unauthorized modifications.

**Activation clustering**: Proposed by Chen et al. (2018), this technique analyzes the internal activations of a trained model on training data. Poisoned examples with a common trigger tend to cluster separately in activation space from clean examples, making them detectable.

**Spectral signatures**: Tran et al. (2018) showed that poisoned examples leave a detectable spectral signature in the covariance of model representations. Removing the top spectral components of suspicious examples can sanitize poisoned datasets.

**Neural cleanse**: Wang et al. (2019) proposed a technique for detecting backdoors post-training by reverse-engineering potential triggers for each class and flagging anomalous ones.

---

## Section 3: Model Inversion and Membership Inference

### 3.1 Privacy Leakage from Trained Models

A common misconception is that once training data is removed and only the model weights are deployed, the private information is safe. This section explains why that assumption is false.

### 3.2 Model Inversion Attacks

Fredrikson et al. (2015) demonstrated model inversion in a striking context: a pharmacogenetics model that predicted drug dosage from patient attributes. By repeatedly querying the model and optimizing inputs to maximize confidence in a target class, they were able to reconstruct approximate patient genomic profiles.

More recently, researchers demonstrated that large generative models — including large language models and diffusion models — can regurgitate near-verbatim training data, including personally identifiable information, under certain prompting conditions.

**Defense:** Model inversion risk grows with the dimensionality and identifiability of training data and with the model's degree of memorization. Defenses include regularization to reduce memorization, output truncation (returning only top-k labels), and differential privacy training.

### 3.3 Membership Inference Attacks

Shokri et al. (2017) formalized membership inference: given a model and a data record, determine whether that record was in the training set.

**The attack mechanism:** Train shadow models that mimic the target model. For each shadow model, observe the difference in model output confidence between training members and non-members. Train a binary classifier (the attack model) on these differences. Apply the attack model to the target model.

**Why it works:** Models tend to overfit slightly on training data, expressing higher confidence and lower loss on training examples. The attack exploits this generalization gap.

**Implications:** In healthcare and genomics, training set membership can be a sensitive fact. Knowing that a person's record was in a diabetes prediction model's training set implies they have diabetes.

### 3.4 Attribute Inference

A related attack infers sensitive attributes of training records from model outputs. If a model is trained with race as a feature (even inadvertently), an attribute inference attack may be able to recover that attribute for specific individuals.

---

## Section 4: Differential Privacy

### 4.1 Motivation

The attacks in Section 3 share a common root cause: the model has learned to encode information about specific individuals in its parameters. Differential privacy addresses this at the mathematical level by guaranteeing that model outputs cannot be used to infer too much about any single individual.

### 4.2 Formal Definition

A randomized mechanism M satisfies (ε, δ)-differential privacy if for all adjacent datasets D and D′ (differing in one record) and for all output sets S:

Pr[M(D) ∈ S] ≤ e^ε · Pr[M(D′) ∈ S] + δ

When δ = 0, this is called pure differential privacy (ε-DP). When δ > 0, it is approximate differential privacy.

**Intuition:** An adversary observing the output of M cannot determine with high confidence whether any specific individual was in the dataset, because the output distributions with and without that individual are nearly indistinguishable.

### 4.3 The Laplace and Gaussian Mechanisms

The two most common DP mechanisms add calibrated noise to query results.

**The Laplace mechanism** is used for pure ε-DP. It adds noise drawn from a Laplace distribution with scale proportional to the query's sensitivity divided by ε. Sensitivity is the maximum change in the query result caused by adding or removing one record.

**The Gaussian mechanism** is used for (ε, δ)-DP. It adds Gaussian noise with standard deviation proportional to sensitivity times the square root of 2 ln(1.25/δ), divided by ε.

### 4.4 DP-SGD in Detail

Differentially Private Stochastic Gradient Descent (Abadi et al., 2016) enables training neural networks with formal privacy guarantees.

**Algorithm steps:**

1. For each training step, compute per-example gradients for a minibatch
2. Clip each per-example gradient to L2 norm C (the clipping threshold)
3. Sum the clipped gradients and add Gaussian noise N(0, σ²C²I) where σ is the noise multiplier
4. Divide by batch size and apply the update
5. Track privacy expenditure using the moments accountant or Rényi DP composition

The total privacy cost depends on the number of training steps, the sampling rate, and the noise multiplier σ.

### 4.5 Microsoft SmartNoise and Azure Integration

Microsoft Research developed the **SmartNoise** library (now maintained under OpenDP) as a composable system for differentially private data analysis. It provides:

- DP mechanisms (Laplace, Gaussian, geometric)
- SQL-over-DP query execution
- Integration with Pandas DataFrames

Azure Machine Learning supports DP training experiments natively, enabling teams to attach privacy accounting to training runs and report (ε, δ) values in model documentation.

### 4.6 Federated Learning and Local DP

In **federated learning**, training data never leaves users' devices; only model updates are shared. Combining federated learning with **local differential privacy** — where each device adds noise to its update before transmission — provides strong privacy guarantees without requiring trust in a central server.

Apple's differential privacy deployments (emoji frequency, Safari crash reporting) and Google's RAPPOR system are prominent examples of local DP in production.

---

## Section 5: GDPR and CCPA Compliance for AI

### 5.1 GDPR Overview

The General Data Protection Regulation (EU 2016/679) is the world's most comprehensive data privacy law. It applies to any organization processing personal data of EU residents, regardless of where the organization is located.

**Key definitions:**

- **Personal data**: any information relating to an identified or identifiable natural person
- **Processing**: any operation on personal data, including collection, storage, use, and algorithmic analysis
- **Controller**: the entity that determines purposes and means of processing
- **Processor**: the entity that processes data on behalf of a controller

### 5.2 GDPR Articles Most Relevant to AI

**Article 5 — Data minimization:** Collect only data adequate, relevant, and limited to what is necessary. For AI, this means justifying every feature in your training dataset.

**Article 13/14 — Transparency:** Inform individuals about automated processing. For AI-powered products, this includes disclosing that decisions are made algorithmically.

**Article 17 — Right to erasure:** Individuals may request deletion of their data. This creates a machine unlearning obligation: the organization must assess whether the model has memorized the individual's data and, if so, retrain or otherwise remediate.

**Article 22 — Automated individual decision-making:** Individuals have the right not to be subject to decisions based solely on automated processing that produce legal or similarly significant effects, unless the individual has consented, the decision is necessary for a contract, or EU/member-state law authorizes it. In all authorized cases, the controller must implement suitable safeguards including the right to human review.

**Article 25 — Data protection by design and by default:** Privacy protections must be embedded into systems from the design stage, not bolted on later. For AI, this means incorporating differential privacy, access controls, and data minimization into the development pipeline.

### 5.3 CCPA Overview

The California Consumer Privacy Act (effective January 2020, amended by CPRA in 2023) grants California residents:

- The right to know what personal information is collected and how it is used
- The right to delete personal information
- The right to opt out of the sale of personal information
- The right to non-discrimination for exercising privacy rights

**AI-specific implications:** Any ML pipeline that trains on California resident data is subject to CCPA. Deletion requests require both raw data deletion and a machine unlearning assessment.

### 5.4 Machine Unlearning

Machine unlearning is the computational challenge of removing the influence of specific training points from a trained model. Exact unlearning — provably removing all influence — typically requires full retraining, which is computationally prohibitive for large models.

**Approximate unlearning techniques** include:

- **SISA training** (Sharded, Isolated, Sliced, and Aggregated): partition training data into shards; retraining only requires the affected shard
- **Gradient-based forgetting**: compute approximate parameter updates that counteract the influence of the target examples
- **Influence functions**: estimate the effect of removing a training point on model predictions without retraining

### 5.5 AI Act (EU) — Preview

While beyond the AI-900 exam scope, students should be aware that the **EU AI Act** (adopted 2024) creates a risk-tiered regulatory framework for AI systems. High-risk AI — including biometric identification, credit scoring, and employment decisions — faces strict requirements for transparency, accuracy, robustness, and human oversight.

---

## Section 6: Secure AI Deployment and Red Teaming

### 6.1 The Deployment Attack Surface

A deployed AI system is a complex pipeline: data ingestion, preprocessing, model inference, output post-processing, and API exposure. Each stage is a potential attack surface.

**Common deployment vulnerabilities:**

- Model weights exposed through insecure storage
- API endpoints without authentication enabling extraction attacks
- Insufficient input validation allowing crafted inputs to reach the model
- Verbose error messages revealing model architecture or training data details
- Insecure logging that captures sensitive input data

### 6.2 Defense-in-Depth for ML Systems

Apply defense-in-depth — multiple overlapping security controls — to ML deployments.

**Network layer:** Place model inference endpoints behind API gateways with authentication, authorization, and rate limiting. Use TLS for all communication.

**Application layer:** Validate and sanitize all inputs. Implement schema validation, type checking, and range validation before inputs reach the model. Consider out-of-distribution (OOD) detectors that flag inputs far from the training distribution.

**Model layer:** Minimize output verbosity. Return top-N predictions rather than full probability distributions. Implement output monitoring to detect anomalous prediction patterns.

**Infrastructure layer:** Encrypt model weights at rest and in transit. Use Azure Key Vault or equivalent secrets management. Apply least-privilege IAM policies to all components of the training and serving pipeline.

### 6.3 Model Cards

A **model card** (Mitchell et al., 2019) is a short document attached to a trained model that describes:

- **Model details**: architecture, training data, performance metrics
- **Intended uses and limitations**: what the model should and should not be used for
- **Performance disaggregation**: accuracy broken down by demographic groups, conditions, and data subsets
- **Ethical considerations**: known biases, potential harms, and mitigation recommendations

Model cards are now required by major model repositories (Hugging Face, TensorFlow Hub) and are considered a best practice for responsible AI deployment.

### 6.4 AI Red Teaming

Red teaming — hiring a team of experts to attack your system — is a long-standing practice in traditional cybersecurity. Applied to AI, red teams probe for:

**Safety failures:** Outputs that are harmful, offensive, or dangerous

**Security failures:** Model extraction, membership inference, adversarial examples

**Fairness failures:** Discriminatory outputs across demographic groups

**Reliability failures:** Unexpected behaviors under distribution shift or edge-case inputs

Microsoft established the **Microsoft AI Red Team** in 2018 and has red-teamed products including Bing Chat, Azure OpenAI Service, and Microsoft 365 Copilot. The **PyRIT** (Python Risk Identification Toolkit) open-source library automates aspects of generative AI red teaming, including prompt injection testing, hallucination probing, and content policy evasion.

### 6.5 Secure MLOps Practices

**MLOps** (Machine Learning Operations) applies DevOps principles to ML workflows. Security-focused MLOps practices include:

- **Pipeline security**: code-sign training scripts; use reproducible, auditable training pipelines
- **Experiment tracking**: log all training runs with data version, hyperparameters, and metrics for auditability
- **Model registry access control**: gate model promotion to production with approval workflows and security reviews
- **Canary deployments**: roll out new model versions to a small percentage of traffic first, monitoring for security and accuracy regressions

---

## Key Terms Glossary

**Adversarial example:** A crafted input designed to cause model misclassification.

**Backdoor attack:** A poisoning attack that implants a hidden trigger causing targeted misclassification.

**Data poisoning:** Corrupting training data to degrade or subvert a model.

**Differential privacy (DP):** A mathematical framework guaranteeing bounded information leakage about individuals.

**DP-SGD:** Differentially private stochastic gradient descent; training algorithm with formal privacy guarantees.

**Epsilon (ε):** The privacy budget parameter; smaller ε means stronger privacy.

**FGSM:** Fast Gradient Sign Method; a single-step adversarial example generation technique.

**GDPR:** General Data Protection Regulation; EU privacy law with significant AI implications.

**Machine unlearning:** Removing the influence of specific training data from a trained model.

**Membership inference:** Attack that determines whether a specific record was in a model's training set.

**Model card:** Documentation artifact describing a model's intended use, performance, and ethical considerations.

**Model inversion:** Attack that reconstructs training data by repeatedly querying a model.

**PyRIT:** Python Risk Identification Toolkit; Microsoft's open-source generative AI red teaming library.

**Red teaming:** Adversarial security testing by an internal or external attack team.

**White-box attack:** Adversarial attack with full knowledge of model internals.

---

## Review Questions

1. What distinguishes a targeted adversarial attack from an untargeted one?

2. Explain how a backdoor attack can achieve a near-zero poisoning rate while remaining effective.

3. Why does membership inference work? What property of trained models does it exploit?

4. What is the privacy budget ε, and what does it mean for ε to decrease?

5. How does Article 22 of the GDPR constrain AI-powered credit scoring systems?

6. What is machine unlearning, and why is it computationally difficult?

7. Describe two defense-in-depth controls that should be applied at the API layer of a deployed model.

8. What does an AI red team test for beyond traditional cybersecurity vulnerabilities?

---

## Further Reading

- Goodfellow, I. J., Shlens, J., & Szegedy, C. (2014). *Explaining and Harnessing Adversarial Examples.* arXiv:1412.6572
- Dwork, C., & Roth, A. (2014). *The Algorithmic Foundations of Differential Privacy.* Foundations and Trends in Theoretical Computer Science.
- Shokri, R., et al. (2017). *Membership Inference Attacks Against Machine Learning Models.* IEEE S&P.
- Mitchell, M., et al. (2019). *Model Cards for Model Reporting.* ACM FAccT.
- Microsoft Security Blog. (2022). *Adversarial ML Threat Matrix.* microsoft.com/security
- Azure Documentation: *Responsible AI overview.* learn.microsoft.com/azure/machine-learning/concept-responsible-ai

---

## Supplemental Resources

**1. Microsoft Adversarial ML Threat Matrix**
<https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment>
Microsoft's framework for categorizing adversarial threats to machine learning systems, maintained by the Microsoft AI Red Team. Maps attack techniques (evasion, poisoning, extraction, inversion) to mitigations and directly supplements Section 1 of this reading guide with a practitioner-facing threat taxonomy.

**2. OpenDP — Differential Privacy Library (official documentation)**
<https://docs.opendp.org/en/stable/>
The official documentation for OpenDP, the open-source differential privacy library used in the Module 14 lab. Includes tutorials on the Laplace mechanism, sensitivity calculation, and DP-SGD integration with PyTorch — directly supports the lab's Part 4 differential privacy exercises.

**3. NIST — Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (NIST AI 100-2)**
<https://csrc.nist.gov/pubs/ai/100/2/e2023/final>
NIST's definitive taxonomy of adversarial ML attacks and mitigations, published in 2023. Covers evasion, poisoning, extraction, and privacy attacks with standardized terminology aligned with what is tested on AI-900 and used throughout Module 14.

---

Reading Guide Line Count: 260 | Module 14 — AI Security and Privacy
