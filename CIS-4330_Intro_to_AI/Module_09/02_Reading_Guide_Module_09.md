# Reading Guide: Module 09 — Conversational AI and Azure Bot Service

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4330 &BULL; INTRODUCTION TO ARTIFICIAL INTELLIGENCE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Domain: Describe features of conversational AI workloads on Azure

---

## Overview

This reading guide covers the Azure Bot Framework, Azure Bot Service, Question Answering, CLU integration, bot channels, and Microsoft Copilot Studio. Estimated reading time: 45–60 minutes.

---

## Section 1: Conversational AI Fundamentals

### The Spectrum of Bot Complexity

Conversational AI systems range from deterministic scripted bots to fully generative large language model agents.

| Type | How It Works | Strengths | Weaknesses |
|------|-------------|-----------|------------|
| Rule-based / decision tree | Fixed logic paths, keyword triggers | Predictable, auditable | Brittle; breaks on novel phrasing |
| Retrieval-based (QA) | Matches questions to pre-written answers | Handles varied phrasing; answers are controlled | Limited to known Q&A pairs |
| Intent-based (CLU) | Classifies intent, extracts entities, executes action | Flexible commands; structured output | Requires training data; schema design effort |
| Generative (LLM) | Generates responses from a language model | Broad coverage; natural conversation | Less predictable; requires guardrails |

For AI-900, focus on retrieval-based (Question Answering) and intent-based (CLU) bots built on Azure Bot Framework and Copilot Studio.

### Three Layers of a Bot

Every conversational AI solution has three layers.

**Language understanding** converts raw user text into structured intent and entity data. This is the NLP layer — CLU, Question Answering, or an LLM.

**Dialog management** determines the bot's next action: ask a clarifying question, call an API, return an answer, or hand off to a human. This is the logic layer — Bot Framework dialogs, Copilot Studio topics, or custom code.

**Channel delivery** sends the bot's response to the user via the appropriate platform. This is the connectivity layer — Azure Bot Service channels.

---

## Section 2: Azure Bot Framework and Bot Service

### Architecture Overview

The Bot Framework follows a request-response model over HTTP.

```text
User → Channel → Azure Bot Service → Bot Endpoint (your code)
User ← Channel ← Azure Bot Service ← Bot Response
```

The Bot Service relays activities between the channel and your bot's web service. Your bot never communicates directly with the channel protocol.

### Activity Types

| Activity Type | Description |
|--------------|-------------|
| message | A text or rich-media message from user or bot |
| conversationUpdate | User joined, left, or bot was added to conversation |
| typing | Indicates the sender is composing a message |
| event | Background signal not shown to the user |
| handoff | Escalation to a human agent |

All activities share a common schema with fields including `type`, `text`, `from`, `recipient`, `channelId`, `timestamp`, and `channelData` for channel-specific metadata.

### Bot Framework SDK Languages

The Bot Framework SDK is available in C# (.NET), JavaScript/TypeScript (Node.js), Python, and Java. All SDK versions implement the same Bot Framework protocol.

### Authentication Modes

| Mode | Description |
|------|-------------|
| Single Tenant | Bot is used only within one Azure Active Directory tenant |
| Multi Tenant | Bot can be used across multiple tenants (typical for public bots) |
| Managed Identity | Uses Azure managed identity; no app secret required |

---

## Section 3: Question Answering — Deep Dive

### Knowledge Base Sources

| Source Type | Description |
|-------------|-------------|
| Manual entry | Type Q&A pairs directly in Language Studio |
| URL import | Scrapes FAQ pages or SharePoint pages automatically |
| File upload | Parses Q&A from PDF, Word, Excel, or TSV files |
| Editorial | Chit-chat personality phrases (greetings, thanks, etc.) |

### Answer Selection

When a user submits a question, Question Answering computes a relevance score between the question and each Q&A pair in the knowledge base. The pair with the highest score is returned, along with the confidence score.

If the confidence score falls below the configured threshold, the knowledge base returns the configured **No answer** fallback message.

### Multi-Turn Conversations

Follow-up prompts convert a flat Q&A knowledge base into a tree of linked answers. Each answer can have up to five follow-up prompts that suggest related questions.

Follow-up prompts are displayed as quick-reply buttons in web chat and Teams, allowing users to navigate without typing.

### Active Learning

When enabled, active learning collects questions that were asked but did not match well to any existing answer. It then suggests these as potential additions to the knowledge base. A human reviewer approves or rejects each suggestion. This improves the knowledge base over time from real user traffic.

