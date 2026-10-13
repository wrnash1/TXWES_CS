# Video Script: Module 14 — AI Security and Privacy

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Production Notes

- **Runtime Target:** 28–32 minutes
- **Slide Deck:** M14_Slides.pptx
- **Graphics:** Attack taxonomy diagram; differential privacy illustration; compliance checklist
- **Tone:** Serious but accessible; use concrete attack examples

---

## SEGMENT 1 — Hook and Module Overview (Slides 1–3) [3 min]

[ON CAMERA]

Let me start with a story. In 2017, researchers at MIT demonstrated something that should have alarmed the AI community. They showed that by placing a small, carefully designed sticker on a stop sign, they could fool a state-of-the-art computer vision system into classifying it as a speed limit sign. The sticker was imperceptible to a human standing five feet away. To the AI, it was decisive.

This is an adversarial attack. And it is not just an academic toy — this class of vulnerability applies to medical imaging AI, financial fraud models, voice assistants, and any other AI system you can name.

Welcome to Module 14. This is the security and privacy module, and it is one of the most important modules in this course for anyone planning a career in AI engineering, AI governance, or cybersecurity.

[SLIDE 1: Title — "AI Security and Privacy"]

[SLIDE 2: Module Learning Objectives]

By the end of this module you will be able to:

- Describe the major categories of adversarial attacks on AI systems
- Explain data poisoning and model inversion attacks
- Define differential privacy and explain its protective mechanism
- Describe secure AI deployment practices
- Identify AI-specific compliance requirements under GDPR and CCPA

[SLIDE 3: Why AI Security Is Different]

Traditional software security focuses on protecting code, networks, and data from unauthorized access. AI security has an additional dimension: the model itself can be attacked. The attack surface includes not just the systems hosting the model but the model's learned behavior. An attacker does not need to access the server — they can attack through the API.

This distinction is fundamental, and it is why organizations cannot simply apply standard cybersecurity practices to AI systems and consider the job done.

---

## SEGMENT 2 — Adversarial Attacks (Slides 4–9) [7 min]

[SLIDE 4: What Is an Adversarial Attack?]

An adversarial attack is a deliberately crafted input designed to cause an AI model to make an incorrect prediction. The key word is *deliberately* — adversarial inputs are not random noise. They are carefully optimized perturbations that exploit weaknesses in the model's decision boundary.

[SLIDE 5: Types of Adversarial Attacks — Taxonomy]

Let me walk through the taxonomy.

**Evasion Attacks** are the most well-known type. At inference time, an attacker modifies an input to cause misclassification. The stop sign sticker example is an evasion attack. In the digital domain, pixel-level changes to an image invisible to the human eye can flip a neural network's classification with 99.9% confidence.

**Poisoning Attacks** occur at training time. An attacker corrupts the training data so that the resulting model behaves incorrectly in specific, attacker-controlled ways.

**Model Extraction Attacks** involve querying a model's API thousands of times to reconstruct a copy of the model without access to the training data or model weights. The attacker builds a "stolen" model.

**Model Inversion Attacks** use the model's outputs to reconstruct information about the training data — potentially recovering private information about individuals who were in the training set.

[SLIDE 6: Evasion Attack — Deep Dive]

Let's spend a moment on evasion attacks because they are the most immediately impactful.

In an image classification model, an adversarial perturbation is often computed using the model's gradient — mathematically, the attacker asks: "In which direction should I change each pixel to maximize the probability of the wrong class?" This is called the Fast Gradient Sign Method (FGSM), the most basic adversarial attack technique.

More sophisticated attacks use iterative optimization to find the smallest possible perturbation that causes misclassification. These can be entirely imperceptible to human observers.

In physical-world attacks — like the stop sign sticker — perturbations must survive printing, weather, and varying lighting conditions. This is harder, but researchers have demonstrated physical-world attacks that work reliably.

[SLIDE 7: Why Adversarial Examples Exist]

