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

---

### Question 11

A BA documents the following requirement after a stakeholder interview: "The system shall allow managers to approve purchase orders." Three months later, a compliance auditor discovers that the business rule is actually that only managers whose spending authority exceeds the purchase order value can approve it — a rule the stakeholder assumed was obvious but never stated. Which elicitation problem does this illustrate?

- A) The BA used the wrong elicitation technique — observation would have caught this rule.
- B) The stakeholder provided a stated requirement that masked an unstated business rule the BA failed to uncover through probing.
- C) The BA violated the BABOK governance process by accepting requirements without change control approval.
- D) The requirement was verified but not validated, causing the gap to remain undiscovered.

**Correct Answer:** B) The stakeholder stated a surface-level requirement without articulating the embedded business rule, and the BA did not probe deeply enough to uncover it.

**Distractor Analysis:**

- *Why B is correct:* Unstated requirements are one of the most common and costly elicitation failures. Experienced stakeholders often omit rules they consider obvious — they assume the BA understands the business context as well as they do. The BA's job is to ask probing questions ("Are there any conditions under which a manager cannot approve?" or "What determines whether a manager is authorized to approve?") that surface the hidden business rules embedded in simple statements.
- *Why A is incorrect:* Observation might have revealed the approval workflow in action, but it would not reliably surface an edge-case business rule about spending authority limits without the BA specifically probing for it. The core problem is incomplete elicitation, not wrong technique selection.
- *Why C is incorrect:* Change control governs changes to baselined requirements; this scenario describes a requirements gap discovered before implementation, not a post-baseline change. Governance is not the issue here.
- *Why D is incorrect:* Verification checks that requirements are well-formed; validation checks that they address the right business need. Neither would catch an unstated rule that was never documented — the gap existed in elicitation, before any verification or validation activity.

---

### Question 12

A BA is using focus groups to gather requirements for a consumer-facing mobile application. After the session, the BA notes that three vocal participants dominated the conversation and several quieter participants rarely contributed. What should the BA do to supplement the focus group findings?

- A) Accept the focus group results as representative — vocal participants typically have the strongest opinions and most relevant experience.
- B) Conduct individual follow-up interviews with the participants who did not contribute to the focus group to gather their perspectives.
- C) Repeat the focus group with only the quiet participants and discard the original session results.
- D) Use document analysis to find documentation that confirms the vocal participants' stated requirements.

**Correct Answer:** B) Follow-up individual interviews with under-represented participants address the participation imbalance from the focus group.

**Distractor Analysis:**

- *Why B is correct:* Focus groups are vulnerable to social dynamics — dominant personalities, groupthink, and reluctance to disagree publicly. Quiet participants often hold views that differ from the vocal majority, and those differences may represent important requirements or risks. Individual follow-up interviews eliminate the social pressure and give each participant space to express their genuine views. This combination of focus group and individual interview is a best practice for mitigating focus group limitations.
- *Why A is incorrect:* Vocal participants are not more reliable than quiet ones — they are simply more confident or willing to speak in group settings. Requirements collected from a biased group sample may not represent the actual user population's needs.
- *Why C is incorrect:* Discarding a completed focus group session wastes the investment and throws away the perspectives of the participants who did contribute. Supplementing the session with follow-up is more efficient than replacement.
- *Why D is incorrect:* Document analysis reviews existing artifacts; it cannot surface the unexpressed views of participants who were present in a focus group but chose not to speak.

---

### Question 13

Which of the following is the primary risk of beginning system design before requirements have been formally confirmed by stakeholders?

- A) The design team may use the wrong diagramming tool, producing artifacts in a format stakeholders cannot read.
- B) Design decisions made against unconfirmed requirements may have to be fully reworked if the requirements change after stakeholder review.
- C) Stakeholders will be unable to review design artifacts because they have not approved the requirements yet.
- D) The project manager cannot create a project schedule without confirmed requirements.

**Correct Answer:** B) Unconfirmed requirements that change after design begins force costly rework of design artifacts that were built on incorrect foundations.

**Distractor Analysis:**

