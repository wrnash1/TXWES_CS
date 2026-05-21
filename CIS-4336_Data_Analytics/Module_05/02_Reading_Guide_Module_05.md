# Reading Guide: Module 05 - Statistical Foundations – Descriptive Statistics
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

### Introduction
Welcome to **Module 05 - Statistical Foundations: Descriptive Statistics**! Before drawing conclusions from data, analysts must first summarize and understand its shape, center, and spread. This module covers the descriptive statistics that appear throughout the **CompTIA Data+** exam — measures of central tendency, measures of dispersion, and the detection of outliers using statistical thresholds.

These concepts are foundational to every subsequent module. An analyst who cannot correctly interpret a mean vs. median, or explain why standard deviation matters, cannot reliably interpret charts, build models, or validate data quality.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Mean**: The arithmetic average of a dataset, calculated by summing all values and dividing by the count. The mean is sensitive to outliers — a single extreme value can pull the mean far from the typical value. In skewed distributions, the mean and median diverge significantly.
*   **Median**: The middle value when data is sorted in ascending order. For an even number of values, the median is the average of the two middle values. The median is resistant to outliers and is the preferred measure of center for skewed distributions such as income or house prices.
*   **Mode**: The value that appears most frequently in a dataset. A dataset can be unimodal (one mode), bimodal (two modes), or multimodal. Mode is the only measure of central tendency applicable to nominal categorical data (e.g., most common product category).
*   **Standard deviation and variance**: Variance is the average of the squared differences from the mean; standard deviation is its square root. Both measure how spread out values are around the mean. A small standard deviation means data points are clustered near the mean; a large one means they are widely dispersed. Standard deviation is expressed in the same units as the original data, making it more interpretable than variance.
*   **Range**: The simplest measure of spread — the difference between the maximum and minimum values in a dataset. Range is highly sensitive to outliers because it depends entirely on the two extreme values.
*   **Imputation and outlier detection using IQR and Z-score**: The Interquartile Range (IQR = Q3 − Q1) measures the spread of the middle 50% of data. Values below Q1 − 1.5×IQR or above Q3 + 1.5×IQR are flagged as potential outliers. A Z-score measures how many standard deviations a value is from the mean; values with |Z| > 3 are commonly flagged as outliers.

---

### 2. Certification Exam Tips
*   **Domain weight:** Statistics concepts appear in Data Mining (Domain 3, ~23%) and Analytics and Reporting (Domain 4, ~23%) of the Data+ DA0-001 exam. Scenario questions frequently ask you to select the correct measure of center or spread for a given situation.
*   **Exam trap — mean vs. median with outliers:** When a question describes a skewed dataset (e.g., "executive salaries inflate the average"), the answer involving the best measure of center is always median, not mean. The exam tests this repeatedly.
*   **Exam trap — standard deviation vs. variance:** Standard deviation is in the same units as the data and is directly interpretable. Variance is in squared units. When a question asks which statistic is more useful for comparing spread to the original data values, the answer is standard deviation.
*   **Exam trap — IQR outlier rule:** The 1.5×IQR rule is the standard Data+ method for flagging outliers in box plots. Know how to compute Q1, Q3, and IQR from a sorted list.
*   **Study Resource:** Chapters on data summarization in [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/) cover all these measures with visual examples including box plots and distribution plots. The [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238) demonstrates computing these statistics using NumPy and Pandas.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the data summarization and distribution chapters in the OER Textbook: [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/). Focus on sections covering central tendency, spread, and visualization of distributions with box plots and histograms.
*   **Required Video:** Watch the statistics and NumPy sections of the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238), which demonstrates calculating mean, median, standard deviation, and IQR on real datasets.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Calculate mean, median, and mode for a dataset of house prices**: Compare all three measures and explain which best represents the typical price given the distribution shape.
*   **Compute IQR and identify outlier prices**: Calculate Q1, Q3, and IQR, then flag any values outside the 1.5×IQR boundaries as outliers.
*   **Impute missing ages using the dataset median**: Justify the choice of median over mean given the age distribution, then verify the imputation did not distort the overall distribution.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the data summarization chapters in [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/).
- [ ] Watch the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238).
- [ ] Review the lab instructions and understand what each task requires.
- [ ] Proceed to the weekly hands-on lab activity.
