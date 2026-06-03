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

## End of Quiz

**Total: 10 questions | 100 points**

Review your answers using the distractor analysis provided. For any question you answered incorrectly, revisit the corresponding section in the Module 10 Reading Guide before proceeding to the lab.