- *Why B is correct:* The cost of defect correction increases dramatically as a project advances — a requirements error caught during elicitation costs a fraction of the same error caught during design, and a tiny fraction of the cost when caught during testing or after deployment. Beginning design on unconfirmed requirements means that when stakeholders review and change the requirements, every design decision made against those requirements must be revisited, revised, or discarded.
- *Why A is incorrect:* Diagramming tool selection is an operational concern that does not represent the fundamental risk of designing against unconfirmed requirements.
- *Why C is incorrect:* There is no formal rule preventing stakeholders from reviewing design artifacts before requirements are confirmed; this describes a process preference, not the primary risk.
- *Why D is incorrect:* Project managers routinely create preliminary schedules before requirements are confirmed; the schedule can be refined as requirements stabilize. The inability to schedule is a minor inconvenience compared to the design rework risk.

---

### Question 14

During an observation session, a BA notices that a warehouse receiving clerk consistently skips the system's "Quality Check" step and marks items as received without completing the inspection. When the BA asks the clerk why, the clerk says "That step always times out after 10 seconds and I have to re-enter everything — it's faster to skip it." What type of finding has the BA discovered, and what should happen next?

- A) A usability defect in the current system and an implicit functional requirement that the new system must complete quality check validation without timeout interruptions.
- B) A compliance violation — the BA should escalate to legal and halt the project.
- C) An assumption — the BA should document that quality checks are not performed and treat this as a stakeholder preference.
- D) An elicitation error — the BA observed the wrong process and should reschedule the observation.

**Correct Answer:** A) A usability defect in the current system that is generating a workaround, surfacing an implicit requirement for the new system.

**Distractor Analysis:**

- *Why A is correct:* The observation has revealed a current-state workaround caused by a system usability defect. This is exactly the type of finding that justifies observation as an elicitation technique — the clerk cannot describe this in a survey or interview because it is an automatic habit. The new system has an implicit requirement: the quality check step must not interrupt the workflow with timeouts. Without observation, this requirement would never be discovered, and the new system might replicate the same defect.
- *Why B is incorrect:* While skipping quality checks may have compliance implications, the BA's role is to document the finding and surface it as a requirement — not to halt the project or escalate to legal unilaterally. The BA should document the finding and raise it with the appropriate stakeholders.
- *Why C is incorrect:* A documented workaround to a broken system step is not a stakeholder preference — it is a symptom of a real system problem that must be addressed in the new design. Treating it as a preference would result in the new system perpetuating the same broken workflow.
- *Why D is incorrect:* The BA has discovered exactly the kind of insight that observation is designed to surface. This is a successful elicitation result, not an error.

---

### Question 15

A BA is preparing for an elicitation workshop with 12 stakeholders representing four departments. Two departments have a known, long-standing conflict over a specific business process. What preparation step is most important for this particular workshop?

- A) Create a comprehensive slide deck presenting the BA's recommended solution to the conflict so stakeholders can react to a concrete proposal.
- B) Pre-interview the conflicting stakeholders individually to understand each side's position, identify the underlying interests behind their stated positions, and prepare facilitation strategies for managing the conflict during the workshop.
- C) Assign a senior manager to attend and make the final decision on the conflict during the session.
- D) Exclude one of the two conflicting departments from the workshop to avoid derailing the session.

**Correct Answer:** B) Pre-workshop individual conversations to understand each side's underlying interests and prepare conflict facilitation strategies.

**Distractor Analysis:**

- *Why B is correct:* Effective conflict facilitation requires understanding both sides' positions and the underlying interests that drive them. Pre-workshop interviews allow the BA to identify common ground, anticipate the specific flashpoints, and prepare facilitation moves — reframing questions, separating positions from interests, identifying areas of agreement first. Walking into a known conflict without preparation is the surest way to have the workshop derailed.
- *Why A is incorrect:* Presenting a BA-recommended solution to a stakeholder conflict would be perceived as taking sides and would likely escalate the conflict rather than resolve it. The BA's role is to facilitate stakeholder decision-making, not to make the decision.
- *Why C is incorrect:* Having a manager make the decision during the session removes ownership from the stakeholders and typically produces compliance without commitment. Stakeholders who feel their concerns were overruled will be difficult to engage throughout the project.
- *Why D is incorrect:* Excluding a stakeholder group because they are in conflict guarantees that their requirements will be missing from the outcome — which is a worse result than managing the conflict.

---

### Question 16

Which BABOK Guide v3 task specifically addresses the BA's responsibility to ensure that stakeholders are collaborating effectively and that interpersonal barriers to requirements quality are being managed?

