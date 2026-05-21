# Reading Guide: Module 04 - Neural Networks and Deep Learning
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 04 - Neural Networks and Deep Learning**! This module covers the architecture and training mechanics of artificial neural networks as tested on the **AI-900 (Microsoft Azure AI Fundamentals)** exam. You will understand how neurons, layers, and activation functions combine to create models capable of learning complex patterns, and how Azure services like Azure Machine Learning and Azure Cognitive Services leverage deep learning under the hood.

As a student, you will learn how missing and inconsistent data prevents models from training correctly, how normalization and encoding prepare features for neural network input, and why these preprocessing steps are critical before any deep learning workflow. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Handling missing data**: The process of addressing null or absent values in a dataset before model training. Common strategies include imputation (replacing missing values with the mean, median, or mode) or dropping rows/columns with too many missing entries. Neural networks cannot process NaN values, making this step mandatory in any preprocessing pipeline.
*   **Normalization**: A feature scaling technique that rescales numerical values to a fixed range, typically [0, 1], using Min-Max scaling. Normalization prevents features with large numeric ranges from dominating gradient updates during neural network training, leading to faster and more stable convergence.
*   **Feature scaling**: The broader category of transformations — including normalization and standardization (zero mean, unit variance) — that bring all input features to a comparable numeric range. Proper feature scaling is a prerequisite for distance-based algorithms and gradient descent optimization used in neural networks.
*   **One-hot encoding for categorical values**: A preprocessing technique that converts a categorical column with N unique values into N binary (0/1) columns, one per category. This allows neural networks and other ML algorithms to process text-based categorical features as numeric inputs without implying false ordinal relationships.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** The exam tests conceptual understanding of neural networks rather than implementation details. Know that deep learning is a subset of ML using multi-layer neural networks, that Azure Cognitive Services uses pre-trained deep learning models (you don't train them), and that Azure Machine Learning is where you train custom deep learning models.
*   **Common AI-900 Trap:** The exam may ask which Azure service to use for a specific deep learning task. Azure Cognitive Services (pre-built, no training required) is different from Azure Machine Learning (custom training). Do not confuse using a pre-trained model via API with training your own neural network from scratch.
*   **Study Resource:** The Microsoft Learn module [Understand the difference between supervised and unsupervised learning](https://learn.microsoft.com/en-us/training/modules/introduction-to-machine-learning/) and the Azure AI fundamentals path on [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/) both cover deep learning concepts at the AI-900 level.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters on neural network architectures and learning algorithms in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). Focus on the sections covering perceptrons, multi-layer networks, and backpropagation.
*   **Required Video:** Watch the neural networks and deep learning segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video explains how deep learning fits within Azure's AI service hierarchy.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Impute missing values using Pandas `fillna()` method**: Replace null entries in numeric columns with the column mean or a fixed value, preventing training errors caused by NaN inputs.
*   **Scale numerical features to 0–1 range using MinMaxScaler**: Apply scikit-learn's `MinMaxScaler` to normalize all numeric feature columns so that no single feature dominates the neural network's gradient updates.
*   **Convert text categories to binary columns using `get_dummies()`**: Transform categorical string columns into one-hot encoded binary indicator columns that can be fed directly into a neural network or any sklearn estimator.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapters on neural networks in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on Neural Networks and Deep Learning in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
