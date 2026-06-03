# Video Script: Module 09 — Conversational AI and Azure Bot Service

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Microsoft Azure AI Fundamentals (AI-900)

---

## INTRO SEGMENT (0:00 – 1:30)

Welcome to Module 9. I'm Professor Nash. In Module 8 we learned how Azure's NLP services understand language. Today we put that understanding to work inside conversational AI — chatbots, virtual assistants, and automated agents.

By the end of this module you will be able to describe the Azure Bot Framework and Azure Bot Service, explain how Question Answering powers FAQ bots, connect CLU intents and entities into a bot dialog flow, understand bot channels and how bots reach users across platforms, and describe Microsoft Copilot Studio as a low-code bot authoring tool.

Let's begin with a question: what makes a bot feel intelligent?

---

## SECTION 1: What Is Conversational AI? (1:30 – 3:30)

A conversational AI system — commonly called a chatbot or virtual agent — allows users to interact with a computer using natural language rather than menus, forms, or command-line syntax.

Conversational AI spans a wide spectrum.

At the simpler end are **rule-based bots** that follow fixed decision trees. "Press 1 for billing, press 2 for support." These are reliable but brittle — they break the moment a user phrases a request differently than anticipated.

In the middle are **retrieval-augmented bots** that use NLP to match user questions to answers in a knowledge base. These handle a much wider variety of phrasings.

At the sophisticated end are **generative AI bots** that use large language models to generate responses dynamically. We will cover those in Module 10.

Azure provides tools at every point on this spectrum. Today we focus on the middle tier — structured bots built with the Bot Framework, Question Answering, and CLU.

A well-designed bot has three layers:

- **Language understanding** — what does the user want?
- **Dialog management** — what should the bot do next?
- **Channel delivery** — where does the conversation happen?

---

## SECTION 2: Azure Bot Framework and Bot Service (3:30 – 6:00)

The **Azure Bot Framework** is an open-source SDK for building bots in C#, JavaScript, Python, or Java. It provides the scaffolding, activity handling, dialog management, and middleware infrastructure that every bot needs.

**Azure Bot Service** is the managed cloud platform for hosting, connecting, and managing bots built with the Bot Framework or other tools.

**[SHOW DEMO]** In the Azure portal, navigate to Create a Resource and search for "Azure Bot." Show the resource creation blade, pointing out the Bot Handle field (globally unique identifier), Messaging endpoint, and the choice between Single Tenant, Multi Tenant, and Managed Identity authentication.

The Bot Framework models conversations as a series of **activities** flowing between the user and the bot. The most common activity type is the message activity — a text or rich media message. Other activity types include conversation-update (user joined or left), typing (bot is processing), and event (background signal).

Bots are implemented as web services. The Bot Service acts as a relay: it receives a message from a channel (Teams, web chat, Slack), forwards it to your bot's messaging endpoint as an HTTP POST, receives the response, and delivers it back to the user.

This architecture means your bot code runs in your own Azure App Service or container, and the Bot Service handles all the channel-specific protocol translation.

---

## SECTION 3: Question Answering (6:00 – 9:00)

The most common bot use case in enterprises is the FAQ bot — a system that answers questions from a structured knowledge base.

**Azure AI Language — Question Answering** (formerly QnA Maker) builds and hosts this kind of knowledge base.

The workflow has four steps.

**Step one: Create a knowledge base project.** You create a Question Answering project in Language Studio.

**Step two: Populate the knowledge base.** You add question-and-answer pairs in three ways: manual entry, import from a URL (FAQ page, SharePoint page), or upload a document (PDF, Word, Excel, TSV).

**Step three: Train and publish.** You train the model and publish the knowledge base to a prediction endpoint.

**Step four: Query the endpoint.** At runtime, your bot sends the user's question to the endpoint and receives the best matching answer with a confidence score.

**[SHOW DEMO]** Navigate to Language Studio. Select "Custom question answering." Create a new project. Click "Add source" and paste in a URL from a publicly accessible FAQ page. Show the auto-extracted question-answer pairs. Edit one to improve the answer. Click "Save changes." Show the "Test knowledge base" panel — type a question and observe the matched answer and confidence score.

### Multi-Turn Conversations

Question Answering supports multi-turn conversations through a feature called **follow-up prompts**. After answering a question, the bot can offer related follow-up questions. This turns a flat FAQ into a navigable conversation tree.