- A) Prepare for Elicitation — planning which techniques and materials to use before a session
- B) Manage Stakeholder Collaboration — facilitating productive working relationships and managing interpersonal dynamics that affect BA work
- C) Plan Stakeholder Engagement — identifying stakeholders and planning how to interact with them
- D) Communicate Business Analysis Information — ensuring requirements are distributed to the right audiences in the right format

**Correct Answer:** B) Manage Stakeholder Collaboration addresses the ongoing facilitation of productive working relationships throughout elicitation.

**Distractor Analysis:**

- *Why B is correct:* BABOK KA 4 includes "Manage Stakeholder Collaboration" as a distinct task focused on ensuring that stakeholders are working together effectively — managing conflict, fostering trust, handling resistance, and maintaining the conditions for high-quality requirements work. It is the task that addresses the human side of elicitation.
- *Why A is incorrect:* Prepare for Elicitation covers logistical and content preparation before a session — selecting techniques, reviewing documents, preparing questions. It does not address managing interpersonal dynamics during the project.
- *Why C is incorrect:* Plan Stakeholder Engagement (KA 2) creates the initial stakeholder register and engagement approach. It is planning-phase work, not ongoing collaboration management during elicitation.
- *Why D is incorrect:* Communicate Business Analysis Information addresses how requirements and BA findings are shared with stakeholders — format, timing, and channels. It does not address interpersonal dynamics or collaboration barriers.

---

### Question 17

A project team has completed requirements elicitation for a new human resources system. The BA discovers a stakeholder was missed during the initial identification process: the organization's external payroll service provider must integrate with the new HR system. What is the most significant risk this omission creates?

- A) The project will be delayed because the external provider's requirements will need to be gathered during the design phase.
- B) Integration requirements for the external payroll provider are missing from the requirements baseline, creating a high risk of integration failures at deployment.
- C) The stakeholder register must be updated, which requires change control board approval and restarts the elicitation phase.
- D) The BA will receive a poor performance review for the missed stakeholder.

**Correct Answer:** B) Missing integration requirements from the external provider create a high-risk gap that will likely produce integration failures at deployment.

**Distractor Analysis:**

- *Why B is correct:* External system integrators are a category of stakeholder that is frequently overlooked during initial identification because they are not internal organizational members. The payroll provider must exchange data with the new HR system — data formats, API specifications, authentication requirements, and timing constraints must all be defined. If these requirements are missing from the baseline, the development team will build the HR system without accounting for integration, and the failure will only be discovered during integration testing or after go-live.
- *Why A is incorrect:* While delay is a possible consequence, it is a symptom, not the primary risk. The primary risk is the technical integration gap, which can cause system failures regardless of schedule.
- *Why C is incorrect:* The Stakeholder Register is a BA planning document, not a requirements artifact. Adding a stakeholder does not require change control board approval; it requires updating the register and initiating elicitation with the new stakeholder.
- *Why D is incorrect:* Performance consequences are not a technical risk to the project. The significant risk is the integration gap in the requirements, not the BA's evaluation.

---

### Question 18

Which of the following is the most accurate description of an "evolutionary prototype" in contrast to a "throwaway prototype"?

- A) An evolutionary prototype is built quickly to gather stakeholder feedback and is then discarded; a throwaway prototype is kept and refined into the final system.
- B) An evolutionary prototype is intended to be refined and eventually become the deliverable system; a throwaway prototype is built for elicitation or validation and discarded after feedback is gathered.
- C) An evolutionary prototype is always higher fidelity (coded) than a throwaway prototype, which is always a paper sketch.
- D) Evolutionary prototypes are used in Agile projects; throwaway prototypes are used in Waterfall projects.

**Correct Answer:** B) An evolutionary prototype is refined into the production system; a throwaway prototype is discarded after its feedback purpose is served.

**Distractor Analysis:**

