# Discussion Forum: Module 10 — Generative AI and Azure OpenAI Service

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## Due Dates: Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM

---

## Overview

Generative AI is moving faster than any previous wave of technology. Every week brings new capabilities, new applications, and new controversies. This discussion asks you to move beyond the technical mechanics and engage with the real deployment decisions, trade-offs, and ethical boundaries that practitioners face right now.

Professor Nash note: These scenarios do not have simple right answers. I am looking for posts that demonstrate both technical precision and ethical maturity — posts that can hold two competing legitimate concerns in tension and reason through them thoughtfully. Cite specific Azure services, prompting techniques, and responsible AI concepts from the module.

---

## Scenario 1: Law Firm Document Summarization

A 200-attorney law firm wants to use Azure OpenAI Service with a RAG architecture to help associates summarize lengthy deposition transcripts and case documents. The system would use Azure AI Search to retrieve relevant document chunks and GPT-4 to generate case summaries that associates review before using them in their work.

Senior partners are concerned about three specific risks: (1) the model hallucinating case facts that associates fail to catch, (2) confidential client documents being sent to a third-party AI company, and (3) junior associates becoming over-reliant on AI summaries and losing the critical reading skills needed to become effective lawyers.

Respond to the following prompts in 175–225 words:

1. For concern (1), explain how the RAG architecture specifically reduces hallucination risk in this scenario. What additional design element in the prompt would further mitigate this risk?
2. For concern (2), explain why Azure OpenAI Service specifically addresses this concern better than the direct OpenAI API. What Azure feature ensures client data does not leave the firm's control?
3. For concern (3), this is not a technical concern but an organizational one. Is it a legitimate concern? How would you design the deployment policy — not the technology — to address it?

---

## Scenario 2: AI-Generated Marketing Content at Scale

A consumer goods company wants to use GPT-4 to automatically generate product descriptions, social media posts, and email marketing copy for its 40,000-product catalog. The marketing VP argues that with GPT-4's quality, human review of every piece of content is unnecessary and cost-prohibitive. The legal team disagrees.

The company's content policy requires that all consumer-facing content be accurate, non-deceptive, and free from claims the product cannot substantively support. The legal team argues that AI-generated content published without review violates this policy and creates FTC liability.

Respond to the following prompts in 175–225 words:

1. What is the specific hallucination risk in this scenario? Give a concrete example of the type of inaccurate content the model might generate for a consumer product.
2. Evaluate the marketing VP's claim that human review of every piece is "unnecessary." Design a middle-ground workflow that reduces human review burden while maintaining the legal team's quality and accuracy requirements. Be specific about which content types require full human review and which could use lighter-touch oversight.
3. The Azure OpenAI content filters screen for hate, sexual content, violence, and self-harm. Would these filters catch the accuracy and FTC compliance risks the legal team is worried about? If not, what additional safeguard would you add?

---

## Scenario 3: Generative AI in an Introductory Computer Science Course

A CS department is debating how to respond to students using ChatGPT and Azure OpenAI to complete programming assignments. Three positions are represented on the faculty committee:

Professor A argues that all AI tool use on programming assignments should be banned because students will not learn to code if a model does it for them.

Professor B argues that AI tools should be fully permitted because professional developers use these tools daily and students should learn to use them effectively.

Professor C argues for a structured middle ground: AI tools are permitted but students must submit their prompts alongside their code, explain every line, and pass an oral examination where they demonstrate they understand the code they submitted.

Respond to the following prompts in 175–225 words:

1. Evaluate all three positions. What is the strongest argument for and the strongest argument against each?
2. Based on what you know about code generation capabilities and limitations from this module, what types of programming errors or quality issues might a student fail to catch in AI-generated code if they do not deeply understand it?
3. Take a position: which faculty approach (A, B, C, or a variation you design) would you recommend to a university dean, and why? Your position should reference both the educational goal and the professional reality students will face after graduation.

---

## Peer Response Requirements

After posting your initial response to one scenario, reply substantively to at least two classmates who chose different scenarios. Each peer response must be at least 75 words and must:

- Add a technical detail about Azure OpenAI, prompt engineering, or responsible AI that your classmate did not mention, or
- Challenge a claim or conclusion in your classmate's post with a reasoned counter-argument, or
- Extend the scenario to a similar real-world case you have encountered or researched

Responses that only express agreement or repeat your classmate's main points will not receive full credit.

---

## Grading Rubric (10 points total)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical accuracy | 3 | Correctly applies Azure OpenAI features, RAG, prompting, and content filtering |
| Depth of analysis | 3 | Engages with trade-offs, competing interests, and nuance |
| Responsible AI reasoning | 2 | Addresses hallucination, human oversight, or fairness substantively |
| Peer engagement | 2 | Two qualifying peer responses per requirements above |

---

End of Discussion — Module 10
