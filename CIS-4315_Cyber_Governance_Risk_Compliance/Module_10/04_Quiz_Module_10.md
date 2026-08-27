# Quiz: Module 10 — Incident Management Planning

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Instructions

This quiz contains 10 multiple-choice questions. Each question has exactly four answer options. Select the single best answer for each question. Each question is worth 10 points for a total of 100 points.

These questions are written in the CISM exam style. Read each question carefully and identify what is specifically being asked before reviewing the options.

---

## Question 1

According to NIST SP 800-61, which of the following BEST describes the primary goal of the Preparation phase of the incident response lifecycle?

A. Identifying and triaging security alerts to determine whether an incident has occurred.

B. Removing threat actor tools, malware, and persistence mechanisms from affected systems.

C. Building the incident response capability — team, tools, procedures, and training — before an incident occurs.

D. Documenting the root cause and updating the IRP based on what was learned during the incident.

### Answer and Analysis — Question 1

**Correct Answer: C**

**Why C is correct**: The Preparation phase of the NIST SP 800-61 lifecycle is everything done before an incident occurs to establish the organization's response capability. This includes building the team, writing procedures, deploying monitoring tools, conducting training, and running exercises. All subsequent phases depend on the quality of preparation.

**Why A is wrong**: Identifying and triaging alerts is the Detection and Analysis phase — the second phase in the lifecycle, not the first.

**Why B is wrong**: Removing malware and persistence mechanisms is the Eradication sub-phase within phase three — Containment, Eradication, and Recovery.

**Why D is wrong**: Documenting root cause and updating the IRP is the Post-Incident Activity phase — the fourth and final phase in the lifecycle.

---

## Question 2

A security manager is building a RACI matrix for incident response activities. For the activity "Patient data breach determination," who should be assigned the Accountable (A) role?

A. The forensic investigator who collected the evidence.

B. The CISO or Incident Response Manager who has organizational authority for the final determination.

C. The legal counsel who will file the regulatory notification.

D. All members of the incident response team, as the determination affects everyone.

### Answer and Analysis — Question 2

**Correct Answer: B**

**Why B is correct**: Accountability (A) in a RACI matrix means ownership of the outcome — the person who has final decision-making authority and is answerable for the result. For a breach determination, this is the CISO or IR Manager, who has the organizational authority to make official determinations that trigger legal and regulatory obligations.

**Why A is wrong**: The forensic investigator is Responsible (R) — they do the work of collecting and analyzing evidence. They do not own the final determination and are not answerable to regulators for it.

**Why C is wrong**: Legal counsel is Consulted (C) on the breach determination — they provide legal input but do not own the determination decision. They become responsible for the notification filing, a separate activity.

**Why D is wrong**: A RACI matrix assigns exactly one A per activity. Having all team members accountable means no one is accountable. Distributed accountability is a RACI anti-pattern that creates confusion and diffuses responsibility.

---

## Question 3

A HIPAA-covered healthcare organization discovers on March 1 that an unauthorized party accessed a server containing 2,300 patient health records beginning on January 10. By what deadline must the organization notify the HHS Office for Civil Rights?

A. March 4 — within 72 hours of discovery.

B. March 31 — within 30 days of discovery.

C. April 30 — within 60 days of discovery.

D. July 10 — within 180 days of the initial breach date.

### Answer and Analysis — Question 3

**Correct Answer: C**

**Why C is correct**: HIPAA Breach Notification Rule requires covered entities to notify the HHS Office for Civil Rights within 60 days of the discovery date for breaches affecting 500 or more individuals. Discovery was March 1, so the deadline is 60 days later: April 30. The breach affecting 2,300 individuals clearly exceeds the 500-individual threshold.

**Why A is wrong**: 72 hours is the GDPR breach notification deadline for supervisory authorities — not the HIPAA deadline. These are different regulatory frameworks with different timelines.

