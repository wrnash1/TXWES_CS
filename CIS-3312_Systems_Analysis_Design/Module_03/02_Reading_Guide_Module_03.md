# Reading Guide: Module 03 - Requirements Elicitation Techniques

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Module 03 covers BABOK Guide v3 Knowledge Area 4: Elicitation and Collaboration. Elicitation is the practice of drawing information out of stakeholders and other sources to understand their needs, constraints, and the context of the business problem. This module is among the most heavily tested on the ECBA exam because it covers the core human-interaction skill of the BA role.

The techniques you choose depend on the type of information you need, the number and availability of stakeholders, and the project approach. Mastering a variety of elicitation techniques — and knowing when each one is and is not appropriate — is essential for both the certification exam and professional practice.

---

## 1. Core Vocabulary

### 1.1 Elicitation

Elicitation is the deliberate process of identifying and collecting information about stakeholder needs, current processes, constraints, and desired outcomes. Unlike passively receiving information, elicitation is an active, structured activity. It aims to uncover both stated needs (what stakeholders explicitly say they want) and unstated needs (what stakeholders assume without articulating). Unstated needs are especially dangerous because they are the most common source of missed requirements.

### 1.2 Structured vs. Unstructured Interview

A structured interview follows a pre-planned question list in a fixed order, producing consistent, comparable data across multiple stakeholders. An unstructured interview is conversational — the BA guides the discussion but follows interesting threads as they emerge. Unstructured interviews are better for exploratory early-stage work; structured interviews work better when collecting consistent data from many people.

### 1.3 Joint Application Development (JAD) Session

A JAD session is a facilitated, time-boxed workshop that brings multiple stakeholders together — business owners, users, and sometimes developers — to define requirements collaboratively. JAD sessions are particularly valuable for resolving conflicting requirements through real-time negotiation. They originated in IBM's mainframe era but remain a widely used requirements technique.

### 1.4 Tacit Knowledge

Tacit knowledge is knowledge that people hold implicitly — the skills, habits, and procedures they perform without consciously thinking about them or being able to easily articulate them verbally. Experienced workers often have extensive tacit knowledge about how to do their jobs. Observation is the primary technique for capturing tacit knowledge because workers demonstrate what they cannot describe.

### 1.5 Prototyping

Prototyping creates a preliminary model of the proposed system — from a hand-drawn paper sketch to a clickable digital wireframe — to give stakeholders something concrete to respond to. Because stakeholders often struggle to describe abstract requirements but can readily critique something they can see and interact with, prototyping is highly effective at surfacing unstated requirements and resolving ambiguities.

### 1.6 Confirmed vs. Unconfirmed Elicitation Results

BABOK distinguishes between raw elicitation output (notes, recordings, sketches captured during sessions — unconfirmed) and confirmed elicitation results (information reviewed with and validated by the stakeholders who provided it). The confirmation step is a named BABOK task and is mandatory before treating captured information as requirements input.

---

## 2. Elicitation Technique Reference Table

| Technique | Best Used When | Limitation | BABOK Notes |
|---|---|---|---|
| Interview (structured) | Consistent data needed from many stakeholders | Time-intensive; stakeholders may describe ideal, not real, process | Most widely used BA technique |
| Interview (unstructured) | Exploring new problem areas; early discovery | Difficult to compare across stakeholders | Good for early-stage exploration |
| Facilitated Workshop / JAD | Consensus needed across multiple stakeholders | Dominant voices can suppress others; requires skilled facilitation | Most efficient for cross-functional alignment |
| Survey / Questionnaire | Large, dispersed stakeholder groups; quantitative data needed | Shallow; cannot follow up on responses | Best for breadth, not depth |
| Observation | Tacit knowledge; undocumented workarounds; process verification | Hawthorne effect — people may behave differently when watched | Active or passive modes |
| Document Analysis | Existing system understanding; preparation for interviews | Documents may be outdated or describe intended, not actual, process | Non-intrusive; good preparation step |
| Prototyping | Stakeholders struggle to articulate abstract requirements | Risk of anchoring — stakeholders may resist changes to the prototype | Iterative; common in Agile contexts |
| Focus Group | User attitudes, priorities, satisfaction with existing systems | Group dynamics can lead to conformity bias | 6–12 participants; discussion, not consensus |
| Brainstorming | Generating options; early ideation; risk identification | Ideas require evaluation and filtering | No criticism during generation |

---

## 3. Elicitation Preparation

Before conducting any elicitation session, the BA should prepare by:

- Reviewing any existing documentation (previous requirements, current-system manuals, process flowcharts)
- Identifying the right stakeholders for the session and confirming their availability
- Deciding which technique is most appropriate for the information needed
- Preparing a session guide — questions for interviews, agenda for workshops
- Scheduling the session with adequate time and a quiet, distraction-free environment

