# Quiz: Module 13 — IT Asset Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Time limit: 20 minutes.

---

## Questions

**Question 1**

Which ITIL 4 practice group does IT Asset Management belong to?

A. Service Management

B. Technical Management

C. General Management

D. Organizational Management

**Correct Answer: C**

**Distractor Analysis:**

- **A (Service Management)** is wrong. Service Management practices include Incident Management, Change Enablement, and Service Level Management — practices more directly tied to service delivery operations.
- **B (Technical Management)** is wrong. Technical Management practices include Deployment Management and Software Development Management — practices requiring deep technical specialization.
- **C (General Management)** is correct. ITIL 4 places IT Asset Management in General Management because the practice spans IT and broader organizational functions including finance, procurement, and legal.
- **D (Organizational Management)** is a made-up category not used in ITIL 4.

---

**Question 2**

An asset discovery scan identifies a server that is not in the organization's asset register. The server is actively communicating on the network and appears to be running a database service. How should this asset be categorized in the reconciliation process?

A. Known and found

B. Known but not found

C. Found but not known

D. Known as disposed

**Correct Answer: C**

**Distractor Analysis:**

- **A (Known and found)** is wrong. "Known" means the asset is in the register. This server is not registered.
- **B (Known but not found)** is wrong. This category applies to assets in the register that the scan did not detect.
- **C (Found but not known)** is correct. The asset was discovered by the scan but has no corresponding record in the asset register — the definition of "found but not known." This is also an example of shadow IT.
- **D (Known as disposed)** is wrong. This category applies to assets registered as disposed that are still discovered — a different situation. There is no registration at all for this server.

---

**Question 3**

What is the primary feature that distinguishes a Configuration Management Database from a simple asset inventory list?

A. The CMDB is updated automatically by discovery tools while the asset register requires manual entry.

B. The CMDB tracks relationships and dependencies between configuration items, not just their individual attributes.

C. The CMDB stores financial information such as asset cost and depreciation.

D. The CMDB is accessible only to IT operations staff while the asset register is shared with finance.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. Both CMDBs and asset registers can be manually or automatically maintained — this is an implementation detail, not a definitional distinction.
- **B** is correct. The defining characteristic of a CMDB is the relationship model: it captures how CIs connect, depend on, host, and interact with each other. This enables impact analysis for incidents and changes — something a flat inventory list cannot support.
- **C** is wrong. Financial information (cost, depreciation) is the domain of the asset register, not the CMDB.
- **D** is wrong. Access controls are an implementation decision, not a defining difference between the two tools.

---

**Question 4**

A school district has 500 Microsoft 365 licenses and discovers that 480 users are actively using the platform. An additional 50 user accounts belong to former employees who left the organization but were never deprovisioned. What is the district's compliance status?

A. Compliant — 480 active users are within the 500-license limit.

B. Non-compliant — the 50 former employee accounts are consuming licenses, bringing total assigned licenses to 530, which exceeds the 500 purchased.

C. Non-compliant — the district should have purchased 530 licenses to cover all accounts.

D. Compliant — former employee accounts are not actively used and do not consume license entitlements.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. It focuses only on active users but ignores that licenses are typically assigned to accounts (including inactive former employee accounts), not just to active users. Assigned accounts count against license entitlements.
- **B** is correct. If 480 active + 50 former employee accounts = 530 assigned accounts against 500 licenses, the district is 30 licenses short and technically out of compliance.
- **C** is wrong. The recommendation is not to buy 530 licenses but to deprovision the 50 former employee accounts, which would bring usage to 480 — well within the 500 licenses owned.
- **D** is wrong. Inactive accounts still consume assigned license seats in most licensing models, particularly Microsoft 365.

---

**Question 5**

Which data sanitization method is described as using a strong magnetic field to erase all data from magnetic storage media, rendering the drive inoperable?

A. Overwriting

B. Degaussing

C. Cryptographic erasure

D. Clearing

**Correct Answer: B**

**Distractor Analysis:**

- **A (Overwriting)** is wrong. Overwriting writes random data patterns over storage sectors — it does not use magnetic fields and the drive remains functional afterward.
- **B (Degaussing)** is correct. Degaussing applies a powerful magnetic field that disrupts the magnetic properties of the media, destroying all stored data. The drive is rendered inoperable and cannot be reused.
- **C (Cryptographic erasure)** is wrong. Cryptographic erasure destroys the encryption key for an encrypted drive, rendering remaining encrypted data unrecoverable — no magnetic field is involved.
- **D (Clearing)** is the NIST SP 800-88 term for overwriting techniques — a software method, not magnetic.

---

**Question 6**

An organization discovers through a software audit that it has 200 installations of a commercial data analytics tool but only 150 per-seat licenses purchased. What is this situation called and what is the immediate risk?

