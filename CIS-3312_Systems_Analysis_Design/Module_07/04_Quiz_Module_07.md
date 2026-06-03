# Quiz: Module 07 — Requirements Elicitation Techniques

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

### Question 1

A BA is beginning a project to replace a legacy accounts payable system. The BA wants to understand how the current process actually works — including workarounds, informal steps, and exception handling that may not be documented anywhere. Which elicitation technique is most directly suited to surfacing this type of tacit knowledge?

- A) Survey — send a questionnaire to all accounts payable staff asking them to describe their current process.
- B) Document analysis — review the current system documentation and procedure manuals to understand the process.
- C) Observation — watch accounts payable staff perform their actual work in the live environment.
- D) Structured interview — conduct a fixed-question interview with each staff member using the same question list.

**Correct Answer:** C) Observation — watching actual work in the live environment surfaces tacit knowledge that surveys, documentation, and structured interviews cannot reliably capture.

**Distractor Analysis:**

- *Why C is correct:* Observation is the elicitation technique specifically designed to reveal the gap between how work is supposed to be performed and how it is actually performed. Tacit knowledge — workarounds, informal steps, exception handling rules that are never written down — shows up in behavior, not in responses to questions or documents. Passive observation of accounts payable staff during a normal working day will reveal the informal rules, communication patterns, and workaround practices that experienced staff perform automatically without conscious awareness.
- *Why A is incorrect:* Surveys capture what people are willing and able to describe about their work. Tacit knowledge, by definition, is not easily articulated — staff cannot reliably describe in a survey form the exception-handling steps they perform automatically. Surveys are excellent for quantifying known requirements across large populations but are poorly suited to discovering unknown or unarticulated knowledge.
- *Why B is incorrect:* Document analysis reveals what the process is supposed to be according to official documentation. It is explicitly described in BABOK as representing the intended state, not the actual state. If the process has evolved since the documentation was written, document analysis alone will not capture the current reality.
- *Why D is incorrect:* Structured interviews ask stakeholders to describe their work verbally. While useful for capturing stated knowledge, they share the same limitation as surveys regarding tacit knowledge — staff can only articulate what they are conscious of knowing. The structured format's additional constraint of fixed questions makes it even less likely to uncover unexpected informal practices.

---

### Question 2

A BA is planning elicitation for a new enterprise resource planning (ERP) system that will affect finance, HR, procurement, and operations departments. All four departments have different requirements that must be reconciled into a unified system design. Initial stakeholder interviews reveal that the finance and operations departments have conflicting views on how purchase approval workflows should work. Which elicitation technique is most appropriate for resolving this conflict efficiently?

- A) Observation — observe both departments performing their current approval workflows to understand the source of the conflict.
- B) Survey — distribute a survey to both departments to quantify which approach has more stakeholder support.
- C) Workshop or JAD session — bring representatives from both departments together in a facilitated session to surface and resolve the conflict collaboratively.
- D) Document analysis — review each department's existing procedures to identify which process is more formally documented.

**Correct Answer:** C) A workshop or JAD session brings conflicting stakeholders together to resolve the conflict in real time with a skilled facilitator.

**Distractor Analysis:**

- *Why C is correct:* Stakeholder conflict resolution is one of the primary use cases for requirements workshops and JAD sessions. Bringing finance and operations representatives into the same facilitated session — with a neutral BA facilitator — creates the conditions for surfacing each side's reasoning, identifying the underlying constraints, and reaching a collaborative decision. JAD sessions are specifically designed for exactly this kind of cross-departmental requirements resolution with formal documentation of agreed outcomes.
- *Why A is incorrect:* Observation helps understand how each department currently performs its work, which may be useful background context. But observation does not create a forum for the departments to interact with each other and resolve the conflict. It addresses understanding, not resolution.
- *Why B is incorrect:* Surveys measure opinion distribution but cannot facilitate negotiation or resolution. If 60% of stakeholders prefer option A, that still leaves 40% who prefer option B — the conflict remains. Requirements decisions are not determined by vote; they require discussion, reasoning, and structured decision-making.
- *Why D is incorrect:* Reviewing existing procedures to identify which is more formally documented establishes an historical baseline but does not resolve a conflict about what the future system should do. The conflict is about future requirements; document analysis addresses past and current state.

---

### Question 3

Which of the following best distinguishes a structured interview from a semi-structured interview in requirements elicitation?

- A) Structured interviews are conducted by two BAs simultaneously; semi-structured interviews are conducted by one BA.
- B) Structured interviews use a fixed set of questions in a defined sequence with no deviation; semi-structured interviews use core prepared questions with freedom to probe and follow unexpected responses.
- C) Structured interviews are used with technical stakeholders; semi-structured interviews are used with business stakeholders.
- D) Structured interviews focus on current-state processes; semi-structured interviews focus on future-state requirements.

