# Video Script: Module 15 — Implementation, Change Management, and Transition

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Production Notes

- **Runtime Target:** 20–24 minutes
- **Format:** Lecture with process diagrams and real-world scenario walk-throughs
- **Slides:** Approximately 26 slides

---

## SEGMENT 1 — Introduction (0:00–2:30)

[OPEN on slide: "Module 15 — Implementation, Change Management, and Transition"]

Welcome back to CIS-3312. I'm Professor Nash. We are in Module 15, which covers one of the most underestimated phases in any systems project: implementation, change management, and transition.

Here is something every experienced BA knows: you can deliver a technically perfect system and still have the project fail. Not because the code was wrong. Not because the requirements were missed. But because the people whose jobs changed did not understand why, did not know how to use the new system, or did not trust it.

Technology does not transform organizations. People adopting technology transforms organizations. And getting people to adopt new technology — especially when it changes how they work every day — requires deliberate, skilled change management.

In this module we cover four interconnected topics. We start with deployment strategies — the mechanics of how a new system goes live. Then we look at change management frameworks, specifically ADKAR, which is the most widely used model in IT-related organizational change. We discuss training plan development. And we close with the post-implementation review — what happens after go-live to confirm the system delivered its intended value.

Let's get into it.

---

## SEGMENT 2 — Deployment Strategies (2:30–6:30)

[SLIDE: "Deployment Strategies — Four Approaches"]

Before we talk about change management, let's talk about the mechanics of deployment. How does the new system actually replace the old one?

There are four primary strategies, and each involves a different risk and cost profile.

### Big Bang Deployment

In a big bang deployment — also called direct cutover — the old system is turned off and the new system goes live on a specific date. All users switch at the same time.

Advantages: simple to manage, no need to run two systems in parallel, lower cost.

Disadvantages: maximum risk. If something goes wrong, you cannot easily fall back. There is no old system running to catch failures.

Big bang is appropriate when: the old system is so fundamentally incompatible with the new one that parallel operation is impractical, or when the cost of parallel operation exceeds the risk of a direct switch.

### Phased Rollout

In a phased rollout, the new system is deployed incrementally — by department, by region, by function, or by user group. Each phase goes live on a staggered schedule.

Advantages: lower risk per phase, lessons from early phases inform later deployments, support resources can be concentrated on a smaller group at each phase.

Disadvantages: longer total deployment timeline, added complexity of managing two systems simultaneously during the transition, potential inconsistency across the organization during the phased period.

### Parallel Operation

In parallel operation, both the old and new systems run simultaneously for a defined period. Users perform the same work in both systems, and results are compared.

Advantages: maximum safety net. If the new system produces wrong results, the old system catches it.

Disadvantages: extremely expensive. Users must do all their work twice. Data entry errors increase. The "parallel period" often extends longer than planned when users are reluctant to trust the new system.

Parallel operation is most appropriate for high-risk, high-consequence systems — payroll, financial ledgers, safety-critical applications.

### Pilot Deployment

In a pilot deployment, the new system goes live for a small, controlled group of users before the full organization deploys.

Advantages: real-world validation in a low-risk environment, allows training refinement, surfaces integration issues with minimal impact.

Disadvantages: pilot group must be representative of the full user population or results will not generalize.

Many organizations combine strategies: a pilot for initial validation, followed by a phased rollout, with parallel operation reserved for the highest-risk modules.

---

## SEGMENT 3 — Change Management Frameworks (6:30–11:30)

[SLIDE: "ADKAR — The Change Management Framework"]

Now let's talk about change management — the discipline of ensuring that people successfully adopt organizational change.

The most widely used model in IT project contexts is ADKAR, developed by Prosci. ADKAR is an acronym. Each letter represents a stage that an individual must work through to successfully adopt a change.

**A — Awareness.** The person understands why the change is happening. Not just "we are getting a new system" but "we are getting a new system because the old one cannot handle our growth, and without it we will face regulatory penalties by year end."

Without Awareness, people do not understand why they should engage with the change. Resistance begins here.

**D — Desire.** The person wants to participate in and support the change. Awareness that a change is necessary does not automatically produce desire to support it. Desire is influenced by personal motivation — will this make my job easier or harder? — and by trust in leadership.

**K — Knowledge.** The person knows how to change — specifically, how to use the new system or process. This is where training lives. Note that Knowledge cannot come before Desire. Training someone who does not want to learn is ineffective.

**A — Ability.** The person can demonstrate the required behaviors and skills in their actual job. Knowledge (knowing how) and Ability (being able to do it under real conditions) are different. A classroom demonstration does not equal job-ready performance.

**R — Reinforcement.** The change is sustained over time. This includes recognizing early adopters, addressing reversion to old behaviors, and embedding the new way of working into standard processes and performance management.

ADKAR is not just a theory — it is a diagnostic tool. When adoption is failing, you can ask: at which ADKAR stage is this person or group blocked? The answer tells you the intervention needed.

[SLIDE: "Common Change Failure Points"]

Where do most change efforts fail? Research consistently points to three places.

First: Awareness is assumed rather than communicated. Leaders believe "everyone knows about this project" when front-line staff have never heard of it.

Second: Desire is never built. The change is announced as a mandate with no explanation of the benefit to the people doing the work. Mandate compliance is not adoption.

