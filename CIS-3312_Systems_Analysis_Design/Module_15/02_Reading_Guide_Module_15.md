# Reading Guide: Module 15 — Implementation, Change Management, and Transition

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Overview

This reading guide supports Module 15's video lecture on implementation, change management, and transition. The BABOK Guide addresses these topics primarily within the Solution Evaluation knowledge area and through the Change Strategy technique. For ECBA candidates, understanding that successful implementation requires both technical and organizational components is essential.

**Estimated reading and study time:** 90–120 minutes

---

## Learning Objectives

By the end of this module you will be able to:

1. Compare the four primary deployment strategies and select the appropriate one for a given scenario.
2. Explain the ADKAR model and diagnose which stage is blocking adoption in a described situation.
3. Develop a structured training plan with audience segmentation and modality selection.
4. Plan and conduct a post-implementation review.
5. Describe the components of a transition plan.
6. Connect implementation and change management to the ECBA Solution Evaluation knowledge area.

---

## Section 1 — Why Implementation Phase Failures Are Different

### 1.1 The Implementation Paradox

Implementation failures are particularly frustrating because they often occur after the hardest work is done. The requirements have been gathered. The system has been built and tested. UAT has been signed off. And then the project fails — not because of technology, but because of people.

Research by Prosci and McKinsey consistently finds that 70% of organizational change initiatives fail to achieve their intended outcomes. The leading causes are not technical. They are resistance from employees, inadequate management support, insufficient training, and poor communication.

This does not mean technical quality is unimportant. It means that technical quality is necessary but not sufficient. A BA who treats go-live as the finish line misunderstands what success means.

### 1.2 The BA's Role in Implementation

The BABOK Guide identifies Solution Evaluation as the knowledge area covering assessment of how well a deployed solution meets business needs. BAs contribute to implementation by:

- Supporting deployment planning
- Facilitating change management activities
- Developing or reviewing training plans
- Conducting post-implementation reviews
- Ensuring the transition to operations is complete

---

## Section 2 — Deployment Strategies

### 2.1 Big Bang (Direct Cutover)

The entire user population switches from the old system to the new system simultaneously on a defined cutover date.

Suitable when:

- The old and new systems cannot coexist technically
- The cost of parallel operation is prohibitive
- The system scope is limited and rollback procedures are robust

Risk factors:

- Highest risk deployment strategy
- Any critical defect discovered post-cutover affects all users immediately
- Rollback may be technically impossible or extremely costly

Mitigation practices:

- Conduct thorough pre-cutover testing including load tests
- Define and test rollback procedures explicitly
- Schedule cutover during low-traffic periods (weekends, off-peak hours)
- Have extended support staffing during the immediate post-cutover period

### 2.2 Phased Rollout

Deployment occurs incrementally across organizational units, geographic regions, or functional areas on a staggered schedule.

Suitable when:

- The organization is geographically distributed
- Different business units can be isolated for transition purposes
- Earlier deployment phases can inform and improve later ones

Risk factors:

- Managing two systems simultaneously increases operational complexity
- Data synchronization between old and new systems during transition requires careful design
- Users in later phases may lose confidence as they wait

Mitigation practices:

- Define clear phase boundaries and cutover dates for each phase
- Establish a data bridge or integration layer if the two systems must share data during transition
- Communicate the phased timeline clearly so later-phase users understand when their transition occurs

### 2.3 Parallel Operation

Both the old and new systems operate simultaneously. Users perform work in both, and results are compared to verify the new system is producing correct outputs.

Suitable when:

- The system handles high-consequence transactions (payroll, financial ledgers, safety controls)
- Data correctness must be verified empirically, not just theoretically
- Regulatory requirements mandate a parallel period

Risk factors:

- Extremely expensive in labor costs
- Users performing double work increases error rates
- Parallel periods tend to extend beyond plan as stakeholders become reluctant to commit to the new system

Mitigation practices:

- Define a strict parallel period end date before parallel operation begins
- Establish objective reconciliation criteria that trigger cutover
- Limit parallel operation to the highest-risk modules rather than the entire system