**Correct Answer:** B) Structured interviews use fixed questions without deviation; semi-structured interviews combine prepared core questions with adaptive follow-up.

**Distractor Analysis:**

- *Why B is correct:* The defining characteristic of a structured interview is the fixed question sequence — every participant receives exactly the same questions in the same order, with no deviation. This makes responses directly comparable across participants. Semi-structured interviews prepare core questions to ensure key topics are covered but allow the interviewer to adapt, probe, and follow interesting responses. Most BA practice uses semi-structured interviews because they balance coverage with the depth needed to surface unexpected insights.
- *Why A is incorrect:* The number of interviewers is not the defining distinction between structured and semi-structured approaches. Either interview type can involve one or multiple BAs.
- *Why C is incorrect:* Structured and semi-structured interviews are not mapped to stakeholder types by role. The choice between them is based on the elicitation goal — consistency and comparability versus depth and flexibility — not the stakeholder's technical or business background.
- *Why D is incorrect:* Both structured and semi-structured interviews can address current-state understanding, future-state requirements, or both. The interview structure type is independent of the content focus.

---

### Question 4

A BA is using a requirements workshop to elicit requirements for a new student enrollment system. During the workshop, the IT Director consistently dominates the discussion and frequently interrupts other participants. Three other stakeholders — two faculty members and the registrar — have barely spoken for the first hour of the three-hour session. What should the BA, acting as facilitator, do?

- A) Allow the IT Director to continue — technical stakeholders typically have the most relevant expertise in system requirements workshops.
- B) Use facilitation techniques to actively draw out the quieter participants — call on them directly, use round-robin sharing, or structure breakout discussions to give everyone space to contribute.
- C) End the workshop early and reschedule individual interviews with the faculty members and registrar instead.
- D) Ask the IT Director to leave so the other participants can share their perspectives.

**Correct Answer:** B) The facilitator's job is to ensure balanced participation — using direct invitations, structured techniques, and facilitation skills to give all participants space to contribute.

**Distractor Analysis:**

- *Why B is correct:* Facilitating balanced participation is a core BA facilitation competency. Dominant participants are common in workshops, and the BA facilitator must manage this without creating conflict. Techniques include: directly inviting quiet participants ("What do you think about this, from the registrar's perspective?"), structured round-robin turns, small group breakouts where no single voice can dominate, and private pre-workshop conversations to encourage quieter stakeholders to share their views. The registrar and faculty members have requirements that are just as relevant as the IT Director's.
- *Why A is incorrect:* Technical stakeholders have important technical constraints to contribute, but a student enrollment system will be used daily by faculty and registrar staff. Their operational requirements are essential. Allowing one voice to dominate produces requirements that reflect one stakeholder's view, not the full picture needed for a successful system.
- *Why C is incorrect:* Ending the workshop abandons the investment made and loses the benefit of cross-functional interaction that workshops are specifically designed to produce. Individual interviews cannot replicate the dynamic of multiple stakeholders interacting and building on each other's input.
- *Why D is incorrect:* Removing the IT Director from the session creates conflict, damages relationships, and eliminates the technical perspective. The facilitation problem is about balance, not about removal.

---

### Question 5

A BA is reviewing a requirement that reads: "The system should be fast and easy to use." Which quality characteristic of requirements does this statement fail, and how should it be rewritten?

- A) Completeness — the requirement is missing context about which system features must be fast.
- B) Verifiability and clarity — "fast" and "easy to use" are subjective and cannot be tested; the requirement should specify measurable criteria such as "the system shall load the patron search results page within 2 seconds for queries returning up to 500 results."
- C) Traceability — the requirement does not reference the business goal it supports.
- D) Feasibility — the requirement cannot be achieved within typical project budgets.

**Correct Answer:** B) The requirement fails verifiability and clarity — "fast" and "easy to use" are subjective terms that cannot be objectively tested without measurable criteria.

**Distractor Analysis:**

- *Why B is correct:* BABOK Guide v3 requires that requirements be verifiable — testable or demonstrably met or not met. "Fast" has no objective threshold; different people define fast differently. "Easy to use" is entirely subjective and cannot be verified by a test. The rewritten requirement specifies an objective, measurable criterion: a specific response time threshold for a specific operation under specific conditions. This can be verified by performance testing.
- *Why A is incorrect:* Incompleteness describes missing information — gaps in what the requirement covers. This requirement is not incomplete in that sense; it covers performance and usability. The problem is that the terms it uses are not specific enough to be testable, which is a verifiability failure.
- *Why C is incorrect:* Traceability refers to the link between a requirement and the business or stakeholder need that motivated it. While adding a source reference would improve the requirement, that is not the primary quality failure. The primary problem is that the requirement cannot be verified.
- *Why D is incorrect:* Feasibility is a project management concern about whether requirements can be achieved within constraints. A measurable performance requirement is generally feasible — the issue is not feasibility but the absence of measurability in the current statement.