For example:

- User: "What is your refund policy?"
- Bot: "Our standard refund window is 30 days." [Follow-up prompts: "How do I start a refund?" | "What items are non-refundable?"]

### Confidence Threshold

You configure a confidence threshold — say 0.70 — below which the bot responds with a fallback message like "I am not sure about that. Would you like to speak with a human agent?" rather than returning a low-confidence answer.

This is good practice and prevents the bot from confidently giving wrong answers.

---

## SECTION 4: Combining CLU and Question Answering (9:00 – 11:30)

Real-world bots typically need both capabilities:

- **CLU** handles task-oriented requests: "Book a meeting," "Cancel my order," "Reset my password"
- **Question Answering** handles informational requests: "What are your hours?" "How long does shipping take?"

The **Orchestration Workflow** feature in Azure AI Language lets you create a meta-model that routes incoming user messages to either a CLU project or a Question Answering project, whichever is the better match.

**[SHOW DEMO]** In Language Studio, show a new project with project type "Orchestration workflow." Show how existing CLU and QA projects are connected as targets. The orchestration model learns which inputs to route to CLU and which to route to QA.

This architecture means you only need to expose one endpoint to your bot. The bot sends every user message to the orchestration endpoint, and the model decides internally whether this is a task request or an informational query.

### Dialog Management

Even after understanding the user's intent, a bot often needs more information before it can complete a task. Collecting this information is the job of **dialog management**.

The Bot Framework SDK provides a dialog system with several built-in dialog types.

**Waterfall dialogs** execute a fixed sequence of prompts. Useful when you always need the same pieces of information in a predictable order.

**Adaptive dialogs** are more flexible — they respond to context and allow branching, interruptions (when the user says something unexpected mid-flow), and dynamic property collection.

**Component dialogs** are reusable dialog modules you can compose into larger conversation flows.

---

## SECTION 5: Bot Channels (11:30 – 13:30)

A bot channel is a platform through which users interact with the bot. Azure Bot Service provides built-in connectors for many popular channels.

| Channel | Common Use Case |
|---------|----------------|
| Web Chat | Embedded on a website or web app |
| Microsoft Teams | Internal enterprise assistant |
| Slack | Workspace automation and support |
| Facebook Messenger | Customer service on social media |
| Twilio SMS | Text message-based interactions |
| Email | Email-triggered automated responses |
| Telephone (Direct Line Speech) | Voice bot using Speech service |

You configure channels in the Azure portal under your Bot Service resource. Each channel has its own connection settings — typically an app ID and secret provided by the channel platform.

The key architectural point is that your bot code does not change when you add a new channel. The Bot Framework SDK normalizes all channel-specific message formats into a uniform Activity object. Your business logic operates on activities, not on channel-specific protocols.

**[SHOW DEMO]** In the Azure portal, navigate to a Bot Service resource. Click "Channels" in the left menu. Show the list of available channel connectors. Click "Microsoft Teams" and show the configuration panel. Highlight that connecting to Teams requires only a few clicks once the bot is deployed.

---

## SECTION 6: Direct Line and the Bot Framework Emulator (13:30 – 15:30)

### Direct Line

**Direct Line** is a REST API channel that allows any custom application — a mobile app, a desktop app, a kiosk — to connect to a Bot Service. Instead of using a pre-built channel connector, you use the Direct Line API to send and receive activities programmatically.

This is how developers embed a bot into a custom web application: the app calls Direct Line to relay messages, giving full control over the user interface.

### Bot Framework Emulator

The **Bot Framework Emulator** is a desktop development tool that lets you test and debug your bot locally before deploying it to Azure Bot Service.

The emulator:

- Simulates the Bot Service relay locally
- Shows all activity traffic in a structured log
- Lets you inspect every request and response in detail
- Supports direct connection to local bot endpoints with NGROK tunneling for testing channel features

This is an essential tool in the Bot Framework development workflow. You do not need Azure Bot Service deployed just to test that your bot logic is working correctly.

**[SHOW DEMO]** Show the Bot Framework Emulator application. Open a connection to a locally running echo bot. Type a message. Point out the activity log panel showing the JSON of the message activity and the response activity.

---

## SECTION 7: Microsoft Copilot Studio (15:30 – 18:30)

