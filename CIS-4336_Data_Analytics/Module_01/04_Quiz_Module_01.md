# Quiz: Module 01 - Data Analytics Fundamentals and Data Types
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
What type of data is a database table containing names, dates, and currency values classified as?
*   A) Unstructured data
*   B) Semi-structured data
*   C) Structured data
*   D) Qualitative data only
*   **Correct Answer:** C) Structured data is highly organized into rigid columns and tables (e.g., relational databases).
*   **Distractor Analysis:**
    *   *Why correct:* Structured data is highly organized into rigid columns and tables (e.g., relational databases).
    *   Unstructured data has no predefined schema (e.g., videos).

---

**Question 2**
In data analytics, which of the following most accurately defines **qualitative vs. quantitative variables**?
*   A) Quantitative variables are numeric measurements that can be averaged or summed (e.g., revenue, age), while qualitative (categorical) variables represent labels or groups that cannot be meaningfully averaged (e.g., region, status).
*   B) Quantitative variables are always stored in text format, while qualitative variables are always stored as integers in a database.
*   C) Qualitative variables are the only type used in business intelligence dashboards; quantitative variables are reserved for scientific research.
*   D) Both variable types are identical in practice; the distinction is only theoretical and does not affect how data is analyzed.
*   **Correct Answer:** A) Quantitative variables are numeric measurements that can be averaged or summed (e.g., revenue, age), while qualitative (categorical) variables represent labels or groups that cannot be meaningfully averaged (e.g., region, status).
*   **Distractor Analysis:**
    *   *Why A is correct:* This accurately captures the operational distinction that determines which statistical methods and chart types an analyst should apply.
    *   *Why B is incorrect:* Storage format (text vs. integer) does not determine whether a variable is qualitative or quantitative.
    *   *Why C is incorrect:* Both variable types appear in business intelligence and scientific contexts; neither is restricted to one domain.
    *   *Why D is incorrect:* The distinction is practically significant — averaging a qualitative variable like postal code produces meaningless results and would misrepresent data.

---

**Question 3**
An analyst receives a folder of customer feedback in the form of free-text email bodies. Which data type does this represent, and what is the correct first step in the analytics lifecycle?
*   A) Structured data; load it directly into a relational database without modification.
*   B) Unstructured data; apply a collection and preprocessing step (e.g., text parsing or NLP tokenization) before analysis.
*   C) Semi-structured data; it can be queried directly with standard SQL without any transformation.
*   D) Quantitative data; calculate the mean of all email bodies to find the central tendency.
*   **Correct Answer:** B) Unstructured data; apply a collection and preprocessing step (e.g., text parsing or NLP tokenization) before analysis.
*   **Distractor Analysis:**
    *   *Why B is correct:* Free-text email bodies are unstructured — they have no fixed schema — and must be preprocessed before analytical methods can be applied.
    *   *Why A is incorrect:* Loading raw unstructured text directly into a relational database without preprocessing would make it unqueryable in a meaningful way.
    *   *Why C is incorrect:* Semi-structured data (like JSON) has partial schema indicators; free-text email bodies do not.
    *   *Why D is incorrect:* Free-text is qualitative, not quantitative; computing a mean on text is not a valid operation.

---

**Question 4**
During which phase of the data analytics lifecycle does an analyst create charts and graphs to communicate findings to business stakeholders?
*   A) Data collection
*   B) Data cleaning
*   C) Data visualization and reporting
*   D) Data storage
*   **Correct Answer:** C) Data visualization and reporting is the phase where findings are communicated through charts, graphs, and dashboards to support decisions.
*   **Distractor Analysis:**
    *   *Why C is correct:* Visualization and reporting come after analysis; the goal is communicating insights, not gathering or cleaning raw data.
    *   *Why A is incorrect:* Data collection is the first lifecycle phase — acquiring raw data from sources.
    *   *Why B is incorrect:* Data cleaning removes errors and inconsistencies; it precedes analysis and visualization.
    *   *Why D is incorrect:* Data storage is an infrastructure concern, not an analytical communication phase.

---

**Question 5**
A dataset contains the column "Customer Satisfaction Score" with values 1, 2, 3, 4, or 5. How should this variable be classified?
*   A) Continuous quantitative, because it uses numbers.
*   B) Ordinal (categorical), because the numbers represent ranked labels, not true numeric measurements with equal intervals.
*   C) Nominal categorical, because all five values are equally ranked with no ordering.
*   D) Discrete quantitative, because it can only take whole-number values between 1 and 10.
*   **Correct Answer:** B) Ordinal (categorical), because the numbers represent ranked labels, not true numeric measurements with equal intervals.
*   **Distractor Analysis:**
    *   *Why B is correct:* A Likert scale uses numbers as labels for ordered categories. The difference between 1 and 2 is not necessarily the same as between 4 and 5, so arithmetic operations like averaging are misleading.
    *   *Why A is incorrect:* The variable uses numbers, but being numeric does not make it continuous or truly quantitative — the scale is ordinal.
    *   *Why C is incorrect:* Nominal variables have no ordering; satisfaction scores from 1–5 are clearly ordered (1 = lowest, 5 = highest).
    *   *Why D is incorrect:* While whole numbers are involved, "discrete quantitative" implies meaningful arithmetic (e.g., count of items), which does not apply to a ranked satisfaction label.
