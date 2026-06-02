# Discussion Forum: Module 01 - DevOps Fundamentals and the DevSecOps Mindset

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Overview

This discussion asks you to apply Module 01 concepts — DevSecOps culture, shift-left security, pipeline automation, and shared responsibility — to real-world organizational scenarios. Read all three scenarios and respond to the one assigned to your group (or the one of your choice if your instructor has not assigned groups). Your initial post is due Wednesday at 11:59 PM; peer responses are due Sunday at 11:59 PM.

---

## Scenario A: The Legacy Audit Model

A financial services company has been conducting security through a dedicated Security Operations team that manually reviews every deployment before it goes to production. Reviews take 5-7 business days. The development teams now deploy 15-20 times per week across 8 microservices. The security team is overwhelmed, and developers complain that their code sits idle for a week waiting for approval. The CISO has asked your team to propose a DevSecOps transformation plan.

In 175-225 words, address the following: Identify the core DevSecOps principle that the current model violates and explain why it is unsustainable at the current deployment frequency. Propose two specific automated pipeline controls that would reduce the manual review burden while maintaining an equivalent or higher security bar. Explain how you would preserve meaningful human security review for the changes that truly require it. Use precise DevSecOps terminology from Module 01 in your response.

---

## Scenario B: The Shared Responsibility Conflict

A retail e-commerce platform suffered a data breach. The breach was caused by a vulnerable version of a popular open-source JSON parsing library with a known CVE that had been in the codebase for 11 months. The Development team says it is a security issue, so it belongs to the Security team. The Security team says they only review the application perimeter, not code internals. Operations says they only manage servers. No team accepted responsibility.

In 175-225 words, address the following: Explain how the DevSecOps shared responsibility model would have assigned clear ownership for this vulnerability before it was exploited. Identify which specific automated control — and at which pipeline stage — would have detected this CVE when it was first introduced 11 months ago. Describe how a post-incident feedback loop should be used to prevent the same class of vulnerability from recurring. Use precise DevSecOps terminology from Module 01 in your response.

---

## Scenario C: The Startup Velocity Problem

A Series A startup is building a SaaS product with a team of 6 engineers. They have no dedicated security staff. The CTO argues that adding security tooling to the CI/CD pipeline will slow down the team and that security can be addressed once they reach Series B and hire a security engineer. One of the developers pushes back, arguing that the cost of a breach at this stage could be fatal to the company.

In 175-225 words, address the following: Evaluate the CTO's argument using the shift-left cost multiplier concept from Module 01. Identify two low-friction DevSecOps controls that a 6-person team with no security staff could realistically implement in a week without significantly impacting velocity. Explain how these controls create the feedback loop needed to catch vulnerabilities early without requiring a dedicated security engineer to review every change. Use precise DevSecOps terminology from Module 01 in your response.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

Due Wednesday at 11:59 PM. Your post must be 175-225 words, address all elements of your chosen scenario, and use precise DevSecOps terminology.

- 5-6 pts: Thoroughly addresses all scenario questions with technical accuracy, clear explanations, and appropriate terminology. Meets the word count.
- 3-4 pts: Addresses most scenario elements but lacks technical depth or precise terminology in one or more areas.
- 0-2 pts: Incomplete, missing, or does not address the scenario elements.

### Peer Responses (4 Points)

Due Sunday at 11:59 PM. Respond to at least two classmates who chose different scenarios from yours.

- 4 pts: Two substantive responses (at least 50 words each) that add technical content, offer an alternative approach, or connect the peer's scenario to concepts from the reading guide.
- 2 pts: Only one substantive peer response, or both responses are superficial (e.g., "Great post, I agree").
- 0 pts: No peer responses submitted.

---

## Professor Nash Note

Focus on precision in your use of terms. "Shift-left" is not a synonym for "move faster" — it specifically means moving a security activity to an earlier SDLC stage. "Feedback loop" is not a synonym for "communication" — it specifically refers to the elapsed time between vulnerability introduction and developer notification. Examiners and interviewers will notice the difference.
