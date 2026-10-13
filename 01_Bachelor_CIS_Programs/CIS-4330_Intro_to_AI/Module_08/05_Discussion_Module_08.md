# Discussion Forum: Module 08 — Natural Language Processing with Azure

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## Due Dates: Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM

---

## Overview

Natural language processing is embedded in systems that touch nearly every domain — healthcare, law, finance, education, customer service, and journalism. This discussion asks you to apply NLP concepts to real-world scenarios and critically evaluate both the capability and the limitations of Azure AI Language services. Strong posts demonstrate technical precision alongside ethical awareness.

Professor Nash note: Each scenario involves a genuine tension between efficiency and risk, or between capability and appropriate use. I am looking for posts that take both sides seriously. Cite specific Azure services and features from the module in every post.

---

## Scenario 1: Automated Sentiment Scoring for Employee Surveys

A company with 8,000 employees conducts quarterly engagement surveys. Each survey includes five open-ended text questions. Leadership wants to use Azure AI Language sentiment analysis and key phrase extraction to automatically score and summarize responses rather than reading them manually.

The HR director argues this will surface systemic issues faster. The employee union representative argues that automated sentiment scoring may misread sarcasm, cultural idioms, and context — particularly from non-native English speakers — and could lead to dismissing real complaints because they score as "neutral."

Respond to the following prompts in 175–225 words:

1. Which specific Azure AI Language features would be used in this system, and what would each feature contribute?
2. The union representative raises a concern about non-native English speakers. Is this a technically founded concern? What does the module say about how language models handle linguistic variation?
3. Propose one safeguard that would address the most serious risk in this system while still achieving the efficiency goal.

---

## Scenario 2: CLU-Powered Legal Intake Bot

A mid-sized law firm wants to deploy a chatbot on its website to triage incoming client inquiries. A CLU model would classify the type of legal matter — PersonalInjury, CorporateLaw, FamilyLaw, RealEstate, Immigration, or None — and extract entities such as the state where the matter occurred and an estimated dollar value if mentioned.

The firm's technology partner proposes auto-routing each inquiry to the correct department and sending an automated acknowledgment email without any attorney review.

Respond to the following prompts in 175–225 words:

1. Design the CLU schema for this bot. Name the intents, describe at least two entities, and identify what entity type (learned, list, prebuilt) you would use for each entity.
2. The None intent is critical in this scenario. Explain what inputs the None intent should capture and what should happen when the model predicts None.
3. The proposal includes sending an automated response without attorney review. What risks does this create, and what design change would you recommend to manage them?

---

## Scenario 3: Multilingual PII Redaction in a Global Support Center

A global technology company operates customer support centers in 12 countries. Support chat transcripts are stored in a central data lake for quality analysis and model training. Transcripts arrive in English, Spanish, French, Portuguese, German, Japanese, and Arabic.

The data engineering team proposes using Azure AI Language PII detection with redaction to automatically scrub all transcripts before storage.

Respond to the following prompts in 175–225 words:

1. Describe how PII detection and redaction works technically. What types of PII would be identified in a typical support chat, and how does the service handle them?
2. The transcripts arrive in seven languages. What does this mean for the PII detection capability, and what limitation should the team be aware of?
3. The team plans to fully automate PII redaction with no human review. Identify one scenario where automated redaction could fail in a way that creates legal or reputational risk, and propose a mitigation.

---

## Peer Response Requirements

After posting your initial response to one scenario, reply substantively to at least two classmates who selected different scenarios. Each peer response must be at least 75 words and must:

- Add a specific technical detail or Azure service consideration your classmate did not mention, or
- Respectfully challenge a claim in your classmate's post using evidence from the module, or
- Extend the scenario to a real-world industry example from your own experience or research

Responses that only agree or summarize what the classmate said will not receive full credit.

---

## Grading Rubric (10 points total)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical accuracy | 3 | Correctly names and applies Azure NLP services and features |
| Depth of analysis | 3 | Engages with trade-offs, limitations, and nuance beyond surface observations |
| Responsible AI reasoning | 2 | Substantively addresses bias, fairness, privacy, or human oversight |
| Peer engagement | 2 | Two peer responses meeting the requirements above |

---

End of Discussion — Module 08