**Why B is wrong**: Thirty days is not the HIPAA notification deadline. Some US state breach notification laws require 30-day notification, but HIPAA OCR notification is 60 days.

**Why D is wrong**: The clock starts on the date of discovery, not the date of the initial breach. Calculating from January 10 would be incorrect. HIPAA notification timing is discovery-based, not breach-occurrence-based.

---

## Question 4

An organization's IRP requires that the incident response team isolate any system showing signs of active compromise. During a ransomware incident, the IR Manager orders isolation of the organization's primary ERP system, which processes all financial transactions. The CFO objects and refuses to authorize the isolation, citing business continuity concerns. Which of the following BEST describes the appropriate resolution?

A. Defer to the CFO's decision, as they have authority over financial systems.

B. Escalate to the CEO to arbitrate between the CISO and CFO before taking action.

C. Proceed with isolation per the IRP, which has pre-authorized executive management to take this action on behalf of the organization.

D. Delay isolation and continue monitoring the ERP system while the business impact is assessed.

### Answer and Analysis — Question 4

**Correct Answer: C**

**Why C is correct**: The IRP must carry explicit executive authorization that empowers the IR team to take necessary containment actions including system isolation, even when business unit owners object. This authorization is why the IRP policy authorization section is critical. If the plan required real-time approval from every affected system owner, timely containment would be impossible. The CFO's concern should have been addressed in the plan design, not during an active incident.

**Why A is wrong**: Deferring to the CFO during an active containment action allows ransomware to continue spreading. The CFO's financial authority over the system does not extend to overriding a security-authorized isolation during an incident.

**Why B is wrong**: Escalating to the CEO creates delay in a time-critical situation. More importantly, this scenario should have been anticipated in the IRP. If the plan required CEO approval for every contested isolation, it was poorly designed.

**Why D is wrong**: Continuing to monitor an actively compromised system without containment allows the incident to spread and potentially worsens both the technical damage and the legal/regulatory exposure. Delay in containment is one of the most expensive decisions in incident response.

---

## Question 5

Which of the following BEST describes the purpose of maintaining pre-drafted notification templates in an Incident Response Plan?

A. To ensure that all notifications comply with plain language requirements for consumer communications.

B. To reduce the time required to prepare legally reviewed notifications during the high-stress, time-constrained conditions of an active incident.

C. To allow the marketing team to control the organization's breach communication messaging.

D. To satisfy PCI-DSS requirements for documented incident response procedures.

### Answer and Analysis — Question 5

**Correct Answer: B**

**Why B is correct**: Pre-drafted templates — reviewed by legal counsel in advance — allow the communications team to issue accurate, legally appropriate notifications quickly during an incident, when both time pressure and emotional stress are high. Without pre-drafting, organizations spend critical hours during an active breach drafting documents from scratch while legal review creates additional delays.

**Why A is wrong**: While plain language compliance is good practice, it is not the primary purpose of pre-drafting templates. Templates serve the operational need for speed and legal adequacy, not primarily a plain language standard.

**Why C is wrong**: Marketing input on crisis communication is appropriate at the drafting stage, but marketing should not control breach notification messaging. Legal counsel must review and approve these templates to ensure regulatory compliance.

**Why D is wrong**: PCI-DSS requires documented incident response procedures but does not specifically require pre-drafted notification templates. The purpose of pre-drafting is operational effectiveness, not a specific compliance checkbox.

---

## Question 6

An organization discovers an active network intrusion at 11 PM on a Friday. The on-call security analyst determines the incident severity is High based on the classification criteria in the IRP. According to the IRP, a High severity incident requires notification of the CISO and Legal within one hour. The analyst cannot reach either person. Which of the following BEST describes the appropriate action?

A. Downgrade the incident to Medium severity so that a Monday morning notification is acceptable.

B. Contact the designated backup contacts specified in the IRP for both the CISO and Legal roles.

