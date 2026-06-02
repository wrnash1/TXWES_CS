# Discussion Forum: Module 02 - Active Directory Domain Services Overview

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion applies the AD DS architecture concepts from the lecture and reading guide to real-world design and troubleshooting scenarios. Choose one scenario below, answer all three sub-questions in your initial post, and engage substantively with at least two classmates.

---

### Scenario A — Single Forest vs. Multiple Forest Design

A large university is planning its Active Directory infrastructure. The IT leadership is debating whether to use a single-forest model with multiple domains for each college (Business, Sciences, Arts), or to use completely separate forests for each college. Each college has its own IT staff and wants administrative independence. The CIO wants students to be able to search for faculty across all colleges in the same directory.

1. What is the fundamental difference between a domain boundary and a forest boundary in AD DS, and which one provides true administrative and security isolation?
2. Given the requirement for cross-directory faculty searches, which model (single forest with multiple domains, or multiple forests) better supports this need, and why?
3. What type of trust would be required if the university chose the multiple-forest model, and what is the operational overhead of that approach compared to the single-forest model?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario B — FSMO Role Failure Diagnosis

During a Monday morning incident, a Help Desk manager reports that users across the organization can log in but cannot change their passwords. A few accounts that should have been unlocked over the weekend are still locked. Additionally, two new servers deployed Friday evening could not have computer accounts created — the DC returned an error during the account creation step.

1. Which FSMO roles are most likely involved in the password change failure and the computer account creation failure? Explain the function of each role that you identify.
2. How would you quickly verify which DCs hold the affected FSMO roles and whether those DCs are online? Name the specific commands you would use.
3. If the RID Master DC is confirmed offline, what is the short-term impact on the environment, and what is the recovery procedure when the server comes back online versus when it needs to be seized to a new DC?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario C — Branch Office Domain Controller Strategy

A company has 15 branch offices, each with 20-50 users. Currently all authentication traffic routes to the main data center. Users in branch offices experience 15-30 second logon times when the WAN link is congested. IT leadership proposes adding a Domain Controller to each branch. A security officer objects, citing concerns about physical server security in some offices.

1. Explain how adding a local DC would improve logon performance and what specific authentication protocols and services would now resolve locally instead of crossing the WAN.
2. For branches with poor physical security, what type of Domain Controller should be deployed, and how does its Password Replication Policy limit the blast radius of a physical compromise?
3. The security officer also asks whether the branch DCs should be Global Catalog servers. What factors determine this decision, and what is the consequence of not having a GC at a branch site when the WAN link goes down?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario, answer all three sub-questions
- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates; minimum 60 words each; try to respond to peers who chose different scenarios
- In peer replies: evaluate the technical accuracy of their FSMO or trust identification, and add one point they did not address

---

### Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post | 6 | Addresses all three sub-questions with technical accuracy and appropriate terminology; meets 175-225 word count |
| Initial Post — Partial | 3-4 | Addresses some sub-questions but lacks technical depth or misses one sub-question |
| Initial Post — Insufficient | 0-2 | Missing, too short, or does not address the scenario |
| Peer Responses | 4 | Responds to at least two peers with substantive technical additions (60+ words each) |
| Peer Responses — Partial | 2 | Only one peer response, or responses are superficial |
| Peer Responses — None | 0 | No peer responses submitted |

---

### Professor Nash's Note

Active Directory design decisions made early in an organization's history are very difficult and expensive to undo later. I have worked in environments where a single-forest design was chosen for simplicity and later caused headaches when two acquired companies needed administrative isolation. The FSMO role failure scenario in Scenario B is not hypothetical — I have personally worked a Monday-morning incident exactly like the one described. Knowing which role is failing and how to check it quickly is the kind of practical skill that separates a good administrator from a great one. Looking forward to your posts.
