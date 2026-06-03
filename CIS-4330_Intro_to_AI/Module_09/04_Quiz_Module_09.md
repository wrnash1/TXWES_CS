# Quiz: Module 09 — Conversational AI and Azure Bot Service

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Domain: Describe features of conversational AI workloads on Azure

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Submit through the course LMS.

---

## Question 1

A university wants to deploy a chatbot on its website that answers common student questions such as "What are the library hours?" and "How do I register for classes?" The answers should come from the university's existing FAQ documents. Which Azure service is most appropriate?

A. Azure AI Language — Conversational Language Understanding

B. Azure AI Language — Question Answering

C. Azure Bot Framework SDK — Waterfall Dialogs

D. Azure AI Vision — Spatial Analysis

### Q1 — Correct Answer

B. Azure AI Language — Question Answering

### Q1 — Distractor Analysis

- A is incorrect: CLU classifies intents and extracts entities for task-oriented commands. It does not retrieve answers from an existing FAQ document.
- C is incorrect: Waterfall Dialogs is a Bot Framework SDK component for managing dialog flow. It is not a service for matching questions to answers; it would require a separate data source and retrieval logic.
- D is incorrect: Spatial Analysis is a computer vision service for analyzing physical spaces and video. It has no conversational or text-retrieval capability.

---

## Question 2

In Azure AI Language Question Answering, a confidence threshold is configured at 0.70. A user asks a question and the best matching answer scores 0.55. What does the bot return?

A. The answer with the 0.55 score, since it is the best available match

B. An error message indicating the knowledge base is unavailable

C. The configured fallback answer, because the score is below the threshold

D. The top three answers scored 0.55, 0.43, and 0.31 for the user to choose from

### Q2 — Correct Answer

C. The configured fallback answer, because the score is below the threshold

### Q2 — Distractor Analysis

- A is incorrect: The confidence threshold exists precisely to prevent low-confidence answers from being returned. When the threshold is not met, the fallback response is used.
- B is incorrect: A score below the threshold triggers the fallback message, not a service error. The knowledge base is functioning correctly.
- D is incorrect: Returning multiple low-confidence options is not the default behavior. The threshold is the decision boundary between returning the best answer and returning the fallback.

---

## Question 3

What is the purpose of the None intent in a Conversational Language Understanding (CLU) project?

A. It stores the training utterances that were rejected during the labeling process

B. It captures user inputs that do not match any defined application intent, preventing false positive intent matches

C. It is the default intent assigned to all inputs until the model is trained

D. It represents the bot's response when it has no more questions to ask the user

### Q3 — Correct Answer

B. It captures user inputs that do not match any defined application intent, preventing false positive intent matches

### Q3 — Distractor Analysis

- A is incorrect: Rejected utterances are not stored in None. None is an active intent with training examples you provide.
- C is incorrect: Untrained models do not assign None by default. None is a deliberately designed intent that requires its own training utterances.
- D is incorrect: Intents represent user goals, not bot states. None is on the user-input side of the conversation, not the bot-response side.

---

## Question 4

A company builds a bot using Azure Bot Framework and wants to deploy it so that employees can interact with it inside Microsoft Teams, and customers can interact with it through the company's public website. How is this typically accomplished?

A. Build two separate bots — one for Teams and one for the website

B. Configure both Microsoft Teams and Web Chat as channels in Azure Bot Service for a single bot

C. Export the bot logic to two different programming languages for each platform

D. Microsoft Teams and web chat cannot be connected to the same Azure bot simultaneously

### Q4 — Correct Answer

B. Configure both Microsoft Teams and Web Chat as channels in Azure Bot Service for a single bot

### Q4 — Distractor Analysis

- A is incorrect: One of the core benefits of Azure Bot Service channels is that a single bot can be connected to multiple channels simultaneously. Building two bots doubles the maintenance burden unnecessarily.
- C is incorrect: The same bot code handles all channels. The Bot Framework SDK normalizes channel-specific activity formats, so no language changes are needed.
- D is incorrect: Azure Bot Service explicitly supports multiple simultaneous channels for a single bot. Teams and Web Chat can both be active at the same time.

---

## Question 5

Which Azure Bot Service channel should a developer use to embed a bot inside a custom-built iOS mobile application?

A. Microsoft Teams

B. Twilio SMS

C. Direct Line

D. Facebook Messenger

### Q5 — Correct Answer

C. Direct Line

### Q5 — Distractor Analysis