C. Wait until 9 AM Monday to notify leadership, as leadership decisions cannot be made outside business hours.

D. Proceed with all technical response actions independently and notify leadership when they are available.

### Answer and Analysis — Question 6

**Correct Answer: B**

**Why B is correct**: A well-designed IRP includes backup contacts for all key roles specifically to address unavailability during off-hours incidents. The analyst should immediately contact the designated backup contacts. The one-hour notification requirement exists for a reason — high-severity incidents require leadership involvement in containment and communication decisions.

**Why A is wrong**: Downgrading an incident's severity to avoid uncomfortable notifications is a serious governance failure. Severity classification must be based on objective criteria, not on the convenience of notification. An analyst who manipulates severity classification creates legal, regulatory, and organizational accountability risk.

**Why C is wrong**: Security incidents do not respect business hours. Incident response procedures must operate 24/7. Waiting until Monday morning for a Friday night High-severity incident could allow days of damage and potentially violate notification obligations.

**Why D is wrong**: While the analyst should continue technical response, proceeding entirely independently on a High-severity incident without leadership notification violates the IRP. Leadership is needed to authorize potentially disruptive containment actions, make regulatory notification decisions, and provide communications oversight.

---

## Question 7

An organization's IRP requires forensic preservation of affected systems before restoration begins. The DRP requires that all Tier-1 systems be restored within 4 hours (RTO = 4 hours). Both requirements apply to a compromised production database. Which of the following represents the BEST approach to resolving this conflict?

A. Always prioritize the DRP RTO, as business continuity is more important than forensic evidence.

B. Always prioritize the IRP forensic requirement, as evidence preservation is legally required.

C. Resolve the conflict by pre-negotiating and documenting the approach for critical systems before an incident occurs.

D. Let the CISO and CIO negotiate the resolution during the incident based on the specific circumstances.

### Answer and Analysis — Question 7

**Correct Answer: C**

**Why C is correct**: The IRP-DRP conflict between forensic preservation and recovery speed is a known and predictable tension. The correct solution is to pre-negotiate and document the approved approach for critical system types before an incident occurs. This might include forensic imaging (which preserves evidence while allowing restoration), pre-defined criteria for when restoration takes priority over forensics, or pre-approved exceptions. Resolving this during an incident creates dangerous delay and inconsistency.

**Why A is wrong**: Business continuity is important, but always prioritizing it destroys forensic evidence that may be legally required and that is essential for understanding the full scope of a compromise. Restoring from a backup that contains the attacker's persistence mechanism reinstates the attack.

**Why B is wrong**: Forensic requirements are important but not always legally required. Many incidents do not involve legal proceedings. Rigidly prioritizing forensics over all RTOs would make DRP targets impossible to meet and would be an excessive business cost.

**Why D is wrong**: Negotiating a resolution during an active incident introduces delay, disagreement, and inconsistency. High-stress incident conditions are the worst time to make complex trade-off decisions. This negotiation must happen in advance.

---

## Question 8

A publicly traded company discovers that a threat actor accessed its executive email accounts and may have obtained non-public financial information about an upcoming acquisition. Which of the following external notification obligations is MOST likely to have the shortest response deadline?

A. HIPAA Breach Notification to HHS — 60 days.

B. State breach notification law — 45 days.

C. SEC Form 8-K for material cybersecurity incidents — 4 business days from materiality determination.

D. GDPR notification to supervisory authority — 72 hours.

### Answer and Analysis — Question 8

**Correct Answer: C**

**Why C is correct**: For publicly traded companies, the SEC requires disclosure of material cybersecurity incidents on Form 8-K within 4 business days of determining that the incident is material. In a scenario involving potential access to non-public financial information about an acquisition, the incident is likely to be deemed material relatively quickly. Four business days is a very short window.

**Why A is wrong**: HIPAA applies to protected health information in healthcare contexts. Email accounts containing financial acquisition data are not HIPAA-covered unless they contain PHI, which is not described in this scenario.

