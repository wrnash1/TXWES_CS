# Lab Activity: Module 13 — Quality Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

## Total Points: 100

---

## Lab Overview

In this lab you will apply the core quality management tools to a realistic IT project scenario. The lab has four parts: constructing and interpreting an Ishikawa diagram, building and analyzing a Pareto chart, analyzing a control chart, and writing a quality improvement recommendation. Parts 1 and 2 require a spreadsheet or drawing tool; Part 3 is analytical; Part 4 is written.

Submit all deliverables as a single PDF or Word document to the Canvas Module 13 Lab assignment.

---

## Scenario Background

Apex Technology Solutions provides managed IT services to 85 business clients. Over the past quarter, the company's help desk has logged 340 unresolved tickets that exceeded the 4-hour SLA response target. The director of service delivery has launched a quality improvement initiative and hired you as the quality analyst to lead the root cause investigation and develop improvement recommendations.

The help desk manager has provided the following data from ticket analysis:

### Defect Frequency Data (Tickets Exceeding 4-Hour SLA — Q3)

| Defect Category | Number of Tickets |
|-----------------|-------------------|
| Escalation routing errors | 98 |
| Technician skill gaps (wrong tier assigned) | 72 |
| Ticket system outages | 45 |
| Unclear or incomplete ticket submissions | 41 |
| Parts/equipment procurement delays | 34 |
| Supervisor approval bottlenecks | 28 |
| Miscellaneous / uncategorized | 22 |
| **Total** | **340** |

### Control Chart Data (Average SLA Breach Rate — Monthly over 12 Months)

The following data shows the monthly SLA breach rate (percentage of tickets exceeding 4 hours) over the past 12 months. The process mean is 18.5% and control limits are UCL = 26.0% and LCL = 11.0%.

| Month | Breach Rate (%) |
|-------|----------------|
| Jan | 16.2 |
| Feb | 17.8 |
| Mar | 19.1 |
| Apr | 21.3 |
| May | 22.7 |
| Jun | 24.1 |
| Jul | 25.8 |
| Aug | 22.4 |
| Sep | 19.6 |
| Oct | 18.1 |
| Nov | 16.9 |
| Dec | 17.2 |

---

## Part 1 — Ishikawa Diagram

### Part 1 Objective

Construct an Ishikawa diagram identifying the root causes of SLA breaches.

### Part 1 Instructions

Using the defect category data and the scenario background, construct an Ishikawa diagram for the effect: "Help desk tickets consistently exceed the 4-hour SLA target."

Your Ishikawa diagram must include at least four major cause category branches. Suggested categories for this IT service context: Methods, Machines, Manpower, Management. You may add additional categories. For each category, identify at least two specific contributing causes drawn from or logically inferred from the scenario data.

Draw your Ishikawa diagram using a drawing tool, diagramming software, or a hand-drawn scan. Label all branches clearly.

After completing the diagram, answer the following:

**Question 1-A:** Select the two cause categories you believe contribute most significantly to the SLA breach problem. For each, cite specific evidence from the scenario data that supports your assessment. Answer in three to four sentences per category.

**Question 1-B:** The Ishikawa diagram shows many contributing causes. Why is it important to use this structured root cause analysis before choosing a corrective action? What happens to quality improvement efforts when teams skip root cause analysis and jump directly to solutions?

**Part 1 Point Value:** 25 points

- Diagram includes at least four labeled cause categories (8 pts)
- At least two specific causes per category (8 pts)
- Causes are plausible and connected to scenario data (5 pts)
- Question 1-A: Two categories selected with scenario evidence (2 pts)
- Question 1-B: Root cause vs. solution jumping explained (2 pts)

---

## Part 2 — Pareto Chart

### Part 2 Objective

Build a Pareto chart from the defect frequency data and identify the vital few causes.

### Part 2 Instructions

Using the defect frequency table from the scenario, complete the Pareto analysis table below.

Step 1: Sort the defect categories from highest to lowest frequency (already done in the table above — verify the sort order).

Step 2: Calculate the cumulative count and cumulative percentage for each row.

| Rank | Defect Category | Count | Cumulative Count | Cumulative % |
|------|----------------|-------|-----------------|-------------|
| 1 | Escalation routing errors | 98 | | |
| 2 | Technician skill gaps | 72 | | |
| 3 | Ticket system outages | 45 | | |
| 4 | Unclear ticket submissions | 41 | | |
| 5 | Parts/equipment delays | 34 | | |
| 6 | Supervisor approval bottlenecks | 28 | | |
| 7 | Miscellaneous / uncategorized | 22 | | |
| **Total** | | **340** | | **100%** |

Step 3: Using the completed table, create a Pareto chart in a spreadsheet. The chart must include: bars for each defect category (left Y-axis = count), a cumulative percentage line (right Y-axis = 0–100%), and a reference line at 80%.

