# Quiz: Module 01 - Introduction to AI and Machine Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe Artificial Intelligence workloads and considerations
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

Which statement most accurately describes the relationship between artificial intelligence, machine learning, and deep learning?

- A) They are three separate and unrelated fields that solve different problems.
- B) Deep learning is the broadest category, with machine learning and AI as subsets.
- C) Machine learning is a subset of AI, and deep learning is a subset of machine learning.
- D) Artificial intelligence and machine learning are synonyms; deep learning is an unrelated neuroscience concept.

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* AI is the broadest umbrella. ML is a subset of AI that learns from data. Deep learning is a subset of ML that uses multi-layer neural networks. This nested hierarchy is explicitly tested on AI-900.
- *Why A is incorrect:* The three are hierarchically related, not separate fields.
- *Why B is incorrect:* This inverts the correct hierarchy. Deep learning is the most specialized, not the broadest.
- *Why D is incorrect:* AI and machine learning are distinct concepts. AI predates ML and includes rule-based systems that do not learn.

---

## Question 2

A developer writes a program with hundreds of explicit if-then rules to determine whether a loan application should be approved. No data training occurs. Which category best describes this system?

- A) Deep learning
- B) Unsupervised machine learning
- C) Traditional rule-based AI
- D) Reinforcement learning

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Rule-based expert systems that follow hand-coded logic are a form of traditional AI. They do not learn from data. This distinction is fundamental to the AI-900 first domain.
- *Why A is incorrect:* Deep learning requires neural networks and training data. No learning occurs in this scenario.
- *Why B is incorrect:* Unsupervised learning discovers patterns in unlabeled data. Writing explicit rules is not a learning process at all.
- *Why D is incorrect:* Reinforcement learning requires an agent, an environment, and a reward signal. None of these are present.

---

## Question 3

A company trains a model using 50,000 customer transaction records, each labeled as either "fraudulent" or "legitimate." The model learns to predict the label for new transactions. Which learning paradigm does this represent?

- A) Unsupervised learning
- B) Reinforcement learning
- C) Transfer learning
- D) Supervised learning

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* The training data includes input features and explicit output labels (fraudulent / legitimate). This is the defining characteristic of supervised learning.
- *Why A is incorrect:* Unsupervised learning has no labels. The word "labeled" in the scenario eliminates this option.
- *Why B is incorrect:* Reinforcement learning uses a reward signal from environmental interaction, not labeled historical records.
- *Why C is incorrect:* Transfer learning is a technique for reusing a pretrained model; it is not a fundamental learning paradigm. It was not described in this scenario.

---

## Question 4

Which of the following scenarios is the best example of a regression task?

- A) Classifying news articles as politics, sports, entertainment, or technology.
- B) Determining whether a patient has diabetes based on lab results.
- C) Predicting the closing stock price of a company at the end of each trading day.
- D) Identifying whether an email is spam or not spam.

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Stock price is a continuous numerical value. Predicting a continuous output is the definition of a regression task.
- *Why A is incorrect:* Classifying articles into discrete categories is a multi-class classification task.
- *Why B is incorrect:* Determining whether a patient has or does not have a condition is binary classification.
- *Why D is incorrect:* Spam / not spam is binary classification. The output is a discrete category, not a continuous number.

---

## Question 5

A data science team builds a model to segment website visitors into behavioral groups without any predetermined labels or known group definitions. Which learning paradigm does this represent?

- A) Supervised learning
- B) Reinforcement learning
- C) Unsupervised learning
- D) Semi-supervised learning

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Discovering group structure in data without labels is clustering — the primary unsupervised learning task. "Without any predetermined labels" is the key phrase.
- *Why A is incorrect:* Supervised learning requires labels. No labels are present in this scenario.
- *Why B is incorrect:* Reinforcement learning requires an agent-environment interaction loop, not website visitor data.
- *Why D is incorrect:* Semi-supervised learning uses a small number of labels combined with large amounts of unlabeled data. This scenario has no labels at all.

---

## Question 6

An organization needs to add real-time language translation to its customer support chat platform. They have no machine learning expertise, no labeled translation data, and need to ship the feature within two weeks. Which Azure service tier is the best fit?

- A) Azure Machine Learning
- B) Azure Cognitive Services
- C) Azure Databricks
- D) Azure DevOps

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Cognitive Services — specifically Azure Translator — provides prebuilt language translation via REST API with no custom training required. This matches the scenario constraints: no ML expertise, no training data, fast delivery.
- *Why A is incorrect:* Azure Machine Learning is for building custom models. It requires data science expertise and training data.
- *Why C is incorrect:* Azure Databricks is a data engineering and analytics platform, not an AI API service.
- *Why D is incorrect:* Azure DevOps is a software development lifecycle tool with no AI translation capability.

