# Discussion: Module 12 — ERP Integration and Middleware

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Instructions

Respond to **one** of the three scenarios below. Your initial post must be 175–225 words and address all embedded questions. After posting, reply substantively to **two classmates** who chose different scenarios. Peer replies must be at least 75 words and add new insight — do not simply agree. Initial posts are due by Thursday at 11:59 PM; peer replies are due by Sunday at 11:59 PM.

---

## Scenario 1: The Integration Meltdown

A regional bank uses Salesforce for customer relationship management and a mainframe core banking system for account data. The two systems are connected by a custom point-to-point integration built by a contractor who left the company three years ago. Every few months the integration silently fails — new Salesforce accounts are not reflected in the core banking system — and nobody notices until a customer calls to complain.

The bank's CTO has asked you to assess the situation and propose a sustainable architecture.

Address the following in your post:

- What are the structural risks of the current point-to-point integration, and why does it fail silently?
- What integration pattern would you recommend as a replacement, and why?
- How would you build in monitoring and alerting so that failures are detected within minutes rather than months?
- What is one non-technical challenge (people, process, or policy) the bank will face in replacing this integration?

Your response should demonstrate understanding of integration patterns, middleware concepts, and operational monitoring principles covered in Module 12.

---

## Scenario 2: The Data Mapping Disaster

A pharmaceutical company is migrating customer master data from their legacy CRM (a custom-built Access database) into Salesforce. The legacy system has 45,000 customer records collected over 15 years. During initial analysis, the integration team discovers:

- Customer names are stored in a single "FULL_NAME" field with inconsistent formatting (sometimes "Last, First," sometimes "First Last," sometimes just a company name)
- Phone numbers have no consistent format (some have country codes, some have extensions written as "x123," some are empty, some contain notes like "cell only")
- 12% of records have duplicate entries with slightly different spellings
- The "State" field contains a mix of abbreviations and full state names
- There is no unique customer identifier — the primary key is an auto-increment integer that has no meaning in Salesforce

Address the following in your post:

- Which of these data quality problems presents the greatest risk to the migration, and why?
- What transform steps would you apply to address at least two of these issues before loading into Salesforce?
- What Salesforce feature would you use to prevent future duplicates after the migration is complete?
- Why is data quality often described as the hardest part of an ERP integration project?

Your response should demonstrate understanding of ETL transformation, data quality principles, and Salesforce duplicate management.

---

## Scenario 3: Build vs. Buy the Middleware

A mid-sized logistics company is planning its first integration between Salesforce and SAP S/4HANA. The VP of IT has asked the team to evaluate two approaches:

**Option A:** Purchase a MuleSoft Anypoint Platform subscription and use pre-built Salesforce and SAP connectors to build the integration visually.

**Option B:** Build custom integration code in Python that calls the Salesforce REST API on one end and SAP's OData API on the other, hosted on the company's existing cloud infrastructure.

The project budget is $200,000 for the first year, and the team has two developers with Python experience but no MuleSoft experience.

Address the following in your post:

- What are the key advantages of Option A (MuleSoft) in this scenario?
- What are the key advantages of Option B (custom code) given this team's skills and budget?
- Which option would you recommend, and what is your primary reason?
- What hidden costs or risks does your recommended option carry that the VP might not have considered?

Your response should demonstrate understanding of middleware platforms, build-vs-buy trade-offs, and integration lifecycle considerations.

---

## Peer Response Guidelines

When replying to a classmate's post:

- Reference a specific point they made and either build on it or respectfully challenge it with evidence from the reading or video
- Add a new consideration, example, or real-world connection they did not address
- Avoid phrases like "Great post!" as a standalone — every reply must add substantive content

---

## 10-Point Grading Rubric

| Criterion | 2 Points | 1 Point | 0 Points |
|-----------|----------|---------|----------|
| **Addresses all scenario questions** | All embedded questions fully addressed | Some questions addressed; one is missing or superficial | Multiple questions missing or response is off-topic |
| **Demonstrates module content mastery** | Correctly applies at least two integration concepts from Module 12 with accurate terminology | Uses module vocabulary but applies it imprecisely or without clear connection to the scenario | Little to no use of module concepts; response is generic |
| **Analysis depth** | Provides specific reasoning for recommendations; considers trade-offs | Makes recommendations without explaining reasoning or trade-offs | States opinions without any supporting analysis |
| **Writing quality** | Well-organized, clear sentences, 175–225 words, no significant grammatical errors | Mostly clear but with organizational or grammatical issues; length within 10% of range | Difficult to follow, significantly below word count, or major grammatical issues impede comprehension |
| **Peer responses (two required)** | Both replies are 75+ words, add substantive new content, and engage with the classmate's specific argument | One strong reply; second reply is brief or generic | Zero or one reply submitted; replies add no new content |

**Total: 10 points**

---

## Sample Strong Opening Lines (to inspire, not copy)

For Scenario 1: "The silent failure mode of this point-to-point integration is a symptom of a deeper architectural problem: without a central monitoring layer, there is no single place to observe message flow or detect gaps..."

For Scenario 2: "The absence of a unique customer identifier is the highest-risk data quality problem in this migration, because without a stable key, the upsert operation cannot reliably distinguish between a new record and an update to an existing one..."

For Scenario 3: "While MuleSoft's pre-built connectors would accelerate delivery, the first-year subscription cost for an enterprise MuleSoft license could consume a significant portion of the $200,000 budget before a single line of integration logic is written..."

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
