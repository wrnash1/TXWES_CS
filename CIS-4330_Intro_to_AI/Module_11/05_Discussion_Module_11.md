# Discussion Forum: Module 11 — AI Ethics and Responsible AI Principles

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## Due Dates: Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM

---

## Overview

This is the final discussion of CIS-4330, and it is the most important. Everything we have learned about AI technology — vision, language, generation — ultimately must be grounded in the question this module asks: how do we build AI that serves humanity rather than harms it?

This discussion is not a test of your ability to identify the correct principle for a given keyword. It is an invitation to engage with genuinely hard problems where the right answer is contested, where legitimate interests conflict, and where your reasoning matters as much as your conclusion.

Professor Nash note: I am looking for posts that demonstrate intellectual honesty — posts that can acknowledge what makes a problem genuinely difficult rather than forcing every scenario into a clean answer. The best posts will show command of the Responsible AI framework alongside an appreciation of its limits. Name principles, reference real Azure services and governance tools, and bring your own perspective.

---

## Scenario 1: Fairness Trade-Off in Bail Risk Assessment

A state court system has adopted an AI tool to assist judges in setting bail amounts for defendants awaiting trial. The tool produces a recidivism risk score from 1 to 10. An independent study reveals the following:

- For white defendants with a score of 3 (medium risk), 18% were subsequently arrested before trial.
- For Black defendants with a score of 3, 35% were subsequently arrested before trial.

This means the same score corresponds to meaningfully different actual risk levels depending on race. If judges calibrate their bail decisions to the score, Black defendants with score-3 ratings will receive bail amounts appropriate for the higher-risk group despite receiving the same score.

Two proposed fixes have been offered. Fix A recalibrates the model to achieve equal predictive accuracy across groups — but doing so requires including race as a feature in the model. Fix B removes race entirely and recalibrates thresholds so a score of 3 means approximately the same absolute risk for both groups — but this reduces overall predictive accuracy.

Respond to the following prompts in 175–225 words:

1. Identify which Responsible AI principles are at stake in this scenario and how they interact.
2. Evaluate Fix A and Fix B. What does each fix achieve, and what ethical objection can be raised against each?
3. A judge argues that because the AI is only an input to their decision — not the final decision — accountability is preserved. Evaluate this claim. What would genuine accountability require in this context?

---

## Scenario 2: Transparency vs. Competitive Advantage

A large insurance company uses a proprietary AI model to set homeowners insurance premiums. The model processes satellite imagery, local weather data, construction records, and social media posts to generate individual risk scores. A consumer advocacy group has filed a complaint arguing that homeowners have a right to know why their premiums are high and what they can do to lower them — a right to explanation under transparency principles.

The insurance company argues that publishing the model's decision factors would enable customers to game the system, expose proprietary risk methodology to competitors, and ultimately increase costs for all policyholders.

Respond to the following prompts in 175–225 words:

1. Which Responsible AI principles are in tension in this scenario? Describe the legitimate interest on each side.
2. What does "meaningful transparency" look like in this context? Is full technical explainability required, or is there a form of transparency that would satisfy the consumer right without exposing the full model?
3. The model uses social media posts as a risk factor. Which additional Responsible AI principles does this raise, and what specific concern does it introduce?

---

## Scenario 3: Accountability Gaps in AI-Assisted Medical Diagnosis

A hospital system deploys an AI tool that analyzes patient lab results and flags potential diagnoses for physician review. The hospital's policy states that physicians must review every AI flag before acting. However, in practice, overworked physicians in a busy emergency department have started accepting AI flags without reviewing the underlying lab values because they trust the AI and it saves time.

A patient is harmed when the AI incorrectly flags a drug interaction that the physician would have caught with a review of the lab values. The physician assumed the AI had already checked for interactions. The hospital argues it is not liable because the policy required physician review. The AI vendor argues it is not liable because the system was functioning as designed.

Respond to the following prompts in 175–225 words:

1. Map the chain of accountability failures in this scenario: what did each party (AI vendor, hospital administration, individual physician) fail to do?
2. This scenario illustrates the concept of "automation bias" — the tendency to over-rely on automated systems. What design choices in the AI system or clinical workflow could have made automation bias less likely?
3. The hospital's defense ("our policy required physician review") is technically accurate but raises deeper accountability questions. What would a genuine Accountability principle implementation require beyond writing a policy?

---

## Peer Response Requirements

After posting your initial response to one scenario, reply substantively to at least two classmates who chose different scenarios. Each peer response must be at least 75 words and must:

- Surface a tension, trade-off, or implication your classmate did not address, or
- Challenge a claim in your classmate's reasoning with a counter-argument grounded in the module content, or
- Connect your classmate's scenario to the other module topics from this course (computer vision, NLP, generative AI) to show how the principle applies broadly

Posts that only express agreement or briefly restate your classmate's argument will not receive full credit.

---

## Grading Rubric (10 points total)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Principle identification and application | 3 | Correctly names and applies the relevant principles with specificity |
| Quality of reasoning | 3 | Engages with the genuine difficulty; does not oversimplify; addresses trade-offs |
| Responsible AI framework depth | 2 | References specific tools, governance mechanisms, or regulatory frameworks from the module |
| Peer engagement | 2 | Two qualifying peer responses that add substance beyond agreement |

---

## A Final Word from Professor Nash

This discussion closes the content of CIS-4330. You have covered an enormous amount of ground — from what a neural network is to how transformer models generate text, from provisioning Azure resources to thinking carefully about who bears responsibility when AI causes harm.

The tools you have built and the concepts you have learned are genuinely powerful. The questions in these scenarios — about fairness, accountability, and who gets to shape AI systems — are questions that practitioners are working through right now, in real organizations, with real consequences.

My hope is that you leave this course not just with Azure AI skills, but with the instinct to ask the harder questions before you deploy. The most important word in "Responsible AI" is the one at the beginning.

Good luck on the AI-900 exam and beyond.

---

End of Discussion — Module 11
