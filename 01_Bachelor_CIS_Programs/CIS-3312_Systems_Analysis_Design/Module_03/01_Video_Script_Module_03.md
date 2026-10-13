# Video Script: Module 03 - Requirements Elicitation Techniques

**Course:** CIS-3312 Systems Analysis and Design
**Estimated Duration:** 23 minutes
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.
- Speaker notes in italics are delivery reminders, not spoken aloud.

---

## Section 1: Welcome and Module Overview [00:00 - 03:30]

Welcome to Module 03. I am Professor Nash, and today we are moving from planning into action. This module covers Requirements Elicitation Techniques, which maps to BABOK Knowledge Area 4: Elicitation and Collaboration.

[SHOW DIAGRAM: Title slide — "Module 03: Requirements Elicitation Techniques" with BABOK KA 4 label and IIBA ECBA badge]

Elicitation is where the BA actually gathers information from stakeholders. It is the most visible part of a BA's job — interviews, workshops, document reviews, observing people at work. But there is a lot of nuance here that the ECBA exam tests heavily. Not every technique works in every situation. Choosing the wrong technique wastes time, produces incomplete information, and frustrates stakeholders.

Here is our roadmap for today. We will cover the eight most tested elicitation techniques, when to use each one, and their limitations. We will then discuss the difference between elicitation and confirmation of results — a distinction BABOK makes explicitly. We will close with exam tips and a lab preview.

---

## Section 2: The Eight Core Elicitation Techniques [03:30 - 13:30]

[SHOW DIAGRAM: Eight-cell grid with one technique per cell — Interview, Workshop, Survey/Questionnaire, Observation, Document Analysis, Prototyping, Focus Group, Brainstorming — each with a one-line description and a best-use icon]

Let me walk through each technique.

Interviews are the BA's most fundamental tool. A structured interview follows a pre-planned set of questions in a fixed order — good for collecting consistent data across many stakeholders. An unstructured interview is more conversational — good for exploring new topics or complex processes where you do not yet know what questions to ask. The risk with interviews is that stakeholders sometimes describe how things should work rather than how they actually work. Always follow up by asking "Can you walk me through a specific recent example?"

Facilitated workshops bring multiple stakeholders together in the same room — or virtual session — to elicit, discuss, and reach consensus on requirements simultaneously. JAD sessions (Joint Application Development) are a specific workshop format used in traditional SDLC contexts. The advantage is efficiency: in a two-day workshop you can accomplish what might take weeks of individual interviews. The risk is group dynamics — dominant personalities can suppress quieter stakeholders' input. The BA must actively facilitate to ensure all voices are heard.

Surveys and questionnaires are the right tool when you need input from a large number of geographically dispersed stakeholders and need consistent, quantifiable data. They are efficient but shallow — you cannot follow up on interesting responses the way you can in an interview. Always pilot test your survey with two or three stakeholders before distributing widely.

Observation — also called job shadowing or ethnographic study — is the technique of watching stakeholders perform their actual work rather than asking them to describe it. This is the most powerful technique for capturing tacit knowledge: the undocumented workarounds, the mental shortcuts, and the informal communication patterns that stakeholders cannot easily articulate in an interview. Active observation includes asking questions while watching; passive observation records without interrupting.

> IIBA ECBA Exam Tip: Observation is the correct answer any time a scenario describes stakeholders who cannot verbally describe their own processes, rely on undocumented workarounds, or whose stated process differs from their actual process. It is also appropriate when existing documentation is known to be outdated.

Document analysis reviews existing artifacts — process manuals, user guides, reports, contracts, sample forms, and old system specifications — to extract information about the current state. It is a low-cost, non-disruptive technique that works well as preparation before interviews. Its limitation is that documents may be outdated, incomplete, or describe the intended process rather than the actual one.

Prototyping involves creating a working or simulated version of the system — even a paper sketch — to elicit feedback. When stakeholders see a concrete representation, they often articulate requirements they could not express abstractly. The risk is anchoring — stakeholders may assume the prototype represents final decisions and resist changes later. Always clarify with stakeholders upfront that a prototype is a thinking tool, not a commitment.

