# Discussion Forum: Module 15 — Post-Report Cleanup and Debriefing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002) — Domain 5: Reporting and Communication

---

## Overview

The post-engagement phase is where professional reputation is won or lost. Technical skill
gets you into the engagement; professional discipline in cleanup, evidence handling, and
communication determines whether clients trust you with the next one. This discussion
challenges you to reason through realistic post-engagement dilemmas that do not have obvious
answers.

---

## Discussion Prompt

You are the lead penetration tester at a security consulting firm. Your team has just
completed a two-week internal assessment for a regional credit union. The engagement went
well — you found meaningful vulnerabilities, wrote a strong report, and delivered it on time.
Now you are in the post-engagement phase, and three issues have arisen.

**Issue 1 — Cleanup Oversight**: Two days after delivering the report, your junior tester
admits that they are not certain whether they removed a reverse shell payload from a Linux
server at `10.0.5.44`. The testing log has an entry showing the payload was uploaded but
the corresponding "Removed" checkbox was left blank. The credit union's IT team has been
working in that environment since the report was delivered.

**Issue 2 — Retest Disagreement**: The credit union's CISO has patched the Apache Struts
vulnerability (FIND-002, originally Critical) and replaced the default credentials on the
network management interface (FIND-005, originally High). She wants a retest report
confirming both are remediated. During your retest, FIND-002 is confirmed remediated. For
FIND-005, the default credentials are gone, but you notice the management interface now uses
a weak 6-character alphabetic password that you crack in under two minutes. The CISO insists
this should be classified as Remediated because "the default password is gone."

**Issue 3 — Evidence Retention Request**: The credit union's legal team contacts you three
months after the engagement (within your 90-day retention window). They are responding to
a regulatory examination and ask you to provide the raw engagement evidence — specifically
the tool output files and screenshots showing the confirmed findings. They want everything
transmitted via unencrypted email "for convenience."

### Initial Post (Due Wednesday at 11:59 PM)

In 250–300 words, address all three issues. For each, explain:

- What the professionally and ethically correct action is
- What specific risk or harm results if the wrong action is taken
- Which principle from Module 15 (cleanup attestation, chain of custody, retest status
  discipline, data handling, or responsible disclosure) directly applies

### Peer Responses (Due Sunday at 11:59 PM)

Write substantive replies of at least 75 words each to at least two peers. In your replies:

- For Issue 2: Evaluate whether your peer's retest status classification and reasoning are
  sound. If you disagree with their classification, explain why using CVSS concepts and the
  three remediation status definitions from Module 15.
- For Issue 3: Propose one specific technical method your peer could use to transmit the
  evidence files securely to the legal team, and explain why that method preserves chain of
  custody while satisfying the legal team's need for the files.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|-----------|--------|----------|
| Initial Post — All three issues addressed | 3 | Each issue answered with correct professional action |
| Initial Post — Principle application | 2 | Correctly identifies the Module 15 principle for each issue |
| Initial Post — Word count and quality | 1 | 250–300 words; professional, specific language |
| Peer Response 1 | 2 | 75+ words; addresses retest status or secure transmission with specific reasoning |
| Peer Response 2 | 2 | 75+ words; addresses retest status or secure transmission with specific reasoning |

---

## Guiding Questions for Deeper Engagement

Consider these questions as you write and respond:

- At what point does a cleanup oversight become a legal liability versus a professional
  embarrassment? What facts would change that distinction in Issue 1?
- Is the CISO's position in Issue 2 technically defensible at all? What would a proper
  password policy remediation look like for the management interface?
- The legal team in Issue 3 cited "convenience" as the reason for unencrypted email. What
  is the tester's professional obligation when a client requests an insecure delivery method
  for sensitive evidence? Can the tester simply comply because the client requested it?
- How does the regulatory context (a credit union is subject to NCUA examination and GLBA
  requirements) change the stakes of any of these three issues compared to a standard
  corporate client?
