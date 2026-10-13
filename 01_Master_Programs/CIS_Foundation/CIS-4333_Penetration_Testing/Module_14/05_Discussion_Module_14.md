# Discussion Forum: Module 14 — Penetration Testing Reports

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002) — Domain 5: Reporting and Communication

---

## Overview

The penetration testing report is the deliverable that transforms technical findings into
actionable business intelligence. In this discussion you will apply module concepts to a
realistic reporting scenario and engage critically with your peers' approaches.

---

## Discussion Prompt

A penetration tester at your firm has just completed a two-week assessment of a regional
hospital's network. The engagement uncovered three significant findings:

1. An unpatched Apache Struts server (CVE-2017-5638, CVSS 10.0 Critical) running on an
   internal host that stores patient scheduling data
2. Default credentials (`admin`/`admin`) on a medical device management portal accessible
   from the hospital's staff WiFi network
3. Overly permissive Active Directory group policies allowing standard user accounts to
   install software on clinical workstations

The lead tester is preparing the report and faces several decisions.

### Initial Post (Due Wednesday at 11:59 PM)

In 200–250 words, address all three of the following questions:

1. **Report Audience and Tone**: The hospital's CEO has asked to receive "the full report"
   because she wants to understand exactly what was found. Should the tester send the CEO
   the complete technical report with evidence screenshots, CVSS vector strings, and
   reproduction steps? Explain your reasoning, referencing the appropriate report structure
   from Module 14.

2. **Risk Rating Adjustment**: Finding 1 (Apache Struts) has a CVSS Base Score of 10.0
   (Critical). However, the affected host is internal — not directly internet-accessible —
   and the hospital has a next-generation firewall with IPS signatures covering CVE-2017-5638
   deployed at the network perimeter. Should the tester report this finding as Critical, High,
   or something else? What factors justify the adjustment, and what must the tester document
   when making it?

3. **Sensitive Data Handling**: While exploiting Finding 1, the tester accessed a directory
   containing 847 patient appointment records including names, dates of birth, and diagnoses.
   The tester captured a screenshot to prove access. How should this evidence be presented
   in the report to prove the finding without creating additional HIPAA exposure?

### Peer Responses (Due Sunday at 11:59 PM)

Read your classmates' posts and write constructive replies of at least 75 words each to at
least two peers. In your replies:

- Evaluate whether their proposed risk rating adjustment for Finding 1 is well-justified
  or whether they either over-adjusted (downgraded too aggressively) or under-adjusted
  (left severity too high without acknowledging the compensating controls)
- Suggest one specific element they could add to strengthen their sensitive data handling
  approach for the patient records evidence

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|-----------|--------|----------|
| Initial Post — Completeness | 3 | Addresses all three questions with specific references to Module 14 concepts |
| Initial Post — Technical Accuracy | 2 | Risk rating adjustment is logically justified; data handling approach is sound |
| Initial Post — Word Count and Clarity | 1 | 200–250 words; clear professional writing |
| Peer Response 1 | 2 | Substantive feedback of 75+ words on risk adjustment and evidence handling |
| Peer Response 2 | 2 | Substantive feedback of 75+ words on risk adjustment and evidence handling |

---

## Guiding Questions for Deeper Engagement

Consider these questions as you draft your post and read peers' responses:

- How does a hospital's regulatory environment (HIPAA) change the stakes of the sensitive
  data handling decision compared to a standard corporate client?
- What is the difference between a compensating control that genuinely reduces risk (the
  IPS signature) and one that merely reduces likelihood without addressing the root cause?
- If the tester discovers during the debrief that the CEO does not understand what "CVSS 10.0
  Critical" means, how should that discovery change how findings are communicated?
- Under what circumstances, if any, would it be appropriate to withhold a finding from the
  report entirely? What ethical and legal obligations apply?

---

## Additional Context

This scenario involves a healthcare organization, making HIPAA compliance directly relevant.
HIPAA's Security Rule requires covered entities to assess risks to electronic protected health
information (ePHI). A pentest report documenting unauthorized access to patient data — even
simulated access in an authorized engagement — may trigger breach notification assessment
procedures. Being aware of the regulatory context of your client's industry is a professional
expectation for senior penetration testers and is tested in PenTest+ Domain 5.
