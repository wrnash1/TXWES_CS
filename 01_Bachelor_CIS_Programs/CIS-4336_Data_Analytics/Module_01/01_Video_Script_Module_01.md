# Video Script — Module 01: Data Analytics Fundamentals and Data Types

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Runtime:** 20–24 minutes
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 1: Data Concepts and Environments

---

## Segment 1 — Introduction (2 minutes)

Welcome to CIS-4336 Data Analytics. I am Professor Nash, and this is Module 01: Data Analytics Fundamentals and Data Types.

This module sets the foundation for everything that follows in the course. Before you can analyze data, clean it, visualize it, or build dashboards, you need to understand what data actually is — how it is classified, where it lives, and why those classifications matter in professional practice.

By the end of this module, you will be able to:

- Define data analytics and explain its role in organizational decision-making
- Distinguish between descriptive, diagnostic, predictive, and prescriptive analytics
- Classify data by structure, type, and scale of measurement
- Explain why data literacy matters for business analysts and IT professionals
- Identify these concepts as they appear on the CompTIA Data+ DA0-001 exam

If you are studying for the Data+ exam, Domain 1 — Data Concepts and Environments — covers approximately 15% of the exam. This module maps directly to that domain. I will flag specific exam-relevant points throughout the lecture.

Let us get started.

---

## Segment 2 — What Is Data Analytics? (3 minutes)

Data analytics is the process of examining raw data to draw conclusions, identify patterns, and support decisions. That definition sounds simple, but it hides significant complexity.

Think about a retail company. Every time a customer makes a purchase, data is generated — item scanned, price charged, timestamp recorded, payment method used, loyalty ID captured. That single transaction produces a dozen data points. Multiply that by thousands of customers across hundreds of stores, and you have a dataset that no human can process manually.

Data analytics provides the tools, techniques, and frameworks to turn that volume of raw facts into actionable insight.

The CompTIA Data+ exam distinguishes between four analytic types. Learn these categories cold — they appear directly on the exam.

**Descriptive analytics** answers the question: what happened? It summarizes historical data. A monthly sales report is descriptive. A dashboard showing yesterday's website traffic is descriptive. Descriptive analytics is the most common type in practice today.

**Diagnostic analytics** answers: why did it happen? It moves beyond summary to root-cause investigation. If sales dropped in Q3, a diagnostic analyst digs into the data to find contributing factors — pricing changes, supply chain disruptions, or competitor promotions.

**Predictive analytics** answers: what is likely to happen? It uses statistical models and machine learning to forecast future outcomes. A credit scoring model predicting loan default probability is predictive analytics.

**Prescriptive analytics** answers: what should we do about it? It goes further than prediction — it recommends actions. A logistics optimization engine that tells a driver which route to take is prescriptive.

[SHOW CHART: Four-quadrant diagram placing Descriptive, Diagnostic, Predictive, and Prescriptive in order of complexity and business value, with an example use case in each quadrant]

Each type builds on the previous one. You cannot do prescriptive analytics without first having strong descriptive and predictive capabilities. Understanding this progression is both conceptually important and practically essential for the exam.

---

## Segment 3 — Structured, Unstructured, and Semi-Structured Data (4 minutes)

Now let us talk about how data is structured — more precisely, how it is organized for storage and processing.

**Structured data** is organized into a predefined schema of rows and columns. A relational database table is the canonical example. Customer ID, First Name, Last Name, Email, Purchase Date — each field has a defined type and every record follows the same format. Structured data is easy to query with SQL and easy to analyze with spreadsheet tools. It represents roughly 20 percent of all data generated today.

**Unstructured data** has no predefined format. Email bodies, social media posts, audio recordings, video files, and PDF documents are all unstructured. The content is rich and meaningful, but analyzing it requires specialized techniques such as natural language processing or computer vision. Approximately 80 percent of enterprise data is unstructured.

**Semi-structured data** sits between those two categories. It does not conform to a rigid schema, but it does contain tags, markers, or keys that impose some organization. JSON files, XML documents, and log files are semi-structured. A JSON API response has named keys, but a given record might have different keys than another, and values might be nested at arbitrary depth.