---

## Question 7

A hiring algorithm trained on 10 years of historical hiring decisions consistently recommends rejecting applications from candidates who graduated from certain universities. An audit reveals that the historical data reflects past biases in the hiring process, not actual job performance. Which Microsoft responsible AI principle is most directly violated?

- A) Reliability and Safety
- B) Inclusiveness
- C) Transparency
- D) Fairness

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* The algorithm perpetuates bias from historical data, resulting in inequitable treatment of candidates based on factors unrelated to job performance. This is a direct violation of the Fairness principle.
- *Why A is incorrect:* Reliability and Safety addresses consistent performance and harm prevention, not discriminatory bias.
- *Why B is incorrect:* Inclusiveness focuses on designing systems that benefit all people, particularly those with disabilities or underserved populations. Bias in hiring is a fairness issue.
- *Why C is incorrect:* Transparency addresses whether the system is understandable and explainable. The bias problem would persist even if the algorithm were fully explained.

---

## Question 8

Which of the following is the primary reason deep learning typically requires more training data than traditional machine learning algorithms?

- A) Deep learning uses a programming language that processes data more slowly.
- B) Deep learning networks have millions of parameters that must be estimated from data, requiring more examples to avoid overfitting.
- C) Deep learning algorithms are designed to run only on Azure and cannot access local data.
- D) Deep learning produces less accurate results and therefore requires redundant data copies.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Deep neural networks have enormous numbers of trainable parameters — sometimes billions. Each parameter requires sufficient data to be estimated reliably. With insufficient data, the network memorizes training examples rather than generalizing.
- *Why A is incorrect:* Deep learning frameworks such as PyTorch and TensorFlow process data using GPU acceleration, often faster than traditional algorithms. Data volume requirements are not related to processing speed.
- *Why C is incorrect:* Deep learning frameworks run locally, in the cloud, and on Azure. Platform constraints do not determine data requirements.
- *Why D is incorrect:* Deep learning often achieves higher accuracy than traditional ML on large unstructured datasets. Lower accuracy is not its characteristic.

---

## Question 9

A pharmaceutical researcher wants to train a custom molecular property prediction model using proprietary chemical data, track 200 training experiments, compare model architectures, and deploy the winning model as a REST endpoint. Which Azure service is the most appropriate choice?

- A) Azure Cognitive Services
- B) Azure Bot Service
- C) Azure Machine Learning
- D) Azure Form Recognizer

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Machine Learning provides custom model training, experiment tracking, model comparison, and endpoint deployment. All four requirements align directly with Azure ML capabilities.
- *Why A is incorrect:* Azure Cognitive Services provides prebuilt AI APIs. It does not support custom model training or experiment tracking.
- *Why B is incorrect:* Azure Bot Service builds conversational chatbots. It is irrelevant to molecular property prediction.
- *Why D is incorrect:* Azure Form Recognizer extracts structured fields from documents. It does not support custom scientific model training.

---

## Question 10

A game development studio is building an AI opponent for a strategy game. The AI learns by playing millions of games against itself, receiving a reward when it wins and a penalty when it loses. Over time, the AI discovers winning strategies without being programmed with any explicit game knowledge. Which learning paradigm does this represent?

- A) Supervised learning
- B) Unsupervised learning
- C) Reinforcement learning
- D) Transfer learning

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The defining elements of reinforcement learning are all present: an agent (the AI), an environment (the game), actions (game moves), and a reward signal (win/lose). The agent learns through trial and error to maximize reward.
- *Why A is incorrect:* Supervised learning requires labeled training examples. Playing self-games does not produce labeled datasets.
- *Why B is incorrect:* Unsupervised learning discovers structure in static data. This scenario involves active interaction with a dynamic environment.
- *Why D is incorrect:* Transfer learning reuses knowledge from one trained model to improve another. This scenario describes learning from scratch through interaction, not transferring pretrained knowledge.

---

### Question 11 (5 points)

Which of the following best describes the concept of "transfer learning"?

