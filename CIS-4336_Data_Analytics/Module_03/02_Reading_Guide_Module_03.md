# Reading Guide: Module 03 - Data Cleaning and Transformation
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

### Introduction
Welcome to **Module 03 - Data Cleaning and Transformation**! Raw data collected from real-world sources is almost never analysis-ready. This module covers the systematic techniques used to detect and correct data quality problems — duplicate records, missing values, type mismatches, inconsistent formats, and outliers — before any analysis begins. These tasks fall squarely within the **CompTIA Data+** Data Mining domain and represent one of the highest-effort phases of any analytics project.

Understanding when to delete, impute, transform, or flag problematic data — and the consequences of each choice — is essential for the exam and for professional practice.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Deduplication**: The process of identifying and removing exact or near-exact duplicate records from a dataset. Duplicates inflate counts and distort aggregations; deduplication typically uses a combination of key-field matching and fuzzy matching algorithms to detect redundancy without discarding legitimate similar records.
*   **Handling missing values**: Strategies for dealing with NULL or empty fields include listwise deletion (drop the entire row), pairwise deletion (exclude only for analyses requiring that field), mean/median/mode imputation (replace with a central tendency estimate), and model-based imputation (predict the missing value using other columns). The choice of strategy affects downstream statistical validity.
*   **Type casting**: Converting a column from one data type to another — for example, changing a text field containing dates into an actual date type, or converting a string "123" into the integer 123. Incorrect data types prevent arithmetic operations and date range filters from working correctly.
*   **Text cleaning with regex**: Regular expressions (regex) are pattern-matching rules used to standardize free-text fields — trimming whitespace, removing special characters, extracting substrings, or validating formats like phone numbers and email addresses. Regex is a core tool in any ETL pipeline.
*   **Normalizing schemas**: Restructuring data to reduce redundancy by organizing it into related tables (1NF, 2NF, 3NF). Normalization eliminates update, insertion, and deletion anomalies. The Data+ exam tests your ability to identify which normal form a given table violates.

---

### 2. Certification Exam Tips
*   **Domain weight:** Data Mining is Domain 3 of the Data+ DA0-001 exam (approximately 23% of scored questions). Data cleaning and transformation questions frequently appear as scenario-based items describing a dirty dataset.
*   **Exam trap — deletion vs. imputation:** The exam may describe a dataset with 2% missing values in one column and 40% missing in another. Always choose deletion or imputation based on the percentage missing and the impact on sample size — imputing 40% of a column's values introduces significant bias; deletion is often better there.
*   **Exam trap — when to use mean vs. median imputation:** Use mean imputation only when the data is roughly symmetric and free of extreme outliers. When outliers are present, median imputation is preferred because the median is resistant to skew.
*   **Study Resource:** The data wrangling and tidy data chapters of [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/) cover these cleaning techniques with worked examples. The [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238) demonstrates Pandas-based cleaning workflows including `dropna()`, `fillna()`, `astype()`, and string methods.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the data wrangling and string processing chapters in the OER Textbook: [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/). Focus on sections covering data import problems, missing data patterns, and string manipulation techniques.
*   **Required Video:** Watch the cleaning and transformation sections of the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238) — this free course demonstrates practical Pandas operations for handling real-world dirty data.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Deduplicate a list of transaction records**: Identify duplicate rows using a combination of key fields and remove them, documenting how many duplicates were found.
*   **Convert text columns to uppercase and standardize formats**: Apply string transformation to normalize inconsistent entries (e.g., "new york", "New York", "NEW YORK" → "NEW YORK").
*   **Handle empty entries using appropriate strategies**: Evaluate each column's null percentage, then apply mean/median imputation for numeric columns and mode imputation or "Unknown" fill for categorical columns.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the data wrangling chapters in [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/).
- [ ] Watch the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238).
- [ ] Review the lab instructions and understand what each task requires.
- [ ] Proceed to the weekly hands-on lab activity.
