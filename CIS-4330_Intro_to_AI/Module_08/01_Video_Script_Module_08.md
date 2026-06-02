# Video Script: Module 08 - Azure Machine Learning Studio

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AI-900 Domain:** Describe fundamental principles of machine learning on Azure (20-25%)

---

## [00:00 - 01:30] Opening

Welcome back. Professor Nash here, and this is Module 08. In the previous modules we covered machine learning concepts, deep learning, and the Azure Cognitive Services portfolio. Today we go deeper on Azure Machine Learning — the platform for data scientists and ML engineers who need to build, train, evaluate, and deploy custom models. Azure ML is a central AI-900 exam topic, and it represents the layer of Azure AI that requires the most configuration and expertise. Let us get into it.

---

## [01:30 - 05:00] What Is Azure Machine Learning?

Azure Machine Learning is Microsoft's cloud platform for the full machine learning lifecycle. Unlike Azure Cognitive Services — which provide prebuilt capabilities with no training required — Azure Machine Learning is for situations where you need a custom model trained on your own data.

When do you need Azure ML instead of Cognitive Services? The key scenarios are:

- Your data is proprietary and domain-specific, and prebuilt models do not recognize the patterns you need.
- You need complete control over the model architecture, training process, and evaluation criteria.
- You have a large-scale training job that requires significant compute resources.
- You need to track experiments — systematically comparing many model configurations to find the best one.
- You need to manage model versions, reproduce past experiments, and audit what changed between model versions.

Azure Machine Learning provides a workspace — the central resource that brings together all ML assets: data, compute, experiments, models, and deployments. The workspace is the logical container for a team's entire ML work.

---

## [05:00 - 09:00] Azure ML Workspace Components

[SHOW DIAGRAM: Azure ML Workspace in the center. Six boxes surrounding it connected by arrows: "Data Assets," "Compute Targets," "Experiments," "Models," "Endpoints," "Pipelines."]

The Azure ML workspace contains several key components. Let me walk through each one.

**Data Assets** are registered datasets. You register a dataset — a CSV file in Azure Blob Storage, a folder of images, a database connection — and give it a name and version. Once registered, the dataset can be referenced in experiments and pipelines without hardcoding file paths. Azure ML tracks which dataset was used to train which model.

**Compute Targets** are the processing resources used for training and inference. Types of compute in Azure ML:

- Compute Instance: a managed virtual machine for individual development and experimentation. Like a cloud-based Jupyter notebook server.
- Compute Clusters: autoscaling clusters of VMs used for training jobs. Scale from zero to dozens of nodes based on demand, reducing cost when idle.
- Inference Clusters (AKS): Azure Kubernetes Service clusters used for real-time inference endpoints at scale.
- Serverless compute: Azure ML now supports serverless compute where you do not provision dedicated machines — the compute scales automatically and you pay per training run.

**Experiments** are the records of training runs. Each time you train a model in Azure ML, it creates a run record that logs: the hyperparameters used, the metrics produced (accuracy, loss, F1, etc.), the dataset used, and the artifacts produced (the trained model file). Experiments organize runs into named groups. You can compare runs within an experiment to identify the best-performing configuration.

**Models** are the trained artifacts registered in the model registry. Once a model is trained and evaluated, you register it with a name, version, and description. The registry tracks the full lineage: which experiment, which run, and which dataset produced this model.

**Endpoints** are the deployed inference services. Once you register a model, you deploy it to an endpoint. Real-time endpoints respond to individual prediction requests within milliseconds. Batch endpoints process large datasets asynchronously. Azure ML generates a REST API endpoint that you can call from any application.

**Pipelines** are automated sequences of ML steps — data preprocessing, feature engineering, model training, evaluation — connected into a reusable workflow. Pipelines can be scheduled, triggered by new data, or run on demand.

---

## [09:00 - 12:30] Azure ML AutoML

[SHOW DIAGRAM: AutoML workflow. Input: "Labeled Dataset + Task Type." Arrow to "AutoML Engine" containing boxes: "Featurization," "Algorithm Selection," "Hyperparameter Tuning," "Cross-Validation." Arrow to "Model Leaderboard" showing ranked models. Arrow to "Deploy Best Model."]

Azure Machine Learning's Automated ML feature — AutoML — is one of the most AI-900-tested topics. AutoML automates the model selection and tuning process for supervised learning tasks.

The AutoML workflow:

Step one: register a labeled dataset in the Azure ML workspace.

Step two: create an AutoML experiment. Specify:

- Task type: Classification, Regression, or Time Series Forecasting
- Target column: the label column to predict
- Compute: the cluster to run training on
- Exit criteria: maximum training time, maximum number of models to try, or minimum metric threshold

Step three: AutoML runs. It automatically applies featurization — handling missing values, encoding categorical features, normalizing numerics. It then tries multiple algorithms (logistic regression, random forest, gradient boosting, XGBoost, LightGBM, etc.) with different hyperparameter settings. Each combination is a child run within the experiment.

