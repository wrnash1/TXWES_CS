# Discussion: Module 08 — Data Mining and Predictive Techniques

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 10 (6 initial post + 4 peer responses)

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 2: Data Analysis

---

## Instructions

Choose ONE of the three scenarios below and write an initial post of 175–225 words. Then respond substantively to at least TWO classmates who chose different scenarios. Peer responses must be at least 75 words — add a new insight, ask a probing question, or identify a consideration your classmate missed.

Initial posts are due by Thursday at 11:59 PM. Peer responses are due by Sunday at 11:59 PM.

---

## Scenario A: The Insurance Claims Model

A health insurance company wants to flag potentially fraudulent claims for manual review. The fraud team can only investigate 50 claims per day. Last year, roughly 3% of all claims (about 1,500 out of 50,000) were confirmed fraudulent. The data science team built two candidate models:

- Model 1: Accuracy = 97.2%, Precision = 48%, Recall = 91%, F1 = 63%
- Model 2: Accuracy = 97.8%, Precision = 72%, Recall = 65%, F1 = 68%

In your initial post, address the following:

- Explain why 97%+ accuracy is not the most useful metric here. What characteristic of the dataset makes accuracy misleading?
- Given the 50-case daily review capacity, which model would you recommend and why? Use precision and recall values to justify your choice — consider both false positive volume and actual fraud caught.
- What is the business cost of a false negative in this context? What is the cost of a false positive? How do these costs influence which metric to optimize?

---

## Scenario B: The Retail Customer Segmentation Project

A national retail chain with 2.3 million loyalty card members wants to use k-means clustering for targeted marketing. Features available include: total spend (last 12 months), number of transactions, average basket size, days since last purchase, and product category breadth.

A junior analyst asks: "Why use clustering instead of manually defining segments in Excel — like 'high spenders' and 'low spenders'?"

In your initial post, address the following:

- How would you explain the advantage of k-means over manual segmentation to the junior analyst? What can the algorithm discover that arbitrary cut-off lines cannot?
- Describe the elbow method in plain, non-technical language a business stakeholder could understand. What would it mean if the elbow plot showed a very gradual, smooth curve with no clear elbow?
- Once clusters are identified, how would you validate that the segments are meaningful from a business perspective beyond looking at centroid values? What additional steps would you take before presenting to marketing leadership?

---

## Scenario C: The Loan Default Prediction Dilemma

A community bank wants to use a decision tree model to automate initial loan application screening. A loan officer raises an ethical concern: "Some of our best long-term customers have unconventional financial profiles that would probably get flagged by an algorithm."

In your initial post, address the following:

- Decision trees are praised for interpretability. What does interpretability mean in a lending context, and why does it matter given regulatory requirements such as the Fair Credit Reporting Act?
- How does overfitting threaten the fairness and reliability of the loan model? Describe a specific scenario where a model that overfits training data could produce unfair outcomes for future applicants.
- If the bank considers switching to a random forest for higher accuracy, what interpretability trade-off do they face? How might they attempt to explain random forest predictions to regulators despite the ensemble's black-box nature?

---

## Peer Response Guidelines

When responding to classmates, consider:

- Did they correctly identify which metric applies to the problem's cost structure?
- Did they accurately describe k-means or decision tree trade-offs?
- Is there a business risk, ethical issue, or technical limitation they did not address?
- Can you offer a real-world example that supports or challenges their recommendation?

---

## Grading Rubric (10 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical accuracy | 3 | Correct application of metrics, algorithms, and trade-offs |
| Business reasoning | 2 | Recommendations tied to real context and constraints |
| Depth of analysis | 2 | Goes beyond surface level; considers limitations and alternatives |
| Peer response quality | 2 | Substantive engagement; adds new perspective or challenges assumptions |
| Writing clarity | 1 | Clear, organized, professional tone; within word count |

---

## Professor Nash Note

These scenarios reflect the most consequential decisions analysts face in practice — not just "which algorithm is more accurate," but "which error is more costly," "how do we explain this to a regulator," and "what does this clustering result actually mean for the business?" Push each other to think past the numbers.

---

End of Module 08 Discussion
