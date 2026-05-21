# Reading Guide: Module 01 - Data Analytics Fundamentals and Data Types
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

### Introduction
Welcome to **Module 01 - Data Analytics Fundamentals and Data Types**! This module introduces the foundational vocabulary and concepts that underpin every domain of the **CompTIA Data+** certification. You will learn how organizations use data to drive decisions, the categories of data that analysts work with, and the lifecycle that transforms raw data into actionable insight.

Understanding data types and the analytics lifecycle is not just theoretical — exam scenario questions will ask you to identify which phase an analyst is in, choose the right data type for a given business situation, and distinguish between structured and unstructured sources. Complete the glossary, readings, and checklist before proceeding to the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Data analytics lifecycle**: The end-to-end process an organization follows to turn raw data into decisions, typically moving through stages of collection, cleaning, analysis, visualization, and communication of results. The CompTIA Data+ exam tests your ability to identify which lifecycle stage a given activity belongs to.
*   **Structured vs. unstructured data**: Structured data is organized into rows and columns with a predefined schema (e.g., a relational database table). Unstructured data has no fixed format and includes text documents, images, video, and social media posts. Semi-structured data (JSON, XML) falls between the two and is increasingly important in modern analytics pipelines.
*   **Qualitative vs. quantitative variables**: Quantitative variables represent numeric measurements that can be added or averaged (e.g., revenue, temperature). Qualitative (categorical) variables represent labels or groups that cannot be meaningfully averaged (e.g., region, product color). The exam distinguishes between continuous quantitative data (any value within a range) and discrete quantitative data (whole-number counts only).

---

### 2. Certification Exam Tips
*   **Domain weight:** Data Concepts and Environments is Domain 1 of the Data+ DA0-001 exam and accounts for approximately 15% of scored questions. Fundamental definitions from this module appear throughout this domain.
*   **Common trap — qualitative vs. quantitative:** The exam often presents a variable like "customer satisfaction score (1–5)" and asks whether it is quantitative or qualitative. Likert-scale scores are ordinal (a type of qualitative/categorical), not truly quantitative, even though they use numbers.
*   **Common trap — structured vs. semi-structured:** Do not confuse CSV files with structured data. A CSV exported from a database is structured; a raw JSON feed from an API is semi-structured. The exam tests this distinction in ETL and data-source questions.
*   **Study Resource:** For a comprehensive free introduction, work through the data concepts chapters of [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/), a free OER textbook that covers foundational analytics vocabulary aligned with Data+ objectives.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the introductory chapters on data types and the analytics process in the OER Textbook: [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/). Pay particular attention to the sections distinguishing variable types and data structures.
*   **Required Video:** Watch the full [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238) — this 4-hour course covers data fundamentals, Pandas, and NumPy in a hands-on format aligned with Data+ practical skills.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Classify raw data inputs as qualitative or quantitative**: Given a sample dataset, identify each column's variable type and justify your classification.
*   **Identify structured vs. unstructured datasets**: Examine three different data sources (CSV, JSON, image folder) and categorize each with an explanation.
*   **Map the steps of the analytics lifecycle**: Take a provided business scenario and annotate which analytics lifecycle stage each task belongs to.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the introductory chapters on data types in [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/).
- [ ] Watch the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238).
- [ ] Review the lab instructions and understand what each task requires.
- [ ] Proceed to the weekly hands-on lab activity.
