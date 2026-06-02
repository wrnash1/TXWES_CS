# Video Script: Module 01 - Introduction to Systems Analysis and the SDLC

**Course:** CIS-3312 Systems Analysis and Design
**Estimated Duration:** 22 minutes
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.
- Speaker notes in italics are delivery reminders, not spoken aloud.
- All diagrams should use high-contrast colors for accessibility.

---

## Section 1: Welcome and Module Overview [00:00 - 03:30]

Hello, everyone, and welcome to Module 01 of CIS-3312 Systems Analysis and Design. I am Professor Nash at Texas Wesleyan University, and I am glad you are here. This module sets the foundation for everything you will learn in this course, and it is directly aligned to the IIBA Entry Certificate in Business Analysis — the ECBA certification — so every concept we cover today is also an investment in your professional credentials.

[SHOW DIAGRAM: Title slide — "Module 01: Introduction to Systems Analysis and the SDLC" with the IIBA ECBA logo and Texas Wesleyan University crest]

Let me give you a quick roadmap of what we are covering today. We have four main sections. First, we will define what a system is and why organizations invest in systems analysis. Second, we will walk through the SDLC phases in order, and I will make sure you understand what happens in each one. Third, we will establish the role of the business analyst and how it fits into the SDLC. Finally, we will close with certification exam tips and a preview of this week's lab.

One thing I want to say upfront: do not think of this module as "just theory." The ECBA exam is scenario-based, which means it will describe a real project situation and ask you to apply these concepts. Understanding them deeply — not just memorizing definitions — is the key to passing.

---

## Section 2: What Is a System and Why Does Systems Analysis Exist? [03:30 - 08:00]

Let us start with the word "system." A system is a collection of interrelated components that work together to achieve a common purpose. That is a broad definition, and intentionally so. An airline reservation system, a university course registration system, a hospital patient records system — they all fit this definition. They have inputs, processing activities, outputs, a boundary separating them from their environment, and feedback loops.

[SHOW DIAGRAM: System components diagram — rectangle labeled "System" with arrows labeled "Inputs" entering from the left, "Processing" in the center, "Outputs" exiting right, a dashed boundary rectangle, and a "Feedback" arrow looping from output back to input]

So why does systems analysis exist as a discipline? Because building or changing a system is expensive and risky, and most project failures trace back to requirements problems — not technology problems. Standish Group research consistently shows that inadequate requirements are among the top causes of project failure. Scope creep, missed stakeholder needs, systems that work perfectly but solve the wrong problem — all of these are requirements failures.

Systems analysis is the formal process of studying a problem domain, identifying what stakeholders actually need, and producing a clear statement of requirements before anyone builds anything. Think of it as the bridge between the problem and the solution.

Now, the BABOK Guide — which is the primary reference for the IIBA ECBA exam — defines business analysis as "the practice of enabling change in an enterprise by defining needs and recommending solutions that deliver value to stakeholders." Write that definition down. It will appear on your exam.

> IIBA ECBA Exam Tip: The ECBA exam frequently tests the distinction between the roles of the business analyst, the project manager, and the developer. The BA defines what needs to be built. The PM manages when and how much it costs to build it. The developer builds it. These are complementary but distinct roles. A common trap question will blend them — know the boundaries.

---

## Section 3: The Software Development Life Cycle [08:00 - 14:30]

[SHOW DIAGRAM: SDLC phase waterfall diagram — five sequential boxes labeled: 1. Planning, 2. Systems Analysis, 3. Systems Design, 4. Implementation, 5. Maintenance and Support — connected by downward arrows]

The Software Development Life Cycle, or SDLC, is the structured framework that guides organizations through the process of building or changing an information system. Every methodology — Waterfall, Agile, Spiral, Iterative — has the same core phases. The methodology determines how you sequence and repeat them. Let us walk through the five classic phases.

Phase one is Planning. This is where the organization decides whether to pursue the project at all. The primary deliverable is a Project Charter or a Feasibility Study. The feasibility study asks four questions: Can we build it? — that is technical feasibility. Should we build it from a financial standpoint? — that is economic feasibility. Will people use it? — that is operational feasibility. Are there any legal or regulatory constraints? — that is legal feasibility. We will go deep on feasibility in Module 08.

Phase two is Systems Analysis. This is the BA's home phase. The goal here is to understand what the new or improved system must do. The BA elicits requirements from stakeholders, documents them precisely, and gets stakeholder sign-off before design begins. The deliverables are a Requirements Specification, a stakeholder analysis, and often process models and diagrams. We will spend most of this course on this phase.

