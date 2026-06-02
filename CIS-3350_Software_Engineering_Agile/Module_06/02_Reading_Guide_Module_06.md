# Reading Guide: Module 06 – Product Backlog: Creation and Refinement

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

The Product Backlog is Scrum's primary planning artifact. It is the single source of truth for what the team will build, in what order, and why. Understanding the Product Backlog deeply — its structure, ownership, refinement process, and quality criteria — is essential for the PSM I exam and for effective Agile practice. This guide covers the Product Backlog from definition through maintenance, including the INVEST criteria and common failure modes.

---

## 1. Product Backlog Fundamentals

### Definition

The Scrum Guide defines the Product Backlog as an emergent, ordered list of what is needed to improve the product. It is the single source of work undertaken by the Scrum Team.

### Key Characteristics

The Product Backlog is never complete: it is dynamic and evolves as long as the product exists.

The Product Backlog is emergent: it grows, changes, and becomes more detailed over time as the team learns more about the product and its users.

The Product Backlog is ordered: items are arranged in a complete ranking, with the highest-value, most-ready items at the top.

The Product Backlog is the single source: there is one Product Backlog per product. Multiple teams working on the same product share one Product Backlog.

### Product Backlog Item (PBI) Attributes

Each Product Backlog item has four standard attributes:

| Attribute | Owner | Description |
|---|---|---|
| Description | Product Owner | What the item is and why it is valuable |
| Order | Product Owner | Position in the ordered list relative to other items |
| Estimate (size) | Developers | Relative effort required to complete the item |
| Value | Product Owner | Business or user value delivered by completing the item |

Additional attributes commonly added by teams: acceptance criteria, definition of done compliance notes, dependencies, and technical notes.

---

## 2. The Product Goal

The Product Goal is the commitment associated with the Product Backlog. It is a long-term objective that describes the future state of the product and serves as the target for the Scrum Team to plan against.

The Product Backlog defines all the work needed to achieve the Product Goal. When the Product Goal is achieved — or abandoned as no longer valuable — the team may set a new Product Goal and build a new Product Backlog around it.

A Scrum Team pursues one Product Goal at a time. The Product Goal gives the Product Backlog coherence: items in the backlog should contribute to achieving the Product Goal; items that do not should be removed or deferred.

---

## 3. Product Backlog Ownership

The Product Owner is fully accountable for the Product Backlog. Their four key responsibilities:

Responsibility 1 — Developing and communicating the Product Goal: The Product Owner is responsible for defining a clear, meaningful Product Goal that the entire organization understands.

Responsibility 2 — Creating and communicating Product Backlog items: The Product Owner writes or facilitates the writing of PBIs, ensuring each item is clear enough to be understood by stakeholders, Developers, and other Product Owners.

Responsibility 3 — Ordering the Product Backlog: The Product Owner makes the hard trade-off decisions about which items to prioritize. Order reflects value, dependency, risk, learning opportunity, or any other factor the Product Owner deems relevant.

Responsibility 4 — Ensuring transparency: The Product Backlog should be visible, understandable, and accessible to the entire Scrum Team and relevant stakeholders.

### Delegation vs. Accountability

The Product Owner may delegate any of these activities to Developers, business analysts, or other team members. However, delegation does not transfer accountability. The Product Owner remains accountable for the outcomes of all Product Backlog decisions.

Stakeholders who want to influence the Product Backlog must go through the Product Owner. They cannot directly add, order, or modify items in the backlog without the Product Owner's involvement.

---

## 4. Product Backlog Refinement

### What Refinement Is

Product Backlog Refinement is the ongoing activity in which the Product Owner and Developers collaboratively decompose large Product Backlog items into smaller, more precise items and add details such as estimates and acceptance criteria.

Refinement is not a Scrum event — it does not appear in the list of the five official Scrum events. It is an ongoing activity that happens throughout the Sprint at whatever frequency the team finds useful.

### Refinement Capacity

The Scrum Guide states that Product Backlog Refinement typically consumes no more than 10% of the Developers' capacity. For a two-week Sprint with five Developers at 8 hours per day, 10% is approximately 4 hours per Developer per Sprint.

### Participants in Refinement

The Product Owner and Developers conduct refinement together. The Scrum Master may participate to facilitate or coach, but refinement is primarily a collaborative conversation between the Product Owner (who brings business context and value information) and the Developers (who bring technical feasibility knowledge and size estimates).

### What Happens During Refinement

During refinement sessions, the team:

- Reviews upcoming Product Backlog items to evaluate whether they are ready for Sprint Planning
- Breaks large items (epics) into smaller stories or tasks
- Adds acceptance criteria to items
- Adds or updates size estimates
- Removes items that are no longer relevant
- Re-orders items as business context changes
- Identifies and documents dependencies between items

### The Gradient of Backlog Detail

A well-refined backlog has a gradient of detail:

- Top of backlog (next 1–2 Sprints): items are small, well-defined, estimated, and ready for Sprint Planning
- Middle of backlog (3–10 Sprints out): items are medium-sized, partially defined, with rough estimates
- Bottom of backlog (more than 10 Sprints out): items are large, vague epics with minimal detail