### 2.4 Pilot Deployment

The new system goes live for a selected subset of users — a pilot group — before full organizational deployment.

Suitable when:

- The full user population is large and a small-scale test is feasible
- Training approaches need refinement before scaled deployment
- Real-world validation of integration points is needed under controlled conditions

Risk factors:

- Pilot group must be representative; an atypically tech-savvy pilot group will not surface problems that average users will encounter
- Pilot success can create premature confidence if the pilot group was not representative

Mitigation practices:

- Select pilot participants who represent the full demographic range of eventual users
- Define specific success metrics for the pilot before it begins
- Conduct a formal pilot debrief before proceeding to full rollout

### 2.5 Hybrid Strategies

Most large-scale implementations use combinations. A pilot validates the approach; a phased rollout manages scale; parallel operation protects the highest-risk modules. BAs document the deployment strategy in the project plan and communicate the rationale to stakeholders.

---

## Section 3 — Change Management Frameworks

### 3.1 Why Change Management Is a BA Responsibility

Some project teams treat change management as a communications activity handled by HR or a dedicated change manager. In practice, BAs are uniquely positioned to contribute because they have the deepest understanding of how processes are changing and what impacts those changes will have on specific user groups.

The BABOK Guide describes Change Strategy as a technique within Enterprise Analysis and Solution Evaluation. The technique involves identifying how the organization will move from its current state to the desired future state, including the human adoption component.

### 3.2 The ADKAR Model

ADKAR is a sequential model of individual change. Each letter names a milestone that must be achieved before the next one is possible.

#### Awareness

Awareness means the individual understands why the change is necessary — the business case, the urgency, and the consequences of not changing. Without awareness, individuals cannot rationally decide whether to support or resist the change.

BA contribution: ensure that stakeholder communications clearly explain not just what is changing but why. Business analysts are often in the best position to articulate the business case in terms that are meaningful to front-line users.

#### Desire

Desire means the individual is motivated to support and participate in the change. Awareness creates the rational case. Desire is the emotional and motivational component.

BA contribution: during requirements and design phases, involve end users in decisions. Participation builds ownership. Users who helped shape the system are more likely to desire its success.

#### Knowledge

Knowledge means the individual knows how to change — specifically what to do differently, how to use the new system, and what the new process looks like. This is the domain of training.

BA contribution: review training materials to confirm they reflect actual system behavior and process changes. Training built on incorrect or incomplete requirements will leave users with knowledge gaps.

#### Ability

Ability means the individual can perform the required behaviors in their actual job, not just in a training environment. Knowledge and Ability are distinct. Someone may know how to perform a task in a classroom setting but struggle when performing it under real production conditions for the first time.

BA contribution: advocate for supervised practice environments and go-live support resources that bridge the gap between training and real performance.

#### Reinforcement

Reinforcement means the change is sustained. Without active reinforcement, individuals and groups tend to revert to familiar behaviors. Reinforcement includes recognition, corrective feedback, performance metrics tied to the new behaviors, and embedding the change into standard processes.

BA contribution: include reinforcement mechanisms in the post-implementation review plan. Track adoption metrics. Flag reversion to old behaviors as a finding requiring intervention.

### 3.3 Diagnosing Adoption Barriers with ADKAR

The power of ADKAR as a diagnostic tool is that it identifies where in the change process a specific individual or group is blocked. Once the blocked stage is identified, the intervention becomes clear.

| Blocked at | Symptom | Intervention |
|---|---|---|
| Awareness | "I don't understand why we're doing this" | Targeted communication from leadership |
| Desire | "I know why but I don't support it" | One-on-one conversations, address personal concerns |
| Knowledge | "I want to but I don't know how" | Training, job aids, coaching |
| Ability | "I know how but I struggle doing it" | Supervised practice, go-live floor support |
| Reinforcement | "I was doing it but I slipped back" | Recognition programs, accountability measures |

### 3.4 Other Change Management Frameworks

ADKAR is the most common in IT project contexts, but BAs should be aware of other frameworks:

