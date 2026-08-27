# Reading Guide: Module 08 – Estimation: Story Points and Planning Poker

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

Agile estimation is a tool for making better planning decisions under uncertainty, not for predicting the future with precision. This module covers the theory and practice of story point estimation, the Planning Poker technique, velocity as a planning tool, and the most common estimation anti-patterns that undermine team effectiveness. Understanding these concepts prepares you for PSM I exam questions and for productive participation in real Agile team planning sessions.

---

## 1. Why Agile Estimation Differs from Traditional Estimation

Traditional project management uses hour-based or day-based estimates to build project schedules with specific completion dates. This approach has a fundamental problem: software estimation is notoriously inaccurate for absolute durations, particularly for complex, novel work.

The software industry has extensively studied this problem:

- Developers consistently underestimate time for novel tasks by a factor of 2–3x (the "planning fallacy")
- External factors (interruptions, dependency delays, technical surprises) are difficult to predict
- Hour estimates create false precision — an estimate of "16 hours" implies a level of certainty that rarely exists

Agile estimation addresses this by shifting from absolute estimates to relative estimates. Relative estimation asks: is this story more or less complex than that story? Teams are generally more accurate at relative comparisons than at absolute duration predictions.

---

## 2. Story Points — Full Definition

Story points are a unit of measure for expressing the overall effort required to implement a Product Backlog item, accounting for:

- Complexity: how technically difficult is the work?
- Effort: how much work is involved, regardless of complexity?
- Uncertainty: how much is unknown that could affect the outcome?

Story points are relative and team-specific. A "5-point story" means this story is roughly the same size as the team's agreed reference story for 5 points. It does not mean "5 hours" or "5 days" — it means "5 units of this team's experience-calibrated complexity scale."

### The Fibonacci Sequence

The most common story point scale uses Fibonacci numbers: 1, 2, 3, 5, 8, 13, 21, and often 34, 55, 89 for very large items.

Why Fibonacci? The increasing gaps between consecutive numbers prevent false precision:

| Consecutive Numbers | Gap | Meaning |
|---|---|---|
| 1 vs. 2 | Small | These stories are similar in size |
| 5 vs. 8 | Medium | Noticeably different; worth discussing |
| 13 vs. 21 | Large | Significantly different; often signals the story needs splitting |

A modified Fibonacci scale (1, 2, 3, 5, 8, 13, 20, 40, 100) is also commonly used in Planning Poker decks.

### The Reference Story

Teams often calibrate their story point scale by agreeing on a reference story — a story everyone knows well from past work, assigned a specific point value (often 3 or 5 points). New stories are estimated relative to the reference story: "Is this bigger or smaller than our reference 3-point story?"

---

## 3. Planning Poker — Step-by-Step

Planning Poker is a consensus-based, gamified estimation technique that combines the wisdom of the team with a structured process to prevent anchoring bias.

### Materials

- A Planning Poker deck for each Developer (cards: 0, 1, 2, 3, 5, 8, 13, 20, 40, 100, ?, infinity)
- The Product Backlog item being estimated (on screen or printed)
- A facilitator (typically the Scrum Master, but any team member can facilitate)

### Process

Step 1 — Story presentation: The Product Owner reads the user story and provides any necessary context. Developers ask clarifying questions.

Step 2 — Individual estimation: Each Developer privately selects a card representing their estimate. No discussion of estimates yet.

Step 3 — Simultaneous reveal: On the facilitator's signal, all Developers reveal their cards at the same time. Simultaneous reveal prevents anchoring.

Step 4 — Discussion: If estimates are close (adjacent Fibonacci values), the team notes the consensus and moves on. If there is significant divergence, the highest and lowest estimators explain their reasoning.

Step 5 — Re-estimation: After the discussion, each Developer re-estimates privately and reveals simultaneously again. This continues until consensus is reached or the team agrees to use the higher estimate due to unresolved uncertainty.

Step 6 — Record and continue: The agreed estimate is recorded against the story in the Product Backlog. The team moves to the next story.

### Special Cards

- Question mark (?): "I don't understand this story well enough to estimate. We need more information before I can give a meaningful number."
- Infinity: "This story is too large to estimate. It needs to be split before we can assess its size."
- 0: "This story is trivial — effectively no effort required."

### Why Simultaneous Reveal Matters

If one Developer reveals their estimate first, they anchor the group. The other Developers' estimates converge on the first number revealed — not because that number is most accurate, but because of the well-documented cognitive bias toward the first number heard. Simultaneous reveal eliminates this bias and allows each Developer's independent assessment to be heard.

---

## 4. Velocity

Velocity is the sum of story points for all Product Backlog items that are Done — meeting the Definition of Done — at the end of a Sprint.

### Using Velocity for Capacity Planning

After a few Sprints, a team's velocity stabilizes within a range. This range is used in Sprint Planning to guide how many story points to select. If the team's last three Sprints yielded 28, 33, and 31 points, selecting 30–33 points for the next Sprint is reasonable.

Velocity is a trailing average, not a target. It tells you what the team accomplished recently, not what they will accomplish next Sprint.

### Velocity Reference Table

| Sprint | Velocity | Notes |
|---|---|---|
| Sprint 1 | 22 | New team, calibrating estimates |
| Sprint 2 | 28 | More familiar with codebase |
| Sprint 3 | 31 | Stable team composition |
| Sprint 4 | 18 | Two Developers out sick |
| Sprint 5 | 33 | Back to full capacity |
| Average (3–5) | 27 | Use ~27 as planning guide |

