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

---

## Question 11

A BA is facilitating a wireframe review session. A stakeholder says: "I love it —
especially the blue and the font choice. Can we make the header taller and use a rounded
font?" The BA has not yet made any visual design decisions. What does this stakeholder
reaction indicate, and how should the BA respond?

A. The stakeholder is engaged and the BA should immediately update the wireframe to reflect
   the visual preferences

B. The reaction indicates that the wireframe is too high-fidelity — its level of detail is
   triggering design discussions prematurely. The BA should redirect by explaining that
   the session's goal is to confirm structure and workflow, not visual design.

C. The reaction confirms that the wireframe is correctly communicating the final design
   intent, and stakeholder approval is complete

D. The BA should document the visual preferences as confirmed requirements and proceed to
   development

### Distractor Analysis — Question 11

**Correct answer: B**

A wireframe is intentionally low-fidelity and free of color and typography precisely to
prevent the reaction described. If stakeholders are discussing fonts and header height,
the wireframe has crossed into mockup territory or the BA needs to reframe the session
purpose.

**Why A is wrong:** Updating the wireframe to reflect visual preferences conflates
structure validation with visual design approval. These are separate stages. Acting on
visual feedback at the wireframe stage wastes time on decisions that are not ready to
be made.

**Why C is wrong:** Stakeholder enthusiasm about visual details is not the same as
approval of the structural design. The BA cannot consider requirements validated when the
wrong design dimension is being discussed.

**Why D is wrong:** Color and font preferences expressed in a wireframe session are not
confirmed requirements. They are premature design preferences. Documenting them as
requirements would constrain the visual design phase unnecessarily.

---

## Question 12

A BA wants to test whether users can find the password reset function on a portal login
page. Which approach best follows the think-aloud protocol for design validation?

A. Show the participant the login page and ask: "Is the password reset link visible enough?"

B. Tell the participant: "Your goal is to reset your password because you forgot it. Begin
   on this screen and narrate everything you are thinking as you try to complete that goal."

C. Walk the participant through each screen while explaining how each element works, then
   ask if they understood

D. Ask the participant to complete a post-session survey rating the login page on a scale
   of 1 to 10

### Distractor Analysis — Question 12

**Correct answer: B**

