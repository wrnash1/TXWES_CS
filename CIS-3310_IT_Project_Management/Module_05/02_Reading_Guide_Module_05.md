# Reading Guide: Module 05 - Cost Management – Budgeting and EVM
## Course: CIS-3310_IT_Project_Management (CompTIA Project+ / PMI CAPM)

---

### Introduction
Welcome to **Module 05 - Cost Management – Budgeting and EVM**! This module covers how project costs are estimated, how a budget is built from those estimates, and how project performance is measured in financial terms using Earned Value Management (EVM). EVM is one of the most calculation-heavy topics on both the CompTIA Project+ and PMI CAPM exams—expect to calculate CPI, SPI, CV, and SV using the EVM formulas.

Cost management is also one of the most practically critical skills for a project manager: projects that go over budget typically face cancellation, reduced scope, or damaged stakeholder relationships. Understanding the estimating techniques and EVM calculations in this module will serve you in both certification exams and real-world PM roles.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Network Diagram**: A graphical representation of project activities and their logical dependencies, used in the Critical Path Method (CPM) to calculate the project's earliest and latest start/finish dates and to identify the critical path. Common formats include the Activity-on-Node (AON) diagram, where each box represents an activity and arrows represent dependencies.
*   **Forward Pass (Early Start / Early Finish)**: A CPM calculation technique that works left-to-right through the network diagram, computing the Earliest Start (ES) and Earliest Finish (EF) for each activity. ES of a successor equals the EF of its predecessor(s); EF = ES + Duration. This establishes the project's minimum duration.
*   **Backward Pass (Late Start / Late Finish)**: A CPM calculation technique that works right-to-left through the network diagram, starting from the project's final finish date, to compute the Latest Finish (LF) and Latest Start (LS) for each activity. LS = LF - Duration. This determines how much delay each activity can absorb.
*   **Float / Slack Time**: The amount of time an activity can be delayed without delaying the overall project finish date (Total Float) or the early start of the next activity (Free Float). Activities on the critical path have zero total float. Float = LS - ES (or LF - EF).

---

### 2. Certification Exam Tips
*   **Project+ Tip – Memorize the CPM Formula Steps**: For the forward pass, remember ES → add duration → EF. For the backward pass, LF → subtract duration → LS. Float = LS - ES. Activities with zero float are on the critical path. Practice at least two full network diagram calculations before the exam.
*   **CAPM Tip – EVM Formulas are Heavily Tested**: The CAPM dedicates significant question density to Earned Value. Memorize: CV = EV - AC (negative = over budget), SV = EV - PV (negative = behind schedule), CPI = EV/AC (below 1.0 = over budget), SPI = EV/PV (below 1.0 = behind schedule), EAC = BAC/CPI (forecast to complete).
*   **Scenario Trap**: A question may give you a CPI below 1.0 and ask if the project is "over budget" or "ahead of schedule." Remember: CPI measures cost efficiency (budget), SPI measures schedule efficiency. Do not mix them up. A CPI of 0.80 means you are spending $1.25 for every $1.00 of work completed—over budget.
*   **Study Resource**: For worked EVM calculation examples, search [YouTube: Earned Value Management EVM Project Management Formulas](https://www.youtube.com/results?search_query=earned+value+management+EVM+formulas+PMP+capm+project+management). Many channels provide free formula cheat sheets you can download.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the schedule and cost management chapters in the OER Textbook, with emphasis on the Critical Path Method and EVM sections: [Project Management Open Textbook – BC Campus](https://opentextbc.ca/projectmanagement/).
*   **Required Video:** Watch the CPM and cost management lectures in the course playlist: [CompTIA Project+ PK0-005 Playlist by Joseph Phillips](https://www.youtube.com/results?search_query=comptia+project%2B+PK0-005+joseph+phillips).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Calculate ES/EF and LS/LF for a network diagram**: Given a provided six-activity network diagram with durations, perform both the forward pass and backward pass manually, recording all ES, EF, LS, LF values in a table.
*   **Identify critical path with zero float time**: Using your CPM calculations, highlight the critical path activities and confirm their total float equals zero.
*   **Compute project duration**: State the minimum project duration derived from your forward pass and explain what would happen to the project end date if one critical path task were delayed by two days.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to apply the forward pass and backward pass from memory.
- [ ] Read the CPM and schedule chapters in the [Project Management Open Textbook](https://opentextbc.ca/projectmanagement/).
- [ ] Watch the CPM video in the [CompTIA Project+ PK0-005 Playlist by Joseph Phillips](https://www.youtube.com/results?search_query=comptia+project%2B+PK0-005+joseph+phillips).
- [ ] Complete the Module 05 Lab activity.
- [ ] Take the Module 05 Quiz.
