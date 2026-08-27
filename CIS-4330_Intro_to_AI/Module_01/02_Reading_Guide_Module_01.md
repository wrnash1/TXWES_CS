# Reading Guide: Module 01 - Introduction to AI and Machine Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe Artificial Intelligence workloads and considerations (15-20%)

---

## Overview

This reading guide accompanies the Module 01 video lecture and prepares you for the quiz, lab, and discussion. Work through each section in order. The glossary and comparison tables are high-priority study tools for the AI-900 exam. Complete the study checklist before moving to the lab activity.

---

## Section 1: Core Vocabulary

Learn these terms precisely. The AI-900 exam tests definitions in context, not just recall.

**Artificial Intelligence (AI)**
The capability of a computer system to perform tasks that would normally require human intelligence. AI includes reasoning, learning, perception, and natural language understanding. AI does not require machine learning — rule-based expert systems are also AI.

**Machine Learning (ML)**
A subset of AI in which algorithms learn statistical patterns from data without being explicitly programmed with rules. The programmer provides training examples and an objective function; the algorithm discovers the mapping from inputs to outputs.

**Deep Learning (DL)**
A subset of machine learning that uses artificial neural networks with multiple hidden layers. Deep learning excels at unstructured data such as images, audio, and text because the layers automatically learn hierarchical feature representations.

**Supervised Learning**
A machine learning paradigm in which the training dataset includes both input features and correct output labels. The algorithm learns to predict the output label for new inputs. Examples: email spam detection, house price prediction, medical image classification.

**Unsupervised Learning**
A machine learning paradigm in which the training dataset contains only input features — no labels. The algorithm discovers hidden structure, such as clusters or latent dimensions. Examples: customer segmentation, anomaly detection without labeled anomalies, topic modeling.

**Reinforcement Learning**
A machine learning paradigm in which an agent learns by interacting with an environment and receiving reward signals. The agent's goal is to maximize cumulative reward over time. Examples: game-playing AI, robotic control, dynamic pricing systems.

**Training Data**
The labeled or unlabeled dataset used to adjust a model's internal parameters during the learning process. Training data quality and quantity are the primary drivers of model performance.

**Feature**
A measurable input variable used by a machine learning model. Features are the columns in a structured dataset or the extracted representations (pixel values, word embeddings) from unstructured data.

**Model**
The mathematical function produced by training an algorithm on data. A trained model maps input features to predicted outputs and can be deployed to make predictions on new, unseen data.

**Inference**
The process of applying a trained model to new data to generate predictions. Inference is distinct from training; it occurs after the model is deployed.

**Overfitting**
A condition in which a model learns the training data too precisely, including noise, and fails to generalize to new data. Symptoms: high training accuracy, low validation accuracy.

**Underfitting**
A condition in which a model is too simple to capture the true patterns in the data. Symptoms: low training accuracy and low validation accuracy.

**Regression**
A supervised learning task in which the output is a continuous numerical value. Example: predicting the sale price of a house given its features.

**Classification**
A supervised learning task in which the output is a discrete category label. Example: classifying an email as spam or not spam. Binary classification has two classes; multi-class has three or more.

**Clustering**
An unsupervised learning task in which data points are grouped into clusters based on similarity. K-means and hierarchical clustering are common algorithms.

**Azure Machine Learning**
Microsoft Azure's cloud platform for building, training, evaluating, and deploying custom machine learning models. Provides compute management, experiment tracking, and an automated ML capability.

**Azure Cognitive Services**
A family of prebuilt AI APIs available on Azure that cover vision, speech, language, and decision capabilities. Requires no model training; developers call the API with input data and receive AI-powered results.

**Azure Applied AI Services**
Specialized Azure services that combine Cognitive Services with custom logic to address specific business scenarios, such as form recognition, knowledge mining, and conversational AI.

---

## Section 2: Comparison Tables

### Table 1: AI vs Machine Learning vs Deep Learning

| Dimension | Traditional AI | Machine Learning | Deep Learning |
|---|---|---|---|
| Learning method | Rule-based logic | Statistical pattern learning | Hierarchical feature learning via neural networks |
| Programming approach | Human writes explicit rules | Human provides data and objective; algorithm finds rules | Human provides raw data; network learns features and rules |
| Data requirement | Low (rules are coded) | Moderate (hundreds to thousands of examples) | High (thousands to millions of examples) |
| Interpretability | High (rules are readable) | Moderate (some algorithms are transparent) | Low (black box without explainability tools) |
| Compute requirement | Low | Moderate | High (GPU/TPU recommended) |
| Best use case | Constrained, well-defined logic | Structured tabular data with clear features | Images, audio, text, video |
| Azure example | Custom logic in Azure Functions | Azure ML AutoML | Azure ML with deep learning frameworks |