Why are neural networks vulnerable to these imperceptible perturbations? The short answer is that neural networks are high-dimensional interpolation machines. They learn to map inputs to outputs based on patterns in training data, but they do not understand objects the way humans do. The input space is astronomically large, and adversarial examples live in the parts of that space the model was never trained on — even when they are very close in pixel space to legitimate training examples.

[SLIDE 8: Adversarial Examples in High-Stakes Domains]

[GRAPHICS: Case study cards]

Consider these high-stakes attack scenarios:

**Medical imaging:** An adversarial perturbation added to a skin lesion photograph causes a cancer detection model to classify a malignant melanoma as benign. A patient receives no treatment.

**Autonomous vehicles:** A stop sign is misclassified as a yield sign. The vehicle does not stop at an intersection.

**Biometric authentication:** A face recognition system is fooled by a printed mask or adversarially perturbed eyeglasses.

**Spam filters:** An adversarial email crafted to resemble legitimate correspondence evades detection.

[SLIDE 9: Defenses Against Adversarial Attacks]

Several defensive techniques exist, though none is a complete solution.

**Adversarial training:** Include adversarial examples in the training data so the model learns to classify them correctly. This is the most effective general defense but requires knowing the attack method in advance.

**Input preprocessing:** Apply transformations (smoothing, denoising, JPEG compression) to inputs before inference. Some perturbations are destroyed by preprocessing.

**Certified defenses:** Mathematical guarantees that the model's prediction is stable within a defined perturbation radius. These are computationally expensive but provide provable security bounds.

**Ensemble methods:** Use multiple diverse models. An adversarial example crafted to fool one model may not fool all members of an ensemble.

---

## SEGMENT 3 — Data Poisoning (Slides 10–12) [5 min]

[SLIDE 10: What Is Data Poisoning?]

Data poisoning is an attack on the training process. An attacker who can inject malicious examples into the training dataset can cause the resulting model to have backdoor behaviors, reduced accuracy on specific inputs, or systematic misclassifications that serve the attacker's goals.

[SLIDE 11: Backdoor Attacks — The Most Dangerous Poisoning Pattern]

A backdoor attack is a poisoning attack where the attacker inserts a "trigger" into the training data. The model trains normally on all other data, achieving good accuracy. But when the trigger pattern is present in an input, the model produces the attacker's desired output.

Example: A facial recognition system for building access is trained on poisoned data that includes images of legitimate employees with a small watermark. The resulting model grants access to anyone wearing a printed watermark — even a non-employee.

The terrifying aspect of backdoor attacks is that the model appears completely normal during testing. The backdoor only activates in the presence of the specific trigger.

[SLIDE 12: Defending Against Data Poisoning]

Data poisoning defenses include:

**Data provenance controls:** Strict access control and audit trails for training data. Every record should have a source, timestamp, and chain of custody.

**Data validation pipelines:** Statistical anomaly detection on training datasets to flag suspicious clusters of examples.

**Clean-label detection:** Methods to identify outlier examples that may be poisoned without obviously wrong labels.

**Certified training methods:** Differential privacy training (covered next) provides some inherent resistance to poisoning by limiting the influence any single training example can have.

The fundamental defense is never training on data you do not control and trust.

---

## SEGMENT 4 — Model Inversion and Privacy Attacks (Slides 13–15) [4 min]

[SLIDE 13: Model Inversion — Privacy Through the Back Door]

Model inversion attacks reconstruct information about training data using a model's predictions. If a model was trained on sensitive personal data — medical records, financial histories, facial images — an attacker can query the model strategically to recover approximate representations of individuals in the training set.

In a 2015 study, researchers demonstrated model inversion against a facial recognition model: by querying the model with optimization-guided inputs, they reconstructed recognizable faces of individuals from the training set without ever accessing the training data or model weights.

[SLIDE 14: Membership Inference Attacks]

