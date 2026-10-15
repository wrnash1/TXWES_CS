# Video Script: Module 14 — Scaled Agile: SAFe and LeSS Overview

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp &bull; Software Engineering Principles & SDLC Architecture &bull; Module 14</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=LzMnsfqjzkA" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/LzMnsfqjzkA" title="freeCodeCamp &bull; Software Engineering Principles & SDLC Architecture" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp &bull; Software Engineering Principles & SDLC Architecture</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Estimated Duration:** 22 minutes

**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Section 1 — Welcome and Why Scaling Matters
Welcome to Module 14. So far in this course, we have focused on a single Scrum Team — three to nine people working together in Sprints, inspecting and adapting. That model works extremely well for a single product with a single team. But what happens when the product is so large, or the organization is so complex, that one team cannot possibly build it alone?

That is the scaling problem. Large software products — enterprise systems, platforms, complex consumer applications — require multiple teams working in parallel. And when multiple teams each run their own Scrum, you immediately face coordination challenges: how do teams synchronize dependencies? Who owns the shared architecture? How does the organization plan across multiple teams when each team plans Sprints independently? How does work get prioritized across a portfolio of products?

Scaling frameworks address these challenges. Two of the most widely adopted are SAFe — the Scaled Agile Framework — and LeSS — Large-Scale Scrum. They take different philosophies toward the problem, and understanding both gives you a vocabulary for the conversations you will have in organizations that have outgrown single-team Scrum.

By the end of this module you will be able to:

- Describe what problem scaling frameworks solve
- Explain the core structure of SAFe including the Program Increment and key roles
- Explain the core structure of LeSS and how it differs from SAFe
- Compare SAFe and LeSS on key design choices: team structure, planning, and product ownership
- Connect scaled Agile concepts to the PSM I exam's emphasis on Scrum values and empiricism

---

## Section 2 — The Scaling Problem
Before I introduce either framework, let me characterize the problem clearly.

A single Scrum Team with a single Product Owner and a shared Product Backlog works because everyone on the team can talk to each other, the Product Owner can prioritize everything in context, and integration happens naturally when three developers are all working in the same codebase.

Now imagine you have eight teams, each running Scrum, each building different parts of the same platform. You immediately face:

Integration: each team's potentially releasable Increment must integrate into a single coherent whole. A team cannot declare their work 'done' if it breaks another team's work.

Dependencies: Team A's Sprint goal may require a component that Team B is building. If Team B's Sprint is delayed, Team A's goal is at risk.

Product Ownership: can one Product Owner effectively manage eight teams' backlogs? The scope is too large for a single person to handle with the depth that Scrum's Product Owner role requires.

Strategy alignment: with eight teams shipping features simultaneously, how does the organization ensure they are all moving toward the same strategic objectives?

SAFe and LeSS each provide answers to these questions — but they answer them in very different ways.

PSM I Exam Tip: The Scrum Guide does not describe how to scale Scrum. SAFe and LeSS are external frameworks built on Scrum's foundation. The exam tests your understanding of core Scrum — but PSM I candidates are expected to know why scaling challenges exist and be aware that frameworks exist to address them.

---

## Section 3 — SAFe: The Scaled Agile Framework
Let me start with SAFe, which is the most widely adopted scaling framework in large enterprises.

SAFe operates at three to four levels depending on the configuration. For PSM I purposes, the Essential SAFe configuration — two levels — is the most important to understand.

At the team level, SAFe teams each run Scrum or Kanban sprints. Nothing changes at the individual team level — they still have Sprints, Sprint Reviews, Retrospectives, and a Team Backlog. In SAFe terminology, the team-level Sprint is called an Iteration.

The program level is what SAFe adds. Multiple teams — typically five to twelve — form an Agile Release Train, abbreviated ART. The ART is the primary SAFe delivery unit. All teams on the ART operate on synchronized Iteration cadences — they all start and end Iterations on the same schedule.

The ART operates on a Program Increment, typically 10 to 12 weeks. A Program Increment is essentially a fixed-timebox of five to six Iterations (Sprints) for the entire ART. At the beginning of every Program Increment, all teams on the ART meet for PI Planning — a two-day face-to-face event where teams plan their Iterations for the entire PI, identify cross-team dependencies, and commit to Program Increment Objectives.

