# Video Script: Module 02 - Business Analysis Planning and Monitoring

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Lucidchart / Enterprise &bull; Systems Analysis & Software Architecture &bull; Module 02</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=UI6lqHOVHic" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/UI6lqHOVHic" title="Lucidchart / Enterprise &bull; Systems Analysis & Software Architecture" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Lucidchart / Enterprise &bull; Systems Analysis & Software Architecture</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Course:** CIS-3312 Systems Analysis and Design
**Estimated Duration:** 21 minutes
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Section 1: Welcome and Module Overview
Welcome back to CIS-3312. I am Professor Nash, and this is Module 02: Business Analysis Planning and Monitoring. If Module 01 was about understanding what systems analysis is and how it fits into the SDLC, then Module 02 is about the very first thing a BA does when a project is officially approved — plan the BA work itself.

This module maps directly to BABOK Knowledge Area 2, which is simply called "Business Analysis Planning and Monitoring." On the ECBA exam, KA 2 questions are among the most commonly tested, and they tend to trip up students who think planning only belongs to project managers. It does not. BAs plan too — and BABOK tells us exactly what to plan.

Here is what we will cover today. First, we will understand the purpose of BA Planning and why it is separate from project planning. Second, we will walk through the four main outputs of KA 2. Third, we will cover stakeholder analysis in detail — power-interest grids, engagement strategies, and the stakeholder register. Fourth, we will talk about choosing the right BA approach — predictive versus adaptive — and close with exam tips.

---

## Section 2: Why BAs Plan — and What They Plan
Let me address the question students most often ask about KA 2: "Isn't planning the project manager's job?" The answer is: project planning is the PM's job. BA planning is the BA's job. They overlap but are not the same.

The project manager plans schedule, budget, resources, and risk. The business analyst plans something different: how BA activities will be conducted. That means planning which elicitation techniques to use, how requirements will be documented and organized, how stakeholders will be engaged, and how requirements changes will be governed. The BA plan answers the question: "Given this project, this team, and these stakeholders, how am I going to do my BA work?

BABOK KA 2 contains five tasks:

- Plan Business Analysis Approach — decide the overall methodology (predictive or adaptive)
- Plan Stakeholder Engagement — identify and analyze stakeholders
- Plan Business Analysis Governance — define how requirements decisions are made and who approves them
- Plan Business Analysis Information Management — decide how requirements artifacts will be stored, versioned, and accessed
- Identify Business Analysis Performance Improvements — monitor BA work quality and make corrections

The outputs of these tasks feed into everything that comes later. Before you can elicit requirements, you need to know who to talk to. Before you know who to talk to, you need a stakeholder analysis. It all begins here in KA 2.

> IIBA ECBA Exam Tip: KA 2 is the planning knowledge area. On the exam, if a question describes a scenario where BA work has gone off track — missed interviews, incomplete documentation, stakeholder dissatisfaction — and asks what the BA should do, the answer will almost always involve a KA 2 monitoring or correction activity: analyze the performance variance, identify the root cause, and update the BA plan.

---

## Section 3: Stakeholder Analysis and the Power-Interest Grid
Stakeholder analysis is the foundation of BA Planning. You cannot plan your elicitation approach until you know who your stakeholders are, what they care about, and how much influence they have over the project.

This is the Power-Interest Grid, sometimes called the stakeholder analysis matrix. It helps the BA decide how to allocate engagement time and effort across a large stakeholder group.

Let me walk through each quadrant.

High power, high interest — Manage Closely. These are your core stakeholders. They have both the authority to affect the project and a strong interest in its outcome. Your sponsor, your primary business owners, and your most senior subject matter experts typically fall here. Meet with them frequently, involve them in key decisions, and never surprise them with bad news.

High power, low interest — Keep Satisfied. These are typically senior executives or external regulators. They can block or derail the project if unhappy, but they do not want to be involved in day-to-day details. Provide high-level summaries at key milestones. Escalate significant decisions to them. Do not waste their time with operational details — and do not let them feel excluded from things that matter.