### What Velocity Is Not

Velocity is not a productivity metric. Comparing velocity across teams, using velocity to evaluate Developers, or setting velocity targets corrupts the measure. Teams will inflate estimates to hit higher numbers — velocity gaming — destroying its planning value.

Velocity is not a commitment. The team's velocity suggests how much they can reasonably take on; it does not guarantee delivery of exactly that number of points.

Velocity is not in the Scrum Guide. The Scrum Guide does not mention velocity by name. It is a widely used practice but not a Scrum framework element. PSM I may test this distinction.

---

## 5. Estimation Scales Comparison

| Scale | Format | Best For |
|---|---|---|
| Story Points (Fibonacci) | 1, 2, 3, 5, 8, 13, 21 | Standard Agile teams; Sprint Planning |
| T-Shirt Sizes | XS, S, M, L, XL, XXL | Early product vision conversations; executives |
| Ideal Days | Number of ideal working days | Teams transitioning from hour estimates |
| #NoEstimates | No estimates; count stories | Highly mature teams with consistent story size |

The Scrum Guide does not mandate any of these. Teams choose what works for their context.

---

## 6. Common Estimation Anti-Patterns

Anti-pattern 1 — Anchoring: An estimate is announced before everyone reveals, pulling all estimates toward that number. Fix: enforce simultaneous reveal.

Anti-pattern 2 — Pressure-based deflation: Developers lower estimates under management or Product Owner pressure to show progress faster. Fix: estimates are owned by the Developers alone; external pressure is not legitimate input.

Anti-pattern 3 — Converting story points to hours: Once you convert to hours in a report, you lose all the benefits of relative estimation. Fix: report velocity in story points; never convert to hours for external communication.

Anti-pattern 4 — Estimating without understanding: Teams rush through estimation without reading stories or asking questions. Fix: require the "Conversation" component of the Three Cs before estimating; use '?' cards when clarity is missing.

Anti-pattern 5 — Velocity as a goal: Management sets a velocity target (e.g., "you must hit 50 points per Sprint"). Fix: educate stakeholders that velocity is a measurement, not a lever; the way to increase output is to reduce impediments and technical debt.

Anti-pattern 6 — Single-person estimation: A manager or senior developer estimates all stories alone. Fix: Planning Poker explicitly requires all Developers to estimate; solo estimation loses the crowd wisdom that makes group estimates more accurate.

---

## 7. PSM I Exam Tips

Tip 1: The Scrum Guide does not mandate story points. It says Developers add size estimates to PBIs but does not specify the format. Questions that say "Scrum requires story points" are incorrect.

Tip 2: Velocity is not in the Scrum Guide. It is a common practice but not a Scrum rule.

Tip 3: Velocity is team-specific and cannot be compared across teams. Two teams with different story point calibrations cannot be compared by velocity.

Tip 4: Only Developers estimate story points. The Product Owner and Scrum Master do not override or modify estimates. The Scrum Guide is explicit: the Developers who will do the work determine how much effort is required.

Tip 5: Velocity should never be used as a performance metric. If a PSM I question describes management using velocity to evaluate Developer performance, the correct response is to explain why this is problematic.

Tip 6: Planning Poker's value is in the discussion, not the cards. The technique surfaces disagreements and hidden knowledge that improve team understanding.

Tip 7: A story that gets the infinity card in Planning Poker needs to be decomposed before it can be selected for a Sprint. This is a refinement signal, not a failure.

Tip 8: The Scrum Guide says estimates belong to the Developers and cannot be overridden by anyone. This is tested on PSM I in scenarios where managers pressure teams to commit to more than they believe they can accomplish.

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 08 topics:

**1. "Story Points Revisited" — Ron Jeffries**
<https://ronjeffries.com/articles/019-01ff/story-points/Index.html>
A reflective essay by one of the original XP practitioners and Agile Manifesto signatories on the value and misuse of story points. Jeffries critically examines whether story points still serve their original purpose in modern teams. Free access.

**2. "How to Use Story Points" — Mountain Goat Software**
<https://www.mountaingoatsoftware.com/blog/what-are-story-points>
Mike Cohn's practical explanation of story points, including the Fibonacci scale rationale, reference story calibration technique, and common misuses. Free access on Mountain Goat Software's blog.

**3. "Planning Poker" — Agile Alliance Glossary**
<https://www.agilealliance.org/glossary/poker/>
The Agile Alliance's canonical glossary entry on Planning Poker. Covers the technique's origins, the anchoring bias rationale, the role of divergent estimates, and variations used in practice. Free access.

---

## 8. Study Checklist

- [ ] Explain why relative estimation (story points) is more accurate than absolute estimation (hours) for complex software work
- [ ] Explain what story points measure: complexity, effort, and uncertainty
- [ ] Explain why the Fibonacci sequence is used rather than a 1–10 scale
- [ ] Describe all six steps of Planning Poker and explain why simultaneous reveal prevents anchoring
- [ ] Define velocity and explain how it is used for Sprint capacity planning
- [ ] State three things velocity is NOT (not a target, not a commitment, not in the Scrum Guide)
- [ ] Describe five estimation anti-patterns and how to address each
- [ ] State whether the Scrum Guide mandates story points (it does not)
- [ ] Complete this module's Lab (Planning Poker simulation) and Quiz

---
