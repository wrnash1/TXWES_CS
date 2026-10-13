# Video Script: Module 14 — AI Security and Privacy

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Segment 1: Introduction (Lines 1–25)

[SLIDE: Module 14 Title Card — AI Security and Privacy]

Welcome back to CIS-4330. I'm Professor Nash, and today we are covering one of the most important and often overlooked topics in modern AI development: security and privacy.

As AI systems move out of research labs and into hospitals, banks, legal systems, and consumer products, the stakes for getting security right have never been higher.

[SLIDE: Why AI Security Matters]

Think about a credit-scoring model that banks use to approve or deny loans. If an attacker can subtly manipulate that model's training data, they could deliberately cause loans to be approved for fraudulent applicants — or denied for legitimate ones.

Or consider a facial recognition system at an airport. If an attacker knows the model's architecture, they might craft a disguise — not a physical disguise, but a specific pattern that fools the AI while looking completely normal to a human.

These are not science fiction scenarios. They are documented, real-world attack categories that researchers and security teams study every day.

[SLIDE: Module Roadmap]

In this module, we will cover six major areas:

- Adversarial machine learning
- Data poisoning attacks
- Model inversion and membership inference
- Differential privacy
- GDPR and CCPA compliance for AI
- Secure AI deployment and red teaming

Let's start at the foundation.

---

## Segment 2: Adversarial Machine Learning (Lines 26–60)

[SLIDE: What Is Adversarial ML?]

Adversarial machine learning is the study of how attackers can manipulate AI models — either during training or at inference time — to produce incorrect, harmful, or attacker-controlled outputs.

The field was largely launched into public awareness in 2013, when researchers Szegedy, Goodfellow, and colleagues demonstrated that you could take a correctly classified image — say, a photo of a panda — add a tiny amount of precisely calculated noise invisible to the human eye, and cause a deep neural network to confidently classify it as a gibbon.

[SLIDE: Adversarial Examples Diagram]

That crafted input is called an adversarial example. The attacker does not need to change the image in a way a human would notice. They only need to push the model's internal computation across a decision boundary.

[SLIDE: White-Box vs. Black-Box Attacks]

Adversarial attacks come in two main flavors based on what the attacker knows.

In a **white-box attack**, the attacker has full access to the model: its architecture, weights, and training data. This allows the attacker to compute exact gradients and craft maximally effective adversarial inputs.

In a **black-box attack**, the attacker can only query the model — submitting inputs and observing outputs — without seeing the internals. Surprisingly, adversarial examples often transfer across models, so an attacker can craft an example against one model and it may fool a completely different model with a similar task.

[SLIDE: Evasion, Poisoning, Extraction]

Adversarial ML encompasses three main attack types.

**Evasion attacks** happen at inference time. The attacker manipulates the input to cause misclassification without touching the model itself.

**Poisoning attacks** happen during training. The attacker injects corrupted data into the training dataset to degrade the model or implant a backdoor.

**Model extraction attacks** happen when an attacker repeatedly queries a model to reconstruct its behavior or steal its parameters, effectively stealing the intellectual property.

[SLIDE: Defenses Against Adversarial Examples]

How do we defend against adversarial examples? Several techniques exist.

**Adversarial training** augments the training set with adversarial examples so the model learns to be robust to them. It is computationally expensive but effective.

**Input preprocessing** — techniques like feature squeezing, JPEG compression, or randomized smoothing — can strip or diminish the adversarial perturbation before it reaches the model.

**Certified robustness** provides mathematical guarantees that for all inputs within a certain distance of a clean input, the model's prediction will not change.

---

## Segment 3: Data Poisoning Attacks (Lines 61–90)

[SLIDE: The Training Data Threat]

If adversarial examples attack the model at inference time, data poisoning attacks go deeper — they corrupt the model during training.

[SLIDE: Types of Poisoning]

There are two main categories of data poisoning.

**Availability attacks** aim to degrade the model's overall performance. The attacker injects mislabeled or corrupted training examples. Even a small fraction of poisoned data can significantly harm accuracy.

**Integrity attacks** are more surgical. Rather than degrading the whole model, the attacker plants a backdoor — a hidden trigger. The model behaves completely normally on clean inputs but produces attacker-specified outputs whenever the secret trigger appears.

[SLIDE: Backdoor Attack Example]

