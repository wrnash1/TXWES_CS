# Quiz: Module 13 — Solution Design and Prototyping

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Quiz Instructions

This quiz contains 10 multiple-choice questions. Each question is worth 10 points. Select the single best answer. Distractor analysis is provided after each question to support your learning.

**Time limit:** 30 minutes

---

## Question 1

A BA is designing a new inventory management system and wants to communicate the layout and placement of interface elements to stakeholders without triggering debates about color schemes and branding. Which artifact is most appropriate?

A. A high-fidelity mockup with full color and typography
B. A wireframe in grayscale showing element placement and labels
C. An interactive prototype with clickable navigation
D. A fully functional throwaway prototype built in the production technology stack

### Distractor Analysis — Question 1

**Correct answer: B**

Wireframes are deliberately low-fidelity and grayscale precisely to keep stakeholder attention on structure and workflow rather than visual design choices. This is their primary purpose.

**Why A is wrong:** A high-fidelity mockup with full color would immediately shift stakeholder focus to visual design preferences rather than layout and workflow validation. This is counterproductive at this stage.

**Why C is wrong:** An interactive prototype adds navigational behavior beyond what is needed to communicate layout. It is higher cost and more than necessary for this purpose.

**Why D is wrong:** A fully functional prototype built in the production stack is extremely expensive and far exceeds the goal of communicating layout. It also risks creating expectations that the prototype is the final system.

---

## Question 2

A development team is using agile methodology with two-week sprints. At the end of each sprint, the product owner and stakeholders review a working increment of the system and provide feedback that shapes the next sprint. This approach to prototyping is best described as which of the following?

A. Throwaway prototyping, because each sprint discards the previous version
B. Evolutionary prototyping, because the working system grows through successive iterations
C. Wireframing, because each sprint produces a new visual design artifact
D. Design validation, because stakeholders review the output and provide feedback

### Distractor Analysis — Question 2

**Correct answer: B**

Evolutionary prototyping builds the system incrementally over iterations, with each version becoming part of the final delivered product. This description matches agile sprint-based delivery exactly.

**Why A is wrong:** Throwaway prototyping produces artifacts that are discarded after use. In agile delivery, the sprint output is never discarded — it becomes part of the growing system.

**Why C is wrong:** Wireframing is a design artifact, not a development strategy. A working increment of software produced in a sprint is not a wireframe.

**Why D is wrong:** Design validation is an activity within the prototyping process, not a prototyping strategy itself. The sprint review includes validation, but the overall approach is evolutionary prototyping.

---

## Question 3

A BA notices that a proposed portal design uses internal database field names as screen labels: "CUST_ACCT_BAL" instead of "Account Balance" and "TXN_DT" instead of "Transaction Date." Which of Nielsen's usability heuristics does this violate?

A. Visibility of system status
B. Error prevention
C. Match between system and the real world
D. Consistency and standards

### Distractor Analysis — Question 3

**Correct answer: C**

"Match between system and the real world" requires that the interface use language and concepts familiar to users, not technical or system-internal terminology. Database field names are a classic violation of this heuristic.

**Why A is wrong:** Visibility of system status is about keeping users informed of what the system is doing — loading states, confirmations, progress indicators. It is not about labeling conventions.

**Why B is wrong:** Error prevention is about designing to avoid user mistakes before they happen. Field naming is a clarity issue, not an error prevention issue.

**Why D is wrong:** Consistency and standards requires the same terms and patterns be used throughout the system. The labels may be consistently wrong (all using database names), which would satisfy consistency while still violating the real-world match heuristic.

---

## Question 4

During requirements elicitation, a BA creates a rough sketch on a whiteboard to explore three different possible layouts for a reporting dashboard. After the meeting, the sketch is photographed but never refined further. What is the primary purpose this artifact served?