PI Planning is SAFe's answer to the dependency coordination problem. By having all teams plan together at the same time, they can surface dependencies, negotiate scope, and create a shared plan before anyone starts Sprint work. The result is a synchronized plan where each team's Iterations are coordinated against other teams' Iterations.

The SAFe roles at the program level include the Release Train Engineer — the Scrum Master equivalent for the ART who facilitates PI Planning and the ART's Inspect and Adapt event. The Product Manager owns the program-level backlog (called the Program Backlog) and prioritizes features for the ART.

The final Iteration of each PI is the Innovation and Planning Iteration — a dedicated Sprint for testing, technical debt reduction, exploration, and PI Planning preparation. It is not a feature development Iteration.

PSM I Exam Tip: SAFe's PI Planning is the most exam-relevant concept from this framework. It addresses the multi-team coordination problem through synchronized planning, visible dependencies, and committed PI Objectives. Know it by name and purpose.

---

## Section 4 — LeSS: Large-Scale Scrum
LeSS takes a fundamentally different approach from SAFe. Where SAFe adds organizational structure, LeSS tries to extend Scrum with as few additions as possible.

The core principle of LeSS is: more teams, same Scrum. One Product Owner owns one Product Backlog for all teams. All teams run the same Sprint — starting and ending on the same date, with the same Sprint length. The Sprint Review and Sprint Retrospective happen across all teams simultaneously or in coordinated fashion.

In LeSS, the teams are called feature teams — they are cross-functional and each capable of delivering end-to-end features from a single Product Backlog. This is different from SAFe, where teams may own separate components. LeSS feature teams select from the shared Product Backlog and coordinate informally during the Sprint. There is no program-level planning event like SAFe's PI Planning.

LeSS coordination mechanisms are lightweight. Teams use inter-team coordination: a shared Sprint Review where all teams show their work, multi-team Sprint Retrospectives where systemic problems can be raised, and optional Scrum of Scrums — a coordination meeting attended by one representative from each team.

LeSS Huge extends the model further for organizations with more than eight teams. LeSS Huge divides the Product Backlog into Requirement Areas — large slices of customer-facing functionality — each with an Area Product Owner. But there is still one overall Product Owner and one Product Owner team.

The key LeSS design philosophy is that scaling problems are often organizational problems. Adding management layers, specialized roles, and coordination machinery treats the symptom. LeSS recommends simplifying the organizational structure first — reducing the number of component teams, handoffs, and approvals — and letting genuine Scrum at scale work through simple coordination mechanisms.

PSM I Exam Tip: LeSS versus SAFe is a classic comparison question. LeSS adds as little as possible to Scrum; SAFe adds substantial structure. LeSS uses one Product Owner and one Backlog for all teams; SAFe has a Product Manager and a Program Backlog layer above team Product Owners.

---

## Section 5 — SAFe vs. LeSS and Closing
Let me close with a direct comparison that will help you apply these concepts.

SAFe is more prescriptive. It tells you exactly how to structure the organization, what roles to create, what meetings to run, and what artifacts to produce. This makes SAFe easier to adopt in large enterprises with existing hierarchy — there is a role for everyone, and the transformation path is documented. The trade-off is complexity and overhead. PI Planning is a significant organizational investment. The ART structure requires coordination roles that do not exist in basic Scrum.

LeSS is more principled. It applies Scrum values and empiricism at scale and trusts that simplicity will emerge from the same inspect-and-adapt discipline that works for a single team. LeSS is harder to adopt in organizations with deep hierarchy because it challenges the need for middle management and specialized coordination roles. It requires genuine organizational redesign, not just role-mapping. The trade-off is that it is closer to Scrum's spirit but demands more change.

Neither framework is universally correct. The right choice depends on the organization's size, maturity, culture, and tolerance for organizational disruption.

For Scrum Masters, the key takeaway from both frameworks is that the scaling problem is ultimately a human and organizational challenge, not a technical one. Dependencies between teams exist because the architecture is componentized, because teams are not cross-functional, or because product ownership is fragmented. The best solutions address those root causes — not just add coordination overhead on top of them.

In Module 15, we will look at software project metrics and velocity tracking — how teams measure progress, identify problems, and communicate status. See you there.

---

## End Card

- Next module: Module 15 – Software Project Metrics and Velocity Tracking
- Additional Resources (Scrum.org only):
  - Scrum Guide (free): scrum.org/resources/scrum-guide
  - PSM I exam details: scrum.org/professional-scrum-master-i-certification

---
