# Discussion Forum: Module 16 — IoT Capstone Project and Certification Preparation

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

## Overview

This final module's discussion is different from previous weeks. Rather than analyzing a fictional scenario, you will reflect on your own capstone design, evaluate two real certification pathways, and engage with your classmates' choices. The goal is to synthesize everything you have built in this course into a coherent narrative about your IoT engineering knowledge and where you want to take it next.

---

## Scenario 1 — Your Capstone Architecture Review

You have designed and documented a four-tier IoT system for the capstone project. Now step back and conduct a critical self-review of your own design.

Discuss the following:

- Identify the single most important architectural decision you made in your capstone design — not just any decision, but the one that most affects the security, reliability, or scalability of the system. Explain why it matters and what would break if you had made the opposite choice.
- Review your OWASP IoT Top 10 analysis from the capstone documentation. Which category is your system most vulnerable to right now (the one you classified as "not yet addressed" or "partially mitigated"), and what specific engineering change would fully address it?
- If you were handed a budget to scale this system from your single ESP32 device to 50,000 deployed devices, what are the three changes you would make to the architecture, and which change is most urgent? Justify your priority ranking.

Your initial post should be 175–225 words. This prompt requires reflection on your actual capstone work — generic IoT system descriptions are not acceptable for full credit. Reference specific decisions from your architecture documentation.

---

## Scenario 2 — Certification Pathway Planning

You are advising a classmate who has just completed CIS-4355 and wants to pursue IoT engineering professionally. They have the following background: strong Python skills, six months of cloud experience (AWS S3, Lambda, and API Gateway, but no IoT-specific services), and have completed all CIS-4355 labs successfully. They have three months before they start job searching and can dedicate 10 hours per week to certification preparation.

Two certifications are under consideration:

Option A: AWS Certified Specialty — IoT Core. This is a professional-level exam that tests AWS IoT services in depth. Market recognition is high. Expected preparation time: 80–120 hours for a candidate with this background.

Option B: CompTIA IoT+ followed (after passing) by a cloud-specific certification (AWS IoT Specialty or AZ-220) in the subsequent six months. CompTIA IoT+ is vendor-neutral and achievable in 20–30 hours of preparation. Market recognition is moderate but growing.

Discuss the following:

- For this specific candidate (Python background, some AWS experience, 3-month timeline, 10 hours/week), which option would you recommend? Calculate whether Option A is achievable within the 3-month, 10-hour/week constraint.
- What specific AWS IoT service gap — identified in Question 3 of this module's quiz — should the candidate prioritize in their preparation? Name the service, explain what it does, and estimate how many hours of hands-on practice would be sufficient to be exam-confident on that topic.
- If the candidate cannot achieve certification in 3 months, what alternative credential or portfolio artifact would you recommend as a substitute to demonstrate IoT competence to employers?

Your initial post should be 175–225 words with a clear recommendation and the arithmetic for the timeline calculation visible.

---

## Scenario 3 — The Production Gap Analysis

A hiring manager at an IoT company reviews a candidate's resume. The candidate completed a university IoT course and built a capstone project: a single ESP32 device publishing temperature data to a Mosquitto broker with TLS. The manager notes that the capstone demonstrates prototype-level skills but not production-level skills, and sends a rejection.

Consider what separates a prototype IoT system from a production-grade one. Review the modules of this course and identify the capabilities that transform a prototype into production-ready IoT.

Discuss the following:

- Identify three specific capabilities — from any module in this course — that distinguish a production IoT system from a prototype. For each capability, explain: what the prototype lacks, what production requires, and which module teaches the skill.
- The rejected candidate's prototype has TLS and a Mosquitto broker — which is further than many student projects. What is the most impactful single addition they could make to the capstone to move it from "prototype" to "production-ready" in a hiring manager's assessment? Justify your choice over other options.
- A classmate argues that fleet management and OTA updates (Module 15) are the most important distinguishing capabilities because "a device you can't update in the field is a liability." A second classmate argues that security hardening (Module 12) is more important because "a device that can be compromised is a worse liability." Take a position in this debate — which capability is more important for production-readiness, and why?

Your initial post should be 175–225 words. Reference at least two specific modules in your response. Peer responses should engage with the debate in the third sub-question.

---

## Discussion Instructions

### Initial Post

Due: Wednesday at 11:59 PM

Choose one scenario (or address all three for extra credit). Write 175–225 words per scenario addressed. Your post must:

- Be grounded in your actual capstone work (Scenario 1) or in specific course content (Scenarios 2 and 3)
- Make a clear recommendation or take a clear position — ambiguous responses do not earn full credit
- Use precise IoT terminology from the course

### Peer Responses

Due: Sunday at 11:59 PM

Reply to at least two classmates (minimum 60 words each). In your replies:

- For Scenario 1: evaluate whether their "most important decision" is genuinely architectural or more of a component-selection choice. Challenge them if the distinction is not clear.
- For Scenario 2: check their timeline arithmetic and challenge the recommendation if the hours do not support the conclusion.
- For Scenario 3: take a position in the Module 12 vs. Module 15 debate if they addressed the third sub-question, and provide at least one concrete technical argument for your side.

---

## Discussion Rubric (10 Points Total)

### Initial Post — 6 Points

- 5–6 pts: Addresses all sub-questions with specific, grounded answers. Clear position taken with technical justification. References actual capstone work (Scenario 1) or specific module content (Scenarios 2–3). Meets 175-word minimum.
- 3–4 pts: Addresses most sub-questions. Position taken but justification is vague or the answer is generic rather than specific to the candidate's or student's actual work.
- 0–2 pts: Post missing, below word count, or entirely generic — could have been written without taking this course.

### Peer Responses — 4 Points

- 4 pts: Two substantive replies that add genuine value — challenge arithmetic, push back on a design decision, or take a clear position in a debate. Each meets the 60-word minimum.
- 2 pts: One substantive reply, or two replies that only express agreement.
- 0 pts: No peer responses submitted.

---
