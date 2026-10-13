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

---

## Question 11 (5 points)

What is Active Learning in the context of Azure AI Language Question Answering?

A. A feature that automatically retrains the entire QA model on a weekly schedule.

B. A feature that analyzes real user queries that did not match existing Q&A pairs and suggests new pairs the developer can review and add to the knowledge base.

C. A feature that dynamically adjusts the confidence threshold based on user feedback ratings.

D. A feature that uses reinforcement learning to improve bot responses over time without human review.

### Q11 — Correct Answer

B. A feature that analyzes real user queries that did not match existing Q&A pairs and suggests new pairs the developer can review and add to the knowledge base.

### Q11 — Distractor Analysis

- A is incorrect: Active Learning does not automatically retrain the model on a schedule. It surfaces suggestions for human review; the developer decides whether to add them.
- C is incorrect: The confidence threshold is configured manually by the developer. Active Learning influences Q&A pair coverage, not threshold values.
- D is incorrect: Active Learning involves human review of suggestions before additions to the knowledge base. It is not an autonomous reinforcement learning process.

---

## Question 12 (5 points)

A company builds an internal IT helpdesk bot. When users ask "How do I reset my password?" the bot should search the IT knowledge base. When users say "Submit a ticket for a broken printer," the bot should start a ticketing workflow. Which Azure AI Language configuration enables both behaviors through a single classifier?

A. Two separate CLU projects connected by an Azure Logic App.

B. Orchestration Workflow — a meta-project that routes inputs to the appropriate CLU or QA sub-project.

C. A single Question Answering knowledge base with ticket-submission answers stored as Q&A pairs.

D. Custom Text Classification with two categories: Informational and Transactional.

### Q12 — Correct Answer

B. Orchestration Workflow — a meta-project that routes inputs to the appropriate CLU or QA sub-project.

### Q12 — Distractor Analysis

- A is incorrect: Connecting separate CLU projects via Logic Apps is a valid integration approach but is not the built-in Azure AI Language feature designed for this routing pattern.
- C is incorrect: Storing ticket-submission workflows as Q&A pairs is an antipattern. QA retrieves answers; it cannot trigger workflows. CLU is needed for task-oriented commands.
- D is incorrect: Custom Text Classification assigns category labels to documents. It is not a routing mechanism for conversational bots and does not connect to CLU or QA projects.

---

## Question 13 (5 points)

In Azure Bot Service, what is the difference between the Web Chat channel and the Direct Line channel?

A. Web Chat is for mobile apps; Direct Line is for desktop web browsers.

B. Web Chat provides a pre-styled embeddable chat widget for websites; Direct Line is a REST API for custom application integration where the developer builds the UI.

C. Web Chat supports audio messages; Direct Line supports only text.

D. Web Chat is for internal employee tools; Direct Line is for external customer-facing deployments.

### Q13 — Correct Answer

B. Web Chat provides a pre-styled embeddable chat widget for websites; Direct Line is a REST API for custom application integration where the developer builds the UI.

### Q13 — Distractor Analysis

- A is incorrect: Both channels can serve mobile and desktop users. The distinction is not about device type but about how the UI is provided.
- C is incorrect: Supported message types depend on the bot implementation and channel configuration, not on an inherent audio/text split between Web Chat and Direct Line.
- D is incorrect: Both channels can serve internal or external users. The distinction is about the integration pattern and UI ownership, not the audience type.

---

## Question 14 (5 points)

A banking chatbot receives the user input: "Can I move $500 to my savings account?" Which CLU design elements are needed to correctly process this request?

A. Intent: TransferFunds. Entities: Amount ($500), DestinationAccount (savings).

B. Intent: None. This request should be escalated to a human immediately.

C. Intent: CheckBalance. Entity: AccountType (savings).

D. No CLU is needed — this is a FAQ question handled by Question Answering.

### Q14 — Correct Answer

A. Intent: TransferFunds. Entities: Amount ($500), DestinationAccount (savings).

### Q14 — Distractor Analysis

- A is correct: The user's goal (intent) is to transfer money. The specific pieces of information needed (amount, destination) are entities the bot must extract to complete the transfer.
- B is incorrect: Fund transfers are a routine banking bot task, not a reason for immediate human escalation. The None intent handles unrecognized inputs, not complex tasks.
- C is incorrect: CheckBalance is for querying account status. The user explicitly wants to move money, which is a distinct intent.
- D is incorrect: "Move $500 to savings" is a task command, not an informational question. It requires CLU intent classification and entity extraction to trigger the correct workflow.

---

## Question 15 (5 points)

What does the Bot Framework Emulator allow a developer to do during bot development?

A. Deploy the bot directly to Azure without requiring an Azure subscription.

B. Test bot conversations locally, inspect the activity JSON for each turn, and debug the dialog logic before deploying to channels.

C. Train CLU intent models without writing code.

D. Monitor live production bot conversations in real time.

### Q15 — Correct Answer

B. Test bot conversations locally, inspect the activity JSON for each turn, and debug the dialog logic before deploying to channels.

### Q15 — Distractor Analysis

- A is incorrect: The Emulator is a local development tool, not a deployment mechanism. Deploying to Azure requires an Azure subscription and deployment commands.
- C is incorrect: CLU model training is performed in Azure Language Studio or via the Azure AI Language SDK. The Bot Framework Emulator is for testing bot behavior, not for NLP model training.
- D is incorrect: Live production monitoring uses Azure Application Insights or Bot Analytics. The Emulator operates locally against a running bot service on the developer's machine.

