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

---

## Question 11

A project manager is planning a kickoff meeting for a new IT infrastructure rollout. Which statement BEST describes the purpose of the project kickoff meeting?

- A) To present the final project schedule to the sponsor for approval
- B) To formally launch project execution, align all stakeholders on objectives, introduce team members, and establish communication norms
- C) To conduct a retrospective on any lessons learned from similar past projects
- D) To review and baseline the project's risk register before work begins

**Correct Answer:** B) To formally launch project execution, align all stakeholders on objectives, introduce team members, and establish communication norms.

**Distractor Analysis:**

- *Why B is correct:* The kickoff meeting is the formal transition from Planning to Executing. Its purpose is to create shared understanding, introduce the team and their roles, confirm project objectives, and set the tone for how the team will work together.
- *Why A is incorrect:* Schedule approval by the sponsor happens during the Planning Process Group, before the kickoff. The kickoff presumes planning is complete.
- *Why C is incorrect:* Reviewing lessons learned from past projects is part of Planning (consulting OPAs). A kickoff meeting looks forward at the current project, not backward at past ones.
- *Why D is incorrect:* The risk register is baselined during Planning. A kickoff meeting may reference top risks but does not baseline them.

---

## Question 12

A stakeholder has High Power and Low Interest in the project. According to the Power/Interest grid, what is the most appropriate engagement strategy?

- A) Manage closely — involve them in all major decisions
- B) Keep satisfied — provide regular updates and address their concerns but do not overwhelm them with detail
- C) Keep informed — send them routine status reports but require no action from them
- D) Monitor — check in occasionally but devote minimal attention

**Correct Answer:** B) Keep satisfied — provide regular updates and address their concerns but do not overwhelm them with detail.

**Distractor Analysis:**

- *Why B is correct:* High Power / Low Interest stakeholders can significantly impact the project if dissatisfied, but they do not want deep involvement. The PM must keep them satisfied with appropriate-level updates without burdening them with operational detail.
- *Why A is incorrect:* Manage closely is for High Power / High Interest stakeholders who want deep involvement and must be kept fully engaged.
- *Why C is incorrect:* Keep informed is for Low Power / High Interest stakeholders who care about the project but cannot directly influence it.
- *Why D is incorrect:* Monitor is for Low Power / Low Interest stakeholders who have minimal impact and minimal interest — the lightest engagement level.

---

## Question 13

Which statement about the project status report is TRUE?

- A) Status reports should only be sent when there is bad news to report.
- B) A well-structured status report should cover project health, schedule status, budget status, open issues, top risks, and upcoming activities.
- C) Status reports replace the need for status meetings.
- D) Status reports are only required for external stakeholders — internal team members communicate verbally.

**Correct Answer:** B) A well-structured status report should cover project health, schedule status, budget status, open issues, top risks, and upcoming activities.

**Distractor Analysis:**

- *Why B is correct:* A comprehensive status report is a routine communication artifact that gives stakeholders a complete snapshot of project health across all key dimensions. It is a standard PMI artifact within the Communications Management knowledge area.
- *Why A is incorrect:* Status reports are routine — they are sent on a defined schedule regardless of project health. Waiting for bad news defeats the purpose of proactive communication.
- *Why C is incorrect:* Status reports and status meetings serve complementary purposes. Reports provide a written record; meetings allow for discussion, Q&A, and real-time decision-making.
- *Why D is incorrect:* Status reports are typically distributed to all stakeholder groups — both internal and external. Internal team members benefit from written status visibility, especially on complex projects.

---

## Question 14

A project manager adds a new vendor to the project team mid-execution. The original team had 8 members; the vendor adds 3 more. How many new communication channels are created?

- A) 3
- B) 24
- C) 27
- D) 30

**Correct Answer:** C) 27

**Distractor Analysis:**

- *Why C is correct:* Original channels = 8(7)/2 = 28. New total with 11 members = 11(10)/2 = 55. New channels = 55 - 28 = 27.
- *Why A is incorrect:* 3 represents only the vendor members added — not the channels created between the 3 new members and the existing 8, plus channels among the 3 new members themselves.
- *Why B is incorrect:* 24 = 8 × 3 — the product of the original and new member counts, not the combinatorial formula.
- *Why D is incorrect:* 30 does not result from any standard formula using these inputs.

---

## Question 15

According to PMI's stakeholder engagement model, which engagement level describes a stakeholder who is actively promoting the project and working to ensure its success?

- A) Supportive
- B) Neutral
- C) Leading
- D) Resistant

**Correct Answer:** C) Leading

**Distractor Analysis:**

- *Why C is correct:* Leading is the highest engagement level. A Leading stakeholder not only supports the project but actively champions it — advocating for it with other stakeholders, removing obstacles, and taking initiative to help the project succeed.
- *Why A is incorrect:* Supportive describes a stakeholder who backs the project and cooperates with requests, but does not proactively advocate or champion the effort.
- *Why B is incorrect:* Neutral describes a stakeholder who is aware of the project but has no strong positive or negative reaction. They neither help nor hinder.
- *Why D is incorrect:* Resistant describes a stakeholder who opposes the project and may actively work against it.

---

## Question 16

