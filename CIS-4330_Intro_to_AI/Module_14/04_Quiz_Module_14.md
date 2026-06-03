# Quiz: Module 14 — AI Security and Privacy

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Instructions

This quiz contains 10 multiple-choice questions. Each question is worth 10 points for a total of 100 points. Select the single best answer for each question. Review your reading guide and video notes before attempting the quiz.

---

## Questions

### Question 1

A researcher adds a tiny, carefully calculated noise pattern to an image of a stop sign. The noise is invisible to humans, but causes an autonomous vehicle's AI system to classify the stop sign as a speed limit sign. This is an example of which attack type?

A) Data poisoning attack

B) Membership inference attack

C) Adversarial evasion attack

D) Model extraction attack

**Correct Answer: C**

**Distractor Analysis:**

- **A — Incorrect.** Data poisoning occurs during the training phase by corrupting training data. This attack happens at inference time against an already-trained model.
- **B — Incorrect.** Membership inference determines whether a data point was in the training set. It does not alter model predictions.
- **C — Correct.** An adversarial evasion attack crafts inputs at inference time to cause misclassification. The perturbation exploits the geometry of the model's decision boundary without modifying the model itself.
- **D — Incorrect.** Model extraction attacks steal model parameters through repeated querying. No prediction theft is occurring here.

---

### Question 2

An attacker gains write access to a company's training data repository and injects thousands of images of a specific person, all labeled as "authorized employee," into a facial recognition training dataset. The model trains normally and achieves normal accuracy, but now grants physical access to that person regardless of actual employment status. This is best described as which type of attack?

A) White-box evasion attack

B) Backdoor poisoning attack

C) Membership inference attack

D) Model inversion attack

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** A white-box evasion attack requires knowledge of model internals and crafts inputs at inference time. The attacker here modified training data, not inference inputs.
- **B — Correct.** A backdoor poisoning attack injects poisoned training examples that associate a trigger (the specific person's face) with a target output (access granted), while the model performs normally on all other inputs.
- **C — Incorrect.** Membership inference is a privacy attack that determines whether a record was in the training set. It does not alter model behavior.
- **D — Incorrect.** Model inversion reconstructs training data by querying a model. The attacker here is injecting data, not extracting it.

---

### Question 3

Which algorithm enables training a neural network with a formal differential privacy guarantee by clipping per-example gradients and adding calibrated Gaussian noise before each parameter update?

A) Federated Averaging (FedAvg)

B) Fast Gradient Sign Method (FGSM)

C) Differentially Private Stochastic Gradient Descent (DP-SGD)

D) Projected Gradient Descent (PGD)

**Correct Answer: C**

**Distractor Analysis:**

- **A — Incorrect.** Federated Averaging is a distributed training algorithm that aggregates model updates from multiple clients. It addresses data locality, not formal privacy guarantees by itself.
- **B — Incorrect.** FGSM is an adversarial attack algorithm used to generate adversarial examples, not a privacy-preserving training method.
- **C — Correct.** DP-SGD (Abadi et al., 2016) clips per-example gradients to a maximum norm and adds Gaussian noise to the aggregate gradient, providing a formal (ε, δ)-differential privacy guarantee on the trained model.
- **D — Incorrect.** PGD is an iterative adversarial attack method, an extension of FGSM. It is not related to differential privacy.

---

### Question 4

Under GDPR Article 22, an EU resident has the right to not be subject to a decision based solely on automated processing when the decision produces a legal or similarly significant effect. Which of the following AI applications is MOST directly constrained by this article?

A) A streaming service recommending movies based on viewing history

B) A spam filter automatically moving emails to the junk folder

C) A bank's AI system automatically approving or denying mortgage applications

D) A search engine ranking results by relevance

**Correct Answer: C**

**Distractor Analysis:**

- **A — Incorrect.** Movie recommendations do not produce legal or similarly significant effects on the individual. Article 22 does not apply.
- **B — Incorrect.** Spam filtering produces a minor, reversible effect (misrouted email) and does not constitute a legal or significantly significant effect triggering Article 22.
- **C — Correct.** A mortgage approval or denial is explicitly a legal or similarly significant effect on the individual. Article 22 requires that the bank provide a mechanism for human review and inform the applicant that automated decision-making is occurring.
- **D — Incorrect.** Search ranking affects visibility of content but does not produce a legal or similarly significant effect on any individual data subject.

---

### Question 5

A data scientist releases aggregate statistics about a hospital patient dataset. She adds Laplace-distributed noise to each statistic before releasing it. The noise magnitude is calibrated so that the privacy budget ε = 0.1. Which statement best describes the privacy guarantee?

A) No individual patient's record is included in the statistics.

B) Each statistic is accurate to within 10 percent of the true value.

C) The output distributions with and without any single patient's record are nearly indistinguishable, bounded by e^0.1.

D) The statistics are encrypted and can only be decrypted by authorized personnel.

**Correct Answer: C**

**Distractor Analysis:**

- **A — Incorrect.** Differential privacy does not exclude individual records from the computation. It adds noise so that the presence or absence of any record has bounded effect on the output.
- **B — Incorrect.** Epsilon is a privacy parameter, not an accuracy bound. The actual accuracy depends on the noise scale relative to the query's sensitivity, not on a fixed percentage.
- **C — Correct.** The formal definition of ε-differential privacy states that for any output set, the probability ratio between outputs computed on adjacent datasets is at most e^ε. With ε = 0.1, e^0.1 ≈ 1.105, meaning outputs are nearly identical regardless of any one person's data.
- **D — Incorrect.** Differential privacy involves adding noise to outputs, not encryption. Encryption protects data in transit and at rest but does not provide statistical privacy guarantees about aggregate releases.

