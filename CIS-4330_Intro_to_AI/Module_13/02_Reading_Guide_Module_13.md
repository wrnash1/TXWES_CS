# Reading Guide: Module 13 - Data Preparation and Feature Engineering
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 13 - Data Preparation and Feature Engineering**! This module covers the critical work that happens before any model is trained — cleaning raw data, handling missing values, encoding categorical variables, scaling numeric features, and engineering new features that make patterns easier for algorithms to learn. These skills underpin every Azure Machine Learning pipeline and are foundational to producing reliable AI systems.

As a student, you will also learn how Azure Cognitive Services are provisioned and called via REST API, giving you a practical understanding of how pre-trained cloud AI models are consumed in real applications. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Feature engineering**: The process of using domain knowledge to transform raw data into features that better represent the underlying problem structure to machine learning algorithms. Examples include creating a "days since last purchase" feature from a transaction date, binning a continuous age variable into age groups, or extracting title words from a job description. Good feature engineering often improves model accuracy more than algorithm tuning alone.
*   **Pre-trained vs. custom models**: Pre-trained models are trained by a vendor (e.g., Microsoft, OpenAI) on large general-purpose datasets and made available via API — developers call the endpoint and receive predictions without providing training data. Custom models are trained by the developer on domain-specific labeled data for tasks where a general model is insufficient. In Azure, pre-trained models are accessed through Cognitive Services; custom models are built in Azure Machine Learning or Azure Custom Vision.
*   **Deploying endpoint services**: Making a trained model accessible for inference by hosting it behind a REST API endpoint. In Azure Machine Learning, a real-time endpoint exposes a model for synchronous, low-latency predictions (e.g., fraud detection at transaction time), while a batch endpoint processes large volumes of data asynchronously. Both require registering the model, configuring compute resources, and generating an API key for authentication.
*   **Data pipeline (ingest, transform, train, evaluate, deploy)**: The end-to-end workflow for building an ML system. Data is ingested from sources (databases, files, APIs), transformed via cleaning and feature engineering, used to train a model, evaluated against a held-out test set, and then deployed as an endpoint. Azure Machine Learning Designer and Azure Synapse Analytics both support visual data pipeline construction that covers these stages.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** The exam tests the data science lifecycle and which Azure tool handles each stage. Know these: **data ingestion and exploration** → Azure Synapse Analytics or Azure Databricks; **data preparation and feature engineering** → Azure Machine Learning Designer or Python SDK; **model training** → Azure Machine Learning (AutoML, Designer, or Notebooks); **model deployment** → Azure Machine Learning real-time or batch endpoints; **monitoring** → Azure Monitor or Azure Machine Learning model monitoring. Recognizing which stage of the pipeline a tool belongs to is a common exam question pattern.
*   **Common AI-900 Trap:** The exam frequently presents a scenario describing a need to call an existing AI capability (e.g., "translate customer emails to English") and asks which service to use. Cognitive Services / Azure AI services (pre-built models, REST API, no training required) are the answer — not Azure Machine Learning (which is for building and training custom models). Mixing these up is the most common source of wrong answers in the Azure AI services section. The decision rule is: "Do I have labeled training data and a unique problem?" → Azure ML. "Do I just need a general AI capability now?" → Cognitive Services.
*   **Study Resource:** The Microsoft Learn module [Explore and analyze data with Python](https://learn.microsoft.com/en-us/training/modules/explore-analyze-data-with-python/) walks through data loading, cleaning, feature engineering, and visualization using Pandas and Matplotlib in a Jupyter notebook environment — directly applicable to the lab work in this module. It is free and includes all code samples.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters on data representation, feature selection, and machine learning pipelines in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). This freely available textbook by Poole and Mackworth covers how data is structured and transformed for AI systems, providing the theoretical grounding for the feature engineering and pipeline concepts in this module.
*   **Required Video:** Watch the data preparation and Azure ML pipeline segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video covers the end-to-end data science lifecycle within Azure Machine Learning and explains how pre-built Cognitive Service endpoints compare to custom-trained model endpoints in terms of setup effort, cost, and flexibility.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Provision a Cognitive Service resource and retrieve API keys**: Use the Azure portal (or the Azure CLI command `az cognitiveservices account create`) to provision an Azure AI Language resource, then navigate to Keys and Endpoint to copy the subscription key and endpoint URL needed to authenticate API calls.
*   **Make an HTTP request to a Cognitive Service translation endpoint**: Use Python's `requests` library to send a POST request to the Azure Translator API with a JSON body containing sample text, then parse the response to display the translated output — demonstrating how any language can be integrated with a pre-trained model via REST without training data.
*   **Engineer new features from a raw dataset**: Load a tabular dataset with Pandas, create at least two new derived columns (e.g., a ratio feature, a binned categorical from a continuous variable), apply `pd.get_dummies()` for one-hot encoding of categorical columns, and use `StandardScaler` to normalize numeric features — completing a full feature engineering pipeline.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapters on data preparation and ML pipelines in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on Data Preparation and Feature Engineering in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