**Why B is wrong**: A 45-day state breach notification timeline is longer than the 4-business-day SEC deadline. For a publicly traded company, the SEC obligation is the more pressing deadline in this scenario.

**Why D is wrong**: GDPR's 72-hour deadline applies to personal data of European residents, not to non-public financial information. Unless the compromised email accounts contained European residents' personal data, GDPR notification is not the primary obligation here. Even if GDPR applied, 72 hours and 4 business days are similar timeframes, but the SEC obligation is the most directly applicable.

---

## Question 9

Which of the following MOST accurately describes the difference between a tabletop exercise and a full-scale simulation for incident response plan testing?

A. A tabletop exercise tests only communication procedures, while a full-scale simulation tests only technical procedures.

B. A tabletop exercise involves verbal discussion of a simulated scenario without activating real systems, while a full-scale simulation activates all response functions across all teams as if a real incident had occurred.

C. A tabletop exercise is used for Critical severity incidents only, while a full-scale simulation is used for all severity levels.

D. A tabletop exercise requires external facilitators, while a full-scale simulation is conducted entirely by the internal team.

### Answer and Analysis — Question 9

**Correct Answer: B**

**Why B is correct**: The definitive distinction between tabletop and full-scale exercises is operational activation. In a tabletop, participants discuss what they would do — no real systems are touched, no real notifications are sent. In a full-scale simulation, all IRP functions are activated: the IR team responds as if the incident is real, technical containment steps are executed in test environments, and communications functions are performed. Full-scale exercises are far more resource-intensive but reveal gaps that tabletops cannot.

**Why A is wrong**: Both exercise types test communication AND decision-making. Tabletops are effective for testing decision trees, escalation logic, and communication protocols. Full-scale exercises add technical execution to those elements. Neither type is limited to only one of these functions.

**Why C is wrong**: Exercise format is not tied to incident severity level. Organizations conduct tabletops for all scenario types, from ransomware to insider threat to supply chain compromise. The choice between exercise formats is based on resource availability and testing objectives, not severity levels.

**Why D is wrong**: Either exercise type can involve external facilitators or be conducted internally. The use of external facilitators is an organizational choice unrelated to the definitional distinction between exercise types.

---

## Question 10

An organization is developing its Incident Response Plan for the first time. The security manager argues that the IRP should be developed by the security team alone to ensure technical accuracy and confidentiality. The CISO disagrees. Which of the following BEST supports the CISO's position?

A. The IRP should be developed exclusively by an external consulting firm to ensure objectivity.

B. The IRP must be developed collaboratively with legal, HR, business units, and executive leadership because incident response affects the entire organization and requires cross-functional authority.

C. The IRP should be classified as a confidential document accessible only to the CISO and the security team.

D. The IRP development should be led by the IT department rather than the security team to ensure alignment with system recovery procedures.

### Answer and Analysis — Question 10

**Correct Answer: B**

**Why B is correct**: An IRP that is developed by the security team alone will lack the legal review needed to address regulatory obligations, the HR input needed for insider threat procedures, the business unit input needed for realistic system isolation decisions, and the executive authorization needed to empower the IR team to take necessary actions. Incident response is fundamentally a cross-functional discipline. The security team executes the technical response, but the IRP must be owned, authorized, and understood across the organization.

**Why A is wrong**: External consultants can add valuable expertise to IRP development, but the plan must be owned and understood internally. A plan developed entirely by an outside firm and handed to the organization will not be understood or executed effectively when an incident occurs.

**Why C is wrong**: While the detailed tactical procedures may be sensitive, the IRP itself — including severity criteria, escalation chains, and communication contacts — must be known to all participants. A plan that only the CISO can read cannot be executed by the rest of the IR team.

**Why D is wrong**: IT leadership of the DRP is appropriate, but the IRP is a security governance document that must be led by the security function with executive authorization. IT leadership would correctly address system recovery but would underweight security investigation, legal obligations, and communication requirements.

