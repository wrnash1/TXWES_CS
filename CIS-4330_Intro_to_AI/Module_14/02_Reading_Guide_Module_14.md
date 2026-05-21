# Reading Guide: Module 14 - Model Evaluation and Deployment
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 14 - Model Evaluation and Deployment**! This module covers the final stages of the machine learning lifecycle: rigorously evaluating a trained model's performance, interpreting the results, and deploying the model as a production-ready endpoint. These skills connect directly to the **AI-900 (Microsoft Azure AI Fundamentals)** exam objectives around Azure Machine Learning and responsible AI deployment practices.

As a student, you will also explore Azure AutoML — the no-code tool that automates feature selection, algorithm sweeping, and hyperparameter tuning — and learn how it fits into the broader model evaluation and deployment workflow. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **AutoML pipelines (feature selection, algorithm sweep, hyperparameter tuning)**: Azure AutoML automates the iterative process of model development by running multiple training experiments in parallel, each testing a different algorithm (e.g., LightGBM, Random Forest, XGBoost) and hyperparameter combination. It ranks all experiments by a chosen primary metric (accuracy, AUC, RMSE) and surfaces the best model, removing the need for manual trial-and-error experimentation. The resulting pipeline includes data preprocessing, feature transformation, and model training steps.
*   **Cross-validation**: A model evaluation technique that divides the training dataset into k equal folds, trains the model k times (each time using a different fold as the validation set and the remaining k-1 folds as training data), and averages the performance metrics. Cross-validation produces a more reliable estimate of real-world performance than a single train/test split, especially on small datasets where a single split may produce misleading results.
*   **Model deployment (real-time vs. batch endpoints)**: Making a trained model available for inference. A **real-time endpoint** (also called an online endpoint in Azure ML) responds to individual prediction requests synchronously with low latency — suited for fraud detection, recommendation systems, or chatbot scoring. A **batch endpoint** processes large datasets asynchronously overnight — suited for monthly churn prediction or batch document classification. Both require registering the model, specifying compute resources, and generating authentication credentials.
*   **Model monitoring and drift detection**: After deployment, a model's performance can degrade over time as real-world data distributions shift away from the training distribution — a phenomenon called **data drift**. Azure Machine Learning's model monitoring service tracks input data statistics and prediction distributions, alerting when drift exceeds a threshold so the model can be retrained. Monitoring is a key component of the MLOps (Machine Learning Operations) lifecycle.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** The exam tests which Azure Machine Learning authoring experience to recommend for a given scenario. Know these three clearly: **AutoML** (no-code; automatically selects the best algorithm and hyperparameters from a dataset; best for users without deep ML expertise); **Designer** (drag-and-drop visual pipeline builder; low-code; good for data scientists who want visual control); **Notebooks** (code-first Python/R Jupyter environment; full control; for experienced data scientists). A scenario saying "business analyst, no coding background, wants best model quickly" → AutoML. A scenario saying "data scientist wants to write custom PyTorch training loop" → Notebooks.
*   **Common AI-900 Trap:** Students often confuse **model evaluation metrics** for regression vs. classification. For regression: use **MAE (Mean Absolute Error)**, **MSE (Mean Squared Error)**, and **R² (coefficient of determination)**. For classification: use **accuracy**, **precision**, **recall**, **F1-score**, and **AUC-ROC**. The exam presents scenarios and asks which metric is appropriate. "Predict house prices" is regression → MSE/MAE. "Classify emails as spam/not spam" is classification → accuracy, precision/recall, F1.
*   **Study Resource:** The Microsoft Learn module [Use Automated Machine Learning in Azure Machine Learning](https://learn.microsoft.com/en-us/training/modules/use-automated-machine-learning/) walks through configuring an AutoML experiment, interpreting the results leaderboard, and deploying the best model as a real-time endpoint. It is free, hands-on, and maps directly to the Azure ML section of the AI-900 exam. A companion module, [Deploy and consume models with Azure Machine Learning](https://learn.microsoft.com/en-us/training/modules/deploy-consume-models-with-azure-machine-learning/), covers the deployment and endpoint consumption workflow in detail.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters on machine learning model evaluation, validation strategies, and deployment in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). This freely available textbook by Poole and Mackworth covers cross-validation, evaluation metrics, and the practical considerations involved in moving a trained model into production.
*   **Required Video:** Watch the model evaluation and Azure ML deployment segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video covers AutoML experiment results, how to interpret the model leaderboard, and the steps to deploy a model as a real-time endpoint in Azure Machine Learning Studio.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure an AutoML run selecting classification as the task type**: Use scikit-learn's `cross_val_score(model, X, y, cv=5, scoring='accuracy')` to simulate a 5-fold cross-validation sweep across three classifier types (Logistic Regression, Random Forest, Gradient Boosting), then build a comparison table ranking each by mean validation accuracy — replicating the logic Azure AutoML uses internally.
*   **Inspect performance rankings of multiple trained models**: Generate a `classification_report()` and plot an ROC curve using `roc_auc_score` for the top-ranked model, interpreting precision/recall tradeoffs and the AUC value to justify which model to deploy.
*   **Select the best model and simulate endpoint deployment**: Register the best model using `joblib.dump(model, 'best_model.pkl')`, then write a scoring function that loads the model and returns predictions — simulating what Azure ML packages into a real-time endpoint container image.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapters on model evaluation and deployment in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on Model Evaluation and Deployment in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