This approach gives a goal-based task, invokes the think-aloud protocol ("narrate
everything you are thinking"), and starts the participant at the relevant screen without
directing their attention. It correctly observes behavior rather than soliciting opinions.

**Why A is wrong:** Asking "Is the password reset link visible enough?" is a leading
question that directs the participant's attention to the element under investigation and
biases the response toward a positive answer. It also asks for an opinion rather than
observing behavior.

**Why C is wrong:** Walking the participant through the screen while explaining elements
is a demonstration, not a validation session. It trains the participant on the design
rather than testing whether the design is discoverable.

**Why D is wrong:** A post-session survey rating the login page captures opinions, not
behavior. The think-aloud protocol and task observation are behavioral methods that
produce more reliable findings than self-reported preferences.

---

## Question 13

A BA presents wireframes for a new inventory system to a group of warehouse supervisors.
After the session, one supervisor says: "This looks completely different from our current
system. We'll need to relearn everything." How should the BA classify and respond to this
feedback?

A. Classify as a cosmetic finding — users always resist change and it will resolve after
   training

B. Classify as a requirements gap and investigate whether existing workflows and
   terminology should be incorporated into the new design to reduce the learning curve,
   referencing the "consistency and standards" and "match between system and the real world"
   heuristics

C. Dismiss the feedback — the purpose of a new system is to improve on the old one, not
   to replicate it

D. Classify as out of scope because the wireframe review is a design activity, not a
   requirements activity

### Distractor Analysis — Question 13

**Correct answer: B**

The supervisor's concern maps directly to two Nielsen heuristics: "consistency and
standards" (is the new system consistent with user expectations from prior systems?) and
"match between system and the real world" (does the interface use terminology and
workflows familiar to the users?). These are legitimate requirements concerns that should
be investigated, not dismissed.

**Why A is wrong:** Classifying change resistance as cosmetic under-weights a finding that
could indicate real usability problems. Users who find the new system completely foreign
will make errors, require more training, and may resist adoption — business impacts that
are not cosmetic.

**Why C is wrong:** Improvement and familiarity are not mutually exclusive. The BA should
explore which elements of the old system are worth preserving in the new design and which
genuinely need to change to deliver value.

**Why D is wrong:** Wireframe reviews are a combined design and requirements activity.
Findings about user expectations and domain vocabulary are requirements feedback, not
outside the scope of the session.

---

## Question 14

A project team is building a tax filing portal for individual taxpayers. During an initial
throwaway prototyping session, users are confused by a field labeled "Filing Status Code"
and enter numbers instead of selecting from a dropdown. What type of requirement does this
finding generate, and which Nielsen heuristic does it address?

A. A performance requirement — the dropdown must load within two seconds

B. A functional requirement specifying that the Filing Status Code field must be
   implemented as a dropdown with plain-language labels, addressing the "match between
   system and the real world" heuristic

C. A security requirement — user input must be validated server-side, addressing the
   "error prevention" heuristic

D. A training requirement — users must receive onboarding before using the portal,
   addressing the "help and documentation" heuristic

### Distractor Analysis — Question 14

**Correct answer: B**

The finding reveals that the field name and input mechanism do not match users' mental
model. The correct response is a functional requirement specifying plain-language options
(Married Filing Jointly, Single, etc.) in a dropdown control. This directly addresses the
"match between system and the real world" heuristic.

**Why A is wrong:** Performance requirements address response time, not usability or
labeling. The observed problem is comprehension, not speed.

**Why C is wrong:** Server-side validation is a security concern but is not the primary
finding. The problem is that users do not understand what to enter, not that malicious
input is a risk.

**Why D is wrong:** Requiring training to use a form field is a design failure, not a
solution. The "help and documentation" heuristic acknowledges that documentation should
exist, but it also states that a well-designed system should not need extensive help to
use for basic tasks.

---

## Question 15

Which of the following scenarios describes the most appropriate use of an interactive
prototype rather than a wireframe?

A. A BA needs to confirm with a stakeholder that the dashboard will display account
   summary information in the top left quadrant

B. A BA needs to validate that a multi-step loan application wizard correctly routes
   users through different paths based on their loan type selection, and that users
   can navigate back to correct earlier answers

C. A BA needs to document the placement of the navigation menu for the development team

D. A BA is exploring three possible layouts for a reporting page in a brainstorming session

### Distractor Analysis — Question 15

**Correct answer: B**

Validating conditional routing logic and backward navigation in a multi-step workflow
requires users to actually experience the interaction sequence. A static wireframe cannot
simulate conditional branching — an interactive prototype is the appropriate artifact for
this level of behavioral validation.

**Why A is wrong:** Confirming the position of a section on a dashboard can be achieved
with a wireframe. No interactivity is needed to validate placement.

**Why C is wrong:** Documenting navigation menu placement for developers is a wireframe
task, not an interactive prototype task. Annotated wireframes efficiently communicate
structural specifications.

**Why D is wrong:** Brainstorming layout alternatives is most efficiently done at the
lowest possible fidelity — sketches or rough wireframes. Creating interactive prototypes
for three speculative layouts during brainstorming is far too costly.

---

## Question 16

A BA documents the following finding after a design validation session: "Participant #2
accidentally clicked 'Submit Loan Application' on the draft review screen while trying
to scroll down to read the terms. The application was submitted before the participant
had finished reviewing. Participant expressed frustration." This finding should be
classified as which severity level?

A. Cosmetic — the participant eventually completed the task

B. Minor — the participant was confused but the application was submitted, which is the
   intended outcome

C. Critical — the action was irreversible and occurred before the participant intended
   it, preventing completion of the review task

D. Major — the participant was frustrated but the system functioned as designed

### Distractor Analysis — Question 16

**Correct answer: C**

An irreversible action triggered accidentally before the user intended it is a critical
finding. The participant could not complete the review task (the actual goal) before
the form was submitted. This represents a task completion failure caused by the design,
which maps directly to the "error prevention" heuristic. The design must be changed
before development.

**Why A is wrong:** A finding is not cosmetic simply because the participant eventually
reached an end state. The participant completed the wrong action at the wrong time — a
design failure with real consequences for loan applicants.

**Why B is wrong:** The participant's intent was to review the application, not to submit
it. An accidental irreversible submission is not a successful task completion. Classifying
this as minor ignores the business impact of an unintended loan application submission.

**Why D is wrong:** The system functioning as designed is irrelevant to severity
classification. The finding evaluates whether the design produces the correct user
experience, not whether the code executes correctly.

---

## Question 17

The "recognition rather than recall" heuristic states that users should be able to
identify options and actions by recognizing them, rather than having to remember them
from prior experience. Which of the following interface features best applies this
heuristic?

A. A blank text field where users type command names to execute actions

B. An error message that reads "Error 403 — operation not permitted"

C. A dropdown menu listing all available report types with descriptive labels so users
   do not need to remember report names

D. A help tooltip that appears only when users hover over an icon for two seconds

### Distractor Analysis — Question 17

**Correct answer: C**

Presenting all available options in a visible dropdown with descriptive labels allows
users to recognize the correct choice rather than recall report names from memory. This
is the canonical application of the recognition over recall heuristic.

**Why A is wrong:** Requiring users to type command names demands recall — users must
remember the exact command syntax. This is the opposite of the recognition heuristic.

**Why B is wrong:** "Error 403" is a technical code requiring users to recall or look up
its meaning. This violates both "match between system and the real world" (technical
language) and "help users recognize, diagnose, and recover from errors" (unhelpful
message).

**Why D is wrong:** A tooltip visible only on hover after a delay is a recall mechanism
in disguise — users must remember that hovering reveals help, and must wait to access
it. Visible, always-present labels better support recognition.

---

## Question 18

A BA is debating whether to use a throwaway prototype or begin evolutionary development
immediately for a new patient intake form. The requirements are well-understood, the
technology stack is mature and familiar to the team, and stakeholders are available for
weekly reviews. Which strategy is most appropriate, and why?

A. Throwaway — because patient data is sensitive and the prototype must be discarded to
   protect privacy

B. Throwaway — because the requirements are well-understood and the team needs to explore
   alternatives before committing

C. Evolutionary — because the conditions favor directly building the system incrementally
   with continuous stakeholder feedback, reducing wasted effort

D. Evolutionary — because the agile methodology requires evolutionary prototyping by
   definition

### Distractor Analysis — Question 18

**Correct answer: C**

When requirements are well-understood, the technology stack is mature, and stakeholders
are available for frequent reviews, the conditions for evolutionary prototyping are ideal.
Throwaway prototyping would waste effort on artifacts that will be discarded when the
team has enough certainty to build directly.

**Why A is wrong:** Data privacy is handled through access controls and security
requirements, not by choosing throwaway over evolutionary prototyping. This reasoning
conflates two unrelated concerns.

**Why B is wrong:** Throwaway prototyping is most valuable when requirements are uncertain
and exploration is needed. Well-understood requirements do not call for exploration;
they call for building.

**Why D is wrong:** Agile methodology supports evolutionary prototyping but does not
require it exclusively. Throwaway prototyping can also be used within agile to resolve
specific uncertainties in a sprint backlog.

---

## Question 19

A BA completes a design validation session and prepares a findings report for the project
sponsor. The report lists 12 findings: 2 critical, 3 major, 5 minor, and 2 cosmetic.
The project sponsor asks: "Can we just fix the critical ones and go to development?" The
BA's most professionally appropriate response is which of the following?

A. "Yes — critical findings are the only ones that block development."

B. "No — all 12 findings must be resolved before development can begin, per the BABOK
   Guide."

C. "The critical findings must be resolved before development begins. I recommend
   addressing the major findings as well, because they cause significant task difficulty
   and will likely create defects or change requests after go-live. The minor and cosmetic
   findings can be deferred to a subsequent release."

D. "Yes — if you approve proceeding, we will document the remaining findings as known
   limitations."

### Distractor Analysis — Question 19

**Correct answer: C**

This response correctly applies the severity classification framework. Critical findings
must be resolved. Major findings should be resolved before development because they are
likely to generate costly change requests or defects later. Minor and cosmetic findings
can be deferred. The response also manages the sponsor relationship professionally without
simply agreeing to lower standards.

**Why A is wrong:** Ignoring major findings before development is a risk the BA should
not accept without clearly communicating the likely consequences. Major findings cause
significant user difficulty — deferring them is a documented business risk, not a neutral
decision.

**Why B is wrong:** The BABOK Guide does not mandate that all findings be resolved before
development. Severity classification exists precisely to allow rational prioritization.
This response is too rigid and not supported by professional standards.

**Why D is wrong:** While documenting known limitations is sometimes appropriate, agreeing
without analysis or recommendation fails the BA's obligation to provide professional
guidance. The BA should advise on the implications of proceeding with open major findings.

---

## Question 20

According to the BABOK Guide, which of the following statements most accurately describes
the relationship between prototyping and requirements elicitation?

A. Prototyping replaces written requirements — once stakeholders approve a prototype, no
   further documentation is needed

B. Prototyping is an elicitation technique that can surface latent requirements and
   resolve conflicts between stakeholder interpretations, complementing other elicitation
   methods

C. Prototyping is only used during the design phase and has no role in requirements
   elicitation

D. Prototyping is a testing activity that confirms requirements have been implemented
   correctly

### Distractor Analysis — Question 20

**Correct answer: B**

The BABOK Guide explicitly lists Prototyping as a technique in the Elicitation and
Collaboration knowledge area. Prototypes surface latent requirements that stakeholders
could not articulate without a visual stimulus and resolve ambiguities between conflicting
interpretations. They complement — not replace — other elicitation methods.

**Why A is wrong:** Prototype approval does not constitute a requirements baseline.
Prototypes are visual aids; requirements documentation captures the full behavioral,
performance, and constraint specifications that developers need. Prototypes are
insufficient substitutes.

**Why C is wrong:** This directly contradicts the BABOK Guide, which lists Prototyping
under Elicitation and Collaboration in addition to Requirements Analysis and Design
Definition. Prototyping occurs across multiple stages of the BA workflow.

**Why D is wrong:** Testing confirms that the built system matches requirements — it is
a verification activity. Prototyping is a requirements and design activity that occurs
before building begins. Conflating the two misrepresents both techniques.

---

*Module 13 Quiz (extended) | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
