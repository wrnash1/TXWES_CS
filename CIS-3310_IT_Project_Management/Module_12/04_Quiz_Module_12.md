# Quiz: Module 12 — Communication and Stakeholder Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Question 1

A project currently has 9 team members. The project manager is adding 2 new members to the team. How many new communication channels are created by this addition?

- A) 2
- B) 9
- C) 19
- D) 21

**Correct Answer: C**

Before addition: `9(8)/2 = 36` channels. After addition (11 members): `11(10)/2 = 55` channels. New channels created: `55 - 36 = 19`.

Distractor Analysis:

- **Why C is correct:** The formula `n(n-1)/2` must be applied before and after the addition, then subtracted. With 9 members there are 36 channels; with 11 members there are 55 channels; the difference is 19 new channels created by adding 2 people.
- **Why A is incorrect:** 2 would suggest each new member adds exactly 1 channel, which is only true when adding a second person to a one-person team. Each new member adds channels to every existing member, not just one.
- **Why B is incorrect:** 9 is the number of new channels created when adding one person to a 9-person team (making it 10 total). This question adds 2 people, requiring two separate increments or a before-and-after calculation.
- **Why D is incorrect:** 21 = `11(10)/2 - 9(8)/2` only if you compute `55 - 34`, which would come from a calculation error in the before-state (using n=8 instead of n=9). Always verify the before-state channels using the original team size.

---

## Question 2

A project manager places project documents, design specifications, and reference guides on the project SharePoint site so team members can access them whenever needed. Which communication method is this?

- A) Push communication
- B) Interactive communication
- C) Formal communication
- D) Pull communication

**Correct Answer: D**

Pull communication makes information available in a central location for stakeholders to retrieve at their discretion. A SharePoint repository is the classic pull communication example — information is accessible but not actively sent to recipients.

Distractor Analysis:

- **Why D is correct:** Pull communication is self-service. Stakeholders access the information when they need it rather than receiving it automatically. Document repositories, intranets, wikis, and project portals are all pull communication channels.
- **Why A is incorrect:** Push communication actively sends information to recipients — they receive it whether they seek it or not. Email, status reports, and meeting minutes are push examples. A SharePoint site that stakeholders must visit to retrieve information is not push.
- **Why B is incorrect:** Interactive communication is real-time two-way exchange — meetings, phone calls, video conferences. A document repository has no real-time or two-way component.
- **Why C is incorrect:** Formal vs. informal is a separate communication dimension (not push/pull/interactive). Formal communication uses established channels and documentation. The question asks about communication method type, which is push/pull/interactive.

---

## Question 3

A project manager needs a tool to clearly define who is responsible for executing each project task, who owns each deliverable's outcome, who must be consulted for input, and who simply needs to be notified. Which tool directly addresses this need?

- A) Communication Management Plan
- B) Stakeholder Register
- C) RACI Matrix
- D) Power-Interest Grid

**Correct Answer: C**

The RACI Matrix defines four roles — Responsible (does the work), Accountable (owns the outcome), Consulted (provides input), and Informed (receives notification) — for every task and deliverable in the project.

Distractor Analysis:

- **Why C is correct:** The RACI matrix directly maps tasks to role assignments across the project team. It is specifically designed to answer "who does what" at a task-by-task level and to ensure every deliverable has a single accountable owner.
- **Why A is incorrect:** The Communication Management Plan documents who needs what information, in what format, and how often. It addresses information distribution, not task-level role assignments. A stakeholder receiving a status report is not the same as being assigned a RACI role on a task.
- **Why B is incorrect:** The Stakeholder Register documents stakeholder characteristics, interests, influence levels, and engagement strategies. It does not assign task-level roles or define who is accountable for specific deliverables.
- **Why D is incorrect:** The Power-Interest Grid determines stakeholder engagement strategies based on power and interest levels. It is an analysis tool for managing relationships, not an accountability assignment tool for project tasks.

---

## Question 4

The project manager assigns two senior developers as Accountable for the same software module deliverable because both contributed equally to its design. What is the problem with this assignment?

- A) There is no problem — co-accountability is encouraged for shared deliverables
- B) Accountable must always be a manager, not a developer
- C) Having two Accountable owners creates accountability diffusion, where neither person fully owns the outcome
- D) The RACI matrix allows multiple Accountable owners as long as both agree to it

**Correct Answer: C**

The core RACI rule is that exactly one person holds the Accountable role per task or deliverable. Assigning two Accountable owners creates accountability diffusion — each person may assume the other is taking responsibility, resulting in neither fully owning the outcome.

Distractor Analysis:

- **Why C is correct:** Accountability requires a single owner. When two people share accountability, ownership becomes ambiguous. Neither person can be held definitively responsible when something goes wrong, and coordination requirements between co-owners often delay decision-making.
- **Why A is incorrect:** Co-accountability is explicitly prohibited in the RACI framework. Shared accountability is functionally the same as no accountability — it eliminates the clarity that the A role is designed to provide.
- **Why B is incorrect:** There is no rule that Accountable must be a manager. A developer can and often should hold the A role for technical deliverables they own. The role is about outcome ownership, not organizational hierarchy.
- **Why D is incorrect:** RACI rules are not subject to agreement between parties. The requirement for exactly one A per task is a fundamental framework principle, not a negotiable preference. Mutual agreement between two parties to share accountability does not make the assignment valid.

---

## Question 5

A stakeholder analysis reveals that the VP of Finance has very high organizational authority but minimal interest in the IT project's day-to-day details. Where does this stakeholder fall on the Power-Interest grid, and what is the appropriate engagement strategy?

- A) High Power, High Interest — Manage Closely
- B) Low Power, Low Interest — Monitor
- C) High Power, Low Interest — Keep Satisfied
- D) Low Power, High Interest — Keep Informed

**Correct Answer: C**

High authority with low interest places a stakeholder in the High Power, Low Interest quadrant. The appropriate strategy is Keep Satisfied — provide regular, high-level updates, respect their time, and ensure they are never surprised by project developments.

Distractor Analysis:

- **Why C is correct:** A VP with budget authority but low day-to-day interest represents the classic High Power/Low Interest stakeholder. They can unilaterally block or redirect the project if dissatisfied, so they must be kept satisfied — but overloading them with detail will not increase engagement and may generate irritation.
- **Why A is incorrect:** Manage Closely applies to High Power, High Interest stakeholders — those who both have authority and are actively engaged with project details. The VP in this scenario has low interest, so intensive management would be inappropriate and unwelcome.
- **Why B is incorrect:** Low Power, Low Interest describes stakeholders with neither significant authority nor strong concern. A VP with high organizational authority belongs in a high-power quadrant regardless of their interest level.
- **Why D is incorrect:** Low Power, High Interest describes stakeholders like end users — highly concerned but without authority to override decisions. A VP with "very high organizational authority" is definitively in a high-power position.

---

## Question 6

During a status meeting, a team member raises a concern that the new payroll system integration may not meet the go-live deadline due to an undiscovered API incompatibility. The PM acknowledges the concern and commits to follow up. Where should the PM document this issue to ensure it is tracked and resolved?

- A) Risk register
- B) Change log
- C) Issue log
- D) Lessons learned register

**Correct Answer: C**

The issue log records raised concerns, open problems, the person responsible for resolution, and the resolution date. It provides formal tracking and accountability for concerns raised during the project, ensuring they are not forgotten after the meeting.

Distractor Analysis:

- **Why C is correct:** An issue log captures current, active problems that require follow-up and resolution. The API incompatibility concern is a known, current issue — not a potential future risk. Once a risk materializes or becomes a confirmed problem, it moves from the risk register to the issue log.
- **Why A is incorrect:** The risk register tracks potential future events that may or may not occur. An API incompatibility that has already been discovered is a current issue, not a future uncertainty. It belongs in the issue log, not the risk register.
- **Why B is incorrect:** The change log tracks approved and pending change requests to project scope, schedule, or budget. The API incompatibility may eventually trigger a change request, but at the point of discovery it is an issue requiring investigation, not a change request.
- **Why D is incorrect:** The lessons learned register captures knowledge and insights for future projects. It is populated during the project but focuses on retrospective learning, not real-time issue tracking and resolution.

---

## Question 7

A project manager sends weekly status reports to the project sponsor. These reports are emailed every Monday morning before the sponsor's leadership briefing. Which type of communication does this represent?

- A) Pull communication
- B) Interactive communication
- C) Push communication
- D) Passive communication

**Correct Answer: C**

Push communication actively sends information to specific recipients — they receive it whether or not they actively seek it. A scheduled status report emailed directly to the sponsor is the most common push communication example in project management.

Distractor Analysis:

- **Why C is correct:** The PM is initiating the communication and sending it directly to the recipient on a scheduled basis. The sponsor receives the report automatically without needing to log into a system or request the information. This is push communication by definition.
- **Why A is incorrect:** Pull communication requires the recipient to actively retrieve information from a central source. If the sponsor had to log into a SharePoint site to view status updates, that would be pull. Receiving an email with the report attached is not pull.
- **Why B is incorrect:** Interactive communication involves real-time two-way exchange between parties. An email report is asynchronous and one-directional — the sponsor receives it but no real-time dialogue occurs as part of the transmission.
- **Why D is incorrect:** Passive communication is not a standard PMI communication method classification. The three recognized methods are push, pull, and interactive. Passive is a distractor term not found in the framework.

