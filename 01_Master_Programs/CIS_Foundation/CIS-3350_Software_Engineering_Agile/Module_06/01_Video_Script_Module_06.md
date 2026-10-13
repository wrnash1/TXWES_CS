# Video Script: Module 06 – Product Backlog: Creation and Refinement

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Estimated Duration:** 21 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Instructor on screen for introduction and transitions
- Slides: Title cards for each section heading
- [SHOW DIAGRAM] tags indicate cuts to prepared visual assets
- Show Product Backlog as a living, ordered list — not a static spreadsheet

---

## Section 1 — Welcome and the Backlog as Living Artifact [00:00–03:30]

"Welcome to Module 6. In the last two modules we covered all five Scrum events. Now we turn to the Scrum artifacts — and specifically to the one artifact that is the center of gravity for everything a product team does: the Product Backlog.

By the end of this module you will be able to:

- Define the Product Backlog and explain its key characteristics
- Explain who owns the Product Backlog and how ownership works in practice
- Describe what good Product Backlog items look like and the INVEST criteria for evaluating them
- Explain Product Backlog Refinement — what it is, how it works, and how much capacity it consumes
- Explain ordering versus prioritization and why the distinction matters
- Create a Product Backlog for a hypothetical product

The Product Backlog is never finished. I want you to hold that phrase in your mind as we go through this module. A Product Backlog is never finished. It grows, it shrinks, it changes order, items are added, items are removed, items are broken down and rewritten. It is a living artifact that reflects the current best understanding of what the product needs to become."

---

## Section 2 — What the Product Backlog Is [03:30–09:00]

"The Scrum Guide defines the Product Backlog as an emergent, ordered list of what is needed to improve the product. It is the single source of work undertaken by the Scrum Team.

Let me break down that definition word by word.

Emergent: The Product Backlog is not written once and followed. It emerges over time as the team builds the product and learns. Early in a product's life, the backlog might have only high-level features. As development proceeds and the team learns more about user needs and technical realities, items become more detailed, more accurate, and more actionable.

[SHOW DIAGRAM: Product Backlog as an iceberg — items near the top are small, well-defined, and ready for Sprints; items deeper down are large, vague, and need more refinement]

Ordered: The Product Backlog is ordered, not just prioritized. Ordering is a more precise concept. Prioritization implies sorting by importance. Ordering implies a complete ranking — item 1 is done before item 2, item 2 before item 3. The Product Owner orders the backlog. They may use priority (value), dependency, risk, learning value, or any other factor in their ordering decisions.

Single source: There is one Product Backlog per product. If there are multiple teams working on the same product, they share a single Product Backlog. This is fundamental to maintaining a coherent product vision.

Product Backlog items — often called PBIs — typically include features, bug fixes, technical improvements, and knowledge acquisition work (spikes). Each PBI has a description, an order, an estimate (size), and a value. Developers add estimates; the Product Owner manages everything else.

PSM I Exam Tip: The Product Backlog is never complete and never frozen. If an exam question describes a Product Backlog that is finished or locked, that description reflects a Waterfall mindset, not Scrum."

---

## Section 3 — Product Backlog Ownership and the Product Goal [09:00–13:00]

"The Product Owner is accountable for the Product Backlog. The Scrum Guide is very clear on this.

[SHOW DIAGRAM: Product Owner at center, with arrows to Product Backlog activities: creating items, ordering items, communicating value, collaborating with Developers on estimates]

The Product Owner's accountability includes:

- Developing and explicitly communicating the Product Goal
- Creating and clearly communicating Product Backlog items
- Ordering Product Backlog items
- Ensuring the Product Backlog is transparent, visible, and understood

The Product Owner may delegate any of these activities to others — to Developers, to business analysts, to stakeholders. But accountability remains with the Product Owner. If a Product Backlog item is unclear, the Product Owner is accountable for clarifying it. If the backlog is not ordered in a way that maximizes value, the Product Owner is accountable for that too.

The Product Goal is the commitment associated with the Product Backlog. It is a long-term objective for the Scrum Team. The team works toward the Product Goal through a series of Sprints, each Sprint delivering an Increment that brings the product closer to that goal.