---

---

### Question 11 (5 points)

An organization discovers that its Incident Response Plan was last updated eighteen months ago, before the company migrated its primary systems to a hybrid cloud environment. The plan's containment procedures reference on-premises network isolation tools that are no longer deployed. What is the most appropriate immediate action?

- A) Declare the current IRP void and begin responding to all incidents using ad hoc judgment until a new plan is written.
- B) Treat the plan as fully current because the incident response lifecycle principles do not change with infrastructure changes.
- C) Identify and document the specific sections made obsolete by the cloud migration and initiate an expedited out-of-cycle review and update of the affected procedures.
- D) Engage an external consulting firm to rewrite the entire IRP before responding to any new incidents.

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Significant infrastructure changes are a defined trigger for an out-of-cycle IRP review. The appropriate response is to identify the specific obsolete sections immediately, document the gap for awareness, and initiate an expedited update process — not to void the entire plan or wait for a full rewrite.
  - *Why A is incorrect:* A partially outdated plan retains value for the sections that remain accurate. Responding purely on ad hoc judgment is far more dangerous than using an imperfect plan as a baseline.
  - *Why B is incorrect:* While lifecycle principles remain constant, specific containment procedures are infrastructure-dependent. A plan referencing decommissioned tools will fail during execution at exactly the worst possible moment.
  - *Why D is incorrect:* Engaging a full external rewrite before responding to any incidents is operationally unreasonable and would leave the organization without any structured response capability during the rewrite period.

---

### Question 12 (5 points)

A financial services company's IRP assigns the role of Incident Response Manager to the CISO. During a major ransomware event on a Tuesday evening, the CISO is on a transatlantic flight and unreachable. The next most senior security manager begins making containment decisions. At what point should this person formally assume the IR Manager role?

- A) Only after the CISO lands and formally delegates authority via email.
- B) Immediately upon determining that the CISO is unreachable and the incident severity requires IR Manager-level decisions — per the backup contact provisions in the IRP.
- C) Never — all significant decisions must wait for the designated IR Manager regardless of availability.
- D) After the incident is fully contained, to avoid creating confusion in the response chain.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A well-designed IRP includes explicit backup contact and role assumption provisions for exactly this scenario. The deputy assumes the IR Manager role as soon as the primary is confirmed unreachable and incident conditions require that authority. Waiting for a delegation email introduces unacceptable delay.
  - *Why A is incorrect:* Requiring a formal email delegation before any IR Manager action could delay critical containment decisions by hours. The IRP's backup provisions eliminate the need for real-time delegation.
  - *Why C is incorrect:* An IRP that requires waiting for an unavailable designated manager has a fatal design flaw. Every critical IRP role must have a named backup with explicitly pre-authorized decision authority.
  - *Why D is incorrect:* Assuming the IR Manager role after the incident is contained provides no operational value. The role assumption is needed during the active response, not as a post-incident administrative formality.

---

### Question 13 (5 points)

During a post-incident review, the team discovers that the IRP required the on-call analyst to notify the CISO "as soon as possible" when a High-severity incident was detected. In the most recent incident, the analyst waited 3 hours before notifying the CISO because they believed they could resolve the issue independently. Which IRP design improvement would most directly prevent this failure?

