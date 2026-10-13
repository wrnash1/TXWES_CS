# Lab Activity: Module 13 — Solution Design and Prototyping

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Lab Overview

In this lab you will practice the full solution design and prototyping workflow used by business analysts. You will create wireframes for a described business scenario, select and justify a prototyping strategy, apply UI/UX heuristics to critique a provided design, and plan a design validation session.

**Estimated time:** 75–90 minutes

**Tools allowed:** Any wireframing tool (Balsamiq, Figma, draw.io, PowerPoint, pencil and paper photographed). Hand-drawn wireframes are fully acceptable.

**Deliverable:** Submit your completed lab as a single PDF combining your wireframes, written responses, and validation plan.

---

## Scenario Background

Lone Star Community Credit Union is building a new member self-service portal. Members will be able to log in, view account balances and transaction history, transfer funds between accounts, and submit loan applications. The credit union currently has no digital self-service capabilities — all transactions are handled in person or by phone.

You have been assigned as the BA for this project. The IT director wants to see initial design concepts within two weeks. The development team uses an agile methodology with two-week sprints.

---

## Part 1 — Wireframe Creation (30 points)

### Part 1A — Dashboard Screen Wireframe

Create a wireframe for the member dashboard — the first screen a member sees after logging in. The dashboard must include:

- Account summary section showing at least two account types (checking and savings)
- Quick-action buttons for the three most common tasks (check balance, transfer funds, view statements)
- Navigation to all major sections of the portal
- A recent transactions preview showing the last five transactions
- A notification area for alerts (low balance, upcoming loan payment due)

Your wireframe must be clearly labeled. Use annotations to describe the behavior of at least three interactive elements. For example: "Clicking account card expands to show full transaction history."

### Part 1B — Fund Transfer Screen Wireframe

Create a wireframe for the fund transfer screen. This screen allows a member to:

- Select a source account from their own accounts
- Select a destination account (own account or external account)
- Enter the transfer amount
- Select a transfer date (immediate or scheduled)
- Review transfer details before confirming
- Receive a confirmation after the transfer is submitted

Include annotations explaining validation behavior — for example, what happens if the member enters an amount exceeding the available balance.

### Part 1C — Navigation Flow Diagram

Draw a simple flow diagram showing how screens connect. At minimum, show the relationship between the Login screen, Dashboard, Transaction History, Fund Transfer, and Loan Application screens. Use arrows to indicate navigation paths.

---

## Part 2 — Prototyping Strategy Selection (20 points)

### Part 2A — Strategy Recommendation

Based on the credit union scenario, recommend either throwaway or evolutionary prototyping for the initial design phase. Write a 150–200 word justification that addresses:

- The current state of requirements (certain or uncertain?)
- The development methodology in use (agile sprints)
- The stakeholder engagement model
- The risk profile of the project
- Which characteristics of the recommended strategy make it the right fit

### Part 2B — Transition Plan

If you recommended throwaway prototyping, describe at what point you would transition from the throwaway prototype to actual development. If you recommended evolutionary prototyping, describe how you would ensure quality standards are maintained from the first sprint.

Write three to five bullet points for your transition plan.

---

## Part 3 — UI/UX Heuristic Evaluation (25 points)

### Provided Design Description

A competitor credit union recently launched a self-service portal with the following characteristics. Review each characteristic and evaluate it against Nielsen's usability heuristics.

**Characteristic 1:** When a member submits a fund transfer, the screen goes blank for eight to twelve seconds while the system processes the request. No loading indicator or message is displayed. After processing, the confirmation page appears.

**Characteristic 2:** The navigation menu uses internal system codes for menu items: ACCT_VIEW, XFER_INIT, LN_APP_SUBMIT. These labels were copied directly from the database table names.

**Characteristic 3:** The loan application form has 47 fields on a single scrolling page. There is no progress indicator, no "Save Draft" option, and submitting the incomplete form displays the generic message: "Submission failed."

**Characteristic 4:** The "Transfer Funds" button and the "Cancel Transfer" button are the same size, the same color, and placed directly next to each other.

**Characteristic 5:** The transaction history page displays the same layout, typography, and interaction patterns as every other page in the portal.

### Evaluation Task

For each characteristic, complete the following:

1. Identify which Nielsen heuristic is violated (or upheld, in the case of characteristic 5).
2. Explain specifically why the characteristic is a violation or an example of good design.
3. Write a corrected requirement for each violation — a one-sentence requirement statement the BA should have documented to prevent this design problem.

