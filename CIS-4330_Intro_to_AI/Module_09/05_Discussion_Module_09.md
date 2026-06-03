# Discussion Forum: Module 09 — Conversational AI and Azure Bot Service

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## Due Dates: Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM

---

## Overview

Conversational AI is one of the most visible and consumer-facing forms of AI in use today. Millions of people interact with chatbots daily for customer service, healthcare navigation, HR inquiries, and technical support. This discussion asks you to evaluate real deployment decisions, design trade-offs, and ethical obligations in conversational AI systems built on Azure.

Professor Nash note: Chatbots are uniquely positioned at the intersection of AI capability and human trust. The strongest posts will engage both the technical design question and the human impact question — not just one or the other. Use specific Azure service names and module concepts throughout your response.

---

## Scenario 1: Hospital Patient Navigation Bot

A regional hospital network is deploying a chatbot to help patients navigate their services. The bot uses Question Answering connected to the hospital's existing FAQ and policy documents, and a CLU model to handle task intents: ScheduleAppointment, FindProvider, GetDirections, and RequestRecords. The bot is available 24/7 on the hospital's patient portal website.

During a pilot, nurses noticed that patients with urgent symptoms were sometimes asking the bot health questions and receiving FAQ answers about hospital hours and visitor policies, because those answers matched their keywords better than anything else in the knowledge base.

Respond to the following prompts in 175–225 words:

1. The bot currently uses Question Answering for informational queries and CLU for task intents, with an Orchestration Workflow routing between them. What design change would address the symptom-question problem? Be specific about Azure services or bot design patterns.
2. From a responsible AI perspective, what disclosure and escalation behaviors must this bot have before it can ethically operate in a healthcare context?
3. The hospital is considering adding medical symptom triage as a feature — the bot would ask about symptoms and suggest whether the patient should call 911, visit urgent care, or schedule a routine appointment. Evaluate this use case: what are the benefits, what are the risks, and what human oversight mechanism would you require?

---

## Scenario 2: Enterprise IT Help Desk Bot in Microsoft Teams

A technology company is replacing its email-based IT help desk with a Copilot Studio bot deployed to Microsoft Teams. The bot handles common IT requests: ResetPassword, RequestSoftware, ReportIssue, and CheckTicketStatus. It connects to a Power Automate flow that creates tickets in ServiceNow and sends confirmation messages to users.

A senior engineer argues the bot should have been built with the Azure Bot Framework SDK instead of Copilot Studio because the company's IT processes are "too complex for a low-code tool."

Respond to the following prompts in 175–225 words:

1. Based on what you know about Copilot Studio and the Azure Bot Framework, evaluate the senior engineer's argument. Is it technically founded? What are the actual capability limits of Copilot Studio that might justify this concern?
2. The bot is deployed only in Teams. The company later wants to also make it available on their intranet website and via SMS for off-network employees. Describe what steps are required to add these channels, and whether the approach differs between Copilot Studio and a Bot Framework bot.
3. One of the IT bot's intents is CheckTicketStatus, which retrieves live data from ServiceNow. If ServiceNow is unavailable, what should the bot say, and what does this reveal about the importance of error handling in conversational AI design?

---

## Scenario 3: Multilingual Customer Support Bot

A global e-commerce company serves customers in North America, Latin America, and Western Europe. Their customer service team speaks English, Spanish, and French. The company wants to deploy a bot that handles order tracking, return requests, and account questions in all three languages through a single Question Answering knowledge base.

The knowledge base was initially authored entirely in English. A localization team translated all Q&A pairs into Spanish and French, but early testing shows the Spanish and French responses are often awkward or technically inaccurate.

Respond to the following prompts in 175–225 words:

1. Azure AI Language Question Answering supports multiple languages within a single project. Describe the correct configuration for a multilingual knowledge base and identify one limitation of the current approach (translated English content).
2. The company is considering adding Azure AI Translator as a pre-processing step: detect the user's language, translate the question to English, query the English-only knowledge base, and translate the answer back. Evaluate the trade-offs of this approach versus maintaining separate language-specific knowledge bases.
3. Some Spanish-speaking customers primarily use informal registers or regional slang. What challenge does this create for the bot, and what approach — technical or editorial — would you recommend to address it?

---

## Peer Response Requirements

After posting your initial response to one scenario, reply substantively to at least two classmates who chose different scenarios. Each peer response must be at least 75 words and must:

- Add a specific Azure service or bot design pattern your classmate did not mention, or
- Challenge a technical or ethical claim with evidence from the module or your own knowledge, or
- Extend the analysis to a similar real-world deployment you have encountered or researched

Responses that only agree or restate your classmate's points will not receive full credit.

---

## Grading Rubric (10 points total)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical accuracy | 3 | Correctly applies Azure Bot Service components, channels, and AI Language features |
| Depth of analysis | 3 | Addresses trade-offs and design decisions with specific reasoning |
| Responsible AI reasoning | 2 | Engages substantively with disclosure, escalation, bias, or error handling |
| Peer engagement | 2 | Two qualifying peer responses per requirements above |

---

End of Discussion — Module 09