- A) Replace the CISO with a more available manager who can respond faster.
- B) Replace "as soon as possible" with a specific, objective time requirement — such as "within 30 minutes of High-severity classification" — making compliance measurable and non-discretionary.
- C) Train analysts to exercise better judgment about when escalation is necessary.
- D) Eliminate the CISO notification requirement for High-severity incidents to reduce unnecessary alerts.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Vague escalation language such as "as soon as possible" is a well-documented IRP weakness. It permits individual discretion and creates inconsistency. Replacing it with a specific time threshold makes the requirement measurable, removes individual judgment from the timing decision, and creates a clear compliance standard.
  - *Why A is incorrect:* The failure was in the escalation criteria language, not in the CISO's availability. Changing personnel does not address the root cause of vague escalation language.
  - *Why C is incorrect:* The IRP's purpose is to eliminate dependence on good individual judgment under high-stress conditions. Relying on better analyst judgment is precisely what the plan should avoid — the plan should make the correct action the only available action.
  - *Why D is incorrect:* Eliminating CISO notification for High-severity incidents would deprive leadership of the situational awareness needed to authorize significant containment actions and manage regulatory obligations.

---

### Question 14 (5 points)

An organization's IRP requires that all digital evidence collected during incident response be preserved in a manner that supports potential legal proceedings. A junior analyst, during the eradication phase, wipes and reimages three compromised servers before forensic images were created. Which consequence is MOST likely to result from this action?

- A) No consequence — reimaging is the correct eradication technique and is always legally acceptable.
- B) The organization may be unable to determine the full scope of the attack and may face spoliation risk if litigation follows the incident.
- C) The organization is required to notify law enforcement immediately about the evidence destruction.
- D) The analyst will be personally criminally liable for destroying electronic evidence.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Wiping systems before forensic imaging destroys evidence of the attack's scope, entry vector, lateral movement, and attacker tools. If litigation or regulatory investigation follows, the organization may face spoliation sanctions — adverse inference or penalties for destruction of potentially relevant evidence. The investigation is also degraded by the loss of this evidence.
  - *Why A is incorrect:* Reimaging is an eradication technique, but the IRP requirement to preserve forensic evidence before eradication means reimaging without prior imaging violates the plan. Legal acceptability depends on whether the organization had a duty to preserve evidence.
  - *Why C is incorrect:* Mandatory law enforcement notification for evidence destruction is not a universal legal requirement. Whether notification is required depends on whether a legal hold was in effect and other jurisdictional factors.
  - *Why D is incorrect:* Personal criminal liability for evidence destruction requires specific statutory conditions, typically a legal hold or ongoing investigation with actual notice. A junior analyst acting outside an established legal hold would not ordinarily face criminal liability, though organizational liability remains.

---

### Question 15 (5 points)

A healthcare organization's IRP contains a section on cyber insurance requirements. The policy requires notification to the insurer "within 72 hours of discovering a covered cyber event." The IR team contains a ransomware attack on Wednesday morning but delays notifying the insurer until the following Monday because they want to have a complete incident report ready. Which risk does this create?

- A) No risk — insurers prefer receiving complete reports and routinely accept delays.
- B) The organization may be at risk of claim denial or reduced coverage if the 72-hour notification requirement was violated, regardless of the completeness of the eventual report.
- C) The organization must contact the regulator instead of the insurer within 72 hours.
- D) The delay is acceptable because 72-hour requirements apply only to GDPR, not cyber insurance policies.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Cyber insurance policies commonly contain prompt notification requirements, and failure to comply can be cited as a basis for claim denial or coverage reduction. Insurers need timely notification to exercise their contractual rights — such as approving response vendors, managing legal exposure, and coordinating with their own representatives. Waiting for a complete report does not satisfy the notification requirement.
  - *Why A is incorrect:* Insurers do not routinely waive notification deadline requirements as a matter of course. Delay in notification may be explicitly cited in policy language as a condition affecting coverage.
  - *Why C is incorrect:* Regulatory notification and insurer notification are separate and independent obligations. Each has its own timeline and recipient. The cyber insurer notification deadline is contractual, not regulatory.
  - *Why D is incorrect:* 72-hour requirements appear in multiple contexts — GDPR supervisory authority notification, cyber insurance policies, and some contractual service agreements all commonly use this timeframe. The source of the requirement here is the insurance policy.

---

### Question 16 (5 points)

