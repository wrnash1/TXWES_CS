# Discussion Forum: Module 14 — Procurement and Contract Management

## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Overview

This discussion forum has three scenarios drawn from real-world IT procurement
situations. For each scenario, post a substantive initial response and reply to at
least one peer per scenario. Responses should demonstrate your understanding of the
procurement concepts from Module 14.

---

## Scenario 1: The Contract Type Dilemma

Northgate Financial Services is upgrading its core banking platform. The project
manager has received two vendor proposals. Vendor Alpha proposes a Firm Fixed Price
contract at $2.1 million with a 14-month delivery timeline. Vendor Beta proposes a
Time and Materials contract at $185/hour for senior engineers with an estimated 9,000
hours (~$1.665M) and a not-to-exceed ceiling of $2.3 million.

The project sponsor strongly prefers Vendor Alpha's FFP because "it protects us from
overruns." However, the business analysts have not yet finalized the requirements for
two of the five integration modules, and the final API specifications from a third-party
payment processor are still pending.

### Initial Post Prompt

Should Northgate accept Vendor Alpha's FFP proposal given the current state of
requirements? Analyze the risk implications for both the buyer and the seller under
each contract type. Recommend a course of action with specific reasoning tied to the
make-or-buy and contract type framework from the module. Your response should be
200–225 words.

### Model Response (200–225 words)

Northgate should not accept the FFP proposal until the requirements are finalized for
all five integration modules and the third-party API specifications are in hand. Committing
to FFP under incomplete requirements transfers an unfair risk to the seller, who will
either price in a large contingency reserve — inflating the contract value — or submit
a low bid and then fight scope disputes throughout execution.

The FFP structure is sound in principle; it does give Northgate cost certainty once
requirements are stable. The sponsor's instinct is not wrong — it is just premature.
The project manager should recommend a phased approach: issue a short T&M contract
for the requirements-definition and API-finalization phase (estimated 600–800 hours),
then reissue an RFP for the implementation phase once requirements are complete and
stable. At that point, an FFP with strong acceptance criteria is entirely appropriate.

Vendor Beta's T&M proposal is better matched to the current state of uncertainty, but
the $2.3M NTE ceiling is only $200K above Vendor Alpha's fixed price — a thin buffer
for a requirements-incomplete implementation. The PM should negotiate a lower NTE
or tighter milestone checkpoints before recommending T&M for the full implementation.

The core principle is this: contract type should follow scope certainty, not preference.
Rushing to FFP with incomplete requirements does not reduce risk — it hides it.

### Peer Response Prompt

Respond to a classmate who reached a different conclusion about whether to accept the
FFP. Do you agree or disagree with their risk assessment? What additional information
would change your recommendation?

---

## Scenario 2: The Vague Statement of Work

A project manager at a regional hospital network issued an RFP for a new patient portal
implementation. The SOW in the RFP states: "The vendor shall implement a patient-facing
web portal that allows patients to view records, schedule appointments, and communicate
with providers. The portal shall be user-friendly and responsive."

The contract was awarded and the vendor delivered a portal six months later. The hospital
is dissatisfied. The portal has no mobile app, no integration with the existing EHR system,
and the secure messaging feature has a 48-hour response window rather than the real-time
chat the clinical staff expected. The vendor maintains they delivered exactly what the SOW
required.

### Initial Post Prompt

Who bears responsibility for this outcome — the hospital, the vendor, or both? Identify
at least three specific weaknesses in the SOW as written and rewrite each weakness as
a strong, measurable acceptance criterion. Discuss what the project manager should have
done differently during procurement planning. Your response should be 200–225 words.

### Model Response (200–225 words)

Responsibility rests primarily with the hospital's project manager. The SOW as written
is severely deficient — it describes desired outcomes in vague, aspirational language
rather than measurable specifications. The vendor delivered a technically compliant
product because the SOW created no enforceable standards.

Three specific weaknesses and stronger rewrites:

First, "user-friendly and responsive" is not measurable. A stronger criterion would be:
"The portal shall render correctly on iOS Safari, Android Chrome, and desktop Chrome and
Firefox, with page load times not exceeding 3 seconds on a standard broadband connection,
verified by automated testing."

Second, EHR integration was not mentioned at all. A stronger deliverable would be:
"The portal shall integrate bidirectionally with the hospital's Epic EHR system via
the HL7 FHIR R4 API, displaying lab results, visit summaries, and medication lists in
real time, with integration verified by a formal test plan."