- *Why B is correct:* BABOK and software engineering literature define the distinction clearly: a throwaway (also called a "rapid" or "horizontal") prototype is built quickly to elicit reactions and feedback, then discarded — it is not intended to become the system. An evolutionary (also called "incremental") prototype is iteratively refined based on stakeholder feedback until it becomes the production system. The choice between them has significant technical implications: throwaway prototypes can use any technology; evolutionary prototypes must be built with production-quality code from the start.
- *Why A is incorrect:* This reverses the definitions of the two prototype types.
- *Why C is incorrect:* Fidelity (paper vs. coded) is a separate dimension from throwaway vs. evolutionary. A high-fidelity coded prototype can still be throwaway; a low-fidelity paper prototype can sometimes be the starting point of an evolutionary approach.
- *Why D is incorrect:* Both prototype types are used in both Agile and Waterfall contexts. The choice is based on intent (retain or discard), not on methodology.

---

### Question 19

A BA sends a post-interview confirmation memo to a stakeholder summarizing eight requirements captured during the interview. The stakeholder responds: "Items 3 and 7 are correct. Items 1, 2, and 5 need minor wording adjustments. Items 4 and 6 are completely wrong — I never said those. Item 8 is correct but I forgot to mention that it only applies to orders placed on weekdays." What does this response demonstrate about the value of the confirmation step?

- A) The interview was poorly conducted and should be redone completely.
- B) The confirmation step caught two incorrect requirements and one incomplete requirement before they entered the requirements baseline, preventing costly downstream errors.
- C) The BA must not have taken notes during the interview, causing the errors.
- D) The stakeholder is being difficult and changing their requirements after the interview.

**Correct Answer:** B) The confirmation step caught errors before they entered the baseline — demonstrating exactly why BABOK requires post-elicitation confirmation.

**Distractor Analysis:**

- *Why B is correct:* This is a textbook illustration of why the "Confirm Elicitation Results" task exists in BABOK KA 4. Items 4 and 6 were incorrect — if they had entered the requirements baseline without confirmation, they would have driven incorrect design, development, and test cases. Item 8 was incomplete — a critical business rule (weekdays only) would have been missed. Catching these issues at the confirmation stage costs almost nothing to fix; catching them during testing would cost significantly more.
- *Why A is incorrect:* Some degree of misunderstanding in complex requirements interviews is normal, not evidence that the entire interview must be redone. The confirmation process is specifically designed to catch and correct these normal errors.
- *Why C is incorrect:* Note-taking quality is one possible factor but is not the only cause of interview documentation errors. Misinterpretation, ambiguity, and complex domain concepts all contribute. The confirmation step catches errors regardless of their cause.
- *Why D is incorrect:* Item 8 is an addition (a condition the stakeholder forgot to mention), not a change of mind. Items 4 and 6 are corrections to errors — the stakeholder did not say those things. This is standard, expected post-interview behavior that the confirmation process is designed to accommodate.

---

### Question 20

A BA has completed elicitation for a new supply chain system. The requirements specification contains 247 requirements. The BA has confirmed all requirements with stakeholders. The project manager now asks: "How do we know all the requirements are still valid when we begin design in three months?" Which BA activity addresses this concern?

- A) Re-interview all stakeholders every two weeks to detect any requirement changes.
- B) Maintain the requirements baseline through BABOK KA 6 Requirements Life Cycle Management, which tracks requirement status, changes, and continued validity throughout the project.
- C) Accept that requirements will not change during a three-month design phase and proceed without further monitoring.
- D) Convert all requirements to user stories and move to an Agile approach where requirements are managed through sprint planning.

**Correct Answer:** B) BABOK KA 6 Requirements Life Cycle Management governs the ongoing validity, traceability, and controlled change of requirements after the baseline is established.

**Distractor Analysis:**

- *Why B is correct:* Requirements Life Cycle Management (KA 6) specifically addresses the concern the PM has raised. After baseline approval, KA 6 tasks include: maintaining requirements, managing requirement changes through a controlled process, and re-validating requirements when the business context changes. This is not a one-time activity — requirements are actively managed from baseline approval through deployment.
- *Why A is incorrect:* Re-interviewing all stakeholders every two weeks is operationally impractical for 247 requirements with multiple stakeholders. KA 6 provides a structured, efficient process for managing requirement validity without constant full re-elicitation.
- *Why C is incorrect:* Business requirements routinely change during a design phase as stakeholders learn more, business conditions shift, or regulatory changes occur. Assuming they will not change is not a management strategy — it is wishful thinking.
- *Why D is incorrect:* Switching methodology mid-project to address a requirements management concern is a major project decision that requires full stakeholder and sponsor agreement. KA 6 applies regardless of methodology; the PM's concern can be addressed without changing the project approach.
