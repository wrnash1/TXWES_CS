# Quiz: Module 09 - Azure Bot Service and Conversational AI
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which computer vision task involves identifying both the locations and classes of multiple objects inside an image using bounding boxes?
*   A) Image Classification
*   B) Object Detection
*   C) Semantic Segmentation
*   D) Optical Character Recognition
*   **Correct Answer:** B) Object detection locates each object in an image with a bounding box and assigns a class label to it, returning both position and identity for every detected instance.
*   **Distractor Analysis:**
    *   *Why correct:* Object detection returns bounding box coordinates plus a class label for every object found — it answers "what is where?" rather than just "what is in the image?"
    *   Classification assigns a single label to the whole image. Semantic segmentation labels every pixel. OCR reads and transcribes printed or handwritten text.

---

**Question 2**
In the context of Azure conversational AI, which of the following is the most accurate definition of **intent recognition**?
*   A) The process of identifying what a user wants to accomplish from a natural language utterance — for example, recognizing that "Book me a flight to Dallas" expresses a BookFlight intent — so a bot can take the appropriate action.
*   B) A technique that converts spoken audio into a written text transcript in real time, enabling voice-driven applications to process spoken commands as text strings.
*   C) A cloud service that translates text from one language to another (e.g., Spanish to English) using neural machine translation models, without understanding the meaning or intent of the content.
*   D) An image preprocessing step that resizes and normalizes pixel values before passing them to a convolutional neural network for classification.
*   **Correct Answer:** A) The process of identifying what a user wants to accomplish from a natural language utterance — for example, recognizing that "Book me a flight to Dallas" expresses a BookFlight intent — so a bot can take the appropriate action.
*   **Distractor Analysis:**
    *   *Why A is correct:* Intent recognition is the core function of Azure AI Language's Conversational Language Understanding (CLU) — it maps free-form user input to a predefined intent category that the bot can act on.
    *   *Why B is incorrect:* This describes Azure AI Speech's speech-to-text capability — audio transcription, not intent extraction from text.
    *   *Why C is incorrect:* This describes Azure Translator — language-to-language translation, which moves text between languages without inferring user intent.
    *   *Why D is incorrect:* This describes image normalization — a computer vision preprocessing step entirely unrelated to conversational AI or natural language understanding.

---

**Question 3**
A developer needs to **calculate the accuracy of model predictions against actual test labels**. Which command is most appropriate?
*   A) accuracy = accuracy_score(y_test, predictions)
*   B) model.fit(X_train, y_train)
*   C) predictions = model.predict(X_test)
*   D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) accuracy = accuracy_score(y_test, predictions)
*   **Distractor Analysis:**
    *   *Why A is correct:* `accuracy_score(y_test, predictions)` compares the model's predicted labels against the true test labels and returns the fraction that match — the standard way to evaluate classification performance.
    *   *Why B is incorrect:* `model.fit()` trains the model on labeled training data; it does not compute a performance metric.
    *   *Why C is incorrect:* `model.predict()` generates predictions from a trained model; it does not compute accuracy.
    *   *Why D is incorrect:* This loads a CSV file into a DataFrame — data loading, not evaluation.

---

**Question 4**
A bot's intent recognition model returns suspiciously high accuracy on the validation set. Investigation reveals the text vectorizer (TF-IDF) was fitted on the combined train and test utterances before splitting. What is this problem and how should it be fixed?
*   A) Data leakage — fit the TF-IDF vectorizer only on training utterances using `.fit_transform()`, then apply `.transform()` to the test set separately to prevent test vocabulary from influencing the training representation.
*   B) Overfitting — add more training utterances or apply dropout regularization to reduce the model's sensitivity to noise in the training data.
*   C) Class imbalance — use oversampling (SMOTE) or class weights to ensure rare intents are represented equally during training.
*   D) Underfitting — increase the number of features or switch to a more complex model such as a transformer-based language model.
*   **Correct Answer:** A) Data leakage — fit the TF-IDF vectorizer only on training utterances using `.fit_transform()`, then apply `.transform()` to the test set separately to prevent test vocabulary from influencing the training representation.
*   **Distractor Analysis:**
    *   *Why A is correct:* Fitting a vectorizer on the full dataset allows test-set vocabulary statistics to influence how training features are constructed, making the model appear more accurate on test data than it truly is on real unseen inputs.
    *   *Why B is incorrect:* Overfitting produces high training accuracy but lower validation accuracy — the opposite of the suspiciously high validation accuracy described here.
    *   *Why C is incorrect:* Class imbalance causes the model to favor majority-class intents; it does not inflate validation accuracy from improper preprocessing.
    *   *Why D is incorrect:* Underfitting produces uniformly low accuracy on both training and validation sets — not inflated validation scores.

---

**Question 5**
Attackers are querying a public bot's language understanding API with thousands of carefully crafted utterances to reconstruct the private training data (including proprietary FAQ content). Which defense best mitigates this **model inversion** attack?
*   A) Apply differential privacy to the training data and rate-limit the public inference API to reduce the attacker's ability to extract information through repeated queries.
*   B) Train the model with adversarial utterances included in the training set and validate all inputs for anomalous patterns before inference.
*   C) Enable full disk encryption on all client endpoints submitting queries to the bot API.
*   D) Enforce role-based access control (RBAC) on the Azure Bot Service resource so only approved Azure AD principals can manage the bot configuration.
*   **Correct Answer:** A) Apply differential privacy to the training data and rate-limit the public inference API to reduce the attacker's ability to extract information through repeated queries.
*   **Distractor Analysis:**
    *   *Why A is correct:* Differential privacy adds calibrated statistical noise to training data, making it mathematically difficult to reconstruct individual records from model outputs. Rate-limiting restricts how many queries an attacker can submit, slowing or blocking the reconstruction attempt entirely.
    *   *Why B is incorrect:* Adversarial training builds robustness against perturbed inputs designed to cause misclassification — it does not protect training data from being reverse-engineered through output analysis.
    *   *Why C is incorrect:* Disk encryption protects data stored on a device at rest; it has no effect on information leaked through the bot's live API responses.
    *   *Why D is incorrect:* RBAC restricts who can manage the bot's Azure configuration, not who can query the public inference endpoint — it does not prevent an attacker from extracting training data through API outputs.
