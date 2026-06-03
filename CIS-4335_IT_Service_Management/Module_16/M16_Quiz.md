# Quiz: Module 16 — ITIL 4 Foundation Exam Preparation and Capstone

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Instructions

This final module quiz focuses on synthesis and integration — applying ITIL 4 concepts across multiple domains simultaneously. Each question is worth 10 points. Time limit: 20 minutes.

---

## Questions

**Question 1**

A user contacts the service desk because she cannot access a critical business application she uses daily. The service desk analyst restores access within 20 minutes by resetting a configuration setting. Later that day, the same user calls again with the same problem. The analyst resolves it again in 15 minutes. Which sequence of practices should be invoked across these two events?

A. Both events are service requests — Service Request Management handles both.

B. Both events are incidents — Incident Management handles both, no further action needed.

C. Both events are incidents — Incident Management handles restoration, and the recurrence should trigger Problem Management to identify the root cause.

D. The second event is a change — the configuration needs to be fixed permanently through Change Enablement.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is wrong. The user cannot access an application she needs — this is an unplanned interruption, not a request for something she does not yet have. Both events are incidents.
- **B** is wrong. Resolving two incidents with the same root cause without investigating the underlying cause is exactly the failure mode Problem Management exists to prevent. Repeated incidents signal an underlying problem.
- **C** is correct. Both events are incidents handled by Incident Management. However, recurrence is the trigger for Problem Management — to identify the root cause, document a known error, and implement a permanent fix. This may eventually lead to a change.
- **D** is partially correct in spirit (a change will eventually fix it) but wrong as a primary answer. Change Enablement governs the fix after Problem Management identifies the root cause — it is not the first practice triggered by the second incident report.

---

**Question 2**

An IT organization has 34 practices in ITIL 4. For the Foundation exam, how many practices are tested and at what two levels of depth?

A. All 34 practices are tested; 20 at full depth and 14 at purpose-only.

B. 15 practices are tested; 7 at full depth (purpose, terms, and application) and 8 at purpose-only.

C. 10 practices are tested; all at the same depth.

D. 17 practices are tested; 10 at purpose only and 7 at key terms level.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. The Foundation exam does not test all 34 practices — it focuses on 15 practices relevant to foundational service management roles.
- **B** is correct. The ITIL 4 Foundation syllabus includes 15 practices: 7 at full depth (purpose, key terms, and application — Continual Improvement, Change Enablement, Incident Management, Problem Management, Service Request Management, Service Desk, Service Level Management) and 8 at purpose-only level.
- **C** is wrong. Neither the number (10) nor the uniform depth description is accurate.
- **D** is wrong. 17 practices and the described depth split do not match the published Foundation syllabus.

---

**Question 3**

Which of the following scenarios represents a violation of the "Focus on Value" Guiding Principle?

A. A team automates a repetitive deployment task, freeing engineers to work on new capabilities.

B. A change management process requires 14 forms and three committee approvals for a single low-risk server restart.

C. The service desk sends a satisfaction survey to users after each incident resolution.

D. A service design team interviews customer representatives to understand desired outcomes before beginning technical design.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is a correct application of "Optimize and Automate" and indirectly "Focus on Value" by freeing capacity for value work.
- **B** is correct. Requiring 14 forms and three approvals for a low-risk restart is bureaucratic overhead that consumes resources without delivering proportional value. "Focus on Value" requires eliminating activities that do not contribute to value creation. This is also a violation of "Keep It Simple and Practical."
- **C** is a correct application of "Collaborate and Promote Visibility" and measuring value perception.
- **D** is a direct application of "Focus on Value" — understanding what customers value before designing.

---

**Question 4**

An organization runs a mature ITSM practice. The IT team regularly creates change records, incident logs, and post-implementation reviews. A third-party auditor arrives to conduct a SOC 2 Type II assessment. Which statement best describes the relationship between the ITSM documentation and the audit?

A. ITSM documentation is irrelevant to SOC 2 audits — a separate compliance program must be maintained.

B. ITSM practice outputs (change records, incident logs, PIRs) naturally serve as audit evidence for change management, incident response, and availability controls.

C. The organization must recreate all documentation in the auditor's preferred format — ITSM system exports are not accepted.

D. SOC 2 only requires technical configuration evidence; process documentation has no value in the audit.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. Well-documented ITIL practices directly generate evidence for multiple SOC 2 controls — they are not separate programs.
- **B** is correct. Change records demonstrate authorized change management (Security criterion). Incident logs with response times demonstrate incident response capability. PIRs demonstrate continuous improvement and retrospective analysis. ITSM practice outputs are natural audit evidence.
- **C** is wrong. Auditors accept evidence from ITSM systems, log exports, and screenshots — they do not require a specific format as long as the evidence is complete and authentic.
- **D** is wrong. SOC 2 auditors review both technical configuration evidence and process/policy documentation. Process evidence (change approvals, incident timelines) is a core component.

---

**Question 5**

The ITIL 4 Service Value System takes two types of inputs and produces one output. What are they?

A. Inputs: Incidents and Changes. Output: Resolved Services.

B. Inputs: Demand and Opportunity. Output: Value.

C. Inputs: Customer Requests and Business Strategy. Output: Service Catalog.

D. Inputs: Practices and Processes. Output: Service Value Chain.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. Incidents and changes are operational artifacts managed within the SVS — not its primary inputs. "Resolved services" is not a meaningful SVS output.
- **B** is correct. The ITIL 4 SVS explicitly takes **Opportunity** (external context, possibilities) and **Demand** (need for services from consumers) as inputs and produces **Value** as its output.
- **C** is wrong. Customer requests and business strategy may inform the SVS inputs but are not the defined terms. The service catalog is a component, not an output.
- **D** is wrong. Practices and processes are internal SVS components — not inputs. The SVC is a component, not an output.