[SHOW CHART: Three-column comparison table showing Structured, Semi-Structured, and Unstructured data with examples, typical storage systems, and query approaches for each category]

On the Data+ exam, you will be asked to classify data examples as structured, unstructured, or semi-structured. Practice this classification until it is automatic.

---

## Segment 4 — Quantitative vs. Qualitative Data (3 minutes)

Beyond structure, we classify data by its nature: is it numeric, or is it categorical?

**Quantitative data** is numeric and measurable. It has meaningful arithmetic relationships. Revenue of $1.2 million is quantitative. Temperature in Fahrenheit is quantitative. You can add, subtract, average, and compute standard deviations on quantitative data.

**Qualitative data** — also called categorical data — represents characteristics or categories. Product category names, country of origin, and customer satisfaction ratings expressed as text are qualitative. You cannot compute the average of "North," "South," "East," and "West." However, you can count frequencies and compute percentages.

Within quantitative data, there is a further split.

**Discrete data** takes on countable, distinct values. Number of items sold and number of support tickets opened are discrete. There is no meaningful value between five tickets and six tickets.

**Continuous data** can take any value within a range. Height, weight, temperature, and elapsed time are continuous. A person can be 5.73 feet tall.

Within qualitative data, there is also a split.

**Nominal data** has categories with no inherent order. Colors, product types, and country names — there is no meaningful ranking among these.

**Ordinal data** has categories with a meaningful order, but the intervals between categories are not necessarily equal. Customer satisfaction on a scale of Poor, Fair, Good, and Excellent is ordinal. Excellent is better than Good, but the gap between them is not precisely quantifiable.

[SHOW CHART: Data classification hierarchy — Quantitative branches to Discrete and Continuous; Qualitative branches to Nominal and Ordinal, with two examples under each branch]

---

## Segment 5 — Scales of Measurement (3 minutes)

Building on the qualitative and quantitative distinction, data scientists use a four-level classification called the scales of measurement, originally developed by psychologist Stanley Stevens in 1946. The CompTIA Data+ exam tests this framework.

**Nominal scale** — Categories with no order and no arithmetic meaning. Examples: gender, zip code, product category. You can count occurrences and compute mode. You cannot compute mean or median.

**Ordinal scale** — Ordered categories with unknown interval spacing. Examples: survey ratings, military rank, academic letter grades. You can rank values and compute median. You should not compute mean because intervals between categories are unequal.

**Interval scale** — Ordered categories with equal intervals but no true zero point. Temperature in Celsius or Fahrenheit is the classic interval example. The difference between 20 degrees and 30 degrees is meaningful and equal to the difference between 30 degrees and 40 degrees. But zero degrees Celsius does not mean "no temperature." You can compute mean and standard deviation, but ratios are not meaningful — 40 degrees is not "twice as hot" as 20 degrees.

**Ratio scale** — All properties of interval scale plus a true zero. Height, weight, income, and distance are ratio measurements. Zero means the complete absence of the quantity. Ratios are fully meaningful: a $100,000 income is twice a $50,000 income.

[SHOW CHART: Table with four rows — Nominal, Ordinal, Interval, Ratio — with columns: Can Order?, Equal Intervals?, True Zero?, Valid Operations, and Examples]

Why does this matter for analytics? Because the scale of measurement determines which statistical operations are valid. Applying an average to nominal data is a common and costly mistake. The exam will test your ability to identify the correct scale and the appropriate operations for each.

---

## Segment 6 — Data Sources and Common File Formats (3 minutes)

Data comes from many places and in many formats. As an analyst, you need to recognize these sources and understand their implications for data quality and analysis workflow.

**Transactional systems** — Point-of-sale systems, ERP platforms, and order management tools generate highly structured operational data at high volume and are typically well-governed.

**Survey data** — Data collected through instruments such as Qualtrics or Google Forms. Often a mix of ordinal Likert scales, nominal multiple-choice fields, and open-ended text responses.