---

## Question 16 (5 points)

A multinational company wants to deploy a customer support bot in 15 languages. The same intents and dialog logic apply in all languages. What is the recommended approach?

A. Build 15 separate CLU projects — one per language — and 15 separate bots.

B. Use a single CLU project with multilingual training enabled, and handle translation at the channel level using Azure AI Translator if needed.

C. Build one English CLU project and require all users to interact in English.

D. Use Copilot Studio's offline translation feature to auto-translate all bot responses.

### Q16 — Correct Answer

B. Use a single CLU project with multilingual training enabled, and handle translation at the channel level using Azure AI Translator if needed.

### Q16 — Distractor Analysis

- A is incorrect: Building 15 separate projects creates enormous maintenance overhead. CLU supports multilingual models that can detect and understand multiple languages from a single trained project.
- C is incorrect: Requiring all users to interact in English is an inclusiveness violation and would significantly degrade user experience for non-English speakers.
- D is incorrect: Copilot Studio does not have a built-in offline translation feature that auto-translates all bot responses without additional configuration.

---

## Question 17 (5 points)

A bot designed for a healthcare provider receives the message: "I think I'm having a heart attack." The bot's intent recognition maps this to a CheckAppointment intent with low confidence. What responsible AI design principle is most important for handling this scenario?

A. The bot should ask the user to clarify whether they mean they have a scheduled heart health checkup.

B. The bot must immediately provide a human escalation path or emergency service contact information when life-threatening phrases are detected, regardless of intent confidence.

C. The bot should log the message for later review but respond with the next menu prompt.

D. The bot should increase its confidence threshold to 0.99 to avoid false positives on medical phrases.

### Q17 — Correct Answer

B. The bot must immediately provide a human escalation path or emergency service contact information when life-threatening phrases are detected, regardless of intent confidence.

### Q17 — Distractor Analysis

- A is incorrect: Asking for clarification in a potential medical emergency delays help and treats a life-threatening situation as a navigation problem.
- C is incorrect: Logging and continuing the regular dialog flow could result in the user not receiving emergency assistance. This violates the Reliability and Safety principle.
- D is incorrect: Raising the confidence threshold does not address the emergency response design gap. Safety-critical responses must be triggered independently of standard intent confidence scoring.

---

## Question 18 (5 points)

In a Copilot Studio bot, what is a "topic"?

A. A list of all the users who have interacted with the bot during a session.

B. A self-contained conversation flow triggered by specific user phrases, containing the bot's questions, responses, and branching logic for one area of functionality.

C. A category label assigned to user messages by the bot's intent classifier.

D. A type of Azure Bot Service channel that connects the bot to SharePoint topic pages.

### Q18 — Correct Answer

B. A self-contained conversation flow triggered by specific user phrases, containing the bot's questions, responses, and branching logic for one area of functionality.

### Q18 — Distractor Analysis

- A is incorrect: User session participants are tracked in conversation state, not in topics. Topics define the bot's dialog flows, not user rosters.
- C is incorrect: In Copilot Studio, topics are the authoring units for conversation flows, not classifier labels. Copilot Studio's trigger phrases are conceptually similar to CLU intents but are managed within the Copilot Studio canvas.
- D is incorrect: SharePoint integration is a separate connector configuration. Topics are a core Copilot Studio authoring concept, not a channel type.

---

## Question 19 (5 points)

What is the primary benefit of configuring a fallback response (also called a "no match" response) in a Question Answering knowledge base?

A. It prevents the bot from being deployed until all possible user questions are answered.

B. It provides a graceful user experience when a question cannot be matched, offering guidance or a human handoff instead of silence or an error.

C. It automatically generates a new Q&A pair whenever a fallback is triggered.

D. It increases the confidence threshold for all existing Q&A pairs.

### Q19 — Correct Answer

B. It provides a graceful user experience when a question cannot be matched, offering guidance or a human handoff instead of silence or an error.

### Q19 — Distractor Analysis

- A is incorrect: The fallback response is deployed alongside the knowledge base to handle unmatched questions during live use. It is not a gate that prevents deployment.
- C is incorrect: The fallback response is a static message defined by the developer. Automatically generating new Q&A pairs is the Active Learning feature, not the fallback response.
- D is incorrect: The fallback response is independent of the confidence threshold. The threshold controls when to display the fallback; the fallback itself is the message shown.

---

## Question 20 (5 points)

A company's bot is being audited for transparency compliance. The audit requires that users always know they are interacting with an automated system and not a human. Which design practice directly addresses this requirement?

A. Configure the bot to use the company's brand colors in the Web Chat widget.

B. Include a clear disclosure in the bot's greeting message and ensure the bot does not claim to be human if asked.

C. Add all conversation logs to a compliance archive database.

D. Enable Active Learning so the bot improves over time.

### Q20 — Correct Answer

B. Include a clear disclosure in the bot's greeting message and ensure the bot does not claim to be human if asked.

### Q20 — Distractor Analysis

- A is incorrect: Branding the chat widget with company colors is a UI customization, not a transparency disclosure. Visual branding does not inform users they are interacting with an AI.
- C is incorrect: Archiving conversations supports compliance and privacy accountability but does not address the user-facing transparency requirement of disclosing automation.
- D is incorrect: Active Learning improves knowledge base coverage over time. It does not communicate to users that the system is automated.

---

End of Quiz — Module 09