- A) Moving a trained model from a development server to a production server.
- B) Applying knowledge gained from training on one task to improve performance on a different but related task.
- C) Transferring labeled data from one organization to another to increase training set size.
- D) Converting a supervised learning model into an unsupervised learning model.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Transfer learning reuses representations learned on a source task (e.g., ImageNet image classification) to accelerate and improve learning on a target task (e.g., medical image diagnosis). This avoids training from scratch and is especially useful when labeled target-task data is scarce.
  - *Why A is incorrect:* Moving a model between environments is deployment or model serving, not transfer learning. Transfer learning refers to knowledge reuse, not physical relocation.
  - *Why C is incorrect:* Sharing datasets between organizations is a data-sharing arrangement. Transfer learning applies to the model weights and learned representations, not the raw data.
  - *Why D is incorrect:* Supervised and unsupervised learning are defined by the presence or absence of labels, not by model conversion. Transfer learning does not change the learning paradigm.

---

### Question 12 (5 points)

A model achieves 99% accuracy on its training dataset but only 61% accuracy on the validation dataset. Which condition does this most likely indicate?

- A) Underfitting
- B) Overfitting
- C) Concept drift
- D) Data leakage

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A large gap between training accuracy (high) and validation accuracy (low) is the textbook symptom of overfitting. The model memorized training examples, including noise, and fails to generalize to unseen data.
  - *Why A is incorrect:* Underfitting produces low accuracy on both training and validation sets because the model is too simple to capture patterns in either.
  - *Why C is incorrect:* Concept drift describes a change in the statistical relationship between inputs and outputs over time in production, not a training/validation gap measured at the time of training.
  - *Why D is incorrect:* Data leakage occurs when information from the test set contaminates the training process, typically causing unrealistically high validation accuracy, not low validation accuracy.

---

### Question 13 (5 points)

Which responsible AI principle is MOST directly addressed by requiring an AI system to provide human-readable explanations of why a loan application was denied?

- A) Fairness
- B) Accountability
- C) Transparency
- D) Privacy and Security

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Transparency requires that AI systems be understandable and explainable. Providing explanations for automated decisions — especially high-stakes ones like loan denials — is a direct implementation of this principle.
  - *Why A is incorrect:* Fairness addresses equitable treatment across demographic groups. An explanation requirement does not directly prevent biased outcomes, though it may help identify them.
  - *Why B is incorrect:* Accountability ensures that people and organizations are answerable for AI system behavior. An explanation to the applicant addresses understandability (Transparency), not organizational ownership.
  - *Why D is incorrect:* Privacy and Security addresses protection of personal data and model resilience to attacks. Explanations of decisions do not directly address data protection.

---

### Question 14 (5 points)

In the context of machine learning, what is a "feature" in a structured tabular dataset?

- A) The final predicted output produced by the model during inference.
- B) A measurable input variable used by the model to make predictions.
- C) The algorithm chosen to train the model.
- D) The validation metric used to evaluate model performance.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A feature is a measurable attribute of each data example — the columns of a structured dataset that serve as model inputs. For a house price model, features include square footage, number of bedrooms, and ZIP code.
  - *Why A is incorrect:* The predicted output is the model's output label or numerical value, commonly called the target, label, or dependent variable — not a feature.
  - *Why C is incorrect:* The algorithm is the mathematical procedure used to fit the model. It is not a property of the data.
  - *Why D is incorrect:* A validation metric such as accuracy or RMSE is an evaluation criterion. It measures model performance and is separate from the input features.

---

### Question 15 (5 points)

An AI system that recommends parole decisions was found to assign significantly higher risk scores to Black defendants than to white defendants with equivalent criminal histories. Which TWO responsible AI principles are most relevant?

- A) Reliability and Safety, and Transparency
- B) Fairness, and Accountability
- C) Inclusiveness, and Privacy and Security
- D) Transparency, and Privacy and Security

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Fairness is violated because the system produces discriminatory outcomes based on race rather than equivalent criminal history. Accountability is relevant because the organization deploying the system must be answerable for these harmful outcomes. Both principles directly apply to biased high-stakes decision systems.
  - *Why A is incorrect:* Reliability and Safety addresses consistency and harm prevention in operation, and Transparency addresses explainability. Neither is the primary principle for a bias-driven discriminatory outcome.
  - *Why C is incorrect:* Inclusiveness addresses access and design for all people — particularly those with disabilities. Privacy and Security addresses data protection. Neither is the primary issue here.
  - *Why D is incorrect:* While Transparency may be part of the remediation strategy, it is not the primary principle violated by a biased outcome. Privacy and Security is unrelated.

---

### Question 16 (5 points)

Which of the following scenarios is the best example of an unsupervised anomaly detection task?

