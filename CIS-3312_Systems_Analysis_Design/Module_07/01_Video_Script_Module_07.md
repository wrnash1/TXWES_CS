# Video Script: Module 07 — Requirements Elicitation Techniques

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA
**Estimated Duration:** 22–25 minutes
**Recorded by:** Professor Nash

---

## Production Notes

- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.
- [PAUSE] cues indicate natural break points for student note-taking.

---

## Section 1: Welcome and Module Overview [00:00 - 02:30]

Welcome to Module 07. I am Professor Nash. Today we are covering Requirements Elicitation Techniques — one of the most essential skill sets in business analysis and one of the most heavily tested areas on the IIBA ECBA exam.

[SHOW DIAGRAM: Title slide — "Module 07: Requirements Elicitation Techniques" with BABOK Guide v3 KA 4 label and IIBA ECBA certification badge]

Elicitation is the process of drawing out, discovering, and capturing stakeholder needs and requirements. Notice the word "drawing out" — requirements are rarely handed to you fully formed. They must be surfaced through disciplined techniques that help stakeholders articulate what they need, often including needs they themselves have not yet consciously identified.

BABOK Guide v3 covers elicitation as part of Knowledge Area 4 — Elicitation and Collaboration. The ECBA exam tests both knowledge of elicitation techniques and judgment about when each technique is appropriate. By the end of this module you will be able to: describe nine elicitation techniques, explain when each is most effective, describe the requirements documentation process, and apply stakeholder management principles.

---

## Section 2: Why Elicitation Is Difficult [02:30 - 05:00]

[SHOW DIAGRAM: The requirements iceberg — visible portion above waterline labeled "Stated requirements"; large submerged portion labeled "Unstated needs, tacit knowledge, assumed requirements, contradictions, unknown unknowns"]

Requirements elicitation sounds straightforward: ask people what they need. In practice, it is one of the most challenging activities in any systems project. Here is why.

Stakeholders know their work domain deeply but often cannot articulate the rules and assumptions they follow intuitively. When you ask someone "how does this process work?" they may describe the ideal case but forget to mention the three exception paths they handle every day. This tacit knowledge — embedded in practice but not in documentation — is one of the most important things to surface.

Stakeholders also have different perspectives. What the marketing director needs from a new CRM system is different from what the sales manager needs, which is different from what the IT team can support. These perspectives are not just different — they may actively conflict. The BA's job is to surface these conflicts early, not discover them during user acceptance testing.

Finally, stakeholders sometimes do not know what they want until they see what they do not want. This is why prototyping is one of the most powerful elicitation techniques — it externalizes an idea so stakeholders can react to it concretely.

---

## Section 3: Interview Techniques [05:00 - 09:00]

[SHOW DIAGRAM: Interview types comparison — Structured (fixed question list, consistent across all subjects) vs. Unstructured (open-ended conversation, flexible follow-up) vs. Semi-structured (core questions plus adaptive follow-up)]

Interviews are the most fundamental elicitation technique. A BA meets with a stakeholder — individually or in a small group — to ask questions, listen carefully, and probe for depth and clarity.

### Types of Interviews

**Structured interviews** use a fixed set of questions asked in the same order to every participant. Structured interviews are useful when comparing responses across multiple stakeholders because consistency enables comparison. The risk is that a rigid structure may prevent the natural exploration of unexpected and important topics.

**Unstructured interviews** begin with an open-ended prompt — "Tell me about your current process" — and follow the conversation where it leads. Unstructured interviews are excellent for exploring unknown territory but difficult to compare across participants.

**Semi-structured interviews** are the most common BA approach: a prepared set of core questions ensures key topics are covered, but the interviewer has freedom to probe interesting responses and follow tangential threads.

[PAUSE]

### Effective Interview Techniques

Ask open-ended questions first: "Describe what happens when a customer order arrives." Follow with clarifying probes: "You mentioned an exception — what triggers that?" Use silence strategically — stakeholders often fill silence with important information if the interviewer does not rush to the next question. Record interviews (with permission) or take detailed notes immediately after.

---

## Section 4: Workshops and JAD Sessions [09:00 - 12:00]

[SHOW DIAGRAM: Workshop layout — facilitator at front, stakeholders from multiple departments around a table, visual outputs (whiteboard, sticky notes, wireframes) on the wall, showing cross-functional collaboration]

### Requirements Workshops

A requirements workshop brings multiple stakeholders together in a structured, facilitated session to elicit, discuss, and validate requirements collaboratively. Workshops are especially effective when requirements involve multiple departments or when there is known conflict between stakeholder groups that must be resolved.

The BA in a workshop plays the role of facilitator — managing discussion, keeping the group on track, surfacing and documenting agreements and disagreements, and ensuring that quieter stakeholders are heard alongside dominant voices.

Workshop outputs include: documented requirements, decision logs, issues lists, and agreed definitions.

### Joint Application Development

JAD — Joint Application Development — is a structured workshop methodology developed by IBM for eliciting software requirements collaboratively. A JAD session follows a formal agenda: the sponsor opens by articulating business goals, the facilitator leads working sessions on specific requirement areas, subject matter experts contribute domain knowledge, scribes document all outputs, and a review session closes with participant sign-off on the session's outputs.

JAD sessions produce high stakeholder engagement and rapid consensus because decisions are made with all relevant parties in the room simultaneously. The investment is significant — JAD sessions often run one to three days — but they compress the elicitation timeline by eliminating the back-and-forth of sequential individual interviews.

---

## Section 5: Observation [12:00 - 14:30]

[SHOW DIAGRAM: Observation types — passive observation (BA watches without participating, takes notes) vs. active observation (BA participates in the work alongside subject, asks questions during the process)]