Focus groups gather a small, carefully selected group of stakeholders (typically 6–12) to share opinions, reactions, and experiences about a topic. They are particularly useful for understanding user attitudes, priorities, and satisfaction with existing systems. They differ from workshops in that their goal is information gathering through discussion, not consensus building or requirement definition.

Brainstorming is a structured creativity technique used to generate a large volume of ideas quickly. It works best in the early stages of a project to generate solution options or identify risk areas. Ground rules — no criticism during idea generation, all ideas are recorded — are essential to prevent premature judgment from shutting down creative input.

---

## Section 3: Choosing the Right Technique [13:30 - 17:30]

Choosing the right technique depends on four factors: the nature of the knowledge you need to capture, the number and availability of stakeholders, the budget and timeline, and the current stage of the project.

[SHOW DIAGRAM: Technique Selection Matrix — rows: Interview, Workshop, Survey, Observation, Document Analysis, Prototyping, Focus Group, Brainstorming; columns: Best for Tacit Knowledge, Best for Large Groups, Best for Consensus, Best for Early Exploration; cells with checkmarks where applicable]

For deep, complex knowledge from a small number of expert stakeholders, use interviews. For cross-departmental consensus on shared requirements, use workshops. For broad input from hundreds of people, use surveys. For undocumented procedural or tacit knowledge, use observation. For understanding the current state without interrupting stakeholders, start with document analysis as preparation.

One important point: elicitation techniques are rarely used in isolation. A professional BA will typically start with document analysis and a few exploratory interviews, then use a workshop to reach consensus, then use surveys to validate findings with a broader audience, and finally use observation to confirm that documented processes match actual practice.

---

## Section 4: Elicitation vs. Confirmation of Results [17:30 - 20:30]

BABOK KA 4 contains two distinct stages: elicitation activities and confirmation of elicitation results.

[SHOW DIAGRAM: Two-step process diagram — Step 1 box: "Conduct Elicitation" with output arrow to "Raw Elicitation Output (notes, recordings, sketches)"; Step 2 box: "Confirm Elicitation Results" with output arrow to "Confirmed Elicitation Results (stakeholder-validated)"]

Raw elicitation output — interview notes, workshop whiteboards, observation field notes — is not the same as confirmed requirements. The BA must go back to stakeholders and verify that the captured information accurately represents what they communicated. This confirmation step catches two types of errors: BA misunderstandings (the BA misinterpreted what the stakeholder said) and stakeholder recollection gaps (a detail was missed or mis-stated during the session).

Both types introduce defects into requirements if not caught here. A defect found during requirements review costs a fraction of the cost of a defect found during testing or after deployment.

> IIBA ECBA Exam Tip: When a BABOK question asks what the BA should do after completing elicitation activities, the answer is always "confirm elicitation results with stakeholders" before moving to requirements analysis. This is a named, mandatory task in BABOK KA 4 — not optional.

---

## Section 5: Lab Preview and Closing [20:30 - 23:00]

This week's lab gives you a realistic elicitation planning scenario. You will be given a project case study and asked to select the most appropriate technique for six different information-gathering situations, justify each choice, and write five interview questions for one of the stakeholders.

Three closing exam reminders. First: know all eight techniques and be able to match each to the scenario that calls for it. Second: observation is the go-to answer for tacit knowledge and undocumented processes. Third: confirmation of elicitation results is a required step before analysis begins — never skip it on an exam question.

Study BABOK Guide v3 KA 4 carefully. Visit iiba.org to review the ECBA exam blueprint — KA 4 is one of the most heavily weighted areas on the exam.

---

## End Card

## Module 03 Complete

Next: Module 04 - Requirements Analysis and Documentation

### Additional Resources

- iiba.org — BABOK Guide v3 KA 4: Elicitation and Collaboration
- iiba.org — ECBA exam blueprint and KA 4 weighting information