---

## Section 4: Orchestration Workflow

### What It Does

The Orchestration Workflow project type in Azure AI Language creates a routing layer that decides whether an incoming user message should be sent to a CLU project, a Question Answering project, or another connected language project.

### When to Use It

Use an Orchestration Workflow when your bot needs to handle both task-oriented commands (CLU) and informational questions (Question Answering) and you want a single API endpoint for your bot code.

Without orchestration, your bot code would need to call both CLU and QA separately and implement its own routing logic. The orchestration model learns to route from training data.

### Configuration

| Setting | Description |
|---------|-------------|
| Connected project type | CLU or Question Answering |
| Connected project name | Name of the existing project in Language Studio |
| Intent name in orchestration | The intent the orchestrator predicts when routing to this project |

---

## Section 5: Bot Channels Reference

### Standard Azure Bot Service Channels

| Channel | Authentication Method | Notes |
|---------|----------------------|-------|
| Web Chat | Direct Line secret | Embeddable HTML/JS component |
| Microsoft Teams | Teams App manifest | Most common enterprise channel |
| Slack | OAuth app credentials | Workspace bots |
| Facebook Messenger | Page access token | Customer service on social |
| Twilio SMS | Account SID + auth token | Text messaging |
| Email | SMTP credentials | Lower-volume workflows |
| Direct Line | Channel secret key | Custom app integration |
| Direct Line Speech | Speech service key | Voice interaction |

### Channel Limitations

Each channel has its own message format and feature support. Not all channels support rich cards, buttons, file attachments, or audio. The Bot Framework normalizes common features across channels, but channel-specific features may require custom `channelData` properties.

---

## Section 6: Microsoft Copilot Studio

### Key Concepts

| Concept | Description |
|---------|-------------|
| Topic | A unit of conversation triggered by phrases; contains the dialog flow |
| Trigger phrases | Example inputs that activate a topic |
| Message node | Bot sends a fixed or dynamic message |
| Question node | Bot asks for user input and stores the response in a variable |
| Condition node | Branch the flow based on variable values or topic context |
| Action node | Call a Power Automate flow or HTTP connector |
| Entity | Built-in or custom data type for question responses |
| Variable | Stores captured values during the conversation |
| Fallback topic | Handles inputs that do not match any topic trigger |

### Copilot Studio vs. Bot Framework

| Dimension | Copilot Studio | Azure Bot Framework SDK |
|-----------|---------------|------------------------|
| Target users | Citizen developers, business analysts | Professional software developers |
| Language | No-code graphical canvas | C#, JavaScript, Python, Java |
| Hosting | Managed by Microsoft | Self-hosted or Azure App Service |
| Customization | Limited to platform capabilities | Unlimited via code |
| Power Platform integration | Native | Via API calls |
| Time to first working bot | Hours | Days to weeks |
| AI-900 exam emphasis | Know it exists; know use case | Know architecture; know components |

### Generative AI in Copilot Studio

Copilot Studio now includes a generative answers feature powered by Azure OpenAI. When no topic matches a user's input, the bot can optionally generate an answer grounded in connected data sources (SharePoint, websites, uploaded documents). This bridges the gap between structured topic-based bots and fully generative agents.

---

## Section 7: Responsible Conversational AI

### Key Principles

**Disclosure.** Users must know they are talking to a bot. This is both an ethical requirement and a legal requirement in many jurisdictions. The disclosure should be prominent — at the start of the conversation, not buried in terms of service.

**Graceful escalation.** Every bot must provide a clear path to a human agent when the bot cannot help. Users should never feel trapped in a loop.

**Scope boundaries.** Bots should be designed to decline out-of-scope requests explicitly rather than attempting to answer anything. A well-scoped bot is more trustworthy than an over-eager one.

**Data handling.** Conversation logs contain sensitive information. Retention policies, access controls, and PII scrubbing should be in place before any bot is deployed to production.

**Bias in knowledge bases.** The Q&A pairs in a knowledge base reflect the language and assumptions of whoever wrote them. If the knowledge base was written for a specific demographic, users outside that demographic may receive less helpful or culturally inappropriate responses.

---

## Section 8: AI-900 Exam Tips

### High-Frequency Exam Topics

**Topic 1 — QA vs. CLU.** This is the most tested distinction in the conversational AI domain. QA = retrieval of answers from a knowledge base. CLU = classification of user intents with entity extraction. A scenario asking which to use will almost always have one clearly correct answer based on whether the user is asking for information or issuing a command.