- A is incorrect: Teams is a Microsoft-specific platform app, not a custom mobile app integration channel.
- B is incorrect: Twilio SMS is for text message-based interactions via phone numbers, not for embedding in a custom mobile application.
- D is incorrect: Facebook Messenger connects the bot to the Messenger platform. It does not enable integration into a custom-built iOS app.

---

## Question 6

A retail company wants to deploy a bot that handles both task requests ("Track my order") and informational questions ("What is your return policy?") through a single API endpoint. Which Azure AI Language feature enables this?

A. Custom Text Classification

B. Orchestration Workflow

C. Active Learning

D. Entity Linking

### Q6 — Correct Answer

B. Orchestration Workflow

### Q6 — Distractor Analysis

- A is incorrect: Custom Text Classification labels documents with custom categories. It is not a routing mechanism for bots.
- C is incorrect: Active Learning is a Question Answering feature that suggests new Q&A pairs from unmatched user queries. It does not route between CLU and QA.
- D is incorrect: Entity Linking connects recognized entities to a knowledge base like Wikipedia. It is an NLP feature, not a bot routing mechanism.

---

## Question 7

Microsoft Copilot Studio is described as a low-code bot authoring tool. Which scenario is it most appropriate for?

A. A software development team building a highly customized bot with proprietary APIs, custom middleware, and complex dialog branching logic written in Python

B. An HR business analyst with no coding experience who needs to build an employee onboarding assistant connected to SharePoint and Teams

C. A data scientist building a bot that uses a custom PyTorch model for intent classification

D. A team that needs to deploy a bot to a custom IoT device running a Linux container

### Q7 — Correct Answer

B. An HR business analyst with no coding experience who needs to build an employee onboarding assistant connected to SharePoint and Teams

### Q7 — Distractor Analysis

- A is incorrect: Complex custom development with proprietary APIs and custom middleware is the use case for the Azure Bot Framework SDK, not Copilot Studio.
- C is incorrect: Custom ML model integration requires code-level control that Copilot Studio's no-code environment does not support.
- D is incorrect: Deploying to Linux containers on IoT devices requires pro-code deployment patterns available in the Bot Framework, not Copilot Studio's managed hosting.

---

## Question 8

In the Azure Bot Framework activity model, what is the most common type of activity exchanged between a user and a bot?

A. conversationUpdate

B. event

C. typing

D. message

### Q8 — Correct Answer

D. message

### Q8 — Distractor Analysis

- A is incorrect: conversationUpdate fires when a user joins or leaves a conversation, or when the bot is added to a channel. It occurs far less frequently than message activities.
- B is incorrect: event activities carry background signals not visible to the user. They are used for system integration, not for standard conversational exchanges.
- C is incorrect: typing indicates that the sender is composing a message. It is a transient signal, not the primary vehicle for conversation content.

---

## Question 9

A travel company deploys a customer service chatbot on its website. The bot is designed to help users find flights. A user asks: "My father passed away and I need to cancel everything urgently." The bot cannot find a flight-related intent and keeps prompting the user to try again. What responsible AI design principle is violated?

A. Fairness — the bot treats users differently based on message length

B. Transparency — the user does not know they are talking to a bot

C. Graceful escalation — the bot has no path to transfer the user to a human agent

D. Privacy — the bot is storing the user's personal situation without consent

### Q9 — Correct Answer

C. Graceful escalation — the bot has no path to transfer the user to a human agent

### Q9 — Distractor Analysis

- A is incorrect: There is no indication the bot is treating users differently by demographic or message length. The failure is about handling out-of-scope distress, not fairness.
- B is incorrect: The scenario does not provide evidence the user is unaware they are talking to a bot. Transparency may be a concern but is not the primary failure in this scenario.
- D is incorrect: While conversation logging raises privacy considerations, the immediate design failure described is the bot looping without offering a human handoff in a clearly sensitive situation.

---

## Question 10

Question Answering (formerly QnA Maker) supports follow-up prompts. What is the primary purpose of this feature?

A. To send the user's question to a CLU model when the QA model is not confident

B. To enable multi-turn conversations by linking answers to related follow-up questions

C. To automatically generate new Q&A pairs from unmatched user queries

D. To translate the answer into the user's detected language

### Q10 — Correct Answer

B. To enable multi-turn conversations by linking answers to related follow-up questions

### Q10 — Distractor Analysis

- A is incorrect: Routing to CLU when confidence is low is the function of an Orchestration Workflow, not follow-up prompts.
- C is incorrect: Generating new Q&A pair suggestions from unmatched queries is the Active Learning feature, not follow-up prompts.
- D is incorrect: Translation is handled by Azure AI Translator, not by Question Answering's follow-up prompt feature.

---

End of Quiz — Module 09
