# Quiz: Module 15 — DevOps, Agile, and ITIL Integration

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Time limit: 20 minutes.

---

## Questions

**Question 1**

Which ITIL 4 Guiding Principle most directly corresponds to the Agile Manifesto's value of "responding to change over following a plan"?

A. Focus on Value

B. Start Where You Are

C. Progress Iteratively with Feedback

D. Think and Work Holistically

**Correct Answer: C**

**Distractor Analysis:**

- **A (Focus on Value)** aligns more with the Agile principle of delivering valuable software — about what is delivered, not the delivery cadence or adaptability.
- **B (Start Where You Are)** aligns with understanding the current state before changing — relevant to planning, not adaptability.
- **C (Progress Iteratively with Feedback)** is correct. This principle directly describes the Agile and DevOps approach of making incremental changes and using feedback to guide the next iteration — the operational expression of "responding to change."
- **D (Think and Work Holistically)** aligns with DevOps systems thinking — but does not specifically correspond to the adaptability value.

---

**Question 2**

In Gene Kim's Three Ways of DevOps, which "Way" is most directly aligned with ITIL 4's Continual Improvement practice?

A. The First Way — Flow

B. The Second Way — Feedback

C. The Third Way — Continual Learning and Experimentation

D. None of the Three Ways aligns with ITIL 4

**Correct Answer: C**

**Distractor Analysis:**

- **A (First Way — Flow)** focuses on optimizing the speed of work through the value stream — more aligned with Lean and the ITIL principle of "Optimize and Automate."
- **B (Second Way — Feedback)** focuses on rapid feedback loops from right (operations) to left (development) — aligns with monitoring, incident management, and service measurement in ITIL.
- **C (Third Way)** is correct. The Third Way is explicitly about creating a culture of continual learning, experimentation, and improvement — the direct philosophical equivalent of ITIL 4's Continual Improvement practice.
- **D** is wrong. ITIL 4 was explicitly designed to align with the Three Ways and DevOps principles.

---

**Question 3**

A development team deploys code to production 15 times per day. Their CI/CD pipeline runs all automated tests and security scans before each deployment. The organization wants to ensure these deployments comply with ITIL Change Enablement without requiring CAB approval for each one. Which change type should these deployments be classified as?

A. Emergency change

B. Normal change

C. Standard change

D. Unauthorized change

**Correct Answer: C**

**Distractor Analysis:**

- **A (Emergency)** is wrong. Emergency changes are reserved for responses to major active incidents — not routine, planned deployments.
- **B (Normal)** is wrong. Normal changes require individual assessment and authorization through the change authority. Requiring CAB review for 15 deployments per day would create an insurmountable bottleneck.
- **C (Standard)** is correct. Standard changes are pre-authorized based on a defined risk profile and procedure. A CI/CD deployment that meets predefined criteria (tests pass, security scan clean, within authorized scope) qualifies for pre-authorization as a standard change, enabling frequent deployment without per-deployment CAB review.
- **D (Unauthorized)** is wrong. A deployment that follows a defined, approved standard change procedure is authorized — not unauthorized.

---

**Question 4**

In the Lean waste framework, which waste type best describes a security patch waiting 72 hours for a Change Advisory Board meeting before it can be deployed?

A. Defects

B. Waiting

C. Inventory

D. Overproduction

**Correct Answer: B**

**Distractor Analysis:**

- **A (Defects)** is wrong. The patch itself is correct — no defect is indicated. The waste is about time, not quality.
- **B (Waiting)** is correct. Work that is ready but cannot proceed because it is queued for an approval, resource, or scheduled event is Waiting waste — the most common form of waste in IT delivery processes.
- **C (Inventory)** is the closest distractor. Inventory waste refers to work items piling up (work in progress). A single item waiting for an approval is more precisely Waiting, though a queue of changes all waiting for CAB could also be described as Inventory.
- **D (Overproduction)** is wrong. Overproduction means producing more than needed — not applicable here.

---

**Question 5**

An organization's SLA promises customers 99.5% monthly availability. The SRE team sets an internal SLO of 99.8% availability. What is the primary reason for setting the internal SLO higher (stricter) than the SLA?

A. To impress customers with performance exceeding contractual commitments.

B. To create a detection buffer so degradation is identified and corrected before the SLA threshold is breached.

C. To increase the error budget available for deployments.

D. Because regulatory requirements mandate internal targets exceed external commitments.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. While exceeding the SLA may impress customers, that is a by-product, not the primary technical reason for setting a stricter SLO.
- **B** is correct. If the SLO (99.8%) is stricter than the SLA (99.5%), the engineering team receives an alert and investigates when availability drops below 99.8% — before it reaches the SLA-breaching 99.5% level. This buffer provides time to remediate before financial penalties or customer-visible SLA violations occur.
- **C** is wrong. A stricter SLO actually reduces the error budget (0.2% vs. 0.5%), making it smaller, not larger.
- **D** is wrong. No universal regulatory requirement mandates internal SLOs exceed SLAs.

