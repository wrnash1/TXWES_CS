# Reading Guide: Module 02 - Supervised vs Unsupervised Learning
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 02 - Supervised vs Unsupervised Learning**! This module covers the two primary machine learning paradigms as tested on the **AI-900 (Microsoft Azure AI Fundamentals)** exam. You will learn how labeled data enables supervised models to predict outcomes, how unsupervised models find hidden structure in unlabeled data, and where each paradigm appears in Azure AI services.

As a student, you will distinguish between regression (predicting continuous values) and classification (predicting discrete labels), understand how clustering groups similar data points without labels, and recognize anomaly detection as a practical unsupervised workload supported by Azure Cognitive Services. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Labeled vs unlabeled data**: Labeled data pairs each input sample with a known correct output (e.g., an email tagged as spam or not spam), enabling supervised learning. Unlabeled data contains only input features with no known output, and is used in unsupervised learning where the model must discover its own structure.
*   **Regression**: A supervised learning task that predicts a continuous numerical output, such as a house price or temperature forecast. Azure Machine Learning supports regression as one of its core automated ML task types on the AI-900 exam.
*   **Classification**: A supervised learning task that assigns input samples to discrete categories or classes (e.g., benign vs malignant, cat vs dog). Multi-class and binary classification are both covered in the AI-900 framework, and Azure Custom Vision is a classification service example.
*   **Clustering**: An unsupervised learning technique that groups data points by similarity without predefined labels. K-Means is a common algorithm; Azure Machine Learning supports clustering workloads in its designer and automated ML tools.
*   **Anomaly detection**: An unsupervised or semi-supervised workload that identifies data points that deviate significantly from normal patterns. The AI-900 exam explicitly lists anomaly detection as one of the five core AI workload types, and Azure Anomaly Detector is the dedicated service.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** The exam maps specific Azure services to workload types. Know that Azure Custom Vision = image classification, Azure Machine Learning = regression and classification for structured data, and Azure Anomaly Detector = time-series anomaly detection. Memorizing these pairings is high yield.
*   **Common AI-900 Trap:** Do not confuse clustering (unsupervised, no labels) with classification (supervised, requires labels). A scenario describing "grouping customers by purchase behavior with no predefined categories" is clustering, not classification — even if the goal feels like categorization.
*   **Study Resource:** The Microsoft Learn module [Explore fundamental AI concepts](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/) covers supervised, unsupervised, and reinforcement learning distinctions tested on AI-900. It is free and maps directly to this module's exam objectives.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapter on machine learning types in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). Focus on the sections covering supervised learning, hypothesis spaces, and unsupervised clustering.
*   **Required Video:** Watch the supervised and unsupervised learning segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video covers the labeled vs unlabeled data distinction and Azure service mappings.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Identify dataset types: regression vs classification**: Examine two sample datasets — one with a continuous target column (house price) and one with a categorical target column (customer churn: yes/no) — and label each as regression or classification.
*   **Examine a dataset to classify customers into segments**: Load a customer dataset, run a K-Means clustering algorithm, and inspect the resulting cluster assignments to see how unlabeled groupings emerge.
*   **Filter a dataset based on feature target values**: Practice subsetting a DataFrame using Pandas boolean indexing to isolate specific classes or value ranges for downstream model training.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapter covering supervised and unsupervised learning in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on Supervised vs Unsupervised Learning in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