**Question 2-A:** Based on your Pareto chart, which defect categories fall into the "vital few" — the categories that account for approximately 80% of SLA breaches? List them and state the cumulative percentage they represent.

**Question 2-B:** The director of service delivery wants to launch improvement initiatives for all seven categories simultaneously. Using the Pareto principle, explain why this approach is less effective than focusing on the vital few. How should limited improvement resources be allocated?

**Question 2-C:** "Miscellaneous / uncategorized" accounts for 22 tickets. What should the quality team do with this category before the next analysis cycle, and why does an uncategorized group undermine Pareto analysis?

**Part 2 Point Value:** 30 points

- Pareto table completed correctly — cumulative counts and percentages (10 pts)
- Pareto chart created with bars, cumulative line, and 80% reference (10 pts)
- Question 2-A: Vital few correctly identified with cumulative percentage (4 pts)
- Question 2-B: Pareto principle applied to resource allocation argument (4 pts)
- Question 2-C: Uncategorized group addressed correctly (2 pts)

---

## Part 3 — Control Chart Analysis

### Part 3 Objective

Analyze the control chart data to determine process stability and identify out-of-control conditions.

### Part 3 Instructions

Using the monthly breach rate data and control limits (UCL = 26.0%, LCL = 11.0%, Mean = 18.5%), answer the following questions. You may create a simple line graph of the data to support your analysis, but the questions can be answered from the data table alone.

**Question 3-A:** Plot or examine each monthly data point against the control limits. Are any individual points outside the UCL or LCL? If yes, identify which months and characterize the variation type (special cause or common cause).

**Question 3-B:** Apply the Rule of Seven to the data. Examine the sequence of monthly values. Is there any point in the 12-month period where seven or more consecutive readings fall on one side of the process mean (18.5%)? If yes, identify the months involved and explain what this indicates about the process.

**Question 3-C:** Looking at the full 12-month trend, describe the overall pattern in plain language. What happened to the SLA breach rate from January through July, and what appears to have happened from August through December? What project management action should have been triggered in the May–June timeframe based on the trend?

**Part 3 Point Value:** 25 points

- Question 3-A: Correct identification of out-of-control points vs. within-limit points (8 pts)
- Question 3-B: Rule of Seven correctly applied; consecutive sequence identified (9 pts)
- Question 3-C: Trend described accurately; appropriate management action identified (8 pts)

---

## Part 4 — Quality Improvement Recommendation

### Part 4 Objective

Synthesize the Ishikawa, Pareto, and control chart findings into a written quality improvement recommendation.

### Part 4 Instructions

Write a quality improvement memo addressed to the Director of Service Delivery at Apex Technology Solutions. Your memo must be 200–300 words and address all of the following:

1. Summary of findings from the Pareto analysis — which categories are the vital few and what percentage of SLA breaches they represent
2. The top root cause finding from your Ishikawa analysis — which cause category poses the greatest risk and why
3. Your interpretation of the control chart — whether the process is currently in control and what the trend suggests
4. A recommendation for one specific process improvement initiative, framed using the PDCA cycle (describe what would happen at each PDCA step for your chosen initiative)
5. A recommendation on whether the organization should prioritize prevention costs, appraisal costs, or both in the near term, with a brief explanation

Format: Write as a professional memo with Subject, Date, and your name as quality analyst. Use plain business language — no acronyms without definition.

**Part 4 Point Value:** 20 points

| Criterion | Points | Description |
|-----------|--------|-------------|
| Completeness | 8 | All five required elements addressed |
| Accuracy | 6 | Findings match your Part 1–3 analysis |
| PDCA application | 4 | All four PDCA steps described for chosen initiative |
| Professional tone | 2 | Memo format; business language; no undefined acronyms |

---

## Deliverables Summary

Submit the following in a single PDF or Word document:

1. Ishikawa diagram image and Questions 1-A and 1-B (Part 1)
2. Completed Pareto table, Pareto chart image, and Questions 2-A, 2-B, and 2-C (Part 2)
3. Written responses to Questions 3-A, 3-B, and 3-C (Part 3)
4. Quality improvement recommendation memo (Part 4)

---

## Grading Rubric Summary

| Section | Points | Key Criteria |
|---------|--------|--------------|
| Part 1: Ishikawa Diagram | 25 | Four categories, two causes each, root cause analysis rationale |
| Part 2: Pareto Chart | 30 | Table complete, chart built, vital few identified, resource argument |
| Part 3: Control Chart Analysis | 25 | Out-of-control points, Rule of Seven, trend interpretation |
| Part 4: Quality Improvement Memo | 20 | Five elements, PDCA applied, findings match data |
| **Total** | **100** | |