A related attack is **membership inference**: given a trained model, determine whether a specific individual's data was used in training. This is a significant privacy risk for healthcare and financial AI — an attacker could confirm that a specific person was in a medical study's training cohort, revealing that person's medical condition.

Membership inference attacks exploit the fact that models tend to be slightly more confident on training examples than on unseen data.

[SLIDE 15: Privacy-Preserving ML Responses]

Three primary techniques protect against these privacy attacks:

**Differential privacy (detailed in the next segment):** Add calibrated noise to prevent any single individual's data from being reconstructable.

**Federated learning:** Train the model across distributed data sources without centralizing raw data. Covered more deeply in Module 15.

**Secure aggregation:** Cryptographic techniques that allow model updates to be aggregated without revealing individual updates.

---

## SEGMENT 5 — Differential Privacy (Slides 16–19) [4 min]

[SLIDE 16: What Is Differential Privacy?]

Differential privacy (DP) is a mathematical framework that provides a formal privacy guarantee. A mechanism satisfies differential privacy if its output is approximately the same whether or not any single individual's data is included in the computation.

In practice, DP is implemented by adding carefully calibrated random noise to computations — either to the training gradients during ML training or to query results in data analysis.

[SLIDE 17: The Intuition Behind DP]

Imagine you want to compute the average income of a group of employees. If you release the exact average, an attacker who knows all other employees' salaries can infer any one individual's salary exactly.

With differential privacy, you add noise to the average before releasing it. The noise is small enough that the answer is still useful for analysis but large enough that any single individual's contribution is hidden.

The privacy budget parameter, epsilon (ε), controls the tradeoff: small ε means more noise and stronger privacy but less accuracy; large ε means less noise and more accuracy but weaker privacy.

[SLIDE 18: Differential Privacy in Machine Learning]

In ML training, DP is applied through **DP-SGD (Differentially Private Stochastic Gradient Descent)**. During training, gradients are clipped to a maximum norm and then Gaussian noise is added. This limits the influence any individual training example can have on the model weights.

Apple uses differential privacy in iOS to collect aggregate usage statistics without learning about any individual user's behavior. Google uses it in Chrome for browser telemetry. The technique is production-proven at scale.

[SLIDE 19: Differential Privacy Tradeoffs]

DP is not free. The accuracy cost can be significant, particularly for small datasets. A DP model trained on 10,000 records with strong privacy guarantees may perform 5–10% worse than a non-private model. For large datasets, the accuracy penalty shrinks considerably.

The decision to use DP involves a principled tradeoff: how much accuracy loss is acceptable to achieve a given level of privacy protection? There is no universal answer — it depends on the sensitivity of the data and the consequences of privacy failure.

---

## SEGMENT 6 — Secure AI Deployment (Slides 20–22) [3 min]

[SLIDE 20: The Defense-in-Depth Framework for AI]

Secure AI deployment applies the defense-in-depth principle: multiple overlapping layers of protection so that no single failure compromises the entire system.

Layers for AI systems include:

1. **Infrastructure security:** Standard cloud security controls — VNet isolation, private endpoints, IAM, key management
2. **Model security:** Adversarial training, input validation, output filtering
3. **Data security:** Encryption at rest and in transit, access control, audit logging for all data access
4. **API security:** Authentication, rate limiting, input sanitization, anomaly detection on query patterns
5. **Monitoring and alerting:** Detect suspicious query patterns (potential model extraction attempts), output anomalies, and performance degradation

[SLIDE 21: Azure Security Tools for AI]

Azure provides specific security tools for AI deployments:

- **Azure Private Link:** Keeps model endpoints on a private network, inaccessible from the public internet
- **Azure Key Vault:** Manages secrets, API keys, and certificates used by AI services
- **Microsoft Defender for Cloud:** Security posture monitoring for Azure resources including AML workspaces
- **Azure Policy:** Governance guardrails that prevent non-compliant deployments
- **Azure Monitor + Sentinel:** Security event detection and incident response