PSM I Exam Tip: If a stakeholder wants to add an item to the Product Backlog, they must go through the Product Owner. Stakeholders do not directly add or order items in the Product Backlog. The Product Owner is the gatekeeper.

One Product Owner may work with multiple Scrum Teams, but there is still one Product Backlog per product. The Product Owner ensures that all teams working on the product are pulling from the same ordered list."

---

## Section 4 — Product Backlog Refinement [13:00–18:00]

"Product Backlog Refinement is the ongoing activity of breaking down and further defining Product Backlog items into smaller, more precise items.

[SHOW DIAGRAM: Large, vague PBI at top of backlog being broken down through Refinement into three smaller, well-defined items with story point estimates and clear descriptions]

Refinement is not a one-time event. It happens continuously throughout the Sprint. The Scrum Guide says it typically consumes no more than 10% of the Developers' capacity per Sprint. For a two-week Sprint with five Developers, that is roughly four hours per Developer per Sprint devoted to refinement activities.

What happens during refinement? The team reviews upcoming Product Backlog items and asks: Is this item clear enough for Sprint Planning? Is it small enough to be completed in one Sprint? Does it have an estimate? Are the acceptance criteria defined?

Items that are ready for Sprint Planning should ideally meet the INVEST criteria — a quality checklist for individual backlog items. INVEST stands for:

Independent: the item can be delivered without depending on another item being done first
Negotiable: the implementation details are not locked; there is room for team judgment
Valuable: the item delivers value to a user or the business
Estimable: the team has enough information to estimate its size
Small: the item can be completed within one Sprint
Testable: you can write a test that definitively says whether the item is done

PSM I Exam Tip: Refinement is an ongoing activity, not a Scrum event. It is not listed among the five official Scrum events. When an exam question asks about Scrum events, refinement is not on the list. But the Scrum Guide acknowledges that it happens and allocates capacity for it.

A common question on PSM I: who participates in refinement? The Scrum Guide says Product Backlog Refinement is done with the Product Owner and the Developers. Not the Scrum Master alone. Not the Product Owner alone. It is a collaborative activity because Developers add the estimates and ask the technical clarifying questions."

---

## Section 5 — What a Good Product Backlog Looks Like [18:00–21:00]

"Let me close with a description of a healthy Product Backlog and the most common problems you will see in the field and on the PSM I exam.

[SHOW DIAGRAM: Healthy Product Backlog — top 10 items are small, well-estimated, and INVEST-ready; items 11–30 are medium-sized with partial estimates; items 31+ are large, vague epics]

A healthy Product Backlog has a gradient of detail. Items at the top — those closest to being selected for a Sprint — are well-defined, small, and estimated. Items in the middle are partially refined. Items at the bottom may be large, vague features or epics that will be broken down further as they get closer to the top.

This gradient reflects the principle of 'just enough' planning. You do not need to fully specify an item you will not build for six months. Spending significant time defining items that might never be built is waste.

The most common Product Backlog problems are:

Problem 1: A backlog that is too long. A backlog with five hundred items is difficult to maintain and likely contains items that will never be built. Regularly pruning items that have been on the backlog for a long time without being selected is a healthy practice.

Problem 2: A backlog with no ordering. If all items are marked 'high priority,' the Product Owner has not made the hard ordering decisions that are their core responsibility.

Problem 3: Items that are too large. If most items require two or three Sprints to complete, the team cannot do Sprint-level planning effectively. Large items (epics) must be broken down through refinement before being selected for a Sprint.

Problem 4: A backlog managed by committee. When multiple stakeholders can directly add and order items without going through the Product Owner, the backlog loses coherence and the Product Owner loses accountability for value.

In Module 7 we go deeper on the items themselves — how to write user stories and acceptance criteria that make Product Backlog items clear, testable, and valuable. See you there."

---

## End Card

- Next module: Module 07 – User Stories and Acceptance Criteria
- Additional Resources (Scrum.org only):
  - Scrum Guide (free): scrum.org/resources/scrum-guide
  - PSM I exam details: scrum.org/professional-scrum-master-i-certification

---