Third: Reinforcement is skipped. The project team celebrates go-live and moves to the next project. Six months later, half the staff have reverted to spreadsheets and workarounds.

As a BA, your contribution to change management is ensuring that the people side of the change is planned with the same rigor as the technical side.

---

## SEGMENT 4 — Training Plans (11:30–15:30)

[SLIDE: "Training Plans — Structure and Design"]

Training is the Knowledge component of ADKAR. A training plan is the structured document that defines who will be trained, on what, by whom, in what format, and by when.

A complete training plan addresses several dimensions.

**Audience segmentation.** Different user groups need different training. A warehouse manager using the inventory management module needs different training than an executive viewing reports. A power user who handles exceptions needs deeper training than a casual user who performs one transaction type. Segment your audiences and build training tracks for each.

**Training modalities.** Options include instructor-led classroom training, virtual instructor-led training, self-paced e-learning modules, job aids and quick reference cards, peer mentoring programs, and hands-on sandbox environments. Most effective training programs combine modalities — a short instructor-led overview followed by hands-on practice, supplemented by job aids at the workstation.

**Training schedule.** Timing matters. Training delivered too early is forgotten before go-live. Training delivered too late leaves users unprepared on day one. Best practice: complete training within two weeks of go-live, with a hands-on practice environment available immediately after.

**Competency verification.** How will you confirm that training worked? Options include knowledge checks (quizzes), observed performance in a sandbox environment, sign-off by a supervisor or trainer that the learner can perform core tasks independently.

**Training materials.** User guides, quick reference cards, annotated screenshots, video walk-throughs. Materials should be written for the audience's vocabulary — business language, not technical jargon.

**Go-live support.** Even well-trained users need support on day one. Go-live support typically includes a dedicated help desk channel, "floor walker" staff who circulate in the work area, and a direct escalation path to the project team for critical issues.

---

## SEGMENT 5 — Post-Implementation Review (15:30–19:30)

[SLIDE: "Post-Implementation Review — Did We Deliver the Value?"]

The post-implementation review, or PIR, is a structured evaluation conducted after the system has been live long enough for real performance data to be available. Typically thirty, sixty, or ninety days after go-live.

The PIR answers three fundamental questions.

**Did the system deliver its intended business value?** Compare actual outcomes against the business case. Did processing time decrease? Did error rates fall? Did revenue targets improve? If the business case projected a 20% reduction in processing time and the actual result is 8%, that is a finding.

**What went well, and what should be done differently next time?** The PIR is a lessons-learned exercise. It is not a blame session. The goal is to capture organizational knowledge so future projects benefit from this one's experience.

**What residual issues require attention?** Deferred defects, training gaps, process adjustments, integration issues that only surfaced under real production load — all of these should be inventoried and assigned to owners.

A PIR is not a project management audit. It is a forward-looking activity. The key deliverable is a recommendations report that feeds into the ongoing operations plan and the organization's project methodology improvement process.

[SLIDE: "PIR Structure"]

A standard PIR includes:

- Business value measurement against baseline metrics from the business case
- User adoption metrics — are people actually using the system as intended?
- System performance metrics — response time, uptime, error rates
- Defect summary — how many production incidents since go-live, what categories?
- Change management effectiveness — did the training work? where are adoption gaps?
- Lessons learned — what would the team do differently?
- Recommendations — specific, owned, time-bound action items

The BA's role is to facilitate the PIR, gather data from stakeholders and system monitoring, and produce the recommendations report. This report is delivered to the project sponsor and, typically, to a project review board or PMO.

---

## SEGMENT 6 — Transition Planning (19:30–21:30)

[SLIDE: "Transition Planning — Handing Off to Operations"]

One final topic before we wrap: transition planning. This is the process of formally handing responsibility for the new system from the project team to the operations team.

A transition plan documents:

- Who is responsible for ongoing system administration
- How incidents and service requests will be handled
- What service level agreements govern system availability
- Where documentation, source code, and configuration records are maintained
- What the support escalation path looks like
- How future enhancements will be requested and prioritized

Without a transition plan, the project team stays informally responsible for the system indefinitely. Every question goes back to the original developers. The organization never truly owns the system.

The BA's role in transition: ensure that the operations team has everything they need — documentation, training, escalation contacts — before the project team disbands.

---

## SEGMENT 7 — Module Wrap-Up (21:30–23:30)

[SLIDE: "Module 15 Summary"]

Let's close with the key takeaways from Module 15.

Deployment strategies — big bang, phased rollout, parallel operation, and pilot — each involve different risk and cost trade-offs. The BA helps select the right strategy by analyzing system complexity, business risk, and organizational readiness.

The ADKAR model frames individual change as five sequential stages: Awareness, Desire, Knowledge, Ability, Reinforcement. Most change failures trace to a specific blocked stage.

Training plans must segment audiences, select appropriate modalities, time delivery near go-live, and include competency verification and go-live support.

The post-implementation review measures actual business value against the business case, captures lessons learned, and produces actionable recommendations.

Transition planning hands off formal responsibility from the project team to operations.

For ECBA preparation, focus on change management as a BA responsibility and the components of a transition plan. These topics appear in the Solution Evaluation knowledge area of the BABOK Guide.

Complete your reading guide, lab, and quiz. Module 16 is our final module — ECBA exam preparation and the capstone.

[END]

---

*Total runtime estimate: 21–23 minutes*