This gradient reflects the Agile principle of "just enough" planning — detailed specification is done only when the work is close enough to matter.

---

## 5. INVEST Criteria for Product Backlog Items

INVEST is a quality checklist for evaluating whether a Product Backlog item is well-written and ready for Sprint-level work.

| Letter | Criterion | What It Means |
|---|---|---|
| I | Independent | The item can be delivered without requiring another item to be Done first |
| N | Negotiable | The implementation approach is not locked; the team has room for judgment |
| V | Valuable | The item delivers clear value to a user, customer, or the business |
| E | Estimable | The team has enough information to estimate the item's size |
| S | Small | The item can be completed within one Sprint |
| T | Testable | Acceptance criteria exist so the team can confirm when the item is Done |

Items that fail multiple INVEST criteria need more refinement before they are suitable for Sprint Planning. A common PSM I exam question will present a PBI and ask whether it is ready for Sprint Planning — applying INVEST is the evaluation framework.

---

## 6. Ordering the Product Backlog

Ordering is more precise than prioritization. Prioritization groups items into categories (high/medium/low). Ordering creates a complete sequence — item 1 before item 2 before item 3. The Product Owner makes explicit trade-off decisions through ordering.

Factors that influence ordering decisions:

- Value to users and the business: higher-value items generally rank higher
- Risk and uncertainty: high-risk items may be ordered early to learn fast (fail early rather than fail late)
- Dependencies: item B that depends on item A must be ordered after A
- Learning value: items that will teach the team something important about the product or technology
- Market timing: items needed for a specific release window
- Cost of delay: the business cost of not delivering an item sooner

The Product Owner owns ordering decisions. Stakeholders, managers, and Developers may provide input, but the Product Owner makes the final call.

---

## 7. Common Product Backlog Problems

Problem 1 — Backlog too large: A Product Backlog with hundreds of items is difficult to maintain and likely contains items that will never be built. Regularly reviewing and pruning low-value, stale items is a healthy practice.

Problem 2 — No ordering: All items marked "high priority" means the Product Owner has not made the hard sequencing decisions that are their core responsibility.

Problem 3 — Items too large for Sprint Planning: If most items require multiple Sprints, the backlog needs more refinement. Large epics must be decomposed into Sprint-sized stories.

Problem 4 — Missing acceptance criteria: Items without acceptance criteria produce ambiguous Done states at Sprint end. Acceptance criteria make the Definition of Done item-specific and testable.

Problem 5 — Backlog managed by committee: When multiple stakeholders add and order items without going through the Product Owner, the backlog loses coherence and the Product Owner loses accountability.

Problem 6 — Backlog as a wish list: A backlog that includes every possible feature idea without ordering or value assessment is not a planning tool — it is a wish list. The Product Owner must make hard choices about what to include and in what order.

---

## 8. PSM I Exam Tips

Tip 1: The Product Backlog is never complete. If an exam question describes a completed or frozen backlog, it is describing non-Scrum behavior.

Tip 2: The Product Owner orders the backlog; Developers estimate the items. These two responsibilities belong to different people and are not interchangeable on the exam.

Tip 3: Product Backlog Refinement is not a Scrum event. It does not appear in the five official events. When exam questions ask how many Scrum events there are, the answer is five, and refinement is not one of them.

Tip 4: The INVEST criteria — Independent, Negotiable, Valuable, Estimable, Small, Testable — are the standard framework for evaluating PBI readiness. Know all six.

Tip 5: Stakeholders influence the Product Backlog through the Product Owner, not directly. Any question that puts stakeholders in direct control of the backlog is describing incorrect Scrum behavior.

Tip 6: The Product Goal is the commitment associated with the Product Backlog. Know this pairing: Product Backlog → Product Goal; Sprint Backlog → Sprint Goal; Increment → Definition of Done.

Tip 7: There is one Product Backlog per product. Multiple Scrum Teams working on the same product share one Product Backlog. This is tested on PSM I.

Tip 8: Refinement consumes no more than 10% of Developers' capacity. This is the Scrum Guide's guidance — know the percentage.

---

## 9. Study Checklist

- [ ] Define the Product Backlog in the Scrum Guide's exact language and explain what "emergent" means in this context
- [ ] List the four attributes of a Product Backlog item and state who is responsible for each
- [ ] Explain what the Product Goal is and how it relates to the Product Backlog
- [ ] Describe the four Product Owner responsibilities for the Product Backlog
- [ ] Explain the difference between delegation and accountability in the context of Product Backlog management
- [ ] Define Product Backlog Refinement: what it is, who participates, and how much capacity it consumes
- [ ] Recite the INVEST criteria from memory and give one example of a PBI that fails each criterion
- [ ] Explain the difference between ordering and prioritization
- [ ] Describe four common Product Backlog problems and how to address each
- [ ] Complete this module's Lab (write a 10-item Product Backlog for a hypothetical product) and Quiz

---
