# Quiz: Module 15 - AI Security and Privacy
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
How is a trained machine learning model typically exposed to client applications in a production deployment?
*   A) As a raw Python script file that clients download and execute locally
*   B) As a web-accessible REST API endpoint that accepts JSON input and returns JSON predictions
*   C) Via a direct SQL database connection where clients query prediction results from a table
*   D) As an email attachment containing the serialized model file
*   **Correct Answer:** B) Models are deployed inside containerized web services that expose REST API endpoints — clients send feature data as a JSON POST request and receive predictions in return, enabling language-agnostic integration at scale.
*   **Distractor Analysis:**
    *   *Why correct:* REST API deployment decouples the model from the client application, enables authentication, supports horizontal scaling, and is the standard pattern used by Azure Machine Learning real-time endpoints and Azure Cognitive Services.
    *   Distributing raw script files or SQL connections creates serious security, versioning, and scalability problems. Email attachments are not a deployment mechanism for production inference services.

---

**Question 2**
In the context of AI security, which of the following is the most accurate definition of a **model inversion attack**?
*   A) An attack in which an adversary repeatedly queries a public model API and analyzes the output probabilities to reconstruct sensitive private data that was used to train the model.
*   B) An attack in which an adversary adds imperceptible perturbations to input data (such as pixel noise in an image) to cause the model to make incorrect predictions with high confidence.
*   C) An attack in which an adversary corrupts a portion of the training dataset before model training to cause the resulting model to behave incorrectly on specific inputs chosen by the attacker.
*   D) An attack in which an adversary crafts a carefully structured user input to override a language model's system prompt instructions and cause the model to follow the attacker's instructions instead.
*   **Correct Answer:** A) An attack in which an adversary repeatedly queries a public model API and analyzes the output probabilities to reconstruct sensitive private data that was used to train the model.
*   **Distractor Analysis:**
    *   *Why A is correct:* Model inversion exploits the information encoded in a model's learned weights — accessible through output confidence scores — to reverse-engineer training examples. Differential privacy and API rate-limiting are the primary defenses.
    *   *Why B is incorrect:* This describes an **adversarial example** attack — perturbing inputs at inference time to cause misclassification. Defense: adversarial training and input filtering.
    *   *Why C is incorrect:* This describes a **data poisoning** attack — corrupting the training set to manipulate model behavior at a specific trigger. Defense: data validation and provenance controls.
    *   *Why D is incorrect:* This describes a **prompt injection** attack — specific to LLMs, where crafted user input overrides system instructions. Defense: output filtering and keeping sensitive logic outside the prompt.

---

**Question 3**
A developer needs to **train a machine learning model on labeled training data**. Which command is most appropriate?
*   A) model.fit(X_train, y_train)
*   B) predictions = model.predict(X_test)
*   C) accuracy = accuracy_score(y_test, predictions)
*   D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    *   *Why A is correct:* `model.fit(X_train, y_train)` passes the feature matrix and target labels to the model, allowing it to learn the input-output mapping through the training algorithm.
    *   *Why B is incorrect:* `model.predict()` generates predictions from a trained model; `fit()` must be called first before prediction is possible.
    *   *Why C is incorrect:* `accuracy_score()` evaluates predictions against true labels — an evaluation step that requires predictions to already exist.
    *   *Why D is incorrect:* This loads a CSV file into a DataFrame — data loading, which occurs at the beginning of the pipeline before any model training.

---

**Question 4**
A security team discovers that an external researcher submitted 50,000 queries to a public medical AI classifier and used the returned diagnosis probabilities to reconstruct individual patient health records from the training data. Which combination of controls would most directly prevent this attack in future deployments?
*   A) Apply differential privacy during model training to add statistical noise to the learned weights, and enforce strict API rate-limiting to cap the number of queries any single client can submit per time period.
*   B) Train the model with adversarially perturbed patient records included in the training set and add input validation to reject malformed feature vectors.
*   C) Enable full disk encryption on all servers hosting the model and require TLS 1.3 for all API connections.
*   D) Deploy the model behind Azure Private Link so only internal hospital network traffic can reach the inference endpoint.
*   **Correct Answer:** A) Apply differential privacy during model training to add statistical noise to the learned weights, and enforce strict API rate-limiting to cap the number of queries any single client can submit per time period.
*   **Distractor Analysis:**
    *   *Why A is correct:* This is a model inversion attack. Differential privacy degrades the statistical signal an attacker can extract from outputs by injecting noise into training. Rate-limiting restricts how many queries the attacker can submit, making reconstruction computationally infeasible.
    *   *Why B is incorrect:* Adversarial training and input validation defend against adversarial example attacks (perturbed inference inputs) — not against an attacker mining training data from API outputs over thousands of legitimate-looking queries.
    *   *Why C is incorrect:* Disk encryption and TLS protect data in transit and at rest, but they do not prevent an authenticated client from extracting training data through the model's output distribution via a large number of normal API calls.
    *   *Why D is incorrect:* Private Link restricts network access, but the attack was conducted by an external researcher through a public API — the correct response is to limit what can be inferred from the outputs themselves, not just who can reach the endpoint.

---

**Question 5**
An organization's deployed image classifier is being targeted by attackers who send images with specially crafted pixel-level noise, causing the model to misclassify dangerous objects as benign with high confidence. Which defense best mitigates this **adversarial example** attack?
*   A) Train the model with adversarial examples included in the training set and implement input pre-processing filters that detect and reject images with statistically anomalous pixel distributions before inference.
*   B) Apply differential privacy to the training image dataset and rate-limit the public inference API to reduce query volume.
*   C) Enable full disk encryption on all edge devices that submit images to the classification endpoint.
*   D) Enforce multi-factor authentication on all accounts with permission to retrain or redeploy the model.
*   **Correct Answer:** A) Train the model with adversarial examples included in the training set and implement input pre-processing filters that detect and reject images with statistically anomalous pixel distributions before inference.
*   **Distractor Analysis:**
    *   *Why A is correct:* Adversarial training teaches the model to correctly classify both clean and perturbed inputs by exposing it to crafted examples during training. Pre-processing filters provide a second line of defense by detecting and blocking anomalous images before they reach the classifier.
    *   *Why B is incorrect:* Differential privacy defends against model inversion (training data reconstruction) — not adversarial perturbations applied to inference inputs. These are distinct attack types requiring different defenses.
    *   *Why C is incorrect:* Disk encryption protects image data stored on edge devices at rest; it has no effect on manipulated images submitted through a live API connection.
    *   *Why D is incorrect:* MFA secures accounts that manage the model pipeline but does not prevent an external attacker from submitting adversarially crafted images through the public inference endpoint.