A. Over-licensing; the organization is wasting money on unused licenses.

B. Under-licensing; the organization is exposed to vendor audit penalties and potential legal liability.

C. Shadow IT; the installations were deployed without IT's knowledge.

D. License drift; the license count will naturally correct at the next renewal.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. Over-licensing means more licenses than installations — the opposite situation. The organization would be wasting money if it had 250 licenses for 200 installations.
- **B** is correct. Under-licensing means more installations than purchased licenses. The organization is using software it has not paid for, which violates the license agreement. This exposes the organization to a vendor audit, back-payment of fees (often at full list price), and potential legal action.
- **C** is wrong. Shadow IT refers to assets deployed without IT's knowledge. The question implies IT is aware of the installations (it ran an audit). The issue is license count, not visibility.
- **D** is wrong. License drift is not a standard ITAM term, and there is no mechanism by which a license shortage automatically corrects itself.

---

**Question 7**

At which stage of the IT asset lifecycle should an asset first be recorded in the asset management system?

A. Deployment — when the asset is configured and placed into service.

B. Operation — when the asset begins generating utilization data.

C. Request and Acquisition — immediately upon purchase or provisioning.

D. Retirement — to ensure the final record is accurate.

**Correct Answer: C**

**Distractor Analysis:**

- **A (Deployment)** is a common mistake in practice but wrong as best practice. Waiting until deployment creates a gap where purchased assets are untracked — vulnerable to loss, theft, or undocumented use.
- **B (Operation)** is even later and introduces a longer gap.
- **C (Request and Acquisition)** is correct. Best-practice ITAM programs register assets at the moment of acquisition so the entire lifecycle is captured from the beginning.
- **D (Retirement)** is clearly wrong — recording an asset only at retirement defeats the purpose of lifecycle management.

---

**Question 8**

Which type of software license allows a limited pool of licenses to be shared across a large number of users, with only those actively using the software at any given time consuming a license?

A. Per-seat license

B. OEM license

C. Concurrent (floating) license

D. Site license

**Correct Answer: C**

**Distractor Analysis:**

- **A (Per-seat)** is wrong. Per-seat licenses are assigned to named individual users regardless of whether they are actively using the software.
- **B (OEM)** is wrong. OEM licenses are tied to specific hardware devices and cannot be transferred — they have nothing to do with shared pools.
- **C (Concurrent / floating)** is correct. Concurrent licenses are drawn from a shared pool; a user consumes a license while the software is running and returns it to the pool when finished. This is efficient when many users need occasional access but few need simultaneous access.
- **D (Site license)** is a common distractor. A site license typically grants unlimited use for an entire site or organization — but it is not the mechanism of a shared pool checked in/out based on active use.

---

**Question 9**

An organization is retiring a server that held employee payroll records. The security team recommends that the storage drives be physically destroyed rather than overwritten or degaussed. According to NIST SP 800-88 terminology, which sanitization level does physical destruction represent?

A. Clear

B. Purge

C. Destroy

D. Sanitize

**Correct Answer: C**

**Distractor Analysis:**

- **A (Clear)** is wrong. NIST defines Clear as overwriting with non-sensitive data — the lowest level, suitable for reuse within the organization.
- **B (Purge)** is wrong. Purge includes stronger overwriting, degaussing, and cryptographic erasure — more thorough but still potentially allowing drive reuse.
- **C (Destroy)** is correct. NIST SP 800-88 defines Destroy as the highest sanitization level, including physical destruction methods such as shredding, disintegration, incineration, and pulverization. Appropriate for highly sensitive data or drives that cannot be purged.
- **D (Sanitize)** is wrong — or rather, it is an umbrella term in NIST 800-88 that encompasses all three levels (Clear, Purge, Destroy), not a specific level itself.

---

**Question 10**

How does IT Asset Management most directly support Information Security Management?

A. By negotiating software licenses at lower cost, freeing budget for security tools.

B. By providing an accurate inventory of hardware and software assets, enabling security teams to identify unpatched, unauthorized, or end-of-life systems.

C. By conducting penetration tests on discovered assets to identify vulnerabilities.

D. By encrypting all asset records in the CMDB to prevent unauthorized access.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. Cost optimization is a ITAM benefit but is not the direct link to Information Security Management.
- **B** is correct. Security teams cannot protect what they cannot see. An accurate, current asset inventory from ITAM directly enables security to identify systems that are unpatched (missing critical updates), unauthorized (shadow IT), or running end-of-life software with no vendor security support.
- **C** is wrong. Penetration testing is a security practice — not an ITAM function.
- **D** is wrong. CMDB encryption is a security control applied to ITAM data, not a function performed by ITAM for security's benefit.

---

*End of Module 13 Quiz — 10 questions with distractor analysis*