---

### Question 6

A security team discovers that an attacker has been querying their deployed image classification API thousands of times per day with systematically varied inputs, recording the confidence scores returned. The attacker's goal is to reconstruct the model's decision boundaries well enough to build a local copy. This is best described as which attack?

A) Data poisoning

B) Model extraction

C) Adversarial training

D) Differential testing

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Data poisoning corrupts training data. The attacker here is querying a deployed model, not modifying training data.
- **B — Correct.** Model extraction (also called model stealing) involves systematically querying a deployed model to reconstruct its behavior or parameters. The attacker uses the input-output pairs to train a surrogate model that approximates the target.
- **C — Incorrect.** Adversarial training is a defense technique, not an attack. It augments training data with adversarial examples to improve robustness.
- **D — Incorrect.** Differential testing compares model behavior across data subsets to detect poisoning anomalies. It is a defensive analysis technique, not an attack.

---

### Question 7

Researchers demonstrate that by optimizing inputs to maximally activate specific output classes of a medical imaging model, they can reconstruct approximate images resembling patients from the training set. This attack is called:

A) Membership inference

B) Model inversion

C) Evasion attack

D) Backdoor extraction

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Membership inference determines whether a specific record was in the training set (a binary determination). It does not reconstruct the actual data.
- **B — Correct.** Model inversion reconstructs training data by optimizing inputs that maximize model confidence in a target class. Fredrikson et al. (2015) demonstrated this against a pharmacogenetics model, reconstructing approximate patient genomes.
- **C — Incorrect.** An evasion attack crafts inputs to cause misclassification, not to reconstruct training data.
- **D — Incorrect.** "Backdoor extraction" is not a standard attack category. Backdoor attacks implant triggers; they do not involve reconstructing training data.

---

### Question 8

Microsoft's open-source **PyRIT** toolkit is designed for which purpose?

A) Training differentially private deep learning models using DP-SGD

B) Automating red team exercises against generative AI systems, including prompt injection and content policy testing

C) Generating adversarial examples using FGSM and PGD for image classifiers

D) Monitoring deployed Azure ML models for data drift and performance degradation

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** DP-SGD training is supported by TensorFlow Privacy and the OpenDP/SmartNoise toolkit, not PyRIT.
- **B — Correct.** PyRIT (Python Risk Identification Toolkit for generative AI) is Microsoft's open-source tool for automating aspects of generative AI red teaming, including prompt injection, hallucination probing, and content safety evasion testing.
- **C — Incorrect.** Libraries such as Foolbox, ART (Adversarial Robustness Toolbox), and CleverHans are designed for adversarial example generation. PyRIT focuses on generative AI safety and security testing.
- **D — Incorrect.** Azure ML's data drift monitoring is a separate built-in capability of Azure Machine Learning Studio, not a function of PyRIT.

---

### Question 9

An organization trains a customer churn prediction model using data that includes records from California residents. After deployment, a customer submits a CCPA deletion request. Which of the following actions is the organization MOST obligated to consider beyond deleting the raw data record?

A) Retraining the model from scratch immediately to ensure no residual influence remains

B) Assessing whether the trained model has memorized the individual's record and applying machine unlearning if necessary

C) Publishing a model card that discloses the individual was in the training set

D) Converting the model to a federated learning architecture to prevent future CCPA obligations

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Full retraining is one possible remediation but is not the most precise description of the obligation. The organization must first assess whether memorization occurred; if the individual's contribution was negligible (e.g., one record in a large dataset), full retraining may be unnecessary.
- **B — Correct.** CCPA deletion requests extend beyond raw data to the model's learned parameters. The organization must assess whether the model memorized the individual's record and, if so, apply machine unlearning techniques or retrain to remove that influence.
- **C — Incorrect.** Disclosing the individual in a model card would further violate their privacy, not remediate the deletion request.
- **D — Incorrect.** Federated learning changes future data collection architecture but does not address existing memorization in an already-trained model.

---

### Question 10

A model card for an AI hiring tool shows that the model achieves 92 percent overall accuracy but only 74 percent accuracy for candidates from a specific demographic group. According to responsible AI deployment principles, what is the PRIMARY concern raised by this finding?

A) The model has been subjected to a data poisoning attack targeting that demographic group.

B) The model exhibits disparate performance across demographic groups, raising fairness and potential legal compliance concerns.

C) The overall accuracy of 92 percent is too low for production deployment in any HR application.

D) The model card format is non-compliant with GDPR Article 22 and must be revised.

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Performance disparity across demographic groups is a common fairness issue arising from biased training data or feature selection, not necessarily a data poisoning attack. There is no evidence of an attack in this scenario.
- **B — Correct.** A significant performance gap across demographic groups is the defining concern of AI fairness. In a hiring context, this disparity could constitute illegal discrimination under employment law (e.g., Title VII in the US, EECD in the EU) and is precisely the type of issue model cards are designed to surface.
- **C — Incorrect.** Whether 92 percent overall accuracy is acceptable depends on the use case. The primary concern here is not the absolute accuracy level but the performance gap across groups.
- **D — Incorrect.** Model cards are a transparency best practice, not a GDPR-mandated document format. Article 22 requires disclosure of automated decision-making but does not specify model card formatting requirements.

---

## Answer Key

| Question | Answer |
|---|---|
| 1 | C |
| 2 | B |
| 3 | C |
| 4 | C |
| 5 | C |
| 6 | B |
| 7 | B |
| 8 | B |
| 9 | B |
| 10 | B |

---

*Quiz Line Count: 175 | Module 14 — AI Security and Privacy*