Format your response as a table with columns: Characteristic, Heuristic, Violation or Upheld, Explanation, Corrected Requirement.

---

## Part 4 — Design Validation Session Plan (25 points)

### Part 4A — Participant Selection

The credit union has the following potential participants available for a design validation session:

- Five branch tellers (daily users of internal systems, some member interaction)
- Three loan officers (heavy portal users expected)
- Four general members aged 25–40 (target demographic)
- Two members aged 65+ (represent less tech-comfortable segment)
- The VP of Operations (executive sponsor)
- The IT director

From this list, select six to eight participants for your validation session. Justify your selections. Explain who you excluded and why.

### Part 4B — Task Scenario Development

Write three task scenarios for the validation session. Each scenario must be:

- Goal-based, not action-based
- Realistic for the target users
- Testable against your wireframe designs from Part 1

For each scenario, write the scenario text that you would read aloud to participants, then write a brief note explaining what design element(s) the scenario is intended to test.

### Part 4C — Findings Log Template

Create a findings log template that the note-taker will use during the session. The template should capture: session date, participant ID, task scenario, behavioral observation, severity classification, and recommended design change. Provide one completed example row using a realistic observation from the fund transfer scenario.

### Part 4D — Post-Session Decision

After the validation session, you discover the following findings:

- Two participants could not locate the fund transfer feature without assistance (critical)
- Three participants attempted to click account balance numbers expecting them to be links (major)
- One participant found the notification area text too small to read comfortably (minor)
- Two participants suggested adding a dark mode option (cosmetic)

Describe the design changes you would make before development begins and explain your rationale. Which findings require immediate action? Which can be deferred?

---

## Submission Checklist

Before submitting, confirm your PDF includes:

- Part 1: Dashboard wireframe with annotations, fund transfer wireframe with annotations, navigation flow diagram
- Part 2: Strategy justification (150–200 words), transition plan bullets
- Part 3: Heuristic evaluation table with all five characteristics addressed
- Part 4: Participant selection with justification, three task scenarios, findings log template with example row, post-session decision narrative

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — Wireframes and flow diagram | 30 |
| Part 2 — Prototyping strategy and transition plan | 20 |
| Part 3 — UI/UX heuristic evaluation | 25 |
| Part 4 — Design validation session plan | 25 |
| **Total** | **100** |

---

---

## Part 9 — Challenge Exercise

This section is optional and not separately graded. It extends the lab into advanced
prototyping and design validation practice aligned with ECBA exam competencies.

### Challenge Step 1: Accessibility Audit of Your Wireframes

Review the two wireframes you created in Part 1 (dashboard and fund transfer screens)
against the WCAG 2.1 Level AA accessibility guidelines. For each wireframe, identify at
least three specific accessibility requirements that must be documented to ensure the
design is accessible to users with visual, motor, or cognitive disabilities. Format your
findings as a table with columns: Screen, Accessibility Concern, WCAG Criterion Reference,
and Required Design Change. Then write a one-paragraph explanation of why accessibility
requirements must be captured by the BA during the design phase rather than left to
developers to discover during implementation. Reference at least one legal or regulatory
context (such as the ADA, Section 508, or the European Accessibility Act) in your
explanation.

### Challenge Step 2: Comparative Prototype Evaluation

Select one screen from Part 1 and create two alternate wireframe versions — a Version A
and a Version B — that apply different design approaches to the same functionality. For
example, design the fund transfer confirmation step as a modal dialog in Version A and
as a full-page confirmation screen in Version B. For each version, apply Nielsen's
heuristics formally: evaluate all ten heuristics and mark each as Satisfied, Partially
Satisfied, or Not Applicable, with a one-sentence note for each. Then write a
recommendation selecting one version and justifying your choice by referencing the
heuristic evaluation results, the target user profile (credit union members aged 25 to
65), and the prototyping principle that design decisions should be evidence-based rather
than preference-based.

### Challenge Step 3: Full Validation Session Report

Using the task scenarios and findings log template from Part 4, write a complete post-
session validation report as if you had conducted the session and observed five
participants completing three tasks. Fabricate realistic but plausible findings across
the four severity levels (at least one critical, two major, two minor, one cosmetic).
Your report must include: an executive summary of session outcomes (one paragraph), the
complete findings log with all observations, a prioritized change list organized by
severity with design change descriptions, a comparison of which design elements performed
well versus which failed, and a recommendation on whether the design is ready to proceed
to development or requires a second validation round. This exercise develops the
reporting and stakeholder communication skills that BAs use after every design validation
engagement.

---

*Module 13 Lab | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
