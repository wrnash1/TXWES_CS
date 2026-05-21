# Reading Guide: Module 05 - Natural Language Processing (NLP) Fundamentals
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 05 - Natural Language Processing (NLP) Fundamentals**! This module covers how computers process and understand human language, a core AI workload category on the **AI-900 (Microsoft Azure AI Fundamentals)** exam. You will explore how text is tokenized, cleaned, and vectorized, how sentiment analysis extracts opinion polarity, and how Azure Cognitive Services provides ready-to-use NLP APIs.

As a student, you will also study the mathematics behind regression models — linear regression for continuous prediction and logistic regression for binary classification — which underpin many NLP scoring systems. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Linear equation (y = mx + b)**: The mathematical form of a simple linear regression model, where y is the predicted output, x is the input feature, m is the slope (learned weight), and b is the intercept (bias). Linear regression minimizes the sum of squared residuals between predicted and actual values to find optimal m and b.
*   **Cost function**: A mathematical measure of how wrong a model's predictions are compared to the actual values. For linear regression, the Mean Squared Error (MSE) is the standard cost function; gradient descent iteratively adjusts model weights to minimize it.
*   **Gradient descent**: An optimization algorithm that iteratively updates model weights in the direction that reduces the cost function most steeply. It is the core learning mechanism behind linear regression, logistic regression, and neural networks.
*   **Logistic sigmoid curve for classification**: The S-shaped sigmoid function σ(z) = 1/(1+e^-z) that maps any real-valued input to a probability between 0 and 1. Logistic regression applies this function to convert a linear score into a class probability, making it suitable for binary classification tasks.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** NLP is one of the five core Azure AI workload types on the exam. Know the specific Azure services: Azure Cognitive Services Language (formerly Text Analytics) for sentiment analysis and key phrase extraction, Azure Translator for translation, and Azure Language Understanding (CLU) for intent recognition in conversational AI scenarios.
*   **Common AI-900 Trap:** The exam may show a scenario asking which service handles "understanding what a user means" versus "translating text." CLU (Conversational Language Understanding) handles intent/entity extraction; Azure Translator handles language-to-language translation. Do not confuse them.
*   **Study Resource:** The Microsoft Learn module [Analyze text with Azure AI Language](https://learn.microsoft.com/en-us/training/modules/analyze-text-with-text-analytics-service/) covers Azure NLP services directly tested on AI-900. It is free, interactive, and includes hands-on exercises with the Azure portal.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters on natural language processing and text representation in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). Focus on sections covering tokenization, bag-of-words, and text classification methods.
*   **Required Video:** Watch the NLP and language AI segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video maps Azure NLP services to real-world use cases tested on the exam.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Import `LinearRegression` from `sklearn.linear_model`**: Import scikit-learn's linear regression class to build a model that predicts a continuous output from one or more numeric features.
*   **Fit a model: `model.fit(X, y)`**: Train the linear regression model by passing the feature matrix X and target vector y, allowing the algorithm to learn optimal weights via least-squares minimization.
*   **Predict outcomes and print model coefficients**: Call `model.predict()` on new data and inspect `model.coef_` and `model.intercept_` to understand the learned relationship between features and the target variable.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapters on NLP and regression in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on NLP Fundamentals in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
