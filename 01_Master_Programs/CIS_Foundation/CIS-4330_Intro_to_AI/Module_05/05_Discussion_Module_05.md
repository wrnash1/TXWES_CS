# Discussion Forum: Module 05 - Natural Language Processing (NLP) Fundamentals

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Due Dates:** Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM
**Total Points:** 10

---

## Instructions

Read all three scenarios below. Choose one scenario for your initial post. Identify your scenario choice (A, B, or C) at the top of your post.

---

## Scenario A: The Automated Customer Support System

A regional bank is deploying an AI-powered customer support chatbot to handle 70% of incoming support calls and messages. The chatbot uses Azure Language Understanding (CLU) for intent recognition and Azure Language Service for sentiment detection. During a pilot, customers who express high negative sentiment are automatically escalated to a human agent. The bank's CTO reports a 40% reduction in average handle time and a 22% reduction in customer service headcount.

However, customer advocacy groups raise two concerns: (1) customers who speak with accents or use non-standard English are being misrouted more often than native English speakers; (2) elderly customers who prefer speaking to a human are being denied that option unless the system detects negative sentiment in their words.

In your initial post (175-225 words), address all of the following:

- Identify which Azure NLP services power the two key functions described (sentiment escalation and intent recognition) and explain how each works conceptually.

- The misrouting rate for non-standard English speakers raises a responsible AI concern. Identify the specific Microsoft principle most relevant and explain why this particular deployment pattern creates the risk.

- Do you believe automatic headcount reduction is a responsible application of conversational AI in a regulated industry like banking? Defend your position using at least one responsible AI principle.

---

## Scenario B: The Multilingual Content Moderation Challenge

A social media platform operates in 47 countries and receives 15 million posts per day in over 60 languages. The trust and safety team needs to detect hate speech, harassment, and misinformation across all languages. The team has built a highly accurate hate speech detection model in English (F1 = 0.91) but has very limited labeled training data in lower-resource languages such as Swahili, Bengali, and Haitian Creole.

The engineering team proposes two options:

Option 1: Use Azure Translator to translate all non-English posts to English, then apply the English hate speech model.

Option 2: Train separate custom classification models for each language using whatever labeled data is available, even if it is only a few hundred examples.

In your initial post (175-225 words), address all of the following:

- Evaluate Option 1 technically. What NLP tasks does this pipeline involve, and what is the key risk introduced by the translation step?

- Evaluate Option 2 technically. What problem does having only a few hundred labeled examples per language create for a custom text classification model?

- From a responsible AI perspective, which option better serves users who write in lower-resource languages? Identify the specific principle and explain your reasoning.

---

## Scenario C: The Legal Document Analysis Tool

A large law firm wants to use NLP to analyze thousands of historical contract documents to extract key parties, financial obligations, important dates, and penalty clauses. The goal is to reduce the time paralegals spend manually reviewing contracts before flagging them for attorney review.

The firm's senior partner is cautious. "Legal documents are highly precise," she notes. "A missed entity or a misread clause could expose our clients to serious risk. How confident are we that the NLP system will not miss critical information?"

In your initial post (175-225 words), address all of the following:

- Which specific Azure NLP capabilities would be required for this use case? Be specific about which are prebuilt and which would require custom training.

- The senior partner raises a concern about missed entities (false negatives). In NLP, this maps to a recall problem. Explain recall in the context of NER and why high recall is more important than high precision in this legal context.

- Propose a workflow that uses NLP automation while keeping human attorneys accountable for the final document review. Which responsible AI principle does your proposed workflow embody?

---

## Peer Response Guidelines

Reply to at least two classmates who chose different scenarios than you. Each peer response must be at least 50 words and must add substantive analysis beyond agreement.

Suggested peer response approaches:

- Challenge the Azure service selection your peer proposed with a more appropriate alternative.

- Raise an NLP limitation (bias, hallucination, low-resource language) that your peer did not address.

- Connect your peer's scenario to a real NLP deployment story you have encountered.

- Propose a metric or evaluation method that would help the organization in your peer's scenario measure NLP system quality.

---

## Grading Rubric (10 Points Total)

### Initial Post — 6 Points

**6 pts:** Addresses all required sub-questions with accurate NLP and responsible AI vocabulary. Meets 175-225 word requirement. Demonstrates original reasoning beyond course definitions.

**4-5 pts:** Addresses most sub-questions with generally correct analysis. Minor vocabulary errors or one sub-question underdeveloped. Word count met.

**2-3 pts:** Fewer than half the sub-questions addressed, or significant factual errors about NLP tasks or Azure services. May not meet word count.

**0-1 pts:** Post missing or does not substantively engage with the scenario.

### Peer Responses — 4 Points

**4 pts:** Substantive responses to at least two peers from different scenarios. Each adds new analysis or a counterpoint. Minimum 50 words each.

**2-3 pts:** Responds to two peers with limited substance, or responds to only one peer.

**0-1 pts:** No responses or all responses superficial.

---

## Professor Nash Note

Scenario B raises a question that real NLP teams at global platforms face every day: how do you build a system that works equitably across languages when your labeled data is concentrated in a few high-resource languages? There is no perfect answer, and both options have genuine drawbacks. The strongest posts will engage seriously with the trade-offs rather than declaring one option clearly superior.
