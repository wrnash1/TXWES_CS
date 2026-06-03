# Video Script: Module 13 — Data Preparation and Feature Engineering

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Instructor:** Professor Nash

**Estimated Duration:** 20–24 minutes

**AI-900 Domain:** Describe machine learning concepts (20-25%)

---

## [00:00 - 01:30] Opening

Welcome back. Professor Nash here, and this is Module 13. In the last module we covered AI business strategy — use cases, ROI, and build-versus-buy decisions. In this module we go back inside the machine learning pipeline and focus on the work that happens before any model is trained: data preparation and feature engineering. If you have heard the phrase "garbage in, garbage out," this module is about why that is true and what to do about it. Data preparation is typically the most time-consuming phase of any ML project — estimates consistently put it at 60 to 80 percent of total project time — and it is also the phase where most projects either succeed or fail. Understanding this work is essential for AI-900 and for any real engagement with ML projects. Let us get into it.

---

## [01:30 - 06:30] Why Data Quality Determines Model Quality

[SHOW DIAGRAM: Pipeline flow from left to right. Boxes labeled: Raw Data → Data Cleaning → Feature Engineering → Training Data → Model Training → Model. Arrow from Raw Data box has a red annotation: "Most project time spent here." Arrow into Model Training has a green annotation: "Quality of this input determines model ceiling."]

Let me start with a core principle: a model cannot learn patterns that are not present in its training data, and a model will learn patterns that are present in the training data even if those patterns are noise or artifacts. This means the quality of your training data sets a hard ceiling on how good your model can ever be.

**What makes data high quality for ML?**

First: completeness. If important values are missing from your dataset — empty cells, nulls, records where a sensor failed to log — the model either has to ignore those records or make assumptions about the missing values. Either choice introduces error.

Second: accuracy. If the labels in your training data are wrong — for example, customer records tagged as "churned" when the customer actually renewed — your model learns from incorrect signal. Mislabeled training data is particularly damaging because the model cannot distinguish between a real pattern and a labeling error.

Third: representativeness. Your training data needs to reflect the real-world distribution the model will encounter in production. If you train a fraud detection model on data from 2018 and deploy it in 2024, the fraud patterns may have shifted significantly. If you train a loan model on data from only one geographic region and deploy it nationally, the model may systematically underperform in regions it never saw during training.

Fourth: relevance. Not every column in your raw data is useful for prediction. Some features will be noise. Some features will be proxies for protected attributes. Some features will be data leakage — information that would not be available at prediction time in production. Selecting the right features and excluding the wrong ones is as important as the model architecture itself.

---

## [06:30 - 11:00] Data Cleaning Techniques

[SHOW DIAGRAM: Table with four rows. Column 1: Data Problem. Column 2: Description. Column 3: Common Technique. Rows: Missing values, Duplicate records, Outliers, Inconsistent formats.]

Data cleaning is the process of finding and correcting problems in raw data before model training. Let me walk through the most common problems and how to handle them.

**Missing values.** Missing values appear when data was not collected, a system failed, or a user skipped a field. There are three main approaches. First, deletion: remove any record with a missing value. This is simple but wastes data — if 10 percent of your records have a missing field, you lose 10 percent of your training data. Second, imputation: fill in missing values with a calculated substitute — the column mean, median, or mode are common choices. For time series data, forward-fill (carry the last known value forward) is common. Third, indicator encoding: add a binary column that flags "this value was missing" and keep the original column with a placeholder. This lets the model learn whether missingness itself is predictive.

**Duplicate records.** If the same real-world entity appears multiple times in your training data, the model effectively sees those examples more often and may overfit to them. Deduplication identifies and removes exact or near-duplicate records before training.

**Outliers.** An outlier is a value that is far outside the typical range — a transaction amount of $10,000,000 in a dataset where 99 percent of transactions are under $500. Outliers can distort statistical calculations (mean, variance) that models use during training. They may be genuine rare events (keep them), measurement errors (investigate and correct), or data entry mistakes (correct or remove). Capping (also called winsorizing) replaces extreme values with a defined threshold rather than removing records entirely.

**Inconsistent formats.** Raw data from multiple systems often has format inconsistencies: dates stored as "Jan 15 2024" in one system and "2024-01-15" in another, city names spelled differently, category labels like "Male," "M," and "male" that all mean the same thing. Standardization converts all values to a consistent format before training.

---

## [11:00 - 16:00] Feature Engineering

[SHOW DIAGRAM: Left side shows raw columns: "OrderDate," "CustomerBirthDate," "ProductPrice," "ProductCategory." Right side shows engineered features: "DayOfWeek," "HourOfDay," "CustomerAge," "PriceCategory (binned)," "IsWeekend (binary)." Arrow connecting them labeled "Feature Engineering."]

Feature engineering is the process of transforming raw data columns into features that make it easier for a model to learn the patterns you care about. Raw data often does not directly express the signal the model needs — you need to transform it.

**Encoding categorical variables.** Machine learning models work with numbers, not text. When a column contains category labels — like "Red," "Blue," "Green" — you must convert those to numbers. One-hot encoding creates a separate binary column for each category value (IsRed, IsBlue, IsGreen). Label encoding assigns each category an integer (Red=1, Blue=2, Green=3). One-hot encoding is preferred for nominal categories (no natural order); label encoding is appropriate for ordinal categories (Low=1, Medium=2, High=3).

