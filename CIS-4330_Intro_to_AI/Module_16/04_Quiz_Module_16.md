# Quiz: Module 16 - Final Exam Prep and Microsoft AI-900 Certification
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
A company wants to add real-time speech-to-text transcription to its customer call center application without training any custom models. Which Azure AI service is most appropriate?
*   A) Azure Machine Learning
*   B) Azure AI Speech (speech-to-text)
*   C) Azure Custom Vision
*   D) Azure AI Language
*   **Correct Answer:** B) Azure AI Speech provides a pre-built speech-to-text capability accessible via REST API or SDK that transcribes spoken audio to written text in real time, with no training data or model development required.
*   **Distractor Analysis:**
    *   *Why correct:* The scenario specifies "no custom models" and a speech input — Azure AI Speech's speech-to-text service is the direct fit. It is one of the five Azure AI workload categories tested on AI-900.
    *   Azure Machine Learning is for building and training custom models, not for pre-built speech transcription. Azure Custom Vision is an image classifier training service. Azure AI Language handles text-based NLP tasks (sentiment, key phrases, intent) — not audio input.

---

**Question 2**
In the context of the AI-900 exam, which of the following is the most accurate definition of **Retrieval-Augmented Generation (RAG)**?
*   A) A generative AI pattern that retrieves relevant passages from an external knowledge source at query time and injects them into the LLM's prompt as context, grounding the model's response in factual source documents and reducing hallucination.
*   B) A supervised learning technique that continues training a pre-trained language model's weights on a smaller domain-specific dataset to specialize its knowledge for a particular task or writing style.
*   C) A text representation method that converts words or sentences into dense numeric vectors encoding semantic meaning, enabling similarity comparisons between documents using cosine distance.
*   D) A neural network training algorithm that calculates the gradient of the loss function with respect to each weight and propagates the error signal backward through the network to update weights via gradient descent.
*   **Correct Answer:** A) A generative AI pattern that retrieves relevant passages from an external knowledge source at query time and injects them into the LLM's prompt as context, grounding the model's response in factual source documents and reducing hallucination.
*   **Distractor Analysis:**
    *   *Why A is correct:* RAG solves the hallucination problem by giving the LLM access to current, specific source material through the prompt rather than relying solely on training data. It is the primary pattern for enterprise LLM deployments requiring factual accuracy.
    *   *Why B is incorrect:* This describes **fine-tuning** — adapting a model's weights with domain-specific training data, which is a different (more expensive) approach to specialization.
    *   *Why C is incorrect:* This describes **embeddings** — vector representations of text used for semantic search; embeddings are often used as part of a RAG system, but they are not RAG itself.
    *   *Why D is incorrect:* This describes **backpropagation** — the neural network training algorithm, which is unrelated to the RAG inference-time retrieval pattern.

---

**Question 3**
A developer needs to **calculate the accuracy of model predictions against actual test labels**. Which command is most appropriate?
*   A) accuracy = accuracy_score(y_test, predictions)
*   B) model.fit(X_train, y_train)
*   C) predictions = model.predict(X_test)
*   D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) accuracy = accuracy_score(y_test, predictions)
*   **Distractor Analysis:**
    *   *Why A is correct:* `accuracy_score(y_test, predictions)` compares the model's predicted labels to the true test labels and returns the fraction that are correct — the standard step for evaluating classification performance after prediction.
    *   *Why B is incorrect:* `model.fit()` trains the model on labeled data; it does not compute an accuracy metric.
    *   *Why C is incorrect:* `model.predict()` generates predictions from a trained model; predictions must exist before accuracy can be computed.
    *   *Why D is incorrect:* This loads a CSV file into a DataFrame — data loading, the first step in the pipeline, not evaluation.

---

**Question 4**
An organization's AI content moderation system flags user-uploaded images. Auditors find the system produces a much higher false positive rate (incorrectly flagging acceptable content) for images submitted by users in certain geographic regions compared to others. Which Responsible AI principle is most clearly being violated, and what is the recommended action?
*   A) Fairness — audit the training dataset for geographic representation gaps, apply fairness-aware evaluation metrics stratified by region, and retrain with a more geographically balanced dataset before redeployment.
*   B) Reliability and Safety — improve the model's overall accuracy by gathering more training data from all regions and retraining to reduce the aggregate false positive rate.
*   C) Transparency — publish a detailed public report explaining the model's architecture, training data sources, and known performance limitations so affected users understand how decisions are made.
*   D) Privacy and Security — encrypt all uploaded images at rest and in transit and restrict access logs to authorized compliance personnel only.
*   **Correct Answer:** A) Fairness — audit the training dataset for geographic representation gaps, apply fairness-aware evaluation metrics stratified by region, and retrain with a more geographically balanced dataset before redeployment.
*   **Distractor Analysis:**
    *   *Why A is correct:* Disparate error rates across demographic or geographic groups is a Fairness violation. The root cause is typically underrepresentation of certain groups in training data. The fix requires group-stratified evaluation and a more balanced training dataset.
    *   *Why B is incorrect:* Reliability addresses inconsistent performance across operating conditions — improving aggregate accuracy without addressing group disparity would not resolve the Fairness violation and might actually widen the performance gap.
    *   *Why C is incorrect:* Transparency (publishing explanations) improves openness but does not address the discriminatory error rate pattern that the Fairness principle requires fixing.
    *   *Why D is incorrect:* Privacy and Security addresses data protection — encrypting images has no effect on the model's biased output distribution across geographic groups.

---

**Question 5**
A healthcare organization deploys an Azure OpenAI Service application that answers clinical questions by retrieving relevant passages from internal medical guidelines. Security researchers discover that crafted user messages can override the system prompt and cause the model to ignore its safety instructions. Which defense best mitigates this **prompt injection** attack?
*   A) Avoid embedding critical safety logic solely in the system prompt; implement output content filtering using Azure OpenAI's built-in content safety features; and monitor for anomalous response patterns that suggest instruction override.
*   B) Apply differential privacy to the medical guidelines training data and rate-limit the number of questions users can submit per session.
*   C) Enable full disk encryption on all Azure compute nodes hosting the OpenAI Service deployment.
*   D) Require clinicians to complete multi-factor authentication before accessing the clinical question-answering application.
*   **Correct Answer:** A) Avoid embedding critical safety logic solely in the system prompt; implement output content filtering using Azure OpenAI's built-in content safety features; and monitor for anomalous response patterns that suggest instruction override.
*   **Distractor Analysis:**
    *   *Why A is correct:* Prompt injection exploits the LLM's instruction-following behavior to override the system prompt via user input. The mitigations are architectural: keep sensitive rules out of the easily-overridable system prompt, use Azure OpenAI's content safety layer to filter outputs, and monitor for responses that deviate from expected patterns.
    *   *Why B is incorrect:* Differential privacy defends against training data reconstruction via model inversion — it does not prevent a deployed model from following injected instructions in user input at inference time.
    *   *Why C is incorrect:* Disk encryption protects data at rest on compute nodes; it has no effect on a language model producing unsafe outputs in response to crafted prompts.
    *   *Why D is incorrect:* MFA authenticates the user's identity but does not prevent an authenticated clinician (or an attacker with stolen credentials) from submitting prompt injection payloads to the application.
