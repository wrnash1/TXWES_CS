# Discussion Forum: Module 09 — Process Modeling with BPMN

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Business Process Modeling

---

### Forum Instructions

Post an original response to ONE of the three scenarios below (A, B, or C). Your initial
post must be 175–225 words written in complete sentences. After posting, reply to at least
two classmates whose posts address a different scenario than yours. Each peer reply must be
at least 60 words and must engage substantively with the classmate's argument — not simply
restate or agree.

**Due dates:** Initial post due by Thursday 11:59 PM. Peer replies due by Sunday 11:59 PM.

---

### Scenario A — Gateway Selection

A business analyst is modeling an employee expense reimbursement process. After an expense
report is submitted, the process requires a manager approval for amounts between $100 and
$500, a director approval for amounts over $500, and automatic approval with no human
review for amounts under $100. Additionally, all approved expenses — regardless of approval
path taken — require an audit review before payment is issued.

Respond to this scenario: Identify which BPMN gateway type should be used to split the
flow into the three approval paths, explain why the other gateway types would be incorrect
here, and identify which gateway type should be used to merge the paths before the audit
review. Then describe what would go wrong in the process if a Parallel Gateway were used
for the split instead of the correct gateway type.

---

### Sample Response A

The correct gateway for splitting the three approval paths is an Exclusive Gateway — also
called an XOR gateway — represented by a diamond with an X or an empty diamond with labeled
outgoing conditions. An Exclusive Gateway is appropriate here because exactly one of the
three conditions will be true for any given expense report: the amount is either below $100,
between $100 and $500, or above $500. These conditions are mutually exclusive and
collectively exhaustive, which is precisely the semantic requirement for an Exclusive
Gateway. The analyst should also add a default path to handle edge cases such as an amount
of exactly $500 that might not match either boundary condition cleanly, depending on how the
conditions are written.

For the merge before the audit review, the matching Exclusive Gateway join is also correct.
An Exclusive join continues as soon as any one of the incoming paths arrives — which is
correct here because only one approval path will ever execute per expense report instance.

If a Parallel Gateway were used for the split, all three approval paths would execute
simultaneously for every expense report. A report for $75 would trigger manager approval,
director approval, and automatic approval at the same time. The audit review merge — now a
Parallel join — would wait for all three approval paths to complete before continuing, which
would never happen correctly because manager and director approvers would be reviewing a
report that already auto-approved. The model would describe a fundamentally broken process
rather than the intended business logic.

---

### Peer Reply Guidance for Scenario A

When replying to a classmate's Scenario A post, consider: Did they correctly identify the
Exclusive Gateway and explain the mutually exclusive condition requirement? Did they address
the merge gateway type? Can you identify a scenario where the boundary conditions they
described might leave an edge case unhandled?

---

### Scenario B — As-Is vs. To-Be Process Modeling

A regional bank currently processes personal loan applications through a paper-based
workflow. An applicant fills out a paper form at a branch, a loan officer manually reviews
it, then phones the credit bureau for a verbal credit check, then calls the applicant with
a decision typically 5–7 business days after submission. The bank is implementing a new
loan origination system that will allow online applications, automated credit bureau
queries, and same-day decisions for applications below $25,000.

Respond to this scenario: Explain what value the As-Is model provides before designing the
To-Be model. Identify at least three specific pain points visible in the As-Is process that
the BPMN model would expose, and describe how the To-Be model would address each one.
Then explain one risk the transition to the To-Be model introduces that the bank must plan
for.

---

### Sample Response B

The As-Is model serves a critical analytical function before the To-Be design begins. By
documenting the current process in BPMN, the bank's project team can validate their shared
understanding of how the process actually works — not how management believes it should
work — and identify every inefficiency that the new system must address. Without the As-Is
baseline, the To-Be design risks overlooking embedded manual steps and informal business
rules that have accumulated over years of practice.

Three specific pain points visible in the As-Is BPMN: first, the manual credit bureau phone
call creates a wait state of unknown duration that the loan officer cannot control, appearing
as a Timer Intermediate Event with no guaranteed response time. Second, the 5–7 day decision
cycle is largely consumed by sequential handoffs between applicant, branch, loan officer,
and credit bureau — each lane crossing in the BPMN is a potential delay. Third, the paper
form creates a data transcription risk: if a loan officer misreads handwriting or enters a
value incorrectly, the decision may be based on wrong data.