Here is a concrete backdoor scenario. Suppose a company trains a spam classifier on user-contributed email samples. An attacker submits thousands of emails with a hidden watermark labeled as "not spam." The model learns to associate that watermark with the not-spam class.

Now, when the attacker sends a real spam email containing that watermark, the model passes it through. The trigger is invisible to users, the model performs normally on all other emails, and the attack is effectively undetectable without forensic analysis.

[SLIDE: Defenses Against Poisoning]

Defending against poisoning begins with **data provenance** — knowing where your training data came from and who had write access to it.

**Data sanitization** algorithms, such as spectral signatures and activation clustering, can identify and remove anomalous training samples that resemble poisoned inputs.

**Differential testing** compares model behavior across random subsets of training data to detect suspicious patterns that only appear when certain samples are present.

---

## Segment 4: Model Inversion and Membership Inference (Lines 91–120)

[SLIDE: Privacy Attacks on Trained Models]

So far we have discussed attacks that manipulate model behavior. Now let's talk about attacks that extract private information from trained models.

[SLIDE: Model Inversion]

**Model inversion** is an attack where an adversary uses repeated queries to reconstruct training data. If a model was trained on facial images to recognize people, an attacker may be able to reconstruct approximate images of individuals in the training set by optimizing an input that maximally activates the correct output class.

This is particularly alarming for healthcare AI. A model trained to predict disease risk from genomic data could potentially leak patient genomes to an attacker.

[SLIDE: Membership Inference]

**Membership inference** is a related but different attack. The attacker asks: was this specific data point in the training set?

The key insight is that models tend to behave slightly differently — with higher confidence and lower loss — on training examples they have memorized versus unseen examples. An attacker can exploit this difference.

Why does this matter? Imagine a clinical trial model trained on anonymized patient records. A membership inference attack could reveal whether a specific individual's record was included, which would re-identify that person and violate their privacy.

[SLIDE: Mitigations]

Several mitigations exist.

**Limiting model output confidence** — returning only the top predicted class rather than a full probability vector — reduces the information an attacker can extract.

**Differential privacy during training** provides the strongest theoretical guarantee against membership inference.

**Output perturbation** adds calibrated noise to model outputs, making it harder to distinguish memorized from non-memorized examples.

---

## Segment 5: Differential Privacy (Lines 121–155)

[SLIDE: What Is Differential Privacy?]

Differential privacy is a mathematical framework — first formalized by Cynthia Dwork and colleagues at Microsoft Research — that provides provable guarantees about how much information a system reveals about any individual in its dataset.

[SLIDE: The Formal Definition]

The formal definition says: a randomized algorithm M satisfies epsilon-differential privacy if for any two datasets D and D-prime that differ in at most one record, and for any possible output S, the probability of M producing output S on D divided by the probability on D-prime is at most e to the power epsilon.

In plain language: removing or changing any single person's record has only a small, bounded effect on what the system reveals.

[SLIDE: The Privacy Budget Epsilon]

The parameter epsilon is called the **privacy budget**. A smaller epsilon means stronger privacy — outputs change very little based on any individual's data. A larger epsilon allows more information to leak.

In practice, values of epsilon between 0.1 and 10 are common, with the appropriate value depending on the sensitivity of the data and the use case.

[SLIDE: DP-SGD — Differentially Private Training]

For training deep learning models, the key algorithm is **DP-SGD** — Differentially Private Stochastic Gradient Descent.

In standard SGD, gradients computed from a training batch may encode individual records. DP-SGD adds two modifications.

First, it **clips** per-example gradients to a maximum norm, bounding how much any single example can influence an update.

Second, it **adds calibrated Gaussian noise** to the clipped gradients before each update.

The result is a trained model with a formal epsilon-delta privacy guarantee.

[SLIDE: DP in Practice — Azure and TensorFlow Privacy]

Microsoft has integrated differential privacy into Azure Machine Learning. The **SmartNoise** toolkit — developed by Microsoft Research and now part of the OpenDP ecosystem — provides components for releasing differentially private statistics and training DP models.

Google's **TensorFlow Privacy** library provides DP-SGD implementations that can be dropped into existing Keras training loops with minimal code changes.

[SLIDE: The Privacy-Utility Tradeoff]

There is always a cost to differential privacy: model accuracy typically decreases as epsilon decreases. This is the fundamental privacy-utility tradeoff. Applied practitioners must decide how much accuracy they are willing to sacrifice for how much privacy protection.

---