Not every organization has developers to write Bot Framework code. **Microsoft Copilot Studio** — formerly known as Power Virtual Agents — is a low-code / no-code platform for building conversational AI agents.

With Copilot Studio you create bots using a graphical conversation designer:

- Define topics — units of conversation triggered by phrases or intents
- Build conversation flows visually using a node-based canvas
- Connect to data via Power Automate for actions like looking up records or sending emails
- Publish to channels including Teams, websites, and custom apps

Copilot Studio is tightly integrated with the Microsoft 365 ecosystem, making it ideal for internal corporate assistants that interact with SharePoint, Outlook, Dynamics 365, and other Microsoft services.

**[SHOW DEMO]** Navigate to copilotstudio.microsoft.com. Show the topic authoring canvas for an existing sample bot. Walk through a topic node: trigger phrases at the top, message nodes, question nodes that collect information, condition branches, and action nodes connected to Power Automate flows.

### When to Use Copilot Studio vs. Bot Framework

| Dimension | Copilot Studio | Azure Bot Framework |
|-----------|---------------|---------------------|
| Target users | Business analysts, citizen developers | Professional developers |
| Coding required | No | Yes (C#, JS, Python) |
| Customization depth | Moderate | Full |
| Integration | Microsoft 365, Power Platform | Any service via code |
| Deployment | Managed by Microsoft | Self-hosted or Azure App Service |
| Time to first bot | Hours | Days to weeks |

For AI-900, you should know both options exist and understand the core distinction: Copilot Studio for low-code, Bot Framework for pro-code.

---

## SECTION 8: Responsible Conversational AI (18:30 – 20:30)

Chatbots introduce a distinct set of responsible AI considerations.

**Transparency.** Users should always know they are talking to a bot, not a human. Microsoft's guidelines and many jurisdictions' regulations require disclosure. Deceptive humanization — giving the bot a name like "Sarah" without disclosing it is AI — erodes trust and may violate consumer protection law.

**Graceful handoff.** Bots will encounter questions or situations they cannot handle. A well-designed bot always offers a path to a human agent. Trapping users in bot loops with no escalation option is a serious usability and trust failure.

**Scope limitation.** Bots should be designed to refuse out-of-scope requests rather than attempt to answer anything. This prevents the bot from providing inaccurate information in domains it was not designed for.

**Bias in training data.** Knowledge bases and CLU training data reflect the language and assumptions of their creators. If the training data systematically excludes certain user populations or phrasings, those users will receive worse service.

**Privacy.** Bot conversations may contain sensitive information — health symptoms, financial details, personal circumstances. Organizations must handle this data with the same care as any sensitive customer data.

**[SHOW DEMO]** Show an example of a well-designed bot conversation that discloses it is an AI at the start and offers "Talk to a human" at every step.

---

## SECTION 9: AI-900 Exam Alignment and Recap (20:30 – 22:30)

Let's connect to AI-900 objectives.

The exam tests your ability to describe the components of a conversational AI solution, identify when to use Question Answering vs. CLU, explain bot channels and how they work, and describe Copilot Studio as a low-code authoring tool.

Key terms for the exam:

- **Azure Bot Framework** — open-source SDK for building bots in code
- **Azure Bot Service** — managed cloud platform for hosting and connecting bots to channels
- **Question Answering** — knowledge-base service that matches questions to answers
- **CLU** — intent classification and entity extraction for command-based bots
- **Orchestration Workflow** — meta-model that routes to CLU or QA
- **Channel** — platform connecting users to the bot (Teams, web chat, SMS)
- **Direct Line** — REST API for custom application channel integration
- **Copilot Studio** — low-code bot authoring tool integrated with Microsoft 365
- **Activity** — the fundamental unit of communication in the Bot Framework
- **Multi-turn** — a conversation requiring multiple exchanges to gather needed information
- **Follow-up prompts** — QA feature enabling multi-turn navigation through related answers
- **Confidence threshold** — minimum score below which QA returns a fallback answer

---

## OUTRO (22:30 – 23:30)

In the lab you will build a Question Answering knowledge base, connect it to a bot in the Bot Framework Emulator, and configure at least one follow-up prompt for a multi-turn conversation.

Next week we move into generative AI and Azure OpenAI Service — one of the fastest-moving areas in all of technology. I will see you in Module 10.

---

End of Script — Module 09. Estimated delivery: 22 minutes with demos.
