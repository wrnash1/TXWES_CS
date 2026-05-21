# Reading Guide: Module 07 - Azure Cognitive Services: Vision, Speech, and Language
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 07 - Azure Cognitive Services: Vision, Speech, and Language**! This module introduces Microsoft's pre-built AI APIs that allow developers to add intelligent features to applications without building or training custom models from scratch. These services are central to the **AI-900 (Microsoft Azure AI Fundamentals)** exam and represent the most practical entry point to cloud AI development.

As a student, you will learn which Azure Cognitive Service to choose for a given scenario, how the Vision, Speech, and Language service families differ, and what each API can and cannot do. You will also study model evaluation metrics — the tools used to measure how well any classifier or regression model performs. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Azure Cognitive Services (pre-built AI APIs)**: A family of cloud-hosted REST APIs provided by Microsoft that deliver ready-to-use AI capabilities — including vision, speech, language, and decision intelligence — without requiring the developer to collect training data or build a model. Developers call the API endpoint with an input (an image, audio clip, or text string) and receive a structured JSON response containing predictions, labels, or transcriptions.
*   **Confusion matrix**: A table used to evaluate the performance of a classification model by displaying the counts of True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN) for each class. It is the foundation for calculating accuracy, precision, recall, and F1-score — all of which can be read directly from its four cells.
*   **Precision and Recall**: Precision is the fraction of predicted positives that are actually positive (TP / (TP + FP)); it answers "of everything the model labeled positive, how many were correct?" Recall (Sensitivity) is the fraction of actual positives that were correctly identified (TP / (TP + FN)); it answers "of all the real positives, how many did the model catch?" High precision is preferred when false positives are costly; high recall is preferred when missing a positive is costly (e.g., cancer screening).
*   **F1-Score**: The harmonic mean of Precision and Recall, calculated as 2 × (Precision × Recall) / (Precision + Recall). It provides a single balanced metric when both false positives and false negatives must be minimized. The F1-Score is especially useful when class distributions are unbalanced, since accuracy alone can be misleadingly high when one class vastly outnumbers the other.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** Azure Cognitive Services is one of the most heavily tested areas on the exam. Know the three main service families: **Azure AI Vision** (image classification, object detection, OCR, spatial analysis), **Azure AI Speech** (speech-to-text, text-to-speech, speaker recognition, real-time transcription), and **Azure AI Language** (sentiment analysis, key phrase extraction, named entity recognition, conversational language understanding). Expect scenario questions asking you to choose the correct service for a described use case.
*   **Common AI-900 Trap:** The exam often asks which Azure service handles a specific task. "Transcribe spoken audio to text" → Azure AI Speech (speech-to-text). "Extract sentiment from customer reviews" → Azure AI Language. "Identify objects in a photo" → Azure AI Vision. "Detect faces and estimate age" → Azure AI Face API. Mixing these up is the most common mistake. Practice matching each service to a realistic business scenario.
*   **Study Resource:** The Microsoft Learn module [Analyze images with Azure AI Vision](https://learn.microsoft.com/en-us/training/modules/analyze-images-computer-vision/) walks through Azure AI Vision capabilities including object detection, OCR, and spatial analysis. It is free, interactive, and directly tests the skills covered on AI-900. A companion module, [Analyze text with Azure AI Language](https://learn.microsoft.com/en-us/training/modules/analyze-text-with-text-analytics-service/), covers the Language service APIs in the same format.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters on machine learning evaluation and cognitive computing in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). This freely available textbook by Poole and Mackworth covers classification evaluation metrics (precision, recall, F1) and provides theoretical grounding for the Azure Cognitive Services covered in this module.
*   **Required Video:** Watch the Azure Cognitive Services segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video maps each Cognitive Service API to real-world deployment scenarios and explains how Microsoft's pre-built models compare to custom-trained models in Azure ML.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Generate a confusion matrix from classifier predictions**: Use `sklearn.metrics.confusion_matrix(y_test, predictions)` to display TP/TN/FP/FN counts for each class, then visually inspect which class pairs are most frequently confused by the model.
*   **Calculate model accuracy, precision, recall, and F1-score**: Use `classification_report(y_test, predictions)` from scikit-learn to produce a formatted table of all four metrics per class, allowing a direct comparison between classes and identifying which class has the weakest recall.
*   **Compute Mean Squared Error (MSE) of regression predictions**: Apply `mean_squared_error(y_test, predictions)` from `sklearn.metrics` to quantify the average squared difference between predicted and actual numeric values — the standard error metric for regression models.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapters on ML evaluation and cognitive computing in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on Azure Cognitive Services in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