### Table 2: Supervised vs Unsupervised vs Reinforcement Learning

| Dimension | Supervised Learning | Unsupervised Learning | Reinforcement Learning |
|---|---|---|---|
| Training data labels | Required (input + label pairs) | Not present (inputs only) | Not required (reward signal) |
| Goal | Predict labeled output | Discover hidden structure | Maximize cumulative reward |
| Primary tasks | Classification, regression | Clustering, dimensionality reduction, anomaly detection | Sequential decision-making |
| Human involvement | Label the training data | Interpret discovered patterns | Design the reward function |
| Example scenario | Fraud detection (labeled transactions) | Customer segmentation (unlabeled purchase data) | Autonomous vehicle navigation |
| AI-900 keyword cues | "predict," "classify," "label," "train on examples" | "group," "segment," "discover patterns" | "agent," "environment," "reward," "action" |

### Table 3: Regression vs Classification

| Dimension | Regression | Classification |
|---|---|---|
| Output type | Continuous numerical value | Discrete category label |
| Examples | House price, temperature, stock price | Spam/not spam, disease/healthy, image category |
| Common algorithms | Linear regression, gradient boosting | Logistic regression, decision tree, neural network |
| Evaluation metrics | MAE, RMSE, R-squared | Accuracy, precision, recall, F1, AUC-ROC |
| Azure ML task type | "Regression" in AutoML | "Classification" in AutoML |

### Table 4: Azure AI Service Tiers

| Tier | Service | Use When | Training Required |
|---|---|---|---|
| Custom models | Azure Machine Learning | You have unique data and need a custom model | Yes |
| Prebuilt APIs | Azure Cognitive Services | You need standard AI capabilities quickly | No |
| End-to-end solutions | Azure Applied AI Services | You need a complete business solution | Optional (customization available) |

---

## Section 3: The Microsoft Responsible AI Principles

The AI-900 exam devotes a domain to responsible AI. Memorize these six principles and their definitions.

**Fairness**
AI systems should treat all people equitably and avoid creating or reinforcing bias. Bias in training data can produce discriminatory outcomes. Example: a loan approval model should not produce significantly different approval rates for equally qualified applicants from different demographic groups.

**Reliability and Safety**
AI systems should perform consistently under normal and unexpected conditions. Safety is especially critical in high-stakes applications such as medical diagnosis and autonomous vehicles.

**Privacy and Security**
AI systems should protect user data and be resilient to adversarial attacks. Training data often contains sensitive personal information, and deployed models can be exploited to extract that information if not protected.

**Inclusiveness**
AI systems should be designed to benefit all people, including those with disabilities or who speak minority languages. Accessibility features and broad language support reflect this principle.

**Transparency**
AI systems should be explainable and understandable. Users and stakeholders should be able to understand how decisions are made, especially when those decisions affect them.

**Accountability**
People and organizations should be accountable for the AI systems they design, build, and deploy. There must be clear ownership and oversight, particularly when AI is used in consequential decisions.

---

## Section 4: The AI-900 Exam Structure

The AI-900 exam contains 40-60 questions and must be completed in 45 minutes. The passing score is 700 out of 1000. The exam is available in English, Japanese, Chinese, Korean, German, French, Spanish, Portuguese, Russian, Indonesian, Arabic, and Italian.

The five exam domains and their approximate weights are:

- Describe AI workloads and considerations: 15-20%
- Describe fundamental principles of machine learning on Azure: 20-25%
- Describe features of computer vision workloads on Azure: 15-20%
- Describe features of NLP workloads on Azure: 15-20%
- Describe features of generative AI workloads on Azure: 15-20%

Module 01 corresponds primarily to the first two domains. Pay careful attention to scenario-based questions — the AI-900 presents a business problem and asks you to identify the correct Azure service, learning paradigm, or responsible AI principle.

---

## Section 5: Common AI-900 Exam Mistakes

**Mistake 1: Confusing ML and AI**
AI is the broader category. Not all AI is machine learning. Rule-based systems, search algorithms, and optimization routines are AI but are not ML. The exam may describe a scenario where a simple rule-based system is the right answer.

**Mistake 2: Assuming deep learning is always better**
Deep learning requires massive data and compute. For small structured datasets, simpler algorithms generalize better and are easier to explain. The exam may reward you for choosing a simpler model.