Third, "communicate with providers" is ambiguous. A stronger standard would be:
"The secure messaging feature shall support real-time in-app messaging with a maximum
provider response time SLA of four business hours, with message delivery confirmed via
read receipt."

The project manager should have convened a requirements workshop with clinical and IT
stakeholders before drafting the SOW, and should have required vendor-proposed
acceptance criteria as part of the RFP response for review and negotiation before award.

### Peer Response Prompt

Your classmate identified different SOW weaknesses than you did. Do their rewrites meet
the standard of being specific, measurable, and testable? Offer one constructive
suggestion to strengthen their rewrite.

---

## Scenario 3: Procurement Closure Under Pressure

Marcus is the project manager for a government IT modernization contract. The vendor
has delivered the final software release. The contract's period of performance ends
in eight days. Marcus has reviewed the deliverables and found three defects: two are
minor cosmetic issues, and one is a functional defect that causes the reporting module
to produce incorrect totals under a specific edge-case condition.

The vendor's project manager calls Marcus and says, "Look, our team is already
reassigned. We need you to sign off on acceptance today so we can issue our final
invoice and close the books. The cosmetic stuff is a known issue — we'll patch it in
the next version."

Marcus's own project sponsor says, "Just sign off. We're out of contract period in
eight days anyway. Legal says we'll lose any leverage we have after that."

### Initial Post Prompt

What should Marcus do? Address the ethics of the sponsor's instruction, the legal
risk of signing acceptance with known defects, and the practical options Marcus has
for the remaining eight days. What procurement closure best practices apply here?
Your response should be 200–225 words.

### Model Response (200–225 words)

Marcus should not sign formal acceptance while a material functional defect remains
unresolved. The sponsor's framing — "sign off or lose leverage" — is actually backwards.
Signing acceptance with a known functional defect eliminates leverage, not preserves it.
Once formal acceptance is issued and final payment is released, the buyer has no
contractual mechanism to compel the vendor to correct defects at no additional cost.

The functional reporting defect producing incorrect totals is not a cosmetic issue. In
a government contract, incorrect financial reporting could constitute a compliance
violation. Marcus has an obligation to escalate this beyond his immediate sponsor if
the sponsor is directing him to accept defective work knowingly.

Practically, Marcus has several options in the eight remaining days. He can issue a
formal notice of defect in writing, triggering the contract's dispute resolution clause
and preserving rights beyond the period of performance. He can negotiate a conditional
acceptance: accept the two cosmetic items, withhold 10–15% of final payment as a
retention amount until the functional defect is patched and verified. He can also
document the vendor's verbal commitment to patch "in the next version" and formalize
it as a written warranty obligation in the contract closeout documentation.

Procurement closure best practices require that all deliverables be accepted against
the acceptance criteria in the SOW — not against verbal assurances of future patches.
Marcus should follow the process, document everything, and push back on the sponsor
through the proper escalation path.

### Peer Response Prompt

Does your classmate's response give Marcus a workable path forward within the eight-day
window? What additional risk — legal, ethical, or professional — do you see that they
may have overlooked?

---

## Grading Rubric — 10 Points Per Scenario (30 Points Total)

| Criterion | Points | Description |
|---|---|---|
| Content accuracy | 4 | Response correctly applies procurement concepts from the module |
| Analytical depth | 3 | Goes beyond surface-level description; identifies trade-offs and root causes |
| Specificity | 2 | Uses specific terminology, examples, or criteria from the scenario |
| Peer engagement | 1 | Peer reply adds new insight rather than simply agreeing |

---

## Professor Nash's Note

These three scenarios are based on real patterns I have observed in IT procurement.
Scenario 2 — the vague SOW — is by far the most common procurement failure mode in
IT projects. I have seen million-dollar disputes arise because no one took the time
to write clear acceptance criteria before contract execution.

The lesson is simple but rarely practiced: the time you invest in the SOW before
contract award is the cheapest time you will ever spend on that project. Every hour
you spend clarifying requirements and acceptance criteria before signing saves ten
hours of dispute, rework, and legal correspondence after.

When you are in the field as a project manager — and many of you will be within a
year of completing this course — resist the pressure to rush procurement. Sponsors
want to move fast. Vendors want to start billing. Your job is to make sure the
contract protects the organization before anyone picks up a pen.

Post your initial responses by Thursday at 11:59 PM. Peer replies are due Sunday
at 11:59 PM. See the course rubric in the LMS for full grading details.

---

*End of Discussion Forum — Module 14*

*Texas Wesleyan University — CIS-3310 IT Project Management*