Kotter's 8-Step Model addresses change at the organizational level rather than the individual level. It is used for large-scale transformation initiatives.

McKinsey's 7-S Framework examines organizational alignment across seven elements: Strategy, Structure, Systems, Shared Values, Style, Staff, and Skills.

For ECBA purposes, ADKAR is the most relevant framework. Familiarity with the other frameworks adds breadth but ADKAR is the expected working knowledge.

---

## Section 4 — Training Plans

### 4.1 Training Plan Components

A complete training plan documents:

- Training objectives by audience segment
- Audience segmentation and estimated participant counts
- Training modalities selected for each segment
- Training schedule with dates relative to go-live
- Trainer qualifications and assignments
- Training environment and logistics
- Materials list with development status
- Competency verification approach
- Go-live support plan

### 4.2 Audience Segmentation

Different user groups have different learning needs, different schedules, and different relationships to the new system. Effective training plans segment the audience before designing content.

Segmentation dimensions include:

- Role (what functions does this group perform?)
- Frequency of system use (daily power users vs. occasional users)
- Technical comfort level
- Geographic location (affects modality options)
- Organizational level (executives need different content than front-line staff)

### 4.3 Training Modalities

| Modality | Best for | Limitations |
|---|---|---|
| Instructor-led classroom | Complex workflows, interactive Q&A | Scheduling complexity, travel cost |
| Virtual instructor-led | Distributed teams | Requires engagement facilitation skills |
| Self-paced e-learning | Consistent delivery at scale | No real-time Q&A, requires learner self-discipline |
| Job aids and quick reference cards | Point-of-use reference | Not a substitute for procedural training |
| Peer mentoring | Building internal champions | Requires identifying and training mentors |
| Sandbox practice environment | Bridging knowledge to ability | Requires a maintained test environment |

### 4.4 Training Timing

Training delivered too early is forgotten. Training delivered too late leaves users unprepared. The professional standard: complete core training within two weeks of go-live, with the practice environment accessible immediately after training and through the go-live period.

### 4.5 Go-Live Support

Training alone is insufficient for most users on day one. Go-live support supplements training with real-time assistance during the period of highest adoption stress. Common go-live support mechanisms:

- Dedicated phone or chat support queue
- Floor walkers stationed in work areas during initial days
- "Super users" embedded within business units who received advanced training
- Clear escalation path to the project team for issues that floor walkers cannot resolve

---

## Section 5 — Post-Implementation Review

### 5.1 Purpose and Timing

The post-implementation review (PIR) confirms whether the deployed solution delivered its intended business value. Timing is important: the PIR must occur after enough time has passed for meaningful operational data to exist — typically thirty to ninety days post-go-live.

### 5.2 Business Value Measurement

The PIR compares actual outcomes against the metrics defined in the original business case. Common measurement dimensions include:

- Process efficiency (cycle time, error rate, transaction volume)
- Cost reduction or avoidance
- Revenue impact
- User satisfaction (measured through surveys or adoption metrics)
- System availability and performance against SLAs

If the business case projected specific, quantifiable outcomes, the PIR measures those outcomes specifically. If outcomes fall short, the PIR identifies contributing factors and recommends corrective actions.

### 5.3 Lessons Learned

The lessons-learned component of the PIR captures what the project team and organization would do differently on the next project. Topics typically covered:

- Requirements elicitation effectiveness
- Change management and communication
- Training adequacy
- Deployment strategy execution
- Testing completeness
- Stakeholder engagement

Lessons learned are only valuable if they are documented, shared, and acted upon. A lessons-learned report filed in a shared drive and never read provides zero organizational benefit.

### 5.4 Residual Issues Register

The PIR also produces a residual issues register: a list of outstanding problems, deferred defects, process gaps, and enhancement requests that emerged post-go-live. Each item should have an owner, a target resolution date, and a priority classification.

---

## Section 6 — Transition Planning

### 6.1 Transition to Operations

Project teams are temporary. Operations teams are permanent. Transition planning ensures that when the project team disbands, the operations team can maintain, support, and evolve the system.