**Machine and sensor data** — IoT devices, server logs, network packet captures, and manufacturing sensors produce time-stamped, high-frequency, semi-structured or structured data streams.

**Web and social media data** — Click-through data, social posts, and web scraping outputs are predominantly unstructured and contain significant noise.

**Third-party data** — Demographic datasets, market research panels, and public government data are useful for enrichment but may carry quality concerns.

Common file formats you will encounter include the following.

- **CSV** — Comma-Separated Values. The most common flat-file format for data exchange. Simple and universally supported, but provides no schema enforcement.
- **JSON** — JavaScript Object Notation. The dominant format for API responses. Semi-structured, human-readable, and natively supports nested structures.
- **XML** — Extensible Markup Language. An older semi-structured format that remains widely used in enterprise system integrations.
- **Parquet** — A columnar binary format used in big data systems. Highly efficient for analytical queries on large datasets.
- **Excel (.xlsx)** — Common in business contexts. Supports formulas and formatting but is not optimal for programmatic analysis at scale.

[SHOW CHART: Data source and format matrix with rows for each source type and columns for typical format, structure category, and primary use case]

---

## Segment 7 — The Data Analytics Lifecycle (2 minutes)

Professional data analytics follows a repeatable lifecycle. Different frameworks use different labels, but the core stages are consistent.

Stage one — **Define the question.** What business problem are we solving? Ambiguous questions produce useless answers. Clarity here determines the quality of everything downstream.

Stage two — **Collect the data.** Identify sources, extract data, and load it into a working environment.

Stage three — **Clean and transform.** Handle missing values, correct errors, normalize formats, and engineer features as needed. This stage typically consumes 60 to 80 percent of total analyst time.

Stage four — **Analyze.** Apply statistical methods, run queries, and build models.

Stage five — **Visualize and communicate.** Create charts, dashboards, and narratives that make findings accessible to decision-makers.

Stage six — **Act and monitor.** Deploy insights into decisions or products, monitor outcomes, and iterate.

[SHOW CHART: Circular lifecycle diagram with six labeled stages and arrows showing the iterative relationship between stages]

The Data+ exam tests your understanding of this lifecycle in the context of governance, documentation, and data management. Keep this framework in mind throughout the course.

---

## Segment 8 — Why Data Literacy Matters (2 minutes)

Data literacy is the ability to read, interpret, communicate, and reason about data. The World Economic Forum has ranked data literacy among the top five skills employers will demand through 2030.

Consider two analysts given the same dataset. The first applies the wrong statistical test, misinterprets a correlation as causation, and builds a dashboard that misleads executives. The second understands the data types involved, chooses appropriate methods, clearly communicates uncertainty, and adds appropriate caveats. Same data — radically different outcomes.

Data+ certification validates foundational data literacy: you understand data types, know what questions analytics can and cannot answer, can evaluate data quality, and can communicate results responsibly.

Throughout this course, we will build every layer of that competency.

---

## Segment 9 — Exam Alignment and Closing (2 minutes)

Before we close, let me connect today's content directly to the Data+ DA0-001 exam.

The exam blueprint lists Domain 1 — Data Concepts and Environments — at approximately 15 percent of total scored questions. Subdomain 1.1 covers data types and formats. Subdomain 1.2 covers common data structures. Subdomain 1.3 covers file formats.

Everything covered today maps directly to those subdomains.

For additional exam preparation resources, I recommend Professor Messer's free study materials at professormesser.com and the official CompTIA exam objectives available at comptia.org. Both are reputable and exam-specific.

Your assignments for Module 01 are as follows.

- Complete the Reading Guide — pay close attention to the data classification tables and the scales of measurement reference.
- Complete Lab 01 — you will classify real datasets and identify appropriate analytical methods.
- Complete the ten-question quiz.
- Post your initial response to the Discussion Board by the Wednesday deadline, then respond to at least two classmates by Sunday.

I will see you in Module 02, where we cover data collection and data sources in depth.

---

End of Module 01 Video Script — Estimated runtime: 22 minutes
