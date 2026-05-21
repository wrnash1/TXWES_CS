# Reading Guide: Module 06 - Computer Vision and Image Recognition
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 06 - Computer Vision and Image Recognition**! This module covers how machines interpret visual data — a core AI workload category on the **AI-900 (Microsoft Azure AI Fundamentals)** exam. You will learn how decision tree and ensemble models relate to computer vision pipelines, and how Azure Cognitive Services Computer Vision, Custom Vision, and Face API provide cloud-ready image analysis capabilities.

As a student, you will understand how splitting criteria drive decision tree learning, how ensemble methods like Random Forests reduce overfitting by combining many weak learners, and how these concepts underpin the classification systems inside Azure Vision services. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Splitting criteria (Gini impurity and Entropy)**: Mathematical measures used by decision tree algorithms to choose which feature and threshold to split on at each node. Gini impurity measures the probability of a random sample being misclassified; Entropy (information gain) measures the reduction in disorder after a split. Lower values indicate purer child nodes after the split.
*   **Leaf nodes**: The terminal nodes of a decision tree that contain no further splits — they hold the final class prediction or regression value. A tree that is too deep (many leaf nodes) tends to overfit; pruning or limiting tree depth is the standard remedy.
*   **Ensemble methods**: Machine learning techniques that combine the predictions of multiple individual models (weak learners) to produce a stronger, more generalized prediction. Bagging (Random Forest) and boosting (XGBoost, Gradient Boosting) are the two primary ensemble strategies tested on the AI-900 exam.
*   **Bootstrap aggregation (Bagging)**: A technique where multiple decision trees are each trained on a different random subset of the training data (sampled with replacement), and their predictions are averaged or voted on. This reduces variance and prevents any single tree from overfitting to noise in the data.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** Computer vision is one of the five core Azure AI workload types. Know the key Azure services: Azure AI Vision (image classification, object detection, OCR, spatial analysis), Azure Custom Vision (training custom classifiers without deep ML expertise), and Azure Face API (face detection, verification, and identification). The exam tests which service to choose for a given scenario.
*   **Common AI-900 Trap:** Azure Custom Vision and Azure AI Vision are often confused. Custom Vision lets you train your own image classifier with your own labeled images; Azure AI Vision uses Microsoft's pre-trained models via REST API. If a scenario says "train with your own images," the answer is Custom Vision, not Azure AI Vision.
*   **Study Resource:** The Microsoft Learn module [Analyze images with Azure AI Vision](https://learn.microsoft.com/en-us/training/modules/analyze-images-computer-vision/) walks through Azure Computer Vision capabilities including object detection, OCR, and spatial analysis — all directly tested on AI-900. It is free and includes a hands-on exercise.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters on decision trees, ensemble methods, and classification in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). Focus on sections covering tree induction, information gain, and ensemble learning strategies.
*   **Required Video:** Watch the computer vision and decision tree segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video connects tree-based classifiers to Azure vision service capabilities.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Train a Decision Tree Classifier on flower classifications**: Use scikit-learn's `DecisionTreeClassifier` to train a model on the Iris dataset, observe how Gini impurity drives each split, and visualize the resulting tree structure.
*   **Examine feature importance outputs**: Inspect `model.feature_importances_` to identify which petal and sepal measurements contribute most to classification accuracy.
*   **Train a Random Forest Ensemble model and compare accuracy**: Replace the single decision tree with scikit-learn's `RandomForestClassifier`, tune `n_estimators`, and compare accuracy scores to demonstrate how bagging reduces overfitting.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapters on decision trees and ensemble methods in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on Computer Vision and Decision Trees in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