### 6.2 Transition Plan Components

A complete transition plan addresses:

- Operations team contacts and responsibilities
- Help desk procedures and escalation paths
- Service level agreements for availability and incident response
- Documentation repository location (technical and user documentation)
- Change request and enhancement request processes
- Vendor and support contract details
- Disaster recovery and business continuity procedures

### 6.3 Knowledge Transfer

The most critical transition activity is knowledge transfer from the project team to operations. This includes:

- System architecture documentation
- Configuration and deployment procedures
- Known issues and workarounds
- Vendor contact information
- License keys and credential management

---

## Key Terms

| Term | Definition |
|---|---|
| Big bang deployment | Simultaneous cutover of all users from old to new system |
| Phased rollout | Incremental deployment across organizational units or regions |
| Parallel operation | Running old and new systems simultaneously with output comparison |
| Pilot deployment | Limited-scope go-live with a representative subset of users |
| ADKAR | Prosci change model: Awareness, Desire, Knowledge, Ability, Reinforcement |
| Change management | Discipline of preparing and supporting people through organizational change |
| Training plan | Document defining who receives training, on what, how, and when |
| Competency verification | Process for confirming that training participants can perform required tasks |
| Post-implementation review | Structured evaluation of whether a deployed solution delivered its intended value |
| Lessons learned | Documented insights from a completed project for future process improvement |
| Transition plan | Document formalizing handoff of system responsibility from project team to operations |
| Go-live support | Resources available to users immediately after system deployment |

---

## Self-Check Questions

Answer these before attempting the quiz.

1. In which scenario would parallel operation be most appropriate?
2. What does the "D" in ADKAR represent, and how is it different from Awareness?
3. Why should training be completed within two weeks of go-live rather than a month before?
4. What is the difference between Knowledge and Ability in the ADKAR model?
5. Name three components of a post-implementation review.
6. Why is a lessons-learned report only valuable if acted upon?
7. What is the purpose of a transition plan, and what happens when one is not created?

---

## Supplemental Resources

The following open educational resources extend module content on implementation, change
management, and transition planning. All are freely accessible without login or purchase.

1. **ADKAR Model Overview — Prosci Change Management**
   <https://www.prosci.com/methodology/adkar>
   Focus: The authoritative source for the ADKAR model covering each stage in depth,
   diagnostic applications, and intervention design. Directly supports Part 2 of the lab
   and reinforces Section 3 of this reading guide for ECBA exam preparation.

2. **Kotter's 8-Step Change Model — Kotter International**
   <https://www.kotterinc.com/methodology/8-steps/>
   Focus: The organizational-level change framework referenced in Section 3.4 of this
   reading guide. Comparing ADKAR (individual level) with Kotter's model (organizational
   level) deepens understanding of why both frameworks are used on large-scale
   implementations.

3. **Solution Evaluation Knowledge Area — IIBA BABOK Guide**
   <https://www.iiba.org/standards-and-resources/babok/>
   Focus: The BABOK Guide's coverage of Solution Evaluation, including performance
   measurement, solution limitations assessment, and recommendations for improvement.
   Reinforces the PIR content in Section 5 and the ECBA exam alignment throughout
   this module.

4. **Post-Implementation Review Guide — Project Management Institute**
   <https://www.pmi.org/learning/library/post-project-review-7195>
   Focus: Practical guidance on structuring and facilitating post-implementation reviews,
   including agenda design, metrics selection, lessons-learned documentation, and
   follow-through processes. Supports Part 4 of the lab directly.

5. **Deployment Strategy Comparison — Atlassian DevOps Resources**
   <https://www.atlassian.com/continuous-delivery/principles/deployment-strategies>
   Focus: Clear comparison of deployment strategies — including big bang, phased, canary
   (pilot), and blue-green (parallel) approaches — with visual diagrams and risk
   assessments. Supplements Section 2 of this reading guide and supports the strategy
   selection task in Part 1 of the lab.

---

*Module 15 Reading Guide | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
