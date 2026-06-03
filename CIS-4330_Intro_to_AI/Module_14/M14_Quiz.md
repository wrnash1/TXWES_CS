# Quiz: Module 14 — AI Security and Privacy

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. The quiz is closed-book and should be completed in 20 minutes.

---

## Questions

**Question 1**

A researcher designs sticker patterns that, when placed on stop signs, cause a self-driving car's computer vision system to classify them as speed limit signs. The stickers are nearly invisible to human observers. What type of adversarial attack is this?

A. Data poisoning attack

B. Model extraction attack

C. Evasion attack

D. Membership inference attack

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Data poisoning corrupts the training dataset before training occurs. The stop sign attack happens at inference time (when the deployed model processes a live input), not at training time.
- **B** is incorrect. Model extraction involves querying a model repeatedly to reconstruct its behavior — it is not about making the model misclassify a specific input.
- **C** is correct. An evasion attack crafts a modified input at inference time to cause misclassification. The adversarial sticker is a physical-world evasion attack.
- **D** is incorrect. Membership inference determines whether a specific record was in the training dataset — it is a privacy attack, not a real-time classification attack.

---

**Question 2**

A company trains a sentiment analysis model and discovers that by making tiny, imperceptible changes to review text, they can flip any negative review to a positive classification. Which defense is most directly targeted at this type of attack?

A. Azure Private Link network isolation

B. Rate limiting on the inference API

C. Adversarial training using generated adversarial text examples

D. Differential privacy applied during model training

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Azure Private Link is a network security control that prevents unauthorized network access — it does not affect how the model classifies adversarially modified inputs.
- **B** is incorrect. Rate limiting prevents bulk queries and model extraction but does not prevent individual adversarial inputs from affecting prediction.
- **C** is correct. Adversarial training augments the training dataset with adversarial examples so the model learns to classify them correctly, making it more robust to this attack.
- **D** is incorrect. Differential privacy protects the privacy of training data records. It adds noise during training to prevent membership inference and model inversion — it does not specifically protect against evasion attacks at inference time.

---

**Question 3**

An attacker systematically queries a deployed machine learning model through its public API, making thousands of carefully chosen requests and recording the outputs. The goal is to build a functionally equivalent copy of the model without accessing the original model weights or training data. What type of attack is this?

A. Backdoor attack

B. Model extraction attack

C. Data poisoning attack

D. Evasion attack

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. A backdoor attack occurs during training — the attacker embeds a hidden trigger in the training data that causes specific behavior at inference time.
- **B** is correct. Model extraction (also called model stealing) uses API queries to reverse-engineer the model's decision boundary and construct a stolen copy.
- **C** is incorrect. Data poisoning corrupts the training dataset — it requires access to the training process, not just the inference API.
- **D** is incorrect. Evasion attacks craft specific inputs to cause misclassification — the goal is a wrong prediction, not building a copy of the model.

---

**Question 4**

A healthcare AI company wants to publish aggregate statistics about patient outcomes to support medical research, while ensuring that no researcher can determine whether any specific individual's data was in the dataset. Which privacy-preserving technique provides a mathematical guarantee of this property?

A. Federated learning

B. Differential privacy

C. Input normalization

D. Model ensembling

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Federated learning keeps raw data distributed across devices or institutions without centralizing it. It reduces data exposure but does not provide a formal mathematical privacy guarantee against inference from published outputs.
- **B** is correct. Differential privacy provides a formal mathematical guarantee: the output (statistics or model) is approximately the same whether or not any individual's data is included. This directly addresses membership inference risk.
- **C** is incorrect. Input normalization is a data preprocessing technique for improving model training — it has no privacy properties.
- **D** is incorrect. Model ensembling combines multiple models to improve accuracy or robustness to adversarial attacks. It does not provide privacy guarantees about training data.

---

**Question 5**

Under GDPR Article 22, when must an organization provide a human review option for an automated AI decision?

A. Only when the model's accuracy falls below 95% on the test set

B. Whenever the AI model uses personal data in any form

C. When the automated decision produces legal or similarly significant effects on an individual

D. Only when the individual explicitly requests information about how the model works

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Article 22 is not triggered by model accuracy levels. It applies based on the consequences of the decision for the individual, not the technical performance of the model.
- **B** is incorrect. Most AI systems use personal data in some form. Article 22 applies specifically when automated decisions produce significant real-world effects, not merely when personal data is used.
- **C** is correct. Article 22 applies when automated processing produces decisions with legal effects (employment, lending, housing decisions) or similarly significant impacts (healthcare, education). The organization must offer human review, explanation, and the ability to contest.
- **D** is incorrect. The right of explanation is triggered by the decision itself, not by the individual proactively requesting information about model internals.

---

**Question 6**

What does the epsilon (ε) parameter control in a differential privacy mechanism?