During a tabletop exercise, a facilitator presents an inject: the organization's domain controller has been compromised and all Active Directory credentials are believed to be exposed. The IR team lead immediately proceeds to "reset all Active Directory passwords." A participant raises a concern. Which concern is most valid from an incident management perspective?

- A) Resetting AD passwords is not a security response action and should not be discussed in an IR context.
- B) Before resetting passwords organization-wide, the team must consider whether such a broad action would alert the attacker to the investigation, prematurely trigger their next phase, or disrupt critical business operations.
- C) Password resets require board approval before execution and cannot be discussed without that authorization.
- D) All AD credentials are considered permanently compromised once exposed; resetting them provides no security value.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Mass credential resets are a valid eradication action but carry significant tactical and operational implications. An advanced persistent threat actor monitoring for investigation activity may accelerate their timeline or trigger destructive actions upon detecting a mass credential rotation. Additionally, an organization-wide AD password reset can disrupt service accounts, automated processes, and user access in ways that create significant business impact. This decision requires careful coordination — not reflexive immediate execution.
  - *Why A is incorrect:* Credential rotation is explicitly an eradication activity in the NIST SP 800-61 framework. It is a core IR response action for credential compromise incidents.
  - *Why C is incorrect:* Operational credential management decisions are within the authority of the IR Manager and CISO acting under the IRP. Board approval is not required for eradication actions.
  - *Why D is incorrect:* Credential rotation is effective and necessary after credential compromise. The value of new credentials is that they replace those the attacker possesses, eliminating their ability to authenticate with previously harvested credentials.

---

### Question 17 (5 points)

An organization is evaluating whether to retain a third-party incident response firm on a break-glass retainer. Which statement most accurately describes the primary governance benefit of a retainer arrangement compared to engaging a firm at the time of an incident?

- A) A retainer arrangement is always less expensive than an on-demand engagement for the same incident.
- B) A retainer arrangement eliminates the need for an internal incident response team.
- C) A retainer arrangement pre-establishes legal agreements, pricing, scope, and onboarding so the firm can begin work in hours rather than days when an incident occurs.
- D) A retainer arrangement guarantees that the firm will be available regardless of concurrent demand from other clients.

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* The primary governance value of a retainer is operational readiness. When an incident occurs, an organization without a retainer must negotiate contracts, approve vendors, and complete legal agreements under the worst possible conditions — active incident pressure. A retainer pre-clears all administrative barriers so the firm can begin substantive response work immediately.
  - *Why A is incorrect:* A retainer involves pre-paid hours and annual fees. It is not always less expensive than on-demand engagement for all incident scenarios. The value is in readiness and speed, not necessarily in cost savings.
  - *Why B is incorrect:* Retainer arrangements supplement internal capability, particularly for surge capacity and specialized expertise. They do not replace the internal IR team, which must still triage, contain, and manage the response.
  - *Why D is incorrect:* Retainer agreements typically include capacity provisions but do not guarantee unlimited availability. During major simultaneous incidents affecting multiple clients, capacity constraints can still occur. However, priority response SLAs are commonly included in retainer agreements.

---

### Question 18 (5 points)

A company's Incident Response Plan classifies a confirmed malware infection on a single, isolated workstation with no network connectivity and no sensitive data as Severity 4 (Low). The on-call analyst treats this as a Severity 2 (High) incident because the malware family involved has been associated with ransomware precursor activity. Which statement best evaluates the analyst's decision?

