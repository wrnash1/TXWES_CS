# Quiz: Module 11 - Azure OpenAI Service and Generative AI
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What core neural network architecture is the foundation for modern Large Language Models (LLMs) like GPT-4?
*   A) Convolutional Neural Network (CNN)
*   B) Recurrent Neural Network (RNN)
*   C) Transformer
*   D) Support Vector Machine (SVM)
*   **Correct Answer:** C) Transformers use self-attention mechanisms to process all tokens in a sequence simultaneously, capturing long-range dependencies and enabling training on massive datasets — which is why they replaced RNNs as the dominant LLM architecture.
*   **Distractor Analysis:**
    *   *Why correct:* The Transformer's parallel processing and self-attention allow it to scale to billions of parameters, which is what makes GPT, BERT, and similar LLMs possible.
    *   CNNs are designed for grid-like data such as images. RNNs process sequences one step at a time and suffer from vanishing gradients over long sequences. SVMs are shallow linear classifiers with no generative capability.

---

**Question 2**
In the context of generative AI and LLMs, which of the following is the most accurate definition of **fine-tuning**?
*   A) The process of continuing to train a pre-trained model's weights on a smaller, task-specific dataset so the model specializes in a particular domain or style without being trained from scratch.
*   B) The practice of crafting input prompts with clear instructions, context, and examples to guide a frozen pre-trained model toward a desired output without modifying any model weights.
*   C) A technique that converts text into dense numeric vectors encoding semantic meaning, enabling similarity comparisons between documents using distance metrics like cosine similarity.
*   D) A neural network mechanism that allows each token in a sequence to dynamically weigh the relevance of every other token, enabling the model to capture long-range contextual dependencies.
*   **Correct Answer:** A) The process of continuing to train a pre-trained model's weights on a smaller, task-specific dataset so the model specializes in a particular domain or style without being trained from scratch.
*   **Distractor Analysis:**
    *   *Why A is correct:* Fine-tuning updates the model's weights using domain-specific examples (e.g., medical records, legal documents), producing a more specialized model than prompt engineering alone can achieve.
    *   *Why B is incorrect:* This describes **prompt engineering** — guiding a model's outputs through carefully designed input text, with no weight updates.
    *   *Why C is incorrect:* This describes **embeddings** — numeric vector representations of text used for semantic search and retrieval, not model adaptation.
    *   *Why D is incorrect:* This describes the **self-attention mechanism** within the Transformer architecture, not the fine-tuning training process.

---

**Question 3**
A developer needs to **load a tabular dataset from a CSV file using the Pandas library**. Which command is most appropriate?
*   A) import pandas as pd; df = pd.read_csv('data.csv')
*   B) model.fit(X_train, y_train)
*   C) predictions = model.predict(X_test)
*   D) accuracy = accuracy_score(y_test, predictions)
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    *   *Why A is correct:* `pd.read_csv()` reads a CSV file from disk into a Pandas DataFrame, which is the standard first step in any Python ML data pipeline.
    *   *Why B is incorrect:* `model.fit()` trains a model on already-loaded data; it does not load data from a file.
    *   *Why C is incorrect:* `model.predict()` generates predictions from a trained model; data must already be loaded and the model already fitted.
    *   *Why D is incorrect:* `accuracy_score()` evaluates predictions against true labels — an evaluation step that occurs after loading, training, and predicting.

---

**Question 4**
An LLM deployed via Azure OpenAI Service is generating confident but factually incorrect answers about a company's internal product catalog. The model has no access to the catalog documents. What is the most effective fix?
*   A) Implement Retrieval-Augmented Generation (RAG) — embed the product catalog documents, retrieve the most relevant passages at query time, and inject them into the prompt as context so the model grounds its answers in actual catalog content.
*   B) Fine-tune the model on a dataset of question-answer pairs derived from the product catalog to encode catalog knowledge directly into the model's weights.
*   C) Apply L2 regularization to the model's output layer to reduce its confidence in low-probability tokens and suppress hallucinated content.
*   D) Increase the model's temperature parameter above 1.0 to generate more diverse and exploratory responses that are less likely to repeat incorrect patterns.
*   **Correct Answer:** A) Implement Retrieval-Augmented Generation (RAG) — embed the product catalog documents, retrieve the most relevant passages at query time, and inject them into the prompt as context so the model grounds its answers in actual catalog content.
*   **Distractor Analysis:**
    *   *Why A is correct:* Hallucinations occur when the model lacks relevant information and generates plausible-sounding but false content. RAG solves this by providing the correct source material in the prompt context, giving the model factual grounding without retraining.
    *   *Why B is incorrect:* Fine-tuning on a static catalog dataset would help but requires significant effort and the catalog can go out of date; RAG is the faster, more maintainable solution for grounding LLMs in live documents.
    *   *Why C is incorrect:* L2 regularization is a training-time technique for reducing weight magnitudes to prevent overfitting — it has no effect on hallucination at inference time and cannot be applied post-deployment.
    *   *Why D is incorrect:* Raising the temperature increases randomness and creative variation in outputs, which would likely increase hallucination rather than reduce it.

---

**Question 5**
Attackers are submitting thousands of specially crafted prompts to an Azure OpenAI Service deployment, attempting to extract the confidential system prompt and proprietary few-shot examples embedded in it. Which defense best mitigates this **prompt injection / system prompt extraction** attack?
*   A) Avoid placing sensitive business logic or proprietary data directly in the system prompt; use output filtering to detect and block responses that appear to be reproducing the system prompt; and monitor for anomalous query patterns.
*   B) Apply differential privacy to the training data and rate-limit the public inference API to reduce the attacker's query volume.
*   C) Enable full disk encryption on all Azure VMs hosting the OpenAI model deployment.
*   D) Rotate the Azure OpenAI API key every 30 days and enforce TLS 1.3 on all API connections.
*   **Correct Answer:** A) Avoid placing sensitive business logic or proprietary data directly in the system prompt; use output filtering to detect and block responses that appear to be reproducing the system prompt; and monitor for anomalous query patterns.
*   **Distractor Analysis:**
    *   *Why A is correct:* System prompt extraction exploits the model's instruction-following behavior to reveal the prompt itself. The mitigations are architectural: keep secrets out of prompts, filter outputs for prompt leakage, and detect high-volume probing behavior.
    *   *Why B is incorrect:* Differential privacy defends against training data reconstruction via model inversion — not against a deployed model repeating its system prompt in response to crafted queries.
    *   *Why C is incorrect:* Disk encryption protects data stored on Azure VMs at rest; it has no effect on an LLM revealing its system prompt through its text outputs at inference time.
    *   *Why D is incorrect:* API key rotation and TLS protect the transport layer and authenticate callers, but they do not prevent an authenticated caller from using prompt injection to extract the system prompt.