A. Evolutionary prototyping — the sketch will be refined into the final design
B. Design validation — the sketch was used to test whether the design meets requirements
C. Low-fidelity throwaway prototyping — the sketch was used to explore options and is now complete
D. Mockup creation — the sketch represents the visual design for stakeholder approval

### Distractor Analysis — Question 4

**Correct answer: C**

A rough sketch created to explore layout options and not refined further is a low-fidelity throwaway prototype. It served its purpose (exploring alternatives) and will not become part of the final design artifact set.

**Why A is wrong:** Evolutionary prototyping means the artifact grows into the final system. A whiteboard sketch that is photographed and set aside does not evolve into anything.

**Why B is wrong:** Design validation is a structured activity involving realistic tasks and behavioral observation. A whiteboard exploration sketch is not a validation session.

**Why D is wrong:** A mockup is a high-fidelity artifact with full visual design applied. A whiteboard sketch is the lowest fidelity artifact possible.

---

## Question 5

A BA is running a design validation session. A participant is trying to find the "submit expense report" function and has been clicking in the wrong area of the screen for 45 seconds. The BA facilitating the session should do which of the following?

A. Immediately point out the correct button to save time
B. Continue observing and note the specific navigation behavior without intervening
C. End the task and move to the next scenario
D. Ask the participant directly: "Did you find the submit button confusing?"

### Distractor Analysis — Question 5

**Correct answer: B**

The participant's struggle is valuable data revealing a navigation problem. The BA should observe and record the specific behavior. Intervening removes the signal that reveals the design flaw.

**Why A is wrong:** Pointing out the correct button eliminates the finding. The 45-second struggle is the data — it shows that the button is not discoverable. Helping the participant hides this problem from the findings log.

**Why C is wrong:** Ending the task prematurely also discards the finding. The participant should be allowed to either complete the task independently or reach a natural stopping point.

**Why D is wrong:** Asking a leading question ("Did you find it confusing?") biases the response. The BA should observe behavior and ask neutral, open-ended follow-up questions after the task, not during.

---

## Question 6

A project sponsor tells the BA: "We need to show the executive committee a demo next week. Can you have the prototype ready?" The BA should clarify which of the following before committing to a deliverable?

A. Whether the prototype should be throwaway or evolutionary
B. What level of fidelity is needed — wireframe, mockup, or interactive prototype
C. Whether the prototype should use Nielsen's heuristics for design
D. Whether the development team will reuse the prototype code

### Distractor Analysis — Question 6

**Correct answer: B**

"Show the executive committee a demo" could mean anything from a click-through mockup to a fully interactive prototype. Before committing to a timeline, the BA must clarify what level of fidelity will satisfy the sponsor's actual need.

**Why A is wrong:** The throwaway vs. evolutionary distinction is about the long-term fate of the prototype, not about what is appropriate for an executive demo. It is a secondary concern at this point.

**Why C is wrong:** Nielsen's heuristics are a design evaluation framework, not a deliverable characteristic. This is not the right clarifying question for this situation.

**Why D is wrong:** Whether development reuses the prototype code is a technical decision for later. The immediate priority is clarifying what the sponsor needs to see.

---

## Question 7

After a design validation session, the BA documents the following finding: "Participant #3 clicked the 'Delete Account' button without reading the confirmation dialog, resulting in a simulated account deletion." The BA classifies this as a critical finding. What design change does this finding most directly call for?

A. Adding a help documentation link to the account management screen
B. Changing the color of the Delete Account button to a less prominent shade
C. Redesigning the confirmation dialog to require active user input (such as typing "DELETE") before the action proceeds
D. Moving the Delete Account button to a separate administration panel

### Distractor Analysis — Question 7

**Correct answer: C**

The finding shows that the confirmation dialog is insufficient — users bypass it without reading. The "error prevention" heuristic calls for a design that makes irreversible actions harder to complete accidentally. Requiring active input (typing a confirmation word) forces deliberate action.

**Why A is wrong:** Adding documentation does not address the interaction problem. Users who ignore confirmation dialogs will also ignore documentation.

