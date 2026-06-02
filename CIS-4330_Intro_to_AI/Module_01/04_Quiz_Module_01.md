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
