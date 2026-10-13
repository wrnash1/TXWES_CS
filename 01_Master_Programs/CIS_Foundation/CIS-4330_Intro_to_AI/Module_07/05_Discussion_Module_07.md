# Discussion Forum: Module 07 — Computer Vision with Azure

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## Due Dates: Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM

---

## Overview

Computer vision is one of the most commercially deployed forms of AI, appearing in retail stores, hospitals, factory floors, and public spaces. This discussion asks you to move beyond the technical mechanics and examine real-world deployment decisions, trade-offs, and ethical considerations. Your posts should demonstrate both your understanding of Azure computer vision services and your ability to reason critically about their use.

Professor Nash note: There are no purely correct answers to these scenarios. I am looking for evidence that you have thought carefully, applied module concepts, and engaged honestly with the tensions involved. Cite specific Azure services and concepts from the lecture and reading guide in your posts.

---

## Scenario 1: Retail Loss Prevention

A national grocery chain is considering deploying Azure AI Vision Spatial Analysis across all 400 of its store locations. The system would use existing overhead security cameras to detect when customers place unpurchased items into bags or pockets. When the system's confidence score exceeds 0.85, it would automatically alert a loss prevention associate, who would then approach the customer.

The chain estimates the system would reduce shrinkage (theft and error) by 30%, saving approximately $12 million per year.

Respond to the following prompts in 175–225 words:

1. Which Azure computer vision capability is central to this system, and how does it technically work?
2. What is one significant benefit and one significant risk of deploying this system as described?
3. The system has a confidence threshold of 0.85 — meaning 15% of alerts could be false positives. What real-world consequence does a false positive carry for the customer who is wrongly approached, and how should the chain address this?

---

## Scenario 2: Custom Vision for Medical Screening

A regional health network wants to use Azure Custom Vision to build an image classification model that screens chest X-ray images and flags potential cases of pneumonia for radiologist review. The model would be trained on 5,000 labeled X-ray images (2,500 pneumonia-positive, 2,500 normal).

The health network stresses that a radiologist will always review every flagged case — the model is a triage tool, not a diagnostic decision-maker.

Respond to the following prompts in 175–225 words:

1. Is Custom Vision Classification or Custom Vision Object Detection more appropriate for this scenario? Justify your choice.
2. The training dataset contains 5,000 images. Based on what you learned about Custom Vision training requirements and performance metrics, is this an adequate dataset? What factors beyond quantity matter?
3. The health network says a radiologist will always review flagged cases. Does this human-in-the-loop design adequately address the responsible AI concerns you might have? Are there remaining risks?

---

## Scenario 3: Face API in Campus Access Control

A university is considering replacing physical key cards with a face recognition system at all campus building entrances. Students, faculty, and staff would enroll by having their photos taken once during orientation. The Azure Face API would then verify identity in real time as people approach building doors.

The university's IT director argues this is more secure and convenient than key cards, which are frequently lost or shared. The student government president objects, citing privacy concerns and potential bias.

Respond to the following prompts in 175–225 words:

1. Which Face API capabilities would this system require, and what Microsoft policy governs access to those capabilities?
2. Evaluate the student government president's bias concern. Is it technically founded? What evidence from the module supports your position?
3. Propose one design change the university could make that would meaningfully address either the privacy concern or the bias concern while still achieving the security goal.

---

## Peer Response Requirements

After posting your initial response to one scenario of your choice, reply substantively to at least two classmates who chose different scenarios. Each peer response must be at least 75 words and must do one of the following:

- Add a technical detail or Azure service consideration your classmate did not mention
- Respectfully challenge an assumption in your classmate's argument with evidence from the module
- Extend the analysis to a real-world example from a different industry

Responses that only agree or restate what the classmate said will not receive full credit.

---

## Grading Rubric (10 points total)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical accuracy | 3 | Correctly names and describes relevant Azure services and capabilities |
| Depth of analysis | 3 | Moves beyond surface observations; addresses trade-offs and nuance |
| Responsible AI reasoning | 2 | Engages substantively with ethical, bias, or privacy dimensions |
| Peer engagement | 2 | Two peer responses that add value per the requirements above |

---

End of Discussion — Module 07