What is the PRIMARY difference between a project kickoff meeting and a project status meeting?

- A) Kickoff meetings are mandatory; status meetings are optional.
- B) Kickoff meetings launch execution and occur once; status meetings are recurring operational reviews during execution.
- C) Status meetings are attended by all stakeholders; kickoff meetings are attended only by the core team.
- D) Kickoff meetings review the risk register; status meetings review the scope baseline.

**Correct Answer:** B) Kickoff meetings launch execution and occur once; status meetings are recurring operational reviews during execution.

**Distractor Analysis:**

- *Why B is correct:* These two meeting types serve fundamentally different purposes. The kickoff is a one-time event that marks the formal start of execution. Status meetings are regular, recurring reviews throughout execution to track progress and make decisions.
- *Why A is incorrect:* Both meeting types are standard project management practice and considered important. Neither is technically "optional" in a well-managed project.
- *Why C is incorrect:* Both meeting types typically involve key stakeholders. Status meetings may be more selective (core team plus sponsor) rather than full-stakeholder gatherings, but the distinction is not who attends.
- *Why D is incorrect:* Risk register review can occur in either meeting type. The distinction is about frequency and purpose, not which artifacts are reviewed.

---

## Question 17

A senior developer on the project team is listed as Consulted (C) in the RACI matrix for the "Define System Architecture" task. What does this mean?

- A) The developer will perform the architecture design work.
- B) The developer will be notified of the final architecture decision after it is made.
- C) The developer's expertise will be solicited before the architecture decision is finalized — two-way communication.
- D) The developer is accountable for the architecture deliverable.

**Correct Answer:** C) The developer's expertise will be solicited before the architecture decision is finalized — two-way communication.

**Distractor Analysis:**

- *Why C is correct:* Consulted (C) means the person's input is actively sought before decisions are made or tasks are completed. It is a two-way, prior communication — the PM asks, the developer responds, and the response shapes the outcome.
- *Why A is incorrect:* Performing the work is the Responsible (R) role, not Consulted.
- *Why B is incorrect:* Being notified after the decision is the Informed (I) role — one-way, after-the-fact communication.
- *Why D is incorrect:* Accountability for the deliverable is the Accountable (A) role — the single person who owns the outcome.

---

## Question 18

A project has 6 team members. The sponsor approves adding 4 additional members. What is the total number of communication channels after the expansion?

- A) 15
- B) 45
- C) 55
- D) 36

**Correct Answer:** B) 45

**Distractor Analysis:**

- *Why B is correct:* New total team size = 6 + 4 = 10. Channels = 10(9)/2 = 45.
- *Why A is incorrect:* 15 = 6(5)/2 — this is the channel count for the original 6-member team before expansion.
- *Why C is incorrect:* 55 = 11(10)/2 — this applies the formula to 11 team members, not 10.
- *Why D is incorrect:* 36 = 9(8)/2 — this uses 9 as the team size rather than 10.

---

## Question 19

A project manager discovers that a key operations manager has moved from "Supportive" to "Resistant" on the Stakeholder Engagement Assessment Matrix over the past month. What is the MOST appropriate first action?

- A) Remove the operations manager from the stakeholder register since they are now a risk.
- B) Send the operations manager a detailed status report to provide more information.
- C) Schedule a one-on-one conversation to understand the root cause of the shift in engagement and address the underlying concern.
- D) Escalate to the project sponsor to have the operations manager's authority reduced.

**Correct Answer:** C) Schedule a one-on-one conversation to understand the root cause of the shift in engagement and address the underlying concern.

**Distractor Analysis:**

- *Why C is correct:* A shift from Supportive to Resistant signals an unaddressed concern. The PM's most effective response is direct engagement — understanding why the stakeholder changed position and addressing the root cause. More information (emails/reports) will not fix a trust or concern issue.
- *Why A is incorrect:* Removing a stakeholder from the register because they are resistant is exactly the wrong response. Resistant stakeholders need more engagement, not less. Removing them creates a blind spot.
- *Why B is incorrect:* Sending more status reports addresses information gaps, not engagement resistance. If the shift is due to a concern (e.g., scope impact on their department), more data will not resolve it.
- *Why D is incorrect:* Escalating to reduce the stakeholder's authority is an adversarial approach that will deepen resistance and damage relationships — a last resort, not a first step.

---

## Question 20

Which component of the PMI sender-receiver communication model ensures that the message was understood as intended?

- A) Encoding
- B) Channel
- C) Decoding
- D) Feedback

**Correct Answer:** D) Feedback

**Distractor Analysis:**

- *Why D is correct:* Feedback closes the communication loop. It is the receiver's response that confirms to the sender that the message was received and understood correctly. Without feedback, the sender cannot verify comprehension.
- *Why A is incorrect:* Encoding is how the sender converts a thought into a message (word choice, format, detail level). It initiates communication but does not confirm understanding.
- *Why B is incorrect:* The channel is the medium through which the message travels (email, meeting, report). It transmits the message but does not confirm receipt or comprehension.
- *Why C is incorrect:* Decoding is how the receiver interprets the message. It is the receiver's internal process — the sender cannot observe it. Feedback is the observable signal that tells the sender decoding was successful.