Observation — sometimes called ethnography in academic contexts — involves the BA watching how work is actually performed rather than asking how it is supposed to be performed. This distinction is critical.

People describe their work ideally. They forget about workarounds, exception handling, undocumented steps, and informal communication. Watching someone actually perform their work reveals all of these. The BA who observes a loan processing team for a day will learn more about the actual process than the BA who interviews the team manager for an hour.

**Passive observation** minimizes interference — the BA watches and takes notes without participating or asking questions during the session. Questions are saved for a debrief afterward.

**Active observation** allows the BA to ask questions during the work session. This is useful for immediately clarifying what is being observed but can interrupt the natural flow of work.

[PAUSE]

Observation is the elicitation technique most likely to surface tacit knowledge — the rules and patterns that experienced workers follow automatically without conscious awareness. It is most effective when combined with interviews: observe first, then interview based on what you saw.

---

## Section 6: Document Analysis and Surveys [14:30 - 17:30]

[SHOW DIAGRAM: Document analysis inputs — existing system documentation, process manuals, sample reports, data schemas, regulatory requirements, audit reports — all pointing to BA analysis output: documented existing requirements, constraints, data elements]

### Document Analysis

Document analysis involves reviewing existing artifacts — procedures manuals, system documentation, sample reports, data dictionaries, regulatory requirements, audit findings, organizational charts — to understand the current state and identify requirements for the future state.

Document analysis is particularly valuable for identifying: existing data structures that must be preserved or migrated, regulatory constraints that must be met, process steps that are documented (even if not followed exactly), and terminology that the organization uses.

The limitation of document analysis is that documents describe the intended state, not the actual state. A procedures manual last updated three years ago may not reflect how the process is actually executed today. Document analysis provides a starting point — it must be validated through other techniques.

### Surveys and Questionnaires

Surveys allow the BA to collect requirements input from large numbers of stakeholders efficiently. They are especially useful when the stakeholder population is geographically distributed, when a large volume of input is needed to identify patterns and priorities, or when the questions are well-defined enough to be answered without facilitation.

Survey design is critical. Ambiguous questions produce ambiguous answers. Closed questions (rating scales, yes/no, multiple choice) produce quantifiable results. Open questions produce richer narratives but require qualitative analysis. Most effective surveys combine both types.

The limitation of surveys is that they cannot probe unexpected responses. If a stakeholder checks "Other" or writes an unexpected comment, the BA cannot follow up in the moment. Surveys work best when paired with follow-up interviews with respondents who provided unusual or high-priority answers.

---

## Section 7: Prototyping [17:30 - 19:30]

[SHOW DIAGRAM: Prototyping types — throwaway prototype (paper wireframe or low-fidelity mockup, used to elicit feedback, then discarded) vs. evolutionary prototype (incrementally refined into the actual system)]

A prototype is a partial, preliminary representation of a system that stakeholders can interact with or react to in order to elicit and validate requirements. Prototyping is particularly effective because it concretizes abstract requirements — stakeholders can see and react to a tangible representation rather than responding to verbal or written descriptions.

**Throwaway prototypes** — also called paper prototypes or wireframes — are low-fidelity representations built quickly to generate stakeholder feedback. A wireframe showing a proposed screen layout takes hours to produce and generates concrete, actionable feedback about navigation, field placement, and workflow. The wireframe is then discarded once requirements are captured.

**Evolutionary prototypes** are incrementally refined. Early versions represent core functionality; later versions add detail. Evolutionary prototyping works well in Agile environments where working software is built iteratively with continuous stakeholder feedback.

Prototyping is most effective when stakeholders struggle to articulate requirements in the abstract but can quickly identify what they do and do not want when shown a concrete representation.

---

## Section 8: Requirements Documentation and Stakeholder Management [19:30 - 22:00]

[SHOW DIAGRAM: Requirements documentation hierarchy — Business requirements (why) → Stakeholder requirements (who needs what) → Solution requirements (what the system must do: functional + non-functional) → Transition requirements (how to get from current to future state)]

### Requirements Documentation

Requirements must be documented — verbal agreements are insufficient. A requirements document provides the shared understanding that all project participants — business stakeholders, developers, testers, and management — can reference, verify, and hold each other accountable to.

Requirements documentation must be: clear (no ambiguity), complete (no gaps), consistent (no contradictions), verifiable (testable), and traceable (connected to the business need that motivated them).

Common documentation formats include: Business Requirements Document (BRD), Software Requirements Specification (SRS), User stories (Agile), and Use cases.

### Stakeholder Management

Not all stakeholders are equal in authority, interest, or influence. A stakeholder analysis identifies who is involved, what they care about, how much influence they have, and how much impact the project has on them. This analysis guides the BA's elicitation strategy — high-influence, high-interest stakeholders receive more intensive engagement than low-influence, low-interest observers.

Managing stakeholder expectations is ongoing. Requirements change, priorities shift, and scope evolves. The BA who keeps stakeholders informed and engaged through these changes reduces the risk of late-project surprises.

---

## Section 9: Lab Preview and Closing [22:00 - End]

Three exam reminders. First: know when to use each elicitation technique — the ECBA exam presents scenarios and asks which technique is most appropriate. Second: the distinction between stated, unstated, and tacit requirements is fundamental. Third: requirements documentation must be clear, complete, consistent, verifiable, and traceable.

This week's lab places you in the role of a BA on a university system implementation project. You will plan an elicitation strategy, conduct a mock requirements interview, analyze a provided document, and draft requirements from your findings.

---

## Module 07 Complete

Next: Module 08 — Feasibility Analysis and Cost-Benefit Analysis

### Additional Resources

- iiba.org — BABOK Guide v3 KA 4: Elicitation and Collaboration
- iiba.org — ECBA exam blueprint and study guide
- nngroup.com — User research and interview technique resources
