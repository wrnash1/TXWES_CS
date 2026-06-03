# Discussion: Module 15 — Emerging AI Technologies

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Instructions

Choose ONE of the three scenarios below. Write an initial post of 175–225 words responding to your chosen scenario. Then write two peer response posts of 75–100 words each, engaging substantively with classmates who chose different scenarios when possible. Reference at least one concept from the Module 15 readings or lecture in your initial post.

**Due dates:**

- Initial post: by end of Day 4 of the module week
- Peer responses: by end of Day 7

---

## Scenario A — The Agentic Workforce

A technology consulting firm announces that it is deploying a fleet of 200 AI agents to replace entry-level analyst positions. Each agent can research market trends, synthesize reports from multiple data sources, generate presentations, and respond to client questions via email — tasks that previously employed 75 analysts. The CEO says: "We are not eliminating jobs, we are eliminating tasks. Our analysts will be promoted to supervise and guide the agents." Three months after deployment, 60 of the 75 analysts have been laid off.

**Prompt:** How should the technology industry and society respond to the rapid deployment of AI agents that displace knowledge workers? Is the CEO's original framing honest or dishonest, and does it matter? What responsibility do organizations deploying agentic AI have to the workers they displace? Apply at least one concept from Module 15 (agent capabilities, responsible AI, or AI governance trends) in your analysis.

---

## Scenario B — Multimodal AI in the Courtroom

A defense attorney in a criminal trial submits a multimodal AI-generated analysis as evidence. The AI was given 50 surveillance photos and asked to analyze clothing patterns, movement signatures, and environmental context to support an alibi defense. The AI returned a detailed report concluding that the visual evidence is "inconsistent" with the defendant being present at the scene.

The prosecution objects, arguing that the AI system could have hallucinated its visual analysis and that the model's reasoning is not transparent enough to be legally reliable.

**Prompt:** Should AI-generated visual analysis be admissible as evidence in court? What standards would need to be met for a multimodal AI analysis to qualify as expert testimony? Specifically, how do the limitations of multimodal AI discussed in Module 15 — visual hallucination, opacity of reasoning — affect this question?

---

## Scenario C — Federated Learning and Data Sovereignty

A global pharmaceutical company wants to train a drug interaction prediction model using patient records from hospitals in the US, EU, Germany, and Japan. Each jurisdiction has different data sovereignty requirements:

- EU GDPR prohibits patient data from leaving EU borders
- Germany has additional federal data protection requirements beyond GDPR
- Japan APPI restricts international data transfers
- US HIPAA permits sharing under business associate agreements

The company proposes using federated learning so that no patient records cross borders, with only model updates being transmitted. A privacy advocacy group argues that even model updates can leak private information and that federated learning does not provide absolute privacy protection.

**Prompt:** Does federated learning adequately address the data sovereignty requirements described? What additional protections would be needed for this deployment to satisfy GDPR, HIPAA, and Japan APPI simultaneously? Is the privacy advocacy group's concern technically valid? How would you respond to their argument using concepts from Modules 14 and 15?

---

## Peer Response Guidelines

Your peer responses should do at least ONE of the following:

- Introduce a real-world precedent (a court ruling, a regulation, a published case) that supports or complicates your classmate's argument
- Challenge a factual claim or ethical assertion with specific reasoning
- Connect the emerging technology in your classmate's scenario to a parallel from an earlier module (MLOps governance, GDPR compliance, adversarial security)
- Ask a follow-up question that would require your classmate to apply a Module 15 concept they did not use in their initial post

Responses that simply agree with or summarize the initial post will receive zero credit.

---

## Grading Rubric — 10 Points Total

| Criterion | Excellent (Full Credit) | Partial Credit | No Credit |
|---|---|---|---|
| **Content Accuracy** (3 pts) | Emerging AI concepts used correctly; technically and ethically sound | Minor errors; mostly correct | Significant errors or no module content referenced |
| **Depth of Analysis** (3 pts) | Multiple perspectives; considers unintended consequences; goes beyond the obvious | Addresses the prompt adequately | Restates scenario without independent analysis |
| **Reading or Lecture Integration** (2 pts) | Explicitly references a specific Module 15 concept (agent capabilities, multimodal limitations, FL privacy, certification landscape) | Vague connection to module material | No module content used |
| **Peer Engagement** (2 pts) | Both responses substantive and advance the discussion | One strong, one weak | Missing or purely social |

---

## Instructor Modeling Response — Scenario B Sample

*The following is a model response at the "Excellent" level to help calibrate your writing.*

The admissibility question is genuinely difficult and turns on a principle the legal system has not yet fully resolved: at what point does AI-generated analysis meet the Daubert standard — requiring that expert evidence be scientifically valid, reliably applied, and falsifiable?

Multimodal AI as described in Module 15 has a well-documented limitation that directly bears on this case: visual hallucination. GPT-4V and similar models can confidently assert visual details that are not present in an image. When the output is "this evidence is inconsistent with the defendant's presence," and that output is generated by a system capable of fabricating visual reasoning, the prosecution's objection is technically valid. The model's reasoning process is not interpretable in the way that a human forensic expert's reasoning is — the expert can be cross-examined, challenged, and tested for internal consistency.

A minimum threshold for admissibility would require: documented validation of the specific model on comparable surveillance analysis tasks with known ground truth, a reproducibility test demonstrating consistent results on the same images, an expert witness who can explain the model's outputs and their limitations, and disclosure of the specific model version and configuration.

The more important principle for AI practitioners is that deploying a multimodal system in a high-stakes domain without adequate validation is irresponsible regardless of what the law permits. The certification and governance trends discussed in Module 15 — AI auditing, conformity assessments, third-party validation — exist precisely to establish trustworthiness standards for these situations.

---

*Discussion prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
