# Discussion: Module 10 — Data Quality and Governance

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 10 (6 initial post + 4 peer responses)

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 5: Data Governance, Quality, and Controls

---

## Instructions

Choose ONE of the three scenarios below and write an initial post of 175–225 words. Then respond substantively to at least TWO classmates who chose different scenarios. Peer responses must be at least 75 words — extend the analysis, challenge an assumption, or offer an alternative governance approach.

Initial posts are due by Thursday at 11:59 PM. Peer responses are due by Sunday at 11:59 PM.

---

## Scenario A: The Pharmaceutical Data Quality Incident

A large pharmaceutical company uses patient clinical trial data to submit drug efficacy reports to the FDA. During a pre-submission audit, the data team discovers the following issues in 120,000 patient records:

- 8% of patient date-of-birth fields are null
- 3% of dosage fields contain values outside the approved trial protocol range
- 6% of records have duplicate patient IDs (the same patient enrolled twice under different IDs)
- Patient records from Site 7 of the trial use metric units (mg/kg) while all other sites use imperial units (mg/lb), but this is not documented anywhere

In your initial post, address the following:

- Map each of the four problems to the correct data quality dimension. For each one, explain precisely why it violates that specific dimension and not one of the others.
- The FDA requires the company to document who is responsible for data quality in clinical trials. Define the appropriate data governance roles for this scenario — who would be the data owner and who would be the data steward? What specific actions would each role take to remediate the four issues before the submission deadline?
- If this data were loaded into a statistical model for efficacy analysis without remediating these issues, which problem would cause the most serious distortion of the results and why?

---

## Scenario B: The Retail Merger Data Consolidation

A regional supermarket chain (Company A) has acquired a competitor (Company B). Both companies have been operating independently for 15 years, each with their own customer loyalty program, product catalog, and supplier database. The combined company now has 2.4 million customer records across both systems — with substantial overlap, since many customers shopped at both chains.

The data team estimates that roughly 320,000 customers exist in both systems under different IDs with slightly different name spellings, different email addresses (some customers updated their email at one chain but not the other), and different purchase histories.

In your initial post, address the following:

- This scenario is a classic MDM problem. Describe what a golden record would look like for a merged customer entity. What data fields should survive from System A, System B, or a combination of both? Define at least two survivorship rules — the logic for choosing which value to keep when the same field has different values in both systems.
- Beyond MDM, which of the six data quality dimensions are most at risk during this merger data consolidation, and what specific quality checks would you run before declaring the merged dataset ready for analytics use?
- The merged company's marketing team wants to run a personalized campaign immediately after the data consolidation. What is the risk of running this campaign before data quality remediation is complete? Describe a specific customer-facing failure scenario that could result from acting on the unverified merged data.

---

## Scenario C: Building a Data Governance Program from Scratch

A 600-person financial services company has never had a formal data governance program. Data is spread across 14 different systems, analysts use different definitions for the same metrics (four different teams calculate "revenue" in four different ways), and no one knows who owns which data or how to contact the right person when data looks wrong.

A new Chief Data Officer has been hired and asks you — a senior data analyst — to propose the first 90 days of a data governance program.

In your initial post, address the following:

- Using the DAMA framework as your organizing structure, identify three of the 11 DAMA knowledge areas that this company should prioritize in its first 90 days. For each area, explain what specific problem it solves in this organization's context and what the first concrete deliverable would be.
- The most visible crisis is the four conflicting definitions of "revenue." Describe exactly how you would resolve this using data governance mechanisms — not just "create a data dictionary." What process, roles, and tools would be involved, and how long would it realistically take?
- The CDO asks whether to start with a data catalog or with an MDM initiative. These are both significant investments. Recommend which to tackle first, and justify your recommendation based on what will deliver the most immediate business value for this specific organization.

---

## Peer Response Guidelines

When responding to classmates, consider:

- Did they correctly map quality issues to the right dimension?
- Did they clearly distinguish data owner from data steward responsibilities?
- Is there a survivorship rule, governance mechanism, or DAMA knowledge area they overlooked?
- Can you offer a real-world example from an industry you know that supports or complicates their recommendation?

---

## Grading Rubric (10 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical accuracy | 3 | Correct dimension mapping, role definitions, MDM/catalog concepts |
| Governance reasoning | 2 | Recommendations grounded in data governance principles and roles |
| Depth of analysis | 2 | Addresses trade-offs and practical constraints, not just definitions |
| Peer response quality | 2 | Substantive engagement; adds new perspective or challenges assumptions |
| Writing clarity | 1 | Clear, organized, professional tone; within word count |

---

## Professor Nash Note

Data quality and governance are often treated as IT problems — something the database team handles behind the scenes. In reality, the decisions that cause most data quality failures happen far upstream: in how forms are designed, how systems are integrated, how job roles are defined, and how business processes handle exceptions. The most effective data analysts understand that fixing data quality means changing business behavior, not just writing SQL cleanup scripts. As you discuss these scenarios, push your thinking past "run a data profile" toward "how do we prevent this from happening again?"

---

End of Module 10 Discussion
