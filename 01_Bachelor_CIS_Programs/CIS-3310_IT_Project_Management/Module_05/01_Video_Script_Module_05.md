# Video Script: Module 05 – Cost Management: Budgeting and EVM

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Google Career Certificates &bull; IT Project Management &bull; Module 05</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLnWPid_vGmUaA620wv1XP0c05G4DiG6Jz" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLnWPid_vGmUaA620wv1XP0c05G4DiG6Jz" title="Google Career Certificates &bull; IT Project Management" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Google Career Certificates &bull; IT Project Management</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Course:** CIS-3310 IT Project Management
**Estimated Duration:** 23 minutes
**Certification Alignment:** CompTIA Project+ (PK0-005) | PMBOK 6th and 7th Editions
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Section 1: Welcome and Module Overview
Welcome back to CIS-3310. I am Professor Nash, and this is Module 05: Cost Management. We have defined scope and built the schedule — now we need to determine how much all of that work will cost and how we will monitor our spending throughout the project.

This module has two major components: budgeting (how we estimate and establish the cost baseline) and Earned Value Management, which is the most calculation-intensive topic on the Project+ exam.

 Module 05 title: "Cost Management — Budgeting and EVM

Today we cover four topics: the cost management process flow; cost estimating techniques; the Cost Baseline and reserves; and Earned Value Management formulas and interpretation.

---

## Section 2: Cost Management Process Flow
PMI defines four processes in Cost Management.

Plan Cost Management develops the cost management plan — the rules for how costs will be estimated, budgeted, and controlled.

Estimate Costs produces cost estimates for each activity or work package. We use several techniques: analogous, parametric, bottom-up, and three-point estimating.

Determine Budget aggregates the activity cost estimates and adds contingency reserves to produce the Cost Baseline. The Cost Baseline is the approved, time-phased spending plan.

Control Costs monitors actual spending against the Cost Baseline, calculates Earned Value metrics, and manages changes to the budget.

 Cost management process chain

---

## Section 3: Cost Estimating Techniques
There are four primary estimating techniques, and the exam tests your ability to choose the right one for a given situation.

Analogous estimating uses data from similar past projects as the basis for the current estimate. It is fast but less accurate. Best used early in the project when scope detail is limited. Accuracy range: roughly -25% to +75% (a ROM estimate).

Parametric estimating uses a statistical relationship between project variables and costs. For example: $500 per server migrated, or 8 hours per application module. It requires reliable unit rate data but is faster than bottom-up.

Bottom-up estimating builds the budget from the ground up by estimating every work package and rolling the totals up through the WBS. Most accurate but most time-consuming. Requires a complete WBS.

Three-point estimating (PERT) applies the formula (O + 4M + P) / 6 to generate a weighted average estimate for individual activities when uncertainty is high.

> **Project+ Exam Tip:** When the exam says "most accurate" estimating technique, the answer is always bottom-up. When the exam says "fastest" or "early phases" or "limited information available," the answer is analogous. Know when to use each.

---

## Section 4: Cost Baseline and Reserves
 Cost Baseline vs. Project Budget diagram

The Cost Baseline is the approved, time-phased budget used as the reference for measuring cost performance. It includes contingency reserves but does NOT include management reserves.

Here is the hierarchy you must memorize:

Work Package Estimates + Activity Contingency Reserves = Cost Baseline.

Cost Baseline + Management Reserves = Project Budget (also called the Cost Budget or Total Funding Requirement).

Contingency reserves are budgeted for known risks — risks documented in the Risk Register. The PM controls contingency reserves and can spend them when a documented risk occurs without seeking additional approval.

Management reserves are funds held by senior management for completely unforeseen events — unknown unknowns. The PM must request management reserve from senior leadership. Management reserve is NOT part of the Cost Baseline.

> **Project+ Exam Trap:** If an exam question says a PM sets aside money for "identified risks in the risk register," the answer is Contingency Reserve. If it says "completely unforeseen events," the answer is Management Reserve. These are different buckets. Getting this wrong is one of the most common exam mistakes.

---

## Section 5: Earned Value Management
 EVM formula reference card

Earned Value Management (EVM) is a performance measurement technique that integrates scope, schedule, and cost into a single quantitative framework. It is the most heavily tested topic in Cost Management.

Three core values:

Planned Value (PV) is the authorized budget assigned to the work that was scheduled to be done by the current date. PV comes from the Cost Baseline.

Actual Cost (AC) is the total cost actually incurred to accomplish the work performed during a given time period. AC is what you actually spent.

Earned Value (EV) is the budgeted value of work actually completed. EV = Percent Complete × BAC (Budget at Completion). EV answers the question: "How much value have we actually produced?

 S-curve with PV, EV, and AC plotted

From these three values, we calculate variances and indices:

Cost Variance (CV) = EV - AC. Negative CV means over budget. Positive CV means under budget.

Schedule Variance (SV) = EV - PV. Negative SV means behind schedule. Positive SV means ahead of schedule. Note: SV is expressed in dollars, not days.

Cost Performance Index (CPI) = EV / AC. CPI < 1.0 means over budget (spending more than earning). CPI > 1.0 means under budget.

Schedule Performance Index (SPI) = EV / PV. SPI < 1.0 means behind schedule. SPI > 1.0 means ahead of schedule.

Estimate at Completion (EAC) = BAC / CPI. This is the most common EAC formula — it assumes future work will continue at the current spending efficiency.

Estimate to Complete (ETC) = EAC - AC. How much more do we expect to spend?

Variance at Completion (VAC) = BAC - EAC. Positive VAC means under budget at completion; negative VAC means over budget at completion.

> **Project+ Exam Tip:** On any EVM question, write down your three knowns (PV, EV, AC) and BAC first. Then apply the formula. The most common exam trap is calculating CV when the question asks for SV, or vice versa. CV uses AC; SV uses PV. Remember: C for Cost, A for Actual. S for Schedule, P for Planned.

---

## End Card
Module 05 is complete. Your assignments: complete the Reading Guide which has a full EVM formula reference; complete the Lab with hands-on EVM calculation exercises; take the Quiz; post your Discussion by Wednesday.

Study resources for EVM formulas: professormesser.com and comptia.org.

Module 06 covers Quality Management — quality planning, quality assurance, quality control tools, and the seven basic quality tools. See you there.

---

## Additional Resources

- CompTIA Project+ exam objectives and study resources: comptia.org
- Free study notes and practice materials: professormesser.com
