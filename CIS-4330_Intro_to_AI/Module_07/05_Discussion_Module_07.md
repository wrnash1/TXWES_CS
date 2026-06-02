# Discussion Forum: Module 07 - Azure Cognitive Services: Vision, Speech, and Language

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Due Dates:** Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM
**Total Points:** 10

---

## Instructions

Read all three scenarios below. Choose one scenario for your initial post. Identify your scenario choice (A, B, or C) at the top of your post.

---

## Scenario A: The Multilingual Customer Service Platform

A global telecommunications company serves customers in 47 countries and receives support contacts in 35 languages via phone, chat, and email. The company wants to build a unified AI-powered customer service platform that can:

1. Transcribe phone calls in real time.
2. Translate non-English transcripts to English for processing.
3. Detect customer sentiment to flag frustrated customers for human escalation.
4. Identify the customer's service request (billing inquiry, technical fault, upgrade request).
5. Route the request to the appropriate department.

In your initial post (175-225 words), address all of the following:

- Map each of the five listed capabilities to the specific Azure Cognitive Service and capability name that would implement it.

- Two of the five capabilities require custom training while three are prebuilt. Identify which two require custom training and explain what training data would be needed for each.

- The sentiment escalation system (capability 3) could reduce the number of human agents needed. Identify one responsible AI concern this raises and which Microsoft principle it most relates to.

---

## Scenario B: The Smart Manufacturing Inspection System

A precision manufacturing company produces automotive components. They want to build a computer vision quality control system with three capabilities:

1. Detect scratches, cracks, and deformations on metal parts (defects are domain-specific and not in standard models).
2. Read serial numbers printed on each part (some printed, some laser-etched).
3. Automatically reject components where the detected defect confidence exceeds 0.85.

The engineering team has 800 labeled images of defective and non-defective parts across five defect categories. They have unlimited images of serial number plates.

In your initial post (175-225 words), address all of the following:

- Map each of the three capabilities to the specific Azure service and capability that would implement it. Explain why custom training is or is not required for each.

- The team has 800 labeled images for five defect categories (160 per category). Is this sufficient for Azure Custom Vision? What factors should they consider when evaluating whether this dataset is adequate?

- The automatic rejection threshold of 0.85 means parts with 0-84% confidence defect scores are passed as acceptable. Discuss the trade-off between false positives (rejecting good parts) and false negatives (passing defective parts) in an automotive safety context.

---

## Scenario C: The Accessible Government Services Portal

A state government wants to redesign its citizen services portal to be more accessible and multilingual. The project has three AI requirements:

1. Convert all written content on the portal to audio, so visually impaired users can hear page content read aloud.
2. Allow citizens to speak their service requests (e.g., "Renew my driver's license") and have the system understand and respond.
3. Translate the portal into 12 additional languages for immigrant populations who do not read English.

The technology director wants to use Azure Cognitive Services for all three capabilities.

In your initial post (175-225 words), address all of the following:

- Map each of the three capabilities to the specific Azure service and capability. For capability 2, identify whether a prebuilt capability is sufficient or whether custom training is needed.

- One of the three services used in this project requires gated access approval from Microsoft. Identify which service feature requires approval, explain why Microsoft requires approval, and evaluate whether the government portal's use case is likely to be approved or denied.

- This project is explicitly designed to improve accessibility and language equity. Identify which Microsoft responsible AI principle the entire project embodies and explain how each of the three capabilities contributes to it.

---

## Peer Response Guidelines

Reply to at least two classmates who chose different scenarios than you. Each peer response must be at least 50 words and must add substantive analysis beyond agreement.

Suggested peer response approaches:

- Identify a service mapping your peer made that you disagree with and propose the correct service with justification.

- Raise a technical limitation of one of the services your peer selected that they did not discuss.

- Challenge the responsible AI reasoning in your peer's post with a counter-argument or a different principle.

- Propose an additional Azure service that would enhance the solution your peer designed.

---

## Grading Rubric (10 Points Total)

### Initial Post — 6 Points

**6 pts:** All service mappings are correct with accurate capability names. Responsible AI reasoning identifies the correct principle. Meets 175-225 word requirement. Demonstrates original reasoning.

**4-5 pts:** Most service mappings correct. Minor capability name errors or one sub-question underdeveloped. Word count met.

**2-3 pts:** Fewer than half the mappings correct, or significant factual errors. May not meet word count.

**0-1 pts:** Post missing or does not engage substantively with the scenario.

### Peer Responses — 4 Points

**4 pts:** Substantive responses to at least two peers from different scenarios. Each adds new analysis or challenges a service mapping. Minimum 50 words each.

**2-3 pts:** Responds to two peers with limited substance, or only one peer.

**0-1 pts:** No responses or all responses are superficial.

---

## Professor Nash Note

Scenario A maps directly to the kind of multi-service architecture question you will encounter on the AI-900 exam. Strong posts will use the exact service and capability names from Table 1 in the reading guide rather than general descriptions. If you find yourself writing "the speech service" or "the language tool," you are not being specific enough. Precision in service naming is a core exam skill.