**Normalization and scaling.** When features have very different scales — for example, "age" ranges from 18 to 90 while "income" ranges from 20,000 to 500,000 — models that use distance calculations (like k-NN) or gradient descent (like neural networks) are sensitive to those scale differences. Normalization (min-max scaling) converts all values to a 0-to-1 range. Standardization (z-score scaling) converts values to have mean zero and standard deviation one. Tree-based models (random forest, gradient boosting) are generally scale-insensitive, but scaling is important for linear models and neural networks.

**Deriving new features from existing ones.** Often the raw column is not the most useful signal. A date column is more useful if you extract: day of week, month, hour of day, whether it is a holiday, whether it is a weekend. A customer birthdate is more useful as age. A price column may be more useful as a price tier (low, medium, high) than as a continuous value. Creating these derived features is where domain knowledge becomes essential — a subject matter expert can suggest transformations that a pure data scientist might not think of.

**Binning.** Binning converts a continuous numeric variable into discrete categories. Age might be binned into 18–25, 26–35, 36–50, 51–65, 65-plus. This can reduce sensitivity to outliers and make patterns more interpretable.

**Interaction features.** Some features are more informative together than separately. "Time of day" and "day of week" may each weakly predict customer purchase behavior, but a combined "weekend evening" interaction feature may be much more predictive.

---

## [16:00 - 19:00] Train-Test Split and Data Leakage

[SHOW DIAGRAM: Dataset bar split into three segments. Left 70% labeled "Training Set — model learns from this." Middle 15% labeled "Validation Set — tune hyperparameters." Right 15% labeled "Test Set — evaluate final model only. Never used during training." Red annotation on Test Set: "Must be sealed until final evaluation. If used earlier, you have data leakage."]

Before training any model, you must split your labeled dataset into at least two parts: a training set and a test set. The training set is used to fit the model. The test set is held out until the end to evaluate how the model performs on data it has never seen.

Why is this split necessary? Because a model that was evaluated on the same data it trained on will appear to perform much better than it actually will in production. The model memorized the training data; the evaluation needs to measure generalization.

A three-way split — train, validation, test — is common for more complex projects. The validation set is used during training to tune hyperparameters (the settings that control how the model learns) without touching the test set. The test set is evaluated only once at the very end.

**Data leakage** is one of the most dangerous mistakes in ML development. Leakage occurs when information that would not be available at prediction time in production somehow gets into the training data. For example: including a "churn_date" column when training a churn prediction model — a model that knows when the customer churned will appear perfect on training data but will have nothing to predict in production where no such date exists. Leakage can also occur from future data sneaking into past-dated training records through improper time-based splits.

Cross-validation is a technique that repeatedly splits the training data into different train-validation folds, trains and evaluates on each fold, and averages the results. This provides a more robust estimate of model performance than a single split, especially on small datasets.

---

## [19:00 - 22:00] Data Preparation in Azure Machine Learning

[SHOW DIAGRAM: Azure ML Studio pipeline canvas with nodes: Data Asset (blue cylinder), Data Transformation component (gear icon), Normalize Data component (gear icon), Split Data component (fork shape), Train Model component (triangle), Evaluate Model component (bar chart icon). Arrow flow from left to right.]

Azure Machine Learning Studio provides built-in components for all of the data preparation tasks we have discussed.

**Data assets** in Azure ML allow you to register a dataset and version it — so every model training run is reproducible because you can reference the exact dataset version used.

**Designer components** for data preparation include: Clean Missing Data (choose imputation strategy), Remove Duplicate Rows, Clip Values (outlier capping), Normalize Data (min-max or z-score), and Split Data (random or stratified split into train and test sets).

**Azure ML pipelines** allow you to chain these transformation steps into a reusable workflow that runs every time new data arrives. This is essential for production scenarios where data is updated regularly and the full preparation pipeline needs to run consistently without manual intervention.

**Feature-based data types** in Azure ML Designer: Numeric features are handled by Normalize Data. Categorical features can be handled by the Edit Metadata component (convert String to Categorical) and then one-hot encoded through Feature Hashing or custom transformation. The key principle is that every transformation you apply to training data must also be applied to scoring data at inference time — the preprocessing pipeline must be part of the deployed model, not separate from it.

---

## [22:00 - 24:00] Module Summary

Let me summarize Module 13.

Data quality determines model quality. The key dimensions of data quality are completeness, accuracy, representativeness, and relevance. Most ML project time is spent on data preparation — this is normal, not a sign of project failure.

The main data cleaning tasks are: handling missing values (deletion, imputation, or indicator encoding), deduplication, outlier treatment, and format standardization.

Feature engineering transforms raw data into model-ready features. The key techniques are: encoding categorical variables (one-hot or label encoding), normalizing and scaling numeric features, deriving new features from existing ones, binning, and creating interaction features.

Train-test split ensures model evaluation on unseen data. Data leakage occurs when future information contaminates training data and must be prevented through careful dataset construction and time-aware splitting.

Azure ML Designer provides built-in components for all preparation steps and supports versioned data assets for reproducibility.

In Module 14 we cover model evaluation — how to interpret confusion matrices, calculate precision, recall, and F1 score, and understand when to use each metric. See you then.

---

## References

- Microsoft Learn — Explore and analyze data with Python: learn.microsoft.com/en-us/training/paths/explore-data-science-tools-in-azure/
- Microsoft Learn — Create and run a machine learning pipeline with SDK v2: learn.microsoft.com/en-us/training/modules/run-pipelines-azure-machine-learning/