- A) The analyst is correct to override the classification because any ransomware-associated malware is automatically a High severity incident.
- B) The analyst is incorrect — the classification framework must be applied objectively, and the current system state meets Severity 4 criteria; intelligence context should be escalated through the documented criteria, not through unilateral reclassification.
- C) The analyst should close the ticket without action since the workstation is isolated.
- D) The analyst should immediately notify the board because ransomware precursor activity always requires board-level escalation.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Severity classification must be applied consistently based on documented criteria. Unilateral analyst reclassification based on intelligence context that the criteria do not cover creates inconsistency, escalation queue problems, and governance accountability issues. The appropriate action is to apply the documented criteria and use the escalation path within the IRP — such as notifying a supervisor about the intelligence context — rather than reclassifying unilaterally.
  - *Why A is incorrect:* While the threat intelligence context is important, automatic severity overrides based on malware family alone are not how classification frameworks function. Classification is based on observable system state, not threat intelligence association alone.
  - *Why C is incorrect:* Closing a confirmed malware infection without remediation, regardless of current isolation, allows the malware to persist on the device. The workstation must be eradicated even if it is isolated.
  - *Why D is incorrect:* Board-level escalation for a single isolated workstation with ransomware precursor malware is disproportionate to the current observable impact. Escalation criteria should be criteria-based, not driven by threat intelligence associations alone.

---

### Question 19 (5 points)

An organization operating in the European Union discovers a data breach affecting 8,000 EU residents' personal data. The organization determines that the breach poses a high risk to those individuals' rights and freedoms. Under GDPR, which of the following notification obligations apply?

- A) Notify the supervisory authority within 72 hours and notify the affected individuals without undue delay.
- B) Notify the supervisory authority within 30 days and notify affected individuals within 60 days.
- C) Notify affected individuals within 72 hours; supervisory authority notification is optional.
- D) No notification is required because the breach did not involve financial data.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* GDPR Article 33 requires notification to the supervisory authority within 72 hours of becoming aware of a personal data breach. GDPR Article 34 requires notification to affected individuals "without undue delay" when the breach is likely to result in a high risk to their rights and freedoms. Both obligations are triggered in this scenario.
  - *Why B is incorrect:* The GDPR supervisory authority notification deadline is 72 hours, not 30 days. The 30 and 60-day timelines describe HIPAA individual notification — a different regulatory framework.
  - *Why C is incorrect:* Under GDPR, when a breach poses high risk to data subjects, individual notification is required — it is not optional. The supervisor notification is also required within 72 hours.
  - *Why D is incorrect:* GDPR applies to personal data of any type. The type of data does not determine whether notification is required; the nature of the breach and the risk to individuals does.

---

### Question 20 (5 points)

An organization receives a subpoena requiring the production of all electronic records related to a specific individual for a period spanning eighteen months. The CISO discovers that the organization's standard log retention policy deletes most logs after ninety days. Which governance failure does this most directly represent?

- A) A technical failure in the backup system that caused logs to be deleted earlier than intended.
- B) A failure to implement a legal hold process that coordinates with legal counsel to preserve records relevant to reasonably anticipated litigation before routine deletion destroys them.
- C) A compliance gap in the organization's SIEM configuration that should have been identified in the last audit.
- D) An acceptable business outcome — log retention policies cannot account for every possible legal proceeding.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Legal hold processes must preserve evidence before routine deletion schedules eliminate potentially relevant records. A mature IRP and information governance program coordinates with legal counsel to identify when litigation is anticipated and implement holds before evidence is lost. The ninety-day deletion policy is a legitimate business decision, but the failure to override it when litigation became foreseeable is a governance failure.
  - *Why A is incorrect:* The deletion followed policy correctly — it is the policy's interaction with the legal hold obligation that created the gap, not a technical failure.
  - *Why C is incorrect:* While SIEM retention is an audit topic, the root governance failure here is the absence of a legal hold process coordinated with legal counsel.
  - *Why D is incorrect:* Legal hold obligations are not optional. When litigation is reasonably anticipated, organizations have a legal duty to preserve relevant records.

---

## End of Quiz

**Total: 20 questions | 10 questions at 10 points each (original) + 10 questions at 5 points each (supplemental) = 150 points**

Review your answers using the distractor analysis provided. For any question you answered incorrectly, revisit the corresponding section in the Module 10 Reading Guide before proceeding to the lab.
