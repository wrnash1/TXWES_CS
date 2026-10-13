# Discussion Forum: Module 05 — Reconnaissance and OSINT

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Professor Nash's Note on Professional Ethics

The topics in this module — OSINT, social media intelligence, and DNS enumeration — are powerful precisely because they are legal to use against authorized targets and powerful for legitimate security assessments. They are equally powerful when misused. As future security professionals, you are learning these skills to protect organizations, not to harm them.

Every tool demonstrated in this course requires written authorization before use against a real target. The scenarios below are designed to develop your professional judgment about scope, ethics, and responsible disclosure — skills that are just as important as technical proficiency. Employers hire security professionals they can trust. Your conduct in this course reflects the professional you are becoming.

---

## Discussion Scenario 1 — The Accidental Exposure

A security consultant is hired to perform a penetration test for a regional bank. During the passive reconnaissance phase — before any active scanning — the consultant queries Certificate Transparency logs and discovers 23 subdomains, including one named `dev-api.bankname.com`. Querying that subdomain in a browser returns a live API endpoint that displays raw JSON containing customer account numbers and transaction data. No authentication is required. The endpoint was never intended to be public.

The consultant has not yet been given authorization to begin active testing — only passive recon was in scope at this stage.

**Discussion Prompt:**

In 175–225 words, address the following:

- What should the consultant do immediately upon discovering this exposure?
- What are the ethical and legal obligations regarding the customer data visible in the JSON response?
- How does the concept of "scope" apply here — is this finding within scope even though active testing has not started?
- What does this scenario illustrate about the real-world value of passive reconnaissance?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Scenario 2 — The LinkedIn Dilemma

A penetration tester is performing a red team engagement for a mid-size technology company. The rules of engagement explicitly include social engineering as an in-scope activity. During OSINT collection using LinkedIn and theHarvester, the tester compiles a list of 47 employee names, email addresses, job titles, and reporting relationships. Among the employees identified is a recent hire in the finance department whose LinkedIn profile shows they just started two weeks ago and lists their personal cell phone number.

The tester's supervisor suggests that this new employee would be an ideal target for a vishing (voice phishing) call pretending to be the IT helpdesk, because new employees are less likely to question unusual IT requests.

**Discussion Prompt:**

In 175–225 words, address the following:

- Even though social engineering is in scope, are there ethical considerations that should influence how the tester selects targets within the authorized scope?
- What boundaries should a professional penetration tester set when conducting social engineering exercises against real employees?
- How should the tester document this finding and the decision-making process regardless of whether the vishing call proceeds?
- What professional standards or frameworks address this type of ethical boundary in security testing?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Scenario 3 — Scope Creep During Recon

A freelance penetration tester is hired by a retail company to assess their e-commerce platform. The scope is defined as: `shop.retailer.com` and associated infrastructure. During passive DNS enumeration, the tester discovers that `shop.retailer.com` is hosted on a shared cloud hosting platform alongside dozens of other clients' websites. A Shodan search for the server IP reveals that the same IP hosts `medicalclinic-records.com` — a medical records portal for an unrelated healthcare provider.

The tester realizes that a vulnerability in the shared hosting configuration could potentially allow lateral movement from the retail target to the medical records system.

**Discussion Prompt:**

In 175–225 words, address the following:

- What are the tester's obligations when reconnaissance reveals potential impact to out-of-scope systems?
- How should the tester document and communicate this finding to the client?
- What is the professional responsibility toward the unrelated medical records system and its patients?
- How does this scenario illustrate the importance of precisely defined scope language in penetration testing contracts?

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM (minimum two responses, 75+ words each)

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|-----------|--------|---------|
| Initial Post — Technical Accuracy | 3 | Demonstrates accurate understanding of reconnaissance concepts and tools discussed in Module 05 |
| Initial Post — Ethical Reasoning | 2 | Addresses the ethical and legal dimensions of the scenario with specificity and professional maturity |
| Initial Post — Word Count and Format | 1 | 175–225 words, organized response, professional tone |
| Peer Response 1 | 2 | Minimum 75 words, adds substantive analysis or respectfully challenges a point with reasoning |
| Peer Response 2 | 2 | Minimum 75 words, introduces a new consideration or connects the scenario to course concepts |

**Note:** Responses of "I agree" or "great post" with no substantive addition receive zero points for that response. Professionalism in your responses is expected — critique ideas respectfully, support claims with reasoning, and engage as the security professional you are becoming.

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