[SLIDE 22: Red Teaming for AI]

Red teaming — where a dedicated team attempts to attack and break the AI system before deployment — is an emerging practice in AI security. Microsoft has published guidance on AI red teaming as part of its Responsible AI standard.

AI red teams test for adversarial examples, prompt injection (for language models), harmful outputs, and privacy leakage. This is different from traditional penetration testing because the attacks target model behavior, not infrastructure vulnerabilities.

---

## SEGMENT 7 — GDPR and CCPA for AI (Slides 23–26) [4 min]

[SLIDE 23: Why AI Has Special Compliance Challenges]

AI systems process personal data at scale, make automated decisions affecting individuals, and often lack interpretability. These characteristics create specific tensions with privacy regulations that were written for human decision-making processes.

[SLIDE 24: GDPR and AI]

The General Data Protection Regulation (GDPR) applies to any organization processing EU residents' data. Key provisions with AI implications:

**Article 22 — Automated Decision-Making:** Individuals have the right not to be subject to decisions based solely on automated processing that produce significant effects. Organizations must provide a way for individuals to request human review.

**Data Minimization:** AI systems should use only the minimum personal data necessary to achieve their purpose. A recommendation engine does not need your exact home address.

**Right of Explanation:** When an automated decision affects an individual, they have the right to a meaningful explanation of the decision logic. This creates tension with "black box" deep learning models.

**Data Subject Rights:** Right of access, right to rectification, right to erasure. If a person requests deletion of their data, the organization must remove it from training sets — a technically complex requirement.

[SLIDE 25: CCPA and AI]

The California Consumer Privacy Act (CCPA, and its expansion CPRA) applies to organizations serving California residents. Key provisions:

**Right to Know:** Consumers can request a list of personal data categories collected and the business purpose.

**Right to Delete:** Consumers can request deletion of personal data. Like GDPR erasure, this is complex when data has been used in training.

**Right to Opt Out of Sale:** Organizations that sell or share personal data for targeted advertising must provide opt-out mechanisms.

**Sensitive Personal Information:** AI systems processing health, financial, or biometric data have heightened restrictions.

[SLIDE 26: Practical Compliance Steps for AI Teams]

If you are building AI systems with personal data, here is the practical compliance checklist:

1. **Data Inventory:** Catalog every personal data source used in training. Know its sensitivity, jurisdiction of the data subjects, and legal basis for processing.
2. **Privacy Impact Assessment:** Before training a new model, conduct a PIA to identify and mitigate privacy risks.
3. **Data Minimization:** Audit features and remove any personal data not directly necessary for model performance.
4. **Model Explainability:** For any model making consequential automated decisions, implement explainability mechanisms (SHAP values, LIME, attention visualization).
5. **Retention and Deletion Procedures:** Define how long training data is retained and how individual deletion requests are honored.
6. **Consent Documentation:** For any data acquired through user consent, maintain auditable consent records.

---

## SEGMENT 8 — Summary and AI-900 Alignment (Slides 27–28) [2 min]

[SLIDE 27: Module 14 Summary]

We covered a lot of ground today. Adversarial attacks — evasion, poisoning, extraction, and inversion — represent the novel attack surface that AI systems introduce. Differential privacy provides a formal mathematical framework for protecting individual privacy in ML systems. Secure deployment requires defense-in-depth across infrastructure, model, data, and API layers. And regulatory compliance — particularly GDPR and CCPA — imposes specific requirements on organizations using AI with personal data.

[SLIDE 28: AI-900 Alignment and Next Module]

For the AI-900 exam, security and privacy appear within the responsible AI principles domain. Know the six Microsoft responsible AI principles: fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Module 15 covers emerging AI technologies: multimodal AI, AI agents, federated learning, edge AI, and what comes next. See you there.

[END OF VIDEO]

---

*Script prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