---

### Question 6

A BA is planning elicitation for a project that will affect 1,200 call center agents across eight locations in four states. The BA needs to understand current pain points with the existing customer management system and identify the most important improvements for daily operations. Which elicitation technique is most appropriate for the initial data collection phase?

- A) Individual interviews — conduct 45-minute interviews with all 1,200 agents.
- B) Observation — observe agents at each of the eight locations performing their daily work.
- C) Survey — distribute a questionnaire to all 1,200 agents to collect quantifiable data on pain points and improvement priorities.
- D) JAD session — convene all 1,200 agents in a single three-day workshop.

**Correct Answer:** C) Survey — the most efficient technique for collecting requirements input from a large, geographically distributed population.

**Distractor Analysis:**

- *Why C is correct:* When the stakeholder population is large (1,200) and geographically distributed (four states, eight locations), a survey is the most efficient way to collect initial data. A well-designed survey can reach all 1,200 agents simultaneously, quantify the most common pain points, and identify the highest-priority improvements across the entire population. The survey results then inform which issues warrant deeper investigation through follow-up interviews or observation at selected locations.
- *Why A is incorrect:* Conducting 1,200 individual 45-minute interviews is logistically impractical. That would require 900 hours of interview time, plus travel to eight locations. Even a team of BAs could not complete this in a reasonable project timeline.
- *Why B is incorrect:* Observation at all eight locations could supplement a survey to surface tacit knowledge at representative sites, but it cannot reach all 1,200 agents and cannot efficiently quantify which pain points are most prevalent across the full population. Observation would be an excellent follow-up to survey data, not the primary technique for initial data collection at this scale.
- *Why D is incorrect:* A 1,200-person JAD session is not operationally feasible — JAD sessions are effective with small groups of 10–25 participants where facilitated discussion produces collaborative requirements decisions. A session of this size cannot function as a workshop.

---

### Question 7

A prototype showing three alternative dashboard layouts is shown to 15 users during requirements elicitation. Nine users prefer layout A; four prefer layout B; two prefer layout C. The project team concludes that layout A is the approved requirement. What is the primary limitation of this prototyping process that the team should be aware of?

- A) The sample of 15 users is too small to be statistically significant for a system that will be used by thousands.
- B) Prototyping cannot be used to make design decisions — it is only valid for surfacing missing requirements, not for choosing between alternatives.
- C) User preference for a layout in isolation may not reflect performance, learnability, or task completion effectiveness — preference and usability are different measures.
- D) The prototype should have been evolutionary rather than throwaway before any decisions were made.

**Correct Answer:** C) User preference for a layout does not guarantee usability — users may prefer familiar layouts that are not actually the most efficient or learnable option.

**Distractor Analysis:**

- *Why C is correct:* Preference testing (which layout do you like?) measures subjective appeal. Usability testing measures actual performance — task completion time, error rates, learnability, and efficiency. Users often prefer layouts that look familiar or aesthetically pleasing without those layouts being the most effective for the tasks they will perform. A BA should interpret prototype preference testing as one useful input, not as a definitive usability validation. Follow-up usability testing with task scenarios would provide a more reliable basis for the decision.
- *Why A is incorrect:* While statistical representativeness is a valid concern for some research, prototype preference testing with representative users is a standard and accepted practice in requirements elicitation. The limitation in this scenario is the type of measure (preference vs. usability), not necessarily the sample size.
- *Why B is incorrect:* Prototyping is explicitly used in BABOK and industry practice for both surfacing requirements and evaluating design alternatives. Using prototypes to evaluate design options is a valid and common BA practice.
- *Why D is incorrect:* Whether the prototype is throwaway or evolutionary does not change the limitation being described. The limitation is about what preference testing measures — it exists regardless of prototype type.

---

### Question 8

According to BABOK Guide v3, requirements are organized into four levels. A requirement stating "the system must provide online access to library catalog records for patron self-service, reducing the need for staff-assisted catalog queries by 40%" is best classified at which level?

- A) Functional requirement — it describes a specific function the system must perform (online catalog access).
- B) Business requirement — it describes a business outcome the organization needs to achieve (self-service access with a measurable staff workload impact).
- C) Stakeholder requirement — it describes what a specific stakeholder needs from the solution.
- D) Transition requirement — it describes how the organization must move from the current state to the future state.

**Correct Answer:** B) Business requirement — it describes why the organization needs the change and what business outcome must be achieved.

**Distractor Analysis:**