**Why B is wrong:** Changing the button color reduces visibility but does not address the real problem: users are clicking through the confirmation without reading it.

**Why D is wrong:** Moving the button is a reasonable secondary option, but it does not address the core problem that when users do reach a destructive action, the confirmation step is not effective.

---

## Question 8

Which of the following best describes the role of annotations in a wireframe?

A. Annotations add color and styling to communicate the visual design intent
B. Annotations describe the behavior of interface elements that cannot be conveyed by the layout alone
C. Annotations replace the need for a separate requirements specification
D. Annotations indicate which parts of the wireframe are optional for development

### Distractor Analysis — Question 8

**Correct answer: B**

Annotations are notes attached to wireframe elements that explain interactive behavior, validation rules, data sources, and other requirements that the static layout cannot communicate. They bridge the wireframe and the requirements document.

**Why A is wrong:** Wireframes deliberately exclude color and styling. Adding those would move the artifact toward a mockup, not an annotated wireframe.

**Why C is wrong:** Annotations complement the requirements specification; they do not replace it. A wireframe with annotations is an analysis artifact, not a complete requirements document.

**Why D is wrong:** Annotations have no standard meaning related to implementation optionality. They document behavior, not development priority.

---

## Question 9

A BA is evaluating two proposals for how to handle a complex insurance claims form with 52 required fields. Proposal A puts all 52 fields on a single scrolling page. Proposal B breaks the form into six themed sections displayed as a step-by-step wizard with a progress indicator and the ability to save a draft and return. Which proposal better reflects Nielsen's usability heuristics, and why?

A. Proposal A, because it gives users all information at once, supporting recognition over recall
B. Proposal A, because consistency requires all form elements to appear in one location
C. Proposal B, because it supports visibility of system status, user control, and error prevention
D. Proposal B, because aesthetic and minimalist design requires fewer fields per screen

### Distractor Analysis — Question 9

**Correct answer: C**

Proposal B addresses three heuristics simultaneously. The progress indicator satisfies visibility of system status. The ability to save and return satisfies user control and freedom. Breaking the form into themed sections reduces cognitive load and the risk of errors from missing fields, satisfying error prevention.

**Why A is wrong:** Recognition over recall is better served by grouping related items clearly — which Proposal B does by theme. A 52-field single page increases cognitive load, which harms usability.

**Why B is wrong:** Consistency applies to using the same patterns throughout a system, not to forcing all form elements onto a single screen. Proposal B can be entirely consistent with the rest of the portal.

**Why D is wrong:** While aesthetic and minimalist design does apply (less is more), the stronger justification for Proposal B is the combination of visibility, user control, and error prevention — not aesthetics alone.

---

## Question 10

According to the BABOK Guide, prototyping as a BA technique appears in which knowledge areas?

A. Business Analysis Planning and Monitoring only
B. Elicitation and Collaboration, and Requirements Analysis and Design Definition
C. Solution Evaluation and Strategy Analysis
D. Requirements Life Cycle Management only

### Distractor Analysis — Question 10

**Correct answer: B**

The BABOK Guide explicitly lists Prototyping as a technique in two knowledge areas: Elicitation and Collaboration (using prototypes to gather requirements from stakeholders) and Requirements Analysis and Design Definition (using prototypes to define, validate, and communicate the solution design).

**Why A is wrong:** Business Analysis Planning and Monitoring covers approach planning, stakeholder analysis, and governance. It does not list prototyping as a technique.

**Why C is wrong:** Solution Evaluation focuses on assessing whether a delivered solution meets business needs. Strategy Analysis focuses on defining the business need and change strategy. Neither lists prototyping as a primary technique.

**Why D is wrong:** Requirements Life Cycle Management covers tracing, maintaining, and approving requirements. While prototypes can inform requirements changes, RLCM is not a knowledge area that lists prototyping as a technique.

---

*Module 13 Quiz | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