**Mistake 3: Misclassifying unsupervised learning**
Unsupervised learning does not mean the algorithm is unsupervised by humans in general. It specifically means the training data has no labels. Clustering algorithms are unsupervised even if a human reviews the results afterward.

**Mistake 4: Mixing up Azure service tiers**
Azure Cognitive Services requires no custom training. Azure Machine Learning is for building custom models. Students frequently select the wrong service because both can solve similar problems in different ways. Read the scenario carefully for clues: "prebuilt," "API," and "no training data" signal Cognitive Services.

**Mistake 5: Ignoring the responsible AI domain**
The responsible AI domain accounts for up to 20% of exam questions. Students sometimes skip it because it seems less technical. Do not underestimate it — these questions require precise knowledge of all six principles.

---

## Section 6: AI-900 Exam Tips

1. The phrase "learns from labeled data" always indicates supervised learning. The phrase "discovers hidden patterns" always indicates unsupervised learning.

2. When a question asks which Azure service to use for image analysis without custom training, the answer is Azure Computer Vision, a Cognitive Service. When it asks you to train a custom image classifier, the answer is Azure Custom Vision or Azure Machine Learning.

3. Deep learning is the correct answer when the input is unstructured data at scale: photos, audio files, long documents. Structured tabular data usually does not require deep learning.

4. The AI-900 exam uses the term "model" broadly. A regression model, a classification model, and a neural network are all "models." Do not assume the word "model" always implies deep learning.

5. Reinforcement learning is almost always the answer when a scenario describes an agent, an environment, actions, and rewards — or a system that improves through trial and error.

6. The responsible AI principle most commonly tested in scenario questions is Fairness. Bias-related scenarios nearly always map to Fairness, not Transparency.

7. Microsoft Learn provides a free AI-900 learning path at learn.microsoft.com. Use the practice assessments embedded in each module to gauge your readiness.

8. On scenario questions, eliminate wrong answers first. AI-900 distractors often describe real Azure services used in the wrong context. Narrow to two choices, then apply domain knowledge to choose the better fit.

---

## Section 7: Required Reading

Complete these readings before the lab activity.

**Microsoft Learn — Get started with AI on Azure**
learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/

This free module covers the AI-900 first domain in full. Complete all units including the knowledge check at the end.

**Microsoft Learn — Explore machine learning concepts**
learn.microsoft.com/en-us/training/modules/explore-machine-learning/

This module introduces the ML workflow and the key learning paradigms tested on AI-900. Pay close attention to the regression and classification examples.

**Microsoft Learn — Responsible AI principles**
learn.microsoft.com/en-us/training/modules/responsible-ai-principles/

This module covers all six responsible AI principles with Azure-specific examples. The knowledge check questions closely resemble AI-900 exam questions.

---

## Section 8: Study Checklist

Work through each item before submitting the lab.

- [ ] Read all vocabulary terms in Section 1 and write each definition in your own words without looking.
- [ ] Complete the Microsoft Learn module: Get started with AI on Azure.
- [ ] Complete the Microsoft Learn module: Explore machine learning concepts.
- [ ] Study Table 1 (AI vs ML vs DL) and be able to place a new scenario in the correct column.
- [ ] Study Table 2 (supervised vs unsupervised vs reinforcement) and practice classifying scenarios.
- [ ] Memorize all six responsible AI principles by name and definition.
- [ ] Review the AI-900 exam domain weights in Section 4.
- [ ] Read all eight exam tips in Section 6.
- [ ] Complete the Module 01 quiz.
- [ ] Complete the Module 01 lab activity.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.
- [ ] Respond to at least two classmates by Sunday at 11:59 PM.

## 9. Supplemental Resources

**1. fast.ai — Practical Deep Learning for Coders (free course)**
<https://course.fast.ai/>
A free, practical deep learning course that covers neural networks, image classification, NLP, and tabular data using Python. Ideal for building intuition about how deep learning systems work in practice before diving into Azure-specific tooling.

**2. Google AI Education — Machine Learning Crash Course**
<https://developers.google.com/machine-learning/crash-course>
A free, self-paced course from Google covering supervised learning, gradient descent, neural networks, and responsible AI. Includes interactive exercises and video lectures that complement the AI-900 conceptual framework covered in this module.

**3. IBM SkillsBuild — AI Fundamentals**
<https://skillsbuild.org/learn/artificial-intelligence>
A free beginner-level AI curriculum from IBM covering AI history, machine learning types, ethics, and real-world applications. Provides an alternative perspective on the same foundational concepts covered in Module 01, reinforcing the AI vs. ML vs. DL hierarchy and responsible AI principles.