- *Why B is correct:* BABOK Guide v3 defines business requirements as the higher-level statements of goals, objectives, and outcomes that the change must achieve. This requirement describes a business outcome — patron self-service — and a measurable performance target — 40% reduction in staff-assisted queries. It answers "why is the organization doing this project?" which is the defining question of a business requirement.
- *Why A is incorrect:* A functional requirement describes what the system must do at a more specific operational level — for example, "the system shall allow patrons to search catalog records by title, author, subject, and ISBN." The requirement in the question is at a higher level of abstraction, describing the business purpose rather than the specific system function.
- *Why C is incorrect:* A stakeholder requirement describes what a specific stakeholder needs from the solution to fulfill their role. This requirement is not attributed to a specific stakeholder — it describes organizational goals, making it a business requirement rather than a stakeholder-level need.
- *Why D is incorrect:* Transition requirements describe what must happen to move from the current state to the future state — data migration, training, change management, parallel operation periods. This requirement describes a desired future-state outcome, not a transition activity.

---

### Question 9

A BA has completed an interview with a department manager and identified requirements for a new inventory management system. The BA wants to verify that the documented requirements accurately represent what the manager intended. Which of the following is the most effective follow-up action?

- A) Present the requirements to the development team immediately for design — developers will identify any inaccuracies during design.
- B) Send a written summary of the documented requirements to the manager for review and confirmation, asking the manager to identify any inaccuracies or omissions.
- C) Conduct a survey of all users in the department to validate that the manager's requirements represent the department's needs.
- D) Assume accuracy — if the manager provided the information, the documentation must reflect it correctly.

**Correct Answer:** B) Sending a written summary to the manager for review and confirmation is the standard post-interview validation practice.

**Distractor Analysis:**

- *Why B is correct:* Post-interview validation is a standard and important practice in requirements elicitation. The BA may have misunderstood something the manager said, omitted an important point, or introduced an interpretation error in documentation. Sending a written summary gives the manager the opportunity to review the documented requirements, correct misunderstandings, and identify anything that was missed. This validation step dramatically reduces the cost of errors — catching a misunderstanding now is far less expensive than discovering it during development or testing.
- *Why A is incorrect:* Presenting unvalidated requirements to the development team passes the risk of misunderstanding downstream where it is more expensive to correct. Developers are not positioned to validate business intent — they will design what is documented, not what was meant.
- *Why C is incorrect:* Surveying the full department to validate one manager's interview is disproportionate for this purpose. A follow-up survey might be appropriate for a separate elicitation goal — but confirming interview accuracy should be done directly with the interview subject.
- *Why D is incorrect:* Assuming accuracy is the single riskiest approach to requirements documentation. Misunderstandings, transcription errors, and interpretation differences between BA and stakeholder are common. Without confirmation, these errors propagate through the project until they are discovered at a much higher cost to fix.

---

### Question 10

A systems analyst is documenting requirements for a hospital patient scheduling system. The requirement reads: "The system shall prevent scheduling a patient for two appointments at the same date and time." This requirement is classified as functional because it describes system behavior. Which non-functional requirement category would address the expectation that this scheduling validation must respond within 1 second of the scheduling attempt?

- A) Security requirement — response time is a security characteristic because slow responses can indicate a system under attack.
- B) Availability requirement — the 1-second threshold specifies how often the system must be available to process scheduling requests.
- C) Performance requirement — response time specifies a quality attribute of how the system must execute its functions under defined conditions.
- D) Usability requirement — 1-second response defines how easy the scheduling system is to use.

**Correct Answer:** C) Performance requirement — response time is a quality attribute of how the system performs, classified as a non-functional performance requirement.

**Distractor Analysis:**

- *Why C is correct:* Non-functional requirements describe quality attributes — characteristics of how well the system performs its functions, not what functions it performs. Performance is a standard non-functional requirement category that includes response time, throughput, transaction processing speed, and resource utilization. A 1-second response time threshold is a measurable, verifiable performance requirement that applies to the scheduling validation function.
- *Why A is incorrect:* Response time is not a security characteristic. Security requirements address confidentiality, integrity, authentication, authorization, and audit. Slow response times may correlate with certain security events, but response time thresholds are performance specifications, not security controls.
- *Why B is incorrect:* Availability requirements specify the percentage of time the system must be operational — for example, "the system shall be available 99.5% of monthly scheduled hours." Availability is about uptime, not response speed. A 1-second threshold specifies speed, not availability.
- *Why D is incorrect:* Usability requirements address how easily users can learn and use the system — ease of navigation, task completion rates, learnability, and error recovery. Response time affects user experience, but it is classified as a performance requirement, not a usability requirement. Usability typically addresses the design of the interface and interaction model, not the system's technical processing speed.