Step four: review the leaderboard. AutoML ranks all attempted models by the primary metric. For classification, the default metric is AUC-weighted. For regression, it is normalized RMSE. You can review individual model performance, explanation reports, and data transformation steps.

Step five: deploy the best model. Select the top model and deploy it to a real-time endpoint with one click.

For AI-900 scenario questions: AutoML is the answer whenever the scenario describes "training a model with minimal code," "automatically trying multiple algorithms," or "finding the best model for a dataset."

---

## [12:30 - 15:30] Azure ML Designer

Azure ML Designer is a visual drag-and-drop interface for building ML pipelines without writing code. You assemble a pipeline by connecting data, transformation, algorithm, and evaluation modules on a canvas.

The Designer workflow:

Step one: drag a dataset asset onto the canvas. Step two: add data transformation modules — normalize data, select columns, clean missing values. Step three: add a split data module to create training and test sets. Step four: drag an algorithm module (e.g., Two-Class Logistic Regression or Multiclass Decision Forest). Step five: add a Train Model module and connect the algorithm and training data. Step six: add Score Model and Evaluate Model modules to generate predictions and metrics on the test set.

Once the pipeline runs successfully, you can publish it as a real-time inference pipeline: swap the training dataset for a web service input, replace the evaluation module with a web service output, and the pipeline becomes a deployable model API.

Designer is particularly useful for learners because it makes the ML workflow visible and inspectable at each step. For AI-900, Designer represents the low-code path to training and deploying models in Azure ML.

---

## [15:30 - 18:30] Model Deployment Options in Azure ML

[SHOW DIAGRAM: Two-column table. Left column: "Real-Time Endpoint." Right column: "Batch Endpoint." Rows: Request type, Latency requirement, Use case example, Compute type, Scaling.]

After training and registering a model, you deploy it to serve predictions. Azure ML offers two deployment types.

**Real-Time Endpoints** respond to individual prediction requests with low latency — typically milliseconds. The endpoint exposes a REST API. Applications send a JSON payload (the input features) and receive a JSON response (the prediction). Real-time endpoints use Azure Container Instances (ACI) for development testing or Azure Kubernetes Service (AKS) for production deployments that need autoscaling.

**Batch Endpoints** process large datasets asynchronously. You submit a batch prediction job — a dataset stored in Azure Blob — and the endpoint returns a file of predictions when processing is complete. No REST API call for individual records; the entire dataset is processed in one job. Batch endpoints are cost-efficient for large periodic prediction workloads (e.g., scoring 10 million customer records overnight).

For AI-900: real-time endpoints are for interactive, request-by-request prediction applications. Batch endpoints are for large-volume, scheduled prediction jobs.

---

## [18:30 - 20:30] MLflow and Experiment Tracking

Azure ML integrates with MLflow, an open-source ML lifecycle management platform. MLflow tracking allows you to log metrics, parameters, and artifacts from any training script — whether running locally or in Azure ML compute.

When you use MLflow in an Azure ML experiment, every training run is logged with:

- Parameters: hyperparameter values used (learning rate, tree depth, etc.)
- Metrics: performance scores at each evaluation step (training loss, validation accuracy, etc.)
- Artifacts: the trained model file, feature importance plots, and confusion matrices

This logging makes experiments reproducible and comparable. A data science team running 200 AutoML trials can identify exactly which parameters produced the best result and compare any two runs side by side.

For AI-900, the key concept is that Azure ML provides experiment tracking — the systematic recording and comparison of model training runs — as a core platform feature.

---

## [20:30 - 22:30] Module Summary and Lab Preview

Let me summarize Module 08.

Azure Machine Learning is the cloud platform for building, training, evaluating, and deploying custom ML models. The workspace organizes data assets, compute targets, experiments, models, endpoints, and pipelines.

AutoML automates algorithm selection and hyperparameter tuning for Classification, Regression, and Time Series Forecasting tasks. The Designer provides a low-code visual pipeline builder. Real-time endpoints serve individual predictions; batch endpoints process large datasets.

This week's lab asks you to trace through an AutoML configuration, match workspace components to their roles, and evaluate model deployment scenarios — all tested directly on AI-900.

See you in Module 09, where we cover Azure Bot Service and conversational AI in depth.

---

## References

- Microsoft Learn — Use Automated Machine Learning in Azure ML: learn.microsoft.com/en-us/training/modules/use-automated-machine-learning/
- Microsoft Learn — Create a regression model with Azure ML Designer: learn.microsoft.com/en-us/training/modules/create-regression-model-azure-machine-learning-designer/
- Microsoft Learn — Deploy machine learning models to managed online endpoints: learn.microsoft.com/en-us/training/modules/deploy-model-managed-online-endpoint/