Low power, high interest — Keep Informed. These are people who care deeply about the outcome but have limited organizational authority. Front-line users often fall here. They cannot force decisions, but they can surface critical requirements you would otherwise miss. Keep them informed with regular updates. Involve them in testing and validation activities.

Low power, low interest — Monitor. These are peripheral stakeholders. They may be affected by the system indirectly, but they are not driving requirements and are not at risk of derailing the project. A quarterly briefing or summary email may be sufficient.

The BA records all stakeholders in a Stakeholder Register. This is a living document — stakeholders join and leave projects, their interest levels change, and new regulatory bodies may enter the picture. Update it throughout the project.

> IIBA ECBA Exam Tip: Exam questions about stakeholder quadrants always give you the power and interest levels in the scenario description. Map them to the grid immediately: high power + high interest = Manage Closely. High power + low interest = Keep Satisfied. The "Keep Satisfied" quadrant is the most commonly tested trap — students instinctively want to "involve them closely" because of their high power, which is wrong. Their low interest means detailed engagement wastes their time and risks backlash.

---

## Section 4: Choosing a BA Approach — Predictive vs. Adaptive
One of the first decisions a BA makes in planning is choosing an overall approach that fits the project context. BABOK describes two broad approaches: predictive and adaptive.

A predictive approach — often called waterfall — works best when requirements are stable and well-understood, the solution technology is mature, regulatory constraints require complete documentation before construction, or a fixed deadline is non-negotiable. Think of a government contract with defined regulatory compliance requirements, or a banking system replacement where every rule must be documented and signed off before a single line of code is written.

An adaptive approach — Agile frameworks like Scrum or Kanban — works best when requirements are likely to evolve, when frequent stakeholder feedback is available and valuable, or when speed of delivery is more important than comprehensive upfront documentation. We will go deep on Agile BA work in Module 14.

Most real projects are hybrid. An organization might use Agile sprints for development but require a formal requirements sign-off document before any sprint can begin. The BA's job in planning is to understand the project context and choose an approach that fits — not to apply a methodology dogmatically.

> IIBA ECBA Exam Tip: Exam scenarios that describe fixed scope, regulatory requirements, or a mandated deadline almost always favor the predictive approach. Scenarios describing innovative products, high stakeholder uncertainty, or rapidly changing business conditions favor the adaptive approach. When a question gives you both characteristics, look for the dominant one.

---

## Section 5: BA Performance Monitoring and Closing
The last task in KA 2 is Identify Business Analysis Performance Improvements. This is the monitoring function — it asks the BA to step back periodically and evaluate whether the BA work itself is going well.

What does that look like in practice? The BA tracks metrics like: Are elicitation sessions producing useful information? Are stakeholder reviews happening on schedule? Are requirement defects being caught in review or discovered late in testing? Are stakeholders satisfied with the quality of requirements documentation?

When metrics show that BA performance is falling short — perhaps interviews are being skipped, or requirements documents are returning from review with high defect rates — the BA analyzes the root cause and updates the BA plan accordingly. This is not about blaming people. It is about treating BA work the same way any professional treats their craft: with systematic reflection and continuous improvement.

Let me close with your exam preparation points for this module. Know the five tasks of KA 2. Know the four quadrants of the Power-Interest Grid and the engagement strategy for each. Know the difference between predictive and adaptive approaches and the conditions that favor each. And know that when a BA monitoring scenario appears on the exam, the answer involves analyzing the variance and updating the plan — not escalating immediately or skipping steps.

For the lab this week, you will analyze a case study stakeholder list and position each stakeholder on the Power-Interest Grid. You will then write an engagement strategy for each quadrant as it applies to your case. Good luck — I will see you in the discussion forum.

---

## End Card

## Module 02 Complete

Next: Module 03 - Requirements Elicitation Techniques

### Additional Resources

- iiba.org — BABOK Guide v3 KA 2 overview and task summaries
- iiba.org — ECBA exam blueprint with KA 2 weighting information
