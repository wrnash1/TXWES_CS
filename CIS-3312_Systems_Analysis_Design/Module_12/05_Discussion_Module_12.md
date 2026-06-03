# Discussion Forum: Module 12 — Database Normalization for Business Analysts

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Forum Instructions

Read all three scenarios below. Choose ONE scenario to respond to in your initial post. Your initial post must be 175–225 words. Then post substantive peer responses to at least TWO classmates who responded to different scenarios than you. Each peer response must be at least 75 words and add analytical value beyond agreement.

**Initial post due:** Thursday, 11:59 PM

**Peer responses due:** Sunday, 11:59 PM

---

## Scenario A — The Legacy Spreadsheet

A regional logistics company is modernizing its operations by replacing a thirty-year-old filing system with a new database application. The BA assigned to the project has been handed a master spreadsheet with 47 columns. The spreadsheet tracks shipments, customers, drivers, routes, and billing all in a single flat file. Some columns contain comma-separated values (e.g., "StopsOnRoute" lists multiple city names). Several column groups repeat — Stop1City, Stop1Arrival, Stop2City, Stop2Arrival, up to Stop8.

The project sponsor is impatient and tells the BA: "Just build the database from the spreadsheet. We don't have time for all this normalization stuff. We've been using this spreadsheet for thirty years without problems."

For your initial post, address the following questions. What specific normalization violations exist in this spreadsheet, and which normal forms do they violate? How would you respond to the sponsor's claim that the spreadsheet has worked "without problems"? What is the business risk of building the new database directly from this unnormalized structure? What is your recommended first step?

---

## Scenario B — The Price History Problem

A retail chain's BA has successfully normalized the product catalog database to 3NF. The Products table stores current price, and the OrderItems table references ProductID as a foreign key. Six months after launch, the finance team discovers a critical business problem: historical orders now show the current product price, not the price that was actually charged at the time of purchase. A dress that cost $49.99 last year now shows as $89.99 on last year's invoices because the price was updated.

The BA is told to fix the problem. One developer proposes storing a snapshot of the price on each OrderItem row — which would technically violate 3NF by introducing redundancy. Another developer says the right fix is to create a PriceHistory table with effective dates.

For your initial post, address the following questions. Why did the original 3NF design fail to capture this business requirement? Is storing the price on OrderItem a normalization violation or a justified denormalization? Compare the two proposed solutions — snapshot price vs. PriceHistory table — from a BA perspective. Which would you recommend, and why?

---

## Scenario C — The Reporting vs. Transactional Database Conflict

A hospital information system uses a fully normalized (3NF) transactional database to record patient appointments, diagnoses, and billing. The clinical reporting team complains that their executive dashboards take four to six minutes to load because each report requires joining twelve to fifteen tables. The IT director suggests creating a separate "reporting database" that is intentionally denormalized — essentially a copy of the data flattened into wide tables optimized for reading.

The BA is asked to evaluate this proposal and make a recommendation to leadership. Some stakeholders worry that having two databases will create data consistency problems. Others argue that the transactional database should simply be optimized with indexes rather than creating a second system.

For your initial post, address the following questions. What are the legitimate business reasons for separating transactional and reporting databases? What risks does a denormalized reporting database introduce, and how are they typically managed? How does this scenario relate to the concept of intentional denormalization covered in Module 12? What questions would you ask stakeholders before making a final recommendation?

---

## Peer Response Guidelines

A strong peer response does at least one of the following:

- Challenges an assumption in the initial post with evidence or reasoning
- Adds a real-world example that extends the analysis
- Identifies a trade-off or risk the initial post did not address
- Connects the scenario to a BABOK concept or ECBA exam topic
- Asks a clarifying question that would deepen the analysis

Responses that only say "Great post, I agree" or restate what the original poster said will not receive full credit.

---

## Discussion Rubric — 10 Points Total

| Criterion | Excellent (Full Credit) | Adequate (Partial Credit) | Needs Improvement (Minimal Credit) |
|---|---|---|---|
| Initial post — content accuracy (3 pts) | Correctly identifies normalization concepts; analysis is technically sound | Minor inaccuracies; concepts mostly applied correctly | Significant errors or missing normalization analysis |
| Initial post — depth of analysis (3 pts) | Addresses all prompt questions; provides business context; reasoning is clear | Addresses most questions; limited business reasoning | Addresses fewer than half the questions; superficial |
| Peer response 1 — analytical value (2 pts) | Extends, challenges, or enriches the original post with substance | Agrees with minimal addition; some new content | Restatement or empty affirmation only |
| Peer response 2 — analytical value (2 pts) | Extends, challenges, or enriches the original post with substance | Agrees with minimal addition; some new content | Restatement or empty affirmation only |

---

*Module 12 Discussion | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