Preparation quality directly affects elicitation quality. A BA who arrives at an interview with no questions wastes the stakeholder's time and returns with shallow, unstructured information.

---

## 4. The Five Tasks of BABOK KA 4

| Task | Purpose |
|---|---|
| Prepare for Elicitation | Plan the session, gather background material, confirm stakeholders |
| Conduct Elicitation | Execute the selected technique and capture the raw output |
| Confirm Elicitation Results | Review captured information with stakeholders to verify accuracy |
| Communicate Business Analysis Information | Package and share confirmed information with the project team |
| Manage Stakeholder Collaboration | Facilitate ongoing communication and resolve conflicts |

---

## 5. Elicitation vs. Requirements Analysis

A critical distinction tested on the ECBA exam:

- Elicitation (KA 4) = gathering raw information from stakeholders
- Requirements Analysis (KA 5) = interpreting, structuring, and validating that information into well-formed requirements

The confirmation task in KA 4 bridges these two: once elicitation results are confirmed with stakeholders, they are ready to be analyzed and structured into formal requirements in KA 5.

---

## 6. SDLC Phase and KA 4 Alignment

Elicitation is most intensive during the Systems Analysis phase of the SDLC, but it is not limited to that phase:

- Planning phase: Initial elicitation of high-level business needs to support feasibility
- Analysis phase: Full requirements elicitation from all identified stakeholders
- Design phase: Elicitation of design constraints and technical preferences
- Implementation phase: Elicitation of test scenarios for UAT
- Maintenance phase: Elicitation of change requests and enhancement needs

---

## 7. Common Elicitation Mistakes

- Eliciting only from the most available stakeholders rather than the most knowledgeable
- Treating a stakeholder's preferred solution as a requirement (confusing solution with need)
- Moving directly to analysis without confirming elicitation results with stakeholders
- Using only one technique when the problem domain requires multiple approaches
- Failing to capture what was not said — notable absences, assumptions, and constraints

---

## 8. Certification Exam Tips

1. The most frequently tested question type in KA 4 presents a scenario and asks which elicitation technique is most appropriate. The critical matching rules are: tacit knowledge or undocumented workarounds → Observation; consensus from multiple stakeholders → Workshop; large dispersed audience → Survey; cannot articulate abstract needs → Prototyping; current system understanding → Document Analysis.

2. The distinction between structured and unstructured interviews is tested. Structured = consistent data collection; unstructured = exploratory discovery. Know which to use and why.

3. "Confirm Elicitation Results" is a named BABOK task and appears on the exam. After elicitation activities are complete, the BA confirms results with stakeholders before moving to analysis — this is not optional.

4. JAD sessions (Joint Application Development) are the same as facilitated workshops in BABOK. Both names appear on exam questions — treat them as equivalent.

5. The Hawthorne Effect — the tendency for people to change their behavior when they know they are being observed — is a limitation of observation as an elicitation technique. Know this term.

6. Document analysis is a preparation technique, not a replacement for stakeholder interviews. Documents describe the intended process; observation and interviews reveal the actual process.

7. Focus groups are for gathering opinions and attitudes, not for reaching consensus on requirements. If the goal is consensus, use a workshop. If the goal is understanding user sentiment, use a focus group.

8. The ECBA exam will present scenarios where a BA has completed elicitation and asks "what should the BA do next?" The answer is always "confirm the results with stakeholders" — not "begin writing requirements" or "move to design."

---

## 9. Required and Supplemental Reading

Required reading:

- BABOK Guide v3, Knowledge Area 4: Elicitation and Collaboration — all five tasks, inputs, outputs, and techniques
- BABOK Guide v3, Chapter 10 (Techniques) — review: Interviews, Workshops, Observation, Document Analysis, Prototyping, Brainstorming, Focus Groups, Surveys/Questionnaires

Supplemental reading:

- Any systems analysis textbook chapter covering requirements elicitation (Satzinger, Dennis/Wixom, or Valacich/George are all solid references)
- iiba.org — ECBA exam blueprint weighting for KA 4

---

## 10. Study Checklist

- [ ] List all eight elicitation techniques from memory with a one-line description of each.
- [ ] For each technique, write one scenario where it is the best choice and one where it is not appropriate.
- [ ] Define tacit knowledge and explain why observation is the primary technique for capturing it.
- [ ] Explain the difference between confirmed and unconfirmed elicitation results.
- [ ] Read BABOK Guide v3 KA 4 (all five tasks).
- [ ] Watch the Module 03 video lecture.
- [ ] Complete the Module 03 lab activity.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.