Phase three is Systems Design. Armed with approved requirements, the team now decides how the system will work. Logical design describes what functions the system will perform using technology-neutral models. Physical design specifies the actual technology — which database, which programming language, which cloud platform. Module 09 covers this in detail.

Phase four is Implementation. Developers write code. Testers run test cases. Users are trained. Data is migrated from legacy systems. This phase ends with deployment — the system goes live. Module 12 covers testing and Module 13 covers implementation strategy.

Phase five is Maintenance and Support. Most systems spend the majority of their useful lives in this phase. Users submit bug reports, request enhancements, and the team evaluates, prioritizes, and delivers changes. The SDLC essentially restarts at a smaller scale with each change request.

[SHOW DIAGRAM: SDLC phase diagram annotated with "BA is most active here" arrow pointing to Systems Analysis phase, and "BA contributes here" arrows pointing to Planning and Systems Design]

> IIBA ECBA Exam Tip: The ECBA exam tests phase sequencing. Requirements come before design. Design comes before implementation. A question that asks you to identify an error in a project approach will often describe a team that jumped from a business problem directly to solution selection or coding. The correct answer will always anchor on completing requirements before design.

---

## Section 4: The Role of the Business Analyst [14:30 - 19:00]

Let us spend a few minutes on the BA role itself because the ECBA exam is essentially an exam about what a BA does.

According to BABOK Guide v3, the business analyst is the person responsible for identifying business needs, analyzing the current state, defining the future state, and facilitating the changes needed to move from one to the other. The BA is not the one who decides which solution to build — that is the sponsor's decision. The BA is not the one who builds it — that is the developer's job. The BA is the one who makes sure the right question is asked, that stakeholders are engaged, that requirements are complete and understood, and that the delivered solution actually solves the business problem.

[SHOW DIAGRAM: BA as bridge graphic — on the left, a group labeled "Business Stakeholders" with thought bubbles; on the right, a group labeled "Technical Team" with code symbols; in the center, a figure labeled "Business Analyst" holding a requirements document, with two-headed arrows connecting to both sides]

BAs use the BABOK Guide as their primary professional reference. BABOK stands for Business Analysis Body of Knowledge, published by the IIBA. It organizes all BA work into seven Knowledge Areas. You do not need to memorize all seven today — we will revisit them throughout the course — but know this: the ECBA exam is built on these seven Knowledge Areas and the tasks and techniques within them.

Stakeholder identification is among the earliest and most critical BA activities. A stakeholder is anyone who has an interest in or is affected by the project outcome. Missing a stakeholder early almost always means missing a requirement that causes expensive rework later. The BA builds a stakeholder register, classifies stakeholders by role and influence, and plans how to engage each one.

> IIBA ECBA Exam Tip: When an exam scenario describes a project that had missed requirements discovered late in development or after go-live, the root cause answer is almost always "a stakeholder was not identified or engaged early enough." Stakeholder identification is not optional — it is foundational.

---

## Section 5: Lab Preview, Exam Tips, and Closing [19:00 - 22:00]

Let me preview this week's lab activity. You will not be writing any code this week — that is intentional. Systems analysis is a thinking and communication discipline, not a programming one. In this week's lab, you will do three things. First, you will be given five project scenarios and asked to identify which SDLC phase each one represents. Second, you will read a short case study and identify the stakeholders, classify them by type, and explain why each one matters. Third, you will sketch a simple system boundary diagram for a university registration system showing inputs, the system process, and outputs.

Before I let you go, let me give you three exam tips to keep in your notes from this module.

First: know the BACCM. The Business Analysis Core Concept Model defines six concepts — Change, Need, Solution, Stakeholder, Value, and Context — that frame all BA work. These six words appear in BABOK Chapter 2 and show up throughout the exam.

Second: know the distinction between verification and validation. Verification asks "Did we build the requirements correctly?" — are they well-written, complete, unambiguous? Validation asks "Did we build the right requirements?" — do they actually solve the business problem? We will revisit this in Module 04.

Third: the ECBA does not require work experience — it requires 21 hours of professional development training. This course satisfies that requirement. Visit iiba.org to review the official ECBA exam blueprint so you know exactly what percentage of questions comes from each Knowledge Area.

For additional study resources, the official IIBA website at iiba.org has free study guides, the exam blueprint, and sample questions. You have everything you need to succeed. I will see you in the discussion forum this week.

---

## End Card

## Module 01 Complete

Next: Module 02 - Business Analysis Planning and Monitoring

### Additional Resources

- iiba.org — ECBA Certification page and free exam blueprint
- iiba.org — BABOK Guide v3 overview and Knowledge Area summaries