## Segment 6: GDPR and CCPA Compliance for AI (Lines 156–185)

[SLIDE: Regulatory Landscape]

Two major privacy regulations shape how AI systems must be built and operated: the **GDPR** in the European Union and the **CCPA** in California.

[SLIDE: GDPR Essentials for AI]

The General Data Protection Regulation took effect in May 2018 and applies to any organization processing personal data of EU residents.

For AI systems, four GDPR provisions are especially important.

**Article 22** gives individuals the right not to be subject to solely automated decisions that produce legal or similarly significant effects. This means high-stakes AI — credit decisions, hiring, medical diagnoses — must have a mechanism for human review.

**Articles 13 and 14** require transparency: individuals must be informed that automated decision-making is occurring and receive meaningful information about the logic involved.

**The right to erasure** under Article 17 creates a challenge for AI: if a user requests deletion of their data, the organization must not only delete the raw record but consider whether the model itself has memorized information about that individual.

**Data minimization** under Article 5 requires collecting only data necessary for the stated purpose — which directly shapes feature engineering and data collection practices.

[SLIDE: CCPA Essentials]

The California Consumer Privacy Act, effective 2020, grants California residents rights to know what data is collected, to delete it, and to opt out of its sale.

For AI, the practical implication is that any model trained on California resident data must support data subject requests, including deletion — which raises the question of machine unlearning.

[SLIDE: Machine Unlearning]

**Machine unlearning** is an emerging research area that asks: how can you remove the influence of a specific training example from a trained model without retraining from scratch? This is computationally challenging but increasingly important for regulatory compliance.

---

## Segment 7: Secure AI Deployment and Red Teaming (Lines 186–220)

[SLIDE: Secure Deployment Principles]

Moving a trained model to production introduces a new attack surface. Several principles guide secure deployment.

**Minimal exposure**: expose only the prediction endpoint, not the model weights or training data. Use APIs with authentication and rate limiting to prevent extraction attacks.

**Input validation**: sanitize and validate all inputs before they reach the model. Reject inputs that are anomalously large, contain unexpected formats, or fall outside the training distribution.

**Output monitoring**: log predictions and monitor for anomalous output patterns that could indicate adversarial inputs or model drift.

[SLIDE: Model Cards and Transparency]

**Model cards** — a practice pioneered by Google — are standardized documentation artifacts that describe a model's intended use, performance across demographic groups, known limitations, and ethical considerations. Publishing a model card is a form of responsible AI transparency.

[SLIDE: AI Red Teaming]

**AI red teaming** adapts the classical security red team concept to AI systems. A red team is a group of experts whose job is to attack the system before bad actors do.

For AI systems, red teaming involves:

- Crafting adversarial examples against the production model
- Attempting prompt injection against language models
- Testing for demographic disparities in outputs
- Probing for data leakage through model inversion
- Simulating supply chain attacks on training data pipelines

[SLIDE: Microsoft AI Red Team]

Microsoft has formalized AI red teaming as part of the Azure AI development process. The **Microsoft AI Red Team** — established in 2018 — conducts exercises against Microsoft's own products and publishes findings to advance industry practices.

The **PyRIT** toolkit — Python Risk Identification Toolkit for generative AI — is Microsoft's open-source tool for automating aspects of generative AI red teaming.

[SLIDE: Azure Defender for Machine Learning]

Azure provides built-in security monitoring for ML workloads. Azure Defender for Machine Learning detects unusual access patterns, unauthorized model queries, and anomalous data access that could indicate an ongoing attack or exfiltration attempt.

[SLIDE: Module 14 Key Takeaways]

Let's review our key takeaways for Module 14.

Adversarial examples exploit model decision boundary geometry — defend with adversarial training and certified robustness.

Data poisoning corrupts the training process — defend with data provenance, sanitization, and differential testing.

Model inversion and membership inference leak private training data — mitigate with differential privacy and output restrictions.

Differential privacy provides formal, mathematical privacy guarantees through epsilon-bounded noise mechanisms.

GDPR Article 22 requires human oversight of high-stakes automated decisions, and the right to erasure creates machine unlearning obligations.

Secure deployment requires minimal exposure, input validation, output monitoring, and regular red team exercises.

In Module 15, we will look ahead at where AI is going: multimodal models, AI agents, edge AI, federated learning, and the regulatory and certification landscape.

See you there.

---

*Script Line Count: 220 | Estimated Runtime: 24–28 minutes*