A. The learning rate used in model training

B. The maximum number of training epochs before the privacy guarantee expires

C. The tradeoff between privacy strength and the accuracy of query results

D. The encryption key length used to protect model weights

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Learning rate is a hyperparameter in gradient descent optimization, unrelated to differential privacy.
- **B** is incorrect. Training epochs are a training configuration parameter. Differential privacy does have a privacy budget that is consumed over training steps, but epsilon does not represent a limit on training epochs.
- **C** is correct. Epsilon is the privacy budget parameter. Smaller epsilon means more noise is added, providing stronger privacy guarantees but reducing the accuracy of statistical results. Larger epsilon means less noise, better accuracy, but weaker privacy.
- **D** is incorrect. Encryption key length is a cryptography concept, not a differential privacy parameter.

---

**Question 7**

An AI company trained a facial recognition model and made the model accessible via a public API. Researchers discover that by making many queries with optimized inputs, they can reconstruct approximate facial images of individuals whose photographs were in the training set. What type of attack is this?

A. Evasion attack

B. Data poisoning attack

C. Membership inference attack

D. Model inversion attack

**Correct Answer: D**

**Distractor Analysis:**

- **A** is incorrect. Evasion attacks modify inputs to cause misclassification at inference time — they do not reconstruct training data.
- **B** is incorrect. Data poisoning attacks corrupt the training dataset — they are training-time attacks, not inference-time attacks.
- **C** is incorrect. Membership inference determines whether a specific individual's data was in the training set — it reveals a yes/no membership fact, not the actual content of training data.
- **D** is correct. Model inversion uses a model's prediction outputs to reconstruct representations of training data, in this case facial images. This is a direct privacy violation because it recovers sensitive personal information from the model.

---

**Question 8**

A company's terms of service stated in 2019 that user data would be used to "improve our services." In 2023, the company trains a new AI model using that same data for a new product line not envisioned in 2019. Under GDPR, what principle may the company be violating?

A. Data minimization

B. Purpose limitation

C. Storage limitation

D. Right to erasure

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Data minimization requires collecting only data necessary for a stated purpose. The violation here is not about the amount of data but about the new purpose.
- **B** is correct. Purpose limitation requires that personal data collected for one purpose not be repurposed for a different, incompatible purpose without new lawful basis or consent. Using 2019 data for a 2023 AI product not covered by the original terms likely violates this principle.
- **C** is incorrect. Storage limitation restricts how long data is retained. If the data is still within its intended retention period, using it is not a storage limitation violation — it is a purpose violation.
- **D** is incorrect. Right to erasure is a data subject right triggered by individual requests, not a principle that a company violates by changing the purpose of data use.

---

**Question 9**

Which of the following is a backdoor attack characteristic that distinguishes it from other poisoning attacks?

A. It causes the model to have uniformly lower accuracy on all test inputs.

B. It requires the attacker to access the model's weights directly.

C. It embeds a hidden trigger so the model behaves normally except when a specific pattern is present in the input.

D. It prevents the model from converging during training.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. A backdoor attack does NOT cause uniform accuracy degradation — that would be easy to detect during evaluation. The model passes all standard tests, appearing completely normal.
- **B** is incorrect. Backdoor attacks are typically training-data attacks — the attacker injects poisoned training examples. They do not require access to model weights.
- **C** is correct. The defining characteristic of a backdoor attack is that the model behaves correctly on all normal inputs, achieving normal accuracy during evaluation, but produces attacker-controlled outputs specifically when the trigger pattern is present.
- **D** is incorrect. A well-designed backdoor attack allows the model to converge normally. If training fails to converge, the attack would be obvious.

---

**Question 10**

Which of the following best describes Microsoft's six responsible AI principles as they relate to AI security and privacy?

A. Technical frameworks for encrypting model weights and protecting API endpoints

B. Legal requirements mandated by the European Union for all AI systems

C. Voluntary guidelines that replace GDPR and CCPA compliance obligations

D. Core values guiding the design, development, and deployment of AI to ensure fairness, reliability, privacy, inclusiveness, transparency, and accountability

**Correct Answer: D**

**Distractor Analysis:**

- **A** is incorrect. The responsible AI principles are high-level ethical and design guidelines, not technical encryption specifications.
- **B** is incorrect. These are Microsoft's internal principles, voluntarily adopted. They are not EU legal mandates. GDPR is the EU legal mandate.
- **C** is incorrect. Responsible AI principles are complementary to GDPR and CCPA compliance, not replacements. Organizations must comply with applicable law regardless of whether they have adopted responsible AI principles.
- **D** is correct. Microsoft's six responsible AI principles — fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability — are ethical guidelines that organizations should embed into AI design and deployment practices throughout the lifecycle.

---

*Quiz prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
