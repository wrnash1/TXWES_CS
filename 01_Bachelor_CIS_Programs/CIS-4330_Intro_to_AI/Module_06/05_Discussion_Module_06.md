# Discussion Forum: Module 06 - Computer Vision and Image Recognition

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Due Dates:** Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM
**Total Points:** 10

---

## Instructions

Read all three scenarios below. Choose one scenario for your initial post. Identify your scenario choice (A, B, or C) at the top of your post.

---

## Scenario A: The School Safety Facial Recognition Proposal

A school district's board is considering deploying a real-time facial recognition system that would scan every person entering district buildings and compare their face against a database of registered sex offenders and individuals with active restraining orders. Supporters argue the system would protect students. Critics raise concerns about accuracy and civil liberties. The vendor's marketing materials claim 96% accuracy and note that the system uses Microsoft Azure Face API.

A technology director notes that Microsoft has restricted access to face identification in Azure Face API for exactly this type of use case.

In your initial post (175-225 words), address all of the following:

- Explain the difference between face detection, face verification, and face identification, and identify which type this school system proposal requires.

- Why has Microsoft restricted access to face identification capabilities in Azure? Reference the specific responsible AI principles involved.

- Take a position: should the school district deploy this system? Defend your answer using at least two responsible AI principles and at least one technical argument about model accuracy.

---

## Scenario B: The Agricultural Drone Vision System

A precision agriculture company is developing a system where drones fly over fields and capture aerial images. An AI model analyzes each image to detect and locate areas with crop disease, pest damage, or nutrient deficiency. The company estimates that early detection reduces crop losses by 30% and reduces pesticide use by 40%.

The computer vision team is deciding between two approaches:

Approach 1: Use Azure Computer Vision's prebuilt analysis capabilities to tag images with disease-related keywords.

Approach 2: Train a custom object detection model using Azure Custom Vision with 2,000 labeled images showing specific disease regions with bounding boxes.

In your initial post (175-225 words), address all of the following:

- Explain why Approach 2 (Custom Vision object detection) is more appropriate than Approach 1 for this use case. Reference the specific limitations of prebuilt tagging for domain-specific agricultural applications.

- The team has 2,000 labeled images but a data scientist argues this is not enough for high accuracy on a five-class detection problem. Explain how transfer learning makes Custom Vision viable with this dataset size.

- If the model has a recall of 0.78 for pest damage (meaning it misses 22% of pest damage instances), describe the business and environmental consequences of these missed detections and whether this recall level is acceptable.

---

## Scenario C: The Retail Shelf Audit System

A consumer packaged goods company deploys an object detection system on tablets carried by sales representatives visiting retail stores. The system analyzes a photo of a shelf and automatically identifies which of the company's products are present, their location, and whether the shelf is "compliant" (all required products stocked) or "non-compliant" (missing products). The system replaces a manual audit process that previously required 20 minutes per store visit.

After six months, the analytics team notices the model has significantly lower accuracy at stores in rural markets compared to urban markets. Investigation reveals the rural stores use different shelf labeling and lighting conditions than the stores used to build the training dataset.

In your initial post (175-225 words), address all of the following:

- Identify the computer vision task this system performs and explain why Azure Custom Vision — rather than the prebuilt Azure Computer Vision service — is required for this application.

- Diagnose the root cause of the rural market accuracy problem using the concept of training data distribution. What specific property of the training data caused the model to underperform in rural settings?

- Propose a concrete remediation plan that addresses the accuracy disparity while applying the Fairness principle to ensure the system works equitably across all store types.

---

## Peer Response Guidelines

Reply to at least two classmates who chose different scenarios than you. Each peer response must be at least 50 words and must add substantive analysis beyond agreement.

Suggested peer response approaches:

- Identify a computer vision limitation your peer did not address (dataset bias, confidence threshold tradeoffs, etc.).

- Propose a different Azure service or architecture than what your peer recommended.

- Challenge the position your peer took on responsible AI, offering a counter-argument.

- Share a real-world computer vision deployment case that supports or complicates your peer's analysis.

---

## Grading Rubric (10 Points Total)

### Initial Post — 6 Points

**6 pts:** Addresses all required sub-questions with accurate computer vision vocabulary and responsible AI reasoning. Meets 175-225 word requirement. Demonstrates original analysis.

**4-5 pts:** Addresses most sub-questions. Minor technical errors or one sub-question underdeveloped. Word count met.

**2-3 pts:** Fewer than half the sub-questions addressed, or significant factual errors. May not meet word count.

**0-1 pts:** Post missing or does not engage substantively with the scenario.

### Peer Responses — 4 Points

**4 pts:** Substantive responses to at least two peers from different scenarios. Each adds new analysis. Minimum 50 words each.

**2-3 pts:** Responds to two peers with limited substance, or only one peer.

**0-1 pts:** No responses or all responses are superficial.

---

## Professor Nash Note

Scenario A involves a real and ongoing policy debate. Cities and school districts across the United States have enacted bans on government use of facial recognition, while others have deployed these systems. Microsoft's decision to restrict face identification in its own commercial product is itself a significant policy statement from a major technology company. Your post should engage with the actual technical constraints, not just the abstract principle.