**Topic 2 — Bot channels.** Know that channels are preconfigured connectors in Azure Bot Service. Know that Web Chat is the embedded website option and that Teams is the enterprise internal channel. Know that Direct Line is for custom apps.

**Topic 3 — Copilot Studio use case.** Copilot Studio is the answer when the scenario involves non-developer users building bots or when the scenario mentions Power Platform, Power Automate, or low-code requirements.

**Topic 4 — Multi-turn QA.** Follow-up prompts are the feature that enables multi-turn navigation in Question Answering. Confidence threshold controls when the fallback response is used.

**Topic 5 — Orchestration Workflow.** When a bot needs both QA and CLU capabilities through a single endpoint, the answer is Orchestration Workflow.

### Common Exam Traps

- The old name "QnA Maker" may appear. It is the same service now called Question Answering under Azure AI Language.
- The old name "LUIS" may appear. It is the same service now called Conversational Language Understanding (CLU).
- Copilot Studio was previously called "Power Virtual Agents" — both names may appear.
- Azure Bot Service is the hosting platform; Azure Bot Framework is the SDK. They are different things.

---

## Section 9: Key Term Glossary

| Term | Definition |
|------|-----------|
| Azure Bot Framework | Open-source SDK for building bots in code (C#, JS, Python, Java) |
| Azure Bot Service | Managed cloud platform for hosting bots and connecting them to channels |
| Question Answering | Azure AI Language feature that matches user questions to knowledge base answers |
| Conversational Language Understanding (CLU) | Azure service for intent classification and entity extraction in conversations |
| Orchestration Workflow | Meta-model that routes user messages to CLU or QA projects |
| Channel | Platform through which users interact with a bot (Teams, web chat, SMS, etc.) |
| Direct Line | REST API channel for custom application integration with Azure Bot Service |
| Activity | Fundamental unit of communication in the Bot Framework |
| Dialog | Bot Framework component managing a conversation flow |
| Multi-turn conversation | Conversation requiring multiple exchanges to complete a goal |
| Follow-up prompt | QA feature linking an answer to related questions, enabling multi-turn navigation |
| Confidence threshold | Minimum score for QA to return an answer; below this, a fallback is used |
| Copilot Studio | Low-code/no-code bot authoring platform integrated with Microsoft 365 |
| Topic (Copilot Studio) | Unit of conversation flow triggered by matching phrases |
| Active learning (QA) | Feature that suggests new Q&A pairs from real user queries |

---

## Section 10: Study Checklist

Work through this checklist before taking the quiz.

- [ ] I can describe the three layers of a conversational AI solution (language understanding, dialog management, channel delivery)
- [ ] I know the difference between the Azure Bot Framework SDK and Azure Bot Service
- [ ] I can explain how Question Answering works end to end
- [ ] I understand follow-up prompts and what they enable
- [ ] I know what a confidence threshold does in Question Answering
- [ ] I can clearly distinguish CLU (task commands) from Question Answering (information retrieval)
- [ ] I know when to use Orchestration Workflow
- [ ] I can name at least four bot channels and describe their use cases
- [ ] I know what Direct Line is and when to use it
- [ ] I can describe Copilot Studio's target user and key capabilities
- [ ] I know the responsible AI considerations specific to chatbots (disclosure, escalation, scope)

---

## 11. Supplemental Resources

**1. Microsoft Learn — Build a bot with Azure AI Language and Azure Bot Service**
<https://learn.microsoft.com/en-us/training/paths/create-conversational-ai-solutions/>
A free Microsoft Learn learning path covering Question Answering, CLU, Orchestration Workflow, and Azure Bot Service end to end. Includes sandboxed environments that align directly with the Module 09 lab activities.

**2. Botframework.com — Bot Framework Emulator (download and documentation)**
<https://github.com/microsoft/BotFramework-Emulator>
The official GitHub repository for the Bot Framework Emulator, including download links, release notes, and documentation on using the emulator for local bot testing and activity inspection. Required tool for the Module 09 lab.

**3. Microsoft AI Blog — Responsible Bots: 10 Guidelines for Developers**
<https://www.microsoft.com/en-us/research/publication/responsible-bots/>
Microsoft Research's guidelines for building responsible conversational AI systems, covering transparency, graceful failure, human escalation, and avoiding harmful outputs. Directly relevant to the Module 09 responsible AI reflection exercise.

---

End of Reading Guide — Module 09