The To-Be model addresses all three: automated credit queries eliminate the phone wait;
online applications remove paper handoffs; and digital form validation prevents
transcription errors. However, the transition introduces a risk: loan officers who have
discretion in the current process may resist a system that makes automated decisions,
potentially undermining adoption. Change management training must accompany the system
rollout to ensure staff trust and use the new workflow correctly.

---

### Peer Reply Guidance for Scenario B

When replying to a classmate's Scenario B post, consider: Did they identify distinct pain
points or did they describe variations of the same problem multiple times? Is their
transition risk specific to this scenario or generic to all system implementations? Can you
suggest an additional risk or mitigation they did not consider?

---

### Scenario C — Swimlane Design Decisions

A business analyst is modeling a hospital patient discharge process. The process involves
activities performed by the patient, the attending physician, the nursing staff, the
pharmacy, the billing department, and the hospital's Electronic Health Record (EHR) system.
A colleague suggests putting all activities into a single pool with six lanes. Another
colleague argues that the EHR system and the hospital should be separate pools with message
flows between them.

Respond to this scenario: Explain the criteria for deciding whether to use one pool with
multiple lanes or multiple pools with message flows. Apply those criteria to this specific
scenario to recommend a pool/lane structure. Identify one practical consequence of using
the wrong structure — either over-splitting into too many pools or collapsing everything
into one pool — and explain how it would mislead readers of the diagram.

---

### Sample Response C

The decision between one pool with multiple lanes versus multiple pools with message flows
depends on whether the participants are internal to the same organizational process or are
autonomous external participants exchanging formal communications. A single pool with lanes
is appropriate when all participants share the same process instance and operate under the
same organizational authority. Separate pools are appropriate when participants are
independent organizations or systems that communicate via formal messages — and when the
interaction between them is explicitly what the model needs to show.

For the hospital discharge scenario, I recommend one pool labeled "Hospital Discharge
Process" with five lanes: Patient, Attending Physician, Nursing Staff, Pharmacy, and
Billing. The EHR system should be modeled as a lane within the same pool — labeled EHR
System — rather than as a separate pool, because the EHR is an internal hospital system
directly controlled by the same organization executing the process. Sequence flow between
the EHR lane and other hospital lanes correctly models internal system interactions.

If the team over-splits by making the EHR a separate pool, every internal EHR interaction
becomes a message flow — a dashed cross-pool arrow — which implies a formal inter-
organizational communication protocol. This would mislead readers into thinking the hospital
and its own EHR system have a contractual message-exchange relationship, like an external
vendor API. Conversely, collapsing all six roles into one flat pool with no lane division
would eliminate the visibility of handoffs between roles — the very information most useful
for identifying bottlenecks in a discharge process where nursing, pharmacy, and billing
handoffs are known delay points.

---

### Peer Reply Guidance for Scenario C

When replying to a classmate's Scenario C post, consider: Did they apply the
internal-versus-external criterion correctly? Do you agree that the EHR should be a lane
rather than a separate pool, or can you argue the other way? Did they identify a consequence
specific to the hospital domain or a generic BPMN abstraction?

---

### Discussion Rubric

| Criterion | Excellent (10) | Proficient (7) | Developing (4) | Beginning (1) |
|---|---|---|---|---|
| Accuracy of BPMN concepts | All elements and rules correctly applied | Minor error in one element | One significant conceptual error | Multiple errors or missing core concept |
| Depth of analysis | Explains reasoning and consequences; goes beyond surface description | Some analytical depth | Mostly descriptive | Restates the scenario with no analysis |
| Word count and completeness | 175–225 words; all required elements addressed | 150–175 words; most elements present | Under 150 words; missing one element | Under 100 words or missing a major element |
| Peer reply quality | Engages substantively with classmate's argument; adds new perspective | Agrees with brief extension | Agreement without substantive engagement | One sentence or off-topic |
| Writing quality | Professional sentences; no spelling or grammar errors | 1–2 minor errors | 3–4 errors affecting clarity | Frequent errors impeding understanding |

---

### Professor Nash Note

For Scenario A: the most common error is choosing an Inclusive Gateway because the problem
mentions "amounts between $100 and $500" and students interpret "between" as potentially
ambiguous. It is not — the three ranges are mutually exclusive and cover all cases, which
is exactly the Exclusive Gateway condition. Read the boundary conditions carefully before
selecting a gateway type. For Scenarios B and C: I am looking for domain-specific reasoning
tied to the library or hospital context, not generic statements about BPMN. Apply the
concepts to the scenario in concrete, specific terms.

---

*Discussion Forum — Module 09 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