---

## Question 8

A project stakeholder has been identified as Resistant. Which approach is most likely to move this stakeholder toward a Supportive engagement level?

- A) Send more frequent status reports to keep the stakeholder better informed
- B) Remove the stakeholder from communication lists to avoid conflict escalation
- C) Engage the stakeholder in direct conversation to understand the source of their resistance and address it specifically
- D) Escalate the resistance to the project sponsor and request that they be overruled

**Correct Answer: C**

Resistance typically stems from a specific concern — fear of change, past negative experience, competing priorities, or distrust. The most effective path to moving a resistant stakeholder toward supportive is direct conversation using active listening to understand and address the specific source of resistance.

Distractor Analysis:

- **Why C is correct:** Resistant stakeholders are not simply uninformed — they have a specific reason for opposing the project. Identifying and addressing that reason through direct engagement is the only reliable path to changing their position. More reports or emails to a resistant stakeholder typically reinforce the resistance.
- **Why A is incorrect:** Sending more status reports is an information strategy, not an engagement strategy. A resistant stakeholder who receives more information they did not ask for may become more resistant, not less. Information overload does not address the root cause of resistance.
- **Why B is incorrect:** Removing a resistant stakeholder from communication is a serious error. A high-power resistant stakeholder who is also uninformed is a severe project threat. Communication should increase, not decrease, when resistance is identified — but it should be targeted conversation, not mass reporting.
- **Why D is incorrect:** Escalating a resistant stakeholder to be overruled does not change their position — it typically deepens it. Bypassing a stakeholder's concerns creates lasting organizational conflict and may generate additional resistant stakeholders among their allies.

---

## Question 9

The project team is meeting to review progress, address current issues, review the top three open risks, and confirm action item assignments for the next two weeks. What type of meeting is this?

- A) Kickoff meeting
- B) Lessons learned meeting
- C) Change control board meeting
- D) Status meeting

**Correct Answer: D**

A status meeting is a regular, recurring project review covering progress against plan, current issues, risks, and action item assignments. It is the standard operational meeting for ongoing project monitoring.

Distractor Analysis:

- **Why D is correct:** The described activities — progress review, issue discussion, risk review, and action item assignment — are the exact components of a standard project status meeting. Status meetings recur on a regular schedule (weekly, biweekly) throughout the project.
- **Why A is incorrect:** A kickoff meeting occurs once, at the formal start of the project or phase. It introduces the team, reviews the charter, and establishes norms. It does not review ongoing progress, current issues, or recurring risk updates.
- **Why B is incorrect:** A lessons learned meeting is conducted at project close (or phase gate) to capture retrospective knowledge. It is backward-looking, not a recurring operational review of current project status.
- **Why C is incorrect:** A change control board meeting is convened specifically to evaluate and decide on submitted change requests. It does not cover general project progress, issues, or risk review unless a change request is directly tied to those items.

---

## Question 10

During encoding of a project status message, the project manager uses highly technical terminology when writing to non-technical business stakeholders. Several stakeholders later report they did not understand the message and took no action on the requested decision. Which communication model component is responsible for this failure?

- A) Channel selection — the PM chose the wrong transmission method
- B) Feedback — the stakeholders did not respond promptly
- C) Encoding — the PM converted the message using language inappropriate for the receiver's context
- D) Noise — external interference disrupted the message transmission

**Correct Answer: C**

Encoding is the process of converting thoughts into a transmittable message — selecting words, format, and detail level. When the sender uses language the receiver cannot interpret correctly, the encoding process has failed regardless of how well the channel or transmission worked.

Distractor Analysis:

- **Why C is correct:** The message was successfully transmitted and received — stakeholders read it. The failure occurred at encoding: the PM's word choices (technical terminology) were mismatched to the audience's background. Encoding failure occurs when the message is formulated in a way that cannot be accurately decoded by the intended receiver.
- **Why A is incorrect:** Channel selection concerns the medium — email vs. meeting vs. report. The scenario does not indicate the wrong channel was used; it indicates the message content was not accessible. The channel delivered the message; the encoding failed to make it understandable.
- **Why B is incorrect:** The stakeholders did respond — they reported they did not understand. Their feedback (confusion and non-action) is evidence that the communication loop completed but the message was not understood. The root cause is encoding, not feedback failure.
- **Why D is incorrect:** Noise refers to external interference — network outages, distractions, misrouted emails, or environmental disruptions. Technical terminology used intentionally by the sender is an internal encoding decision, not external noise. The sender controlled the word choices.
