# Reading Guide: Module 03 - Unsupervised Learning – Clustering and Dimensionality Reduction
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 03 - Unsupervised Learning: Clustering and Dimensionality Reduction**! This module dives deeper into unsupervised ML techniques as tested on the **AI-900 (Microsoft Azure AI Fundamentals)** exam. You will understand how K-Means clustering partitions data, how Principal Component Analysis (PCA) reduces high-dimensional feature spaces, and how these techniques appear in Azure Machine Learning workflows.

As a student, you will learn to work with the Pandas library to load and inspect tabular datasets, compute descriptive statistics, and visualize data distributions — foundational skills for every subsequent AI lab in this course. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Pandas DataFrames**: A two-dimensional, labeled data structure in Python's Pandas library that stores tabular data with named rows (index) and columns. DataFrames are the standard input format for scikit-learn ML pipelines and are used throughout Azure Machine Learning Designer data preparation steps.
*   **Loading CSV files**: The process of reading a comma-separated values file into memory as a structured table using `pd.read_csv()`. This is typically the first step in any ML pipeline — data must be loaded before it can be cleaned, transformed, or modeled.
*   **Descriptive statistics**: Summary measures — including count, mean, standard deviation, minimum, quartiles, and maximum — that describe the central tendency and spread of a numerical dataset. In Azure ML, understanding data distribution is required before selecting appropriate preprocessing and model types.
*   **Basic plots**: Visual representations of data distributions and relationships, such as histograms (value frequency), scatter plots (feature correlation), and box plots (outlier detection). Visualizing data before modeling is a best practice aligned with the Responsible AI principle of transparency.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** The AI-900 exam tests your ability to identify when unsupervised learning is appropriate. A scenario with no labeled output column and a goal of "discovering natural groupings" signals clustering. Know that Azure Machine Learning supports K-Means clustering as an automated ML task type.
*   **Common AI-900 Trap:** PCA (dimensionality reduction) is sometimes confused with feature selection. PCA creates new synthetic features (principal components) that are linear combinations of originals; feature selection simply removes existing features. The exam may use both terms and expect you to distinguish them.
*   **Study Resource:** The Microsoft Learn path [Introduction to machine learning](https://learn.microsoft.com/en-us/training/modules/introduction-to-machine-learning/) covers unsupervised workloads and data exploration concepts tested on AI-900. Review the "Understand data for machine learning" section specifically.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapter on data representation and unsupervised learning in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). Focus on sections covering feature spaces, similarity measures, and clustering algorithms.
*   **Required Video:** Watch the data exploration and unsupervised learning segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). Pay attention to how clustering is framed as an Azure AI workload category.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Load Iris dataset: `df = pd.read_csv('iris_sample.csv')`**: Import the classic Iris flower dataset into a Pandas DataFrame, setting the foundation for all subsequent exploration and modeling steps.
*   **Inspect top 5 rows: `df.head()`**: Preview the first five rows of the dataset to confirm column names, data types, and that the file loaded correctly before performing any transformations.
*   **Generate dataset descriptive summary: `df.describe()`**: Compute count, mean, standard deviation, min, and quartile statistics for all numeric columns to understand the data distribution before selecting a clustering algorithm.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapter covering unsupervised learning and data exploration in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on unsupervised learning in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