---

**Question 6**

What is "toil" in the Site Reliability Engineering context?

A. Any incident that causes a service outage.

B. Manual, repetitive operational work that scales linearly with service growth and provides no enduring improvement.

C. The effort required to conduct a blameless postmortem after an incident.

D. Documentation tasks that engineers consider low-value.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. Incidents are not toil — incidents require investigation and resolution and can produce lasting improvements (when root causes are addressed). Toil is specifically repetitive, non-improving work.
- **B** is correct. SRE's definition of toil has specific characteristics: it is manual (not automated), repetitive (done over and over), scales with service growth (more users = more toil), and provides no enduring value (same work done again next week). Restarting a service manually when it crashes periodically is classic toil — it should be automated.
- **C** is wrong. Postmortems are valuable learning activities — the opposite of toil. They produce enduring improvements.
- **D** is wrong. While engineers may perceive documentation as low-value, this is not the SRE definition of toil.

---

**Question 7**

Which statement best describes the "Wall of Confusion" in DevOps?

A. The technical complexity of integration testing between development and production environments.

B. The organizational tension created by opposing incentives: development optimizes for change velocity while operations optimizes for stability.

C. The documentation barrier that prevents non-technical stakeholders from understanding IT processes.

D. The security boundary between internal networks and the public internet.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. This describes a technical challenge, not the organizational phenomenon the Wall of Confusion refers to.
- **B** is correct. The Wall of Confusion is the organizational divide caused by misaligned incentives: developers are rewarded for releasing new features quickly (frequent change); operations teams are rewarded for keeping systems stable (minimizing change). This creates the classic conflict where developers throw code "over the wall" to operations, who throw it back when it breaks.
- **C** is wrong. Documentation accessibility is a communication challenge, not the Wall of Confusion.
- **D** is wrong. This describes a network security concept (DMZ / firewall), not an organizational pattern.

---

**Question 8**

Value Stream Mapping reveals that a team's process has a total cycle time of 4 hours and a total wait time of 36 hours. What is the process efficiency?

A. 10%

B. 11.1%

C. 90%

D. 44.4%

**Correct Answer: A**

**Distractor Analysis:**

- **A** is correct. Process efficiency = Cycle Time ÷ (Cycle Time + Wait Time) × 100% = 4 ÷ (4 + 36) × 100% = 4 ÷ 40 × 100% = 10%. This means only 10% of elapsed time is actually adding value — 90% is waste (waiting).
- **B** is wrong. 11.1% would result from 4 ÷ 36, which is cycle time as a percentage of wait time only — not the correct formula.
- **C** is wrong. 90% is the waste percentage (100% - 10%), not the efficiency.
- **D** is wrong. 44.4% has no basis in the correct formula.

---

**Question 9**

Which practice from ITIL 4 is most closely aligned with the SRE practice of blameless postmortems?

A. Change Enablement

B. Service Level Management

C. Problem Management

D. Incident Management

**Correct Answer: C**

**Distractor Analysis:**

- **A (Change Enablement)** is wrong. Change Enablement focuses on authorizing and managing changes — not analyzing root causes of incidents.
- **B (Service Level Management)** is wrong. SLM manages agreements and performance reporting — it does not conduct root cause analysis.
- **C (Problem Management)** is correct. Problem Management in ITIL 4 is explicitly focused on identifying root causes of incidents and implementing fixes to prevent recurrence — the same goal as the blameless postmortem. Both seek to improve the system rather than blame individuals.
- **D (Incident Management)** is the most common distractor. Incident management restores service — it does not investigate root causes. A blameless postmortem begins where incident management ends.

---

**Question 10**

An organization discovers through Value Stream Mapping that the largest source of waste in their delivery pipeline is that only one senior engineer has the knowledge and authority to perform production deployments, creating a bottleneck. Which Lean waste category describes this situation?

A. Waiting

B. Transportation

C. Non-utilized talent

D. Inventory

**Correct Answer: C**

**Distractor Analysis:**

- **A (Waiting)** is the most tempting distractor because work does sit in queue waiting for the senior engineer. However, the root cause is not just scheduling — it is a knowledge and authority concentration problem. The underlying waste is the inability to use other team members' talent.
- **B (Transportation)** is wrong. Transportation refers to unnecessary handoffs or movement of work — not talent concentration.
- **C (Non-utilized talent)** is correct. The waste is that other qualified engineers are not being utilized for deployments because the knowledge and authority are concentrated in one person. Broader team skills are not being applied. This is a classic non-utilized talent waste scenario.
- **D (Inventory)** is wrong. Inventory refers to work items piling up — a queue. The bottleneck creates inventory as a symptom, but the root cause waste category for the knowledge concentration problem is non-utilized talent.

---

*End of Module 15 Quiz — 10 questions with distractor analysis*