---

**Question 6**

A new CIO joins a company and immediately announces plans to replace the entire ITSM platform, redesign all processes from scratch, and retrain 200 service desk staff — all within six months. Which ITIL 4 Guiding Principle is most clearly being violated?

A. Optimize and Automate

B. Start Where You Are

C. Keep It Simple and Practical

D. Progress Iteratively with Feedback

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. The plan does not clearly involve automating or optimizing in the correct direction — but "optimize and automate" is not the primary violated principle here.
- **B** is correct. "Start Where You Are" warns against discarding the current state before understanding it. The CIO is proposing a complete replacement without first assessing what works, what does not, and what can be reused. This is a classic violation.
- **C** is wrong. "Keep It Simple" could be cited, but simplification does not require starting from scratch — it requires eliminating non-value steps from what exists.
- **D** is wrong. "Progress Iteratively" is also violated (a 6-month big-bang transformation), but the root violation is failing to start with a current-state assessment.

---

**Question 7**

Which four DORA metrics are used to measure software delivery performance?

A. Deployment frequency, change lead time, mean time to resolve, customer satisfaction score.

B. Deployment frequency, lead time for changes, change failure rate, mean time to restore.

C. Sprint velocity, deployment frequency, defect escape rate, incident rate.

D. Code coverage, deployment frequency, availability percentage, change volume.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. "Customer satisfaction score" is not a DORA metric. "Mean time to resolve" is a plausible invention but "Mean time to restore" is the correct DORA term.
- **B** is correct. The four DORA metrics are: **Deployment frequency** (how often), **Lead time for changes** (code commit to production), **Change failure rate** (percentage of deployments causing issues), and **Mean time to restore** (MTTR — how fast service recovers).
- **C** is wrong. Sprint velocity, defect escape rate, and incident rate are not DORA metrics.
- **D** is wrong. Code coverage and availability percentage are useful metrics but not DORA metrics.

---

**Question 8**

A service desk receives a call. The user says: "I know you reset passwords, but I'd like to report that our email system has been intermittently bouncing outbound messages since this morning. About 20% of our sent emails are not delivering." Which practice should primarily handle this contact?

A. Service Request Management — the user is requesting a service action.

B. Change Enablement — the email system needs to be modified.

C. Incident Management — an unplanned degradation in service quality is reported.

D. Problem Management — intermittent problems always indicate a root cause to investigate.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is wrong. The user is not requesting a pre-defined service they are entitled to — they are reporting a service degradation. This is not a service request.
- **B** is wrong. A change may eventually be needed to fix the root cause, but the immediate response to a service degradation is incident management — restore service first.
- **C** is correct. A 20% email delivery failure is an unplanned reduction in service quality — an **incident**. The service desk should log an incident, classify it, and begin the resolution process. Incident Management is the correct primary practice.
- **D** is a common trap. While the intermittent nature suggests a problem worth investigating, Problem Management begins after or alongside incident management — not instead of it. The immediate priority is service restoration, not root cause analysis. Problem Management would be triggered as a parallel or follow-on activity.

---

**Question 9**

A cloud services company has a policy that any new employee who passes the background check, signs an NDA, and completes security training in their first week receives automatic access to the standard development environment. This is handled without an individual approval for each new hire. Which ITIL change type does provisioning this access represent?

A. Normal change

B. Emergency change

C. Unauthorized change

D. Standard change

**Correct Answer: D**

**Distractor Analysis:**

- **A** is wrong. Normal changes require individual risk assessment and authorization. The scenario describes a pre-authorized, repeatable procedure — not individual case-by-case evaluation.
- **B** is wrong. Emergency changes are for urgent responses to incidents or critical situations — not routine onboarding access provisioning.
- **C** is wrong. The access provisioning follows a defined, approved policy — it is authorized, not unauthorized.
- **D** is correct. A **standard change** is pre-authorized, low-risk, and follows a defined procedure. The new hire access provisioning process — with defined prerequisites (background check, NDA, training) and automatic execution — is exactly what standard changes enable.

---

**Question 10**

A student has answered 15 of 40 questions on the ITIL 4 Foundation exam. She realizes she has spent 25 of her 60 minutes on these 15 questions. What exam strategy should she apply for the remaining 25 questions?

A. Continue at the same pace — thoroughness is more important than speed.

B. Accelerate to approximately 90 seconds per question; flag uncertain questions for review at the end.

C. Skip all remaining questions and focus on the 15 she has already answered.

D. Request additional time — she is entitled to 90 minutes as a non-native English speaker.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is wrong. At 25 minutes for 15 questions, she is averaging 100 seconds per question. If she continues at this pace, she will complete only about 36 questions in 60 minutes — risking not finishing. She must accelerate.
- **B** is correct. The target pace is 90 seconds per question (60 minutes ÷ 40 questions). With 35 minutes remaining and 25 questions left, she has 84 seconds per question — slightly tight but achievable. Flagging uncertain questions and returning at the end is standard exam strategy.
- **C** is wrong. Skipping 25 questions guarantees failure — each missed question is 0 points. The passing threshold of 65% (26/40) requires answering all questions and getting most right.
- **D** is wrong unless she was pre-approved for this accommodation before the exam. You cannot request accommodations during the exam; they must be arranged in advance.

---

*End of Module 16 Quiz — 10 questions with distractor analysis*