- A) A bank trains a model on labeled fraudulent and legitimate transactions to flag future fraud.
- B) A network monitoring system learns the typical traffic patterns of a server and alerts when traffic deviates significantly — with no labeled attack examples ever provided.
- C) A medical device manufacturer tests a physical sensor under simulated extreme conditions to verify it does not fail.
- D) A help desk system classifies support tickets as billing, technical, or account issues using labeled historical tickets.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The system learns from only normal, unlabeled traffic data and flags deviations. There are no labeled attack examples, which makes this unsupervised. Identifying deviations from a learned normal distribution is the defining pattern of unsupervised anomaly detection.
  - *Why A is incorrect:* This is supervised learning — the training data contains explicit fraud/legitimate labels. The model learns to predict the label for new examples.
  - *Why C is incorrect:* This is physical product testing, not a machine learning task at all.
  - *Why D is incorrect:* Using labeled historical tickets to train a classifier is supervised multi-class classification.

---

### Question 17 (5 points)

Which Azure service would be most appropriate for a company that wants to build a conversational chatbot to handle customer service inquiries, with a prebuilt no-code interface for defining topics and responses?

- A) Azure Machine Learning
- B) Azure Cognitive Services Translator
- C) Azure Bot Service with Power Virtual Agents
- D) Azure Databricks

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Azure Bot Service combined with Power Virtual Agents (now Microsoft Copilot Studio) provides a no-code/low-code interface specifically designed for building conversational chatbots with topic-based dialog management. No custom ML training is required.
  - *Why A is incorrect:* Azure Machine Learning is for training custom models. Building a customer-service chatbot with no code is not its purpose.
  - *Why B is incorrect:* Azure Translator is a text translation API, not a dialog management platform. It translates between languages, not manages conversation flows.
  - *Why D is incorrect:* Azure Databricks is a data analytics and engineering platform. It has no built-in chatbot-building capability.

---

### Question 18 (5 points)

A dataset used to train a hiring model contains 80% male applicants because historically fewer women applied for the role. As a result, the trained model has lower accuracy for female applicants. What is the root cause of this problem?

- A) The model architecture is too simple.
- B) The training data is not representative of the full population the model will serve.
- C) The model was overfitted to the training data.
- D) The validation set was too small.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* When training data does not proportionally represent all groups that the model will encounter in production, the model learns biased patterns. The 80/20 imbalance means the model has far fewer examples to learn from for female applicants, degrading its accuracy for that group.
  - *Why A is incorrect:* Model architecture complexity is unrelated to the demographic imbalance described. A more complex model would still learn from biased data.
  - *Why C is incorrect:* Overfitting describes memorizing training data too precisely. The issue here is data composition bias, not memorization.
  - *Why D is incorrect:* Validation set size affects how reliably you measure model performance but does not cause the underlying accuracy disparity.

---

### Question 19 (5 points)

Which of the following best describes the difference between model training and model inference?

- A) Training runs on cloud hardware; inference always runs on local hardware.
- B) Training adjusts the model's internal parameters using labeled data; inference applies the fixed trained model to new data to generate predictions.
- C) Training and inference are synonyms for the same process.
- D) Training is done by data scientists; inference is done by software engineers.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Training is the iterative process of adjusting parameters (weights) to minimize prediction error on labeled training data. Inference (also called scoring or prediction) applies the fixed trained model to new inputs to produce outputs. The parameters do not change during inference.
  - *Why A is incorrect:* Both training and inference can run on cloud or local hardware depending on deployment requirements. Hardware location does not define the distinction.
  - *Why C is incorrect:* Training and inference are distinct phases of the ML lifecycle. Conflating them is a fundamental misconception.
  - *Why D is incorrect:* While roles often do specialize, training and inference are defined by their technical function (parameter adjustment vs. prediction), not by who performs them.

---

### Question 20 (5 points)

A self-driving vehicle AI processes raw camera pixels to simultaneously detect lanes, read traffic signs, recognize pedestrians, and predict their movement — all within 50 milliseconds. Which category best describes the core technology enabling this capability?

- A) Traditional rule-based AI
- B) Unsupervised clustering
- C) Deep learning with convolutional neural networks
- D) Linear regression

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Processing raw pixel inputs to detect multiple object types and predict motion at real-time speeds is the defining application domain of deep learning. Convolutional neural networks (CNNs) automatically learn spatial hierarchies of features — edges, shapes, objects — from raw image data, enabling simultaneous multi-task perception.
  - *Why A is incorrect:* Rule-based AI cannot feasibly encode rules for every possible road scene. Autonomous perception at this scale requires learned feature representations.
  - *Why B is incorrect:* Unsupervised clustering groups data points by similarity. It does not perform real-time multi-task perception or motion prediction.
  - *Why D is incorrect:* Linear regression predicts a single continuous numerical output. It cannot handle multi-task image perception and has no mechanism for learning spatial features from pixels.
