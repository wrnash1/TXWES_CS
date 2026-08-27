# Lab Activity: Module 16 - Final Exam Submission
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

## Objective
Schedule and complete the official **Salesforce Certified Associate / SAP Certified Associate** industry certification exam, and submit your score verification report to Professor Nash.

## Instructions
1.  Register for the exam at the on-campus testing center or an authorized provider.
2.  Complete the exam.
3.  Obtain your official score report PDF showing your name, passing status, and date.
4.  Upload the official score report PDF to the Canvas LMS assignment box for this module to receive final credit.

---

## Part 9 — Challenge Exercise

### Challenge 1: Full-Course Synthesis — Enterprise Architecture Design

A private equity firm has acquired three mid-sized manufacturing companies (each 400–800 employees) and intends to consolidate them onto a single SAP S/4HANA instance with Salesforce CRM integrated for all three entities within 24 months. Each acquired company currently runs a different legacy ERP (one on Microsoft Dynamics, one on Oracle EBS, one on a custom-built system). Each has its own chart of accounts, customer numbering scheme, and vendor master records — with significant overlap (the same vendor appears in all three systems under different IDs).

1. Design the enterprise architecture for the consolidated platform. Identify: (a) which SAP organizational units (Company Codes, Controlling Areas, Plants, Sales Organizations) you would configure for a three-entity structure, (b) whether you would use a single Salesforce org or three separate orgs for the CRM layer and why, and (c) how middleware integration between Salesforce and SAP would handle the multi-entity routing problem (an Opportunity closed in Salesforce for Entity B must create a Sales Order in Entity B's SAP Company Code, not Entity A's).

2. The data migration is the highest-risk workstream. Each legacy system has vendor master records with different numbering schemes. You must merge the three vendor master datasets into one SAP vendor master without creating duplicate vendors. Design the vendor master consolidation approach: define the matching logic you would use to identify duplicates across systems, describe the data quality dimensions (completeness, uniqueness, accuracy, consistency) you would validate before migration, specify the SAP transaction used to create vendor masters in bulk, and explain how you would handle a case where Vendor "Acme Industrial" in System A and "Acme Ind. Supply" in System B turn out to be the same legal entity.

3. The three companies have different Segregation of Duties (SoD) maturity levels: Company A has formal SoD controls audited annually; Company B has informal controls enforced by manager review; Company C has no SoD controls at all. Design a phased SoD implementation approach for the consolidated SAP system: which company's control framework should be used as the template, how you would use SAP GRC Access Control to detect and remediate conflicts during the consolidation project, and what your go-live criterion is for SoD compliance across all three entities.

4. The 24-month timeline requires three parallel implementation streams (one per entity) converging on a single production system. Using SAP Activate methodology, describe how you would structure the project governance to manage three simultaneous Realize phases — specifically: how design decisions made for Entity A are evaluated for reuse or conflict with Entity B and C requirements, what the escalation path is when Entity B wants a customization that Entity A and C would not need, and what the "code freeze" policy is for the shared production system when Entity C's go-live is still 6 months away after Entity A goes live.

---

### Challenge 2: Certification Exam Strategy Under Pressure

A student sitting the Salesforce Certified Associate exam completes question 35 of 40 and realizes they have only 8 minutes remaining. They have not yet answered questions 12, 23, and 31 (which they marked for review) and have just reached question 36.

1. Apply the time management principles from Module 16 to this situation. Calculate whether 8 minutes is sufficient to complete the remaining work (questions 36–40 plus returning to questions 12, 23, 31). Describe the optimal sequencing strategy: should they finish 36–40 first and then return to marked questions, or return to marked questions first? Justify the sequencing decision with reference to the no-penalty guessing rule and the risk of running out of time.

2. Question 23 (marked for review) presents this scenario: "A Salesforce administrator needs to give a group of 15 users in the Customer Service team read access to a custom field on the Case object that all other users should not see. The administrator should not modify the existing Profile. What is the most appropriate solution?" The student's two remaining choices after elimination are: (A) Create a Permission Set with Read access to the field and assign it to the 15 users, or (B) Create a new Profile with Read access to the field and assign it to the 15 users. Apply the constraint-elimination strategy from Module 16: identify the constraint in the scenario that distinguishes the two answers, explain why one violates it and one satisfies it, and select the correct answer with justification.

3. After completing the exam, the student receives their score report: 61% — one question below the 62% passing threshold. They must decide whether to reschedule immediately or wait. Design a 3-week targeted re-study plan for a second attempt: (a) identify which Salesforce Associate exam topic areas a student who scored 61% is most likely to have missed based on the topic weightings, (b) specify the exact Trailhead resources to target, (c) describe the practice exam strategy for the final 3 days before the retake, and (d) address the psychological dimension — what the research on exam retake performance says about time between attempts and confidence rebuilding.

4. The same student is also preparing for the SAP S/4HANA Essentials exam scheduled 6 weeks after the Salesforce retake. Describe how the study content overlaps and how it diverges. Identify three specific concepts that appear on both exams (in different contexts) and three concepts that are unique to the SAP exam with no Salesforce parallel. For each overlap concept, explain how understanding the Salesforce version helps or hinders understanding the SAP version.

---

### Reflection Questions

1. Module 14 covered BI and reporting; Module 13 covered security; Module 12 covered data migration; Module 15 covered implementation methodology. Looking across all four of these operational domains, identify the single governance mechanism that would have the highest impact on project success if it were established at the very start of an ERP implementation — before any technical work begins. Justify your choice by explaining how the absence of this mechanism creates failure risk in each of the four domains simultaneously.

2. The Salesforce Certified Associate and SAP S/4HANA Essentials certifications are entry-level credentials. After earning them, a practitioner will encounter real implementations where the textbook process and the actual business requirement diverge — where "fit to standard" conflicts with a specific client's regulatory environment, a legacy integration that cannot be replaced, or a political reality that blocks the technically correct solution. Describe the professional judgment competency that certifications cannot teach but that this course has attempted to develop, and identify two specific scenarios from Modules 01–15 that illustrate the gap between certification knowledge and real-world ERP practice.

End of Lab — Module 16

**Certification Alignment:** Salesforce Certified Associate / SAP S/4HANA Essentials
