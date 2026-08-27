# Lab 09 — Conversational AI and Azure Bot Service

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Alignment: Describe features of conversational AI workloads on Azure

---

## Lab Overview

In this lab you will build a Question Answering knowledge base, test it with multi-turn follow-up prompts, connect it to a bot using the Bot Framework Emulator, and explore a Copilot Studio sample bot. You will document your results with screenshots and written analysis.

### Learning Objectives

By completing this lab you will be able to:

- Create and populate an Azure AI Language Question Answering project
- Configure follow-up prompts for multi-turn conversation
- Test the knowledge base using the built-in test interface
- Use the Bot Framework Emulator to interact with a QA bot
- Explore a Copilot Studio environment and describe its components
- Explain one responsible AI consideration for a deployed chatbot

### Prerequisites

- Active Azure for Students subscription
- Completion of Module 08 lab (Azure AI Language familiarity assumed)
- Python 3.8+ installed, or use Azure Cloud Shell
- Bot Framework Emulator installed (free download at `aka.ms/bf-emulator`)

### Time Estimate

Approximately 90–120 minutes.

---

## Part A: Create a Question Answering Knowledge Base (30 minutes)

### Step A1: Provision an Azure AI Language Resource

If you still have your `cis4330-mod08-rg` resource group and Language resource from Lab 08, you may reuse it. Otherwise:

1. Sign in to the Azure portal at portal.azure.com.
2. Create a new resource group: `cis4330-mod09-rg`.
3. Create a **Language service** resource (Free F0 tier) in that resource group.
4. Retrieve your **Key 1** and **Endpoint** URL from Keys and Endpoint.

### Step A2: Create a Question Answering Project

1. Navigate to Language Studio at language.cognitive.azure.com.
2. Select **Custom question answering** from the "Answer questions" section.
3. Click **Create new project**.
4. Fill in the project form:

   - **Name**: `lab09-faq`
   - **Description**: University IT Help Desk FAQ
   - **Default answer language**: English
   - **Default answer when no match found**: "I'm sorry, I don't have an answer for that. Please contact the IT help desk at <helpdesk@example.edu>."

5. Click **Next** and then **Create project**.

### Step A3: Populate the Knowledge Base

Add at least 10 Q&A pairs covering a university IT help desk scenario. Use a mix of manual entry and URL import.

Manual entry examples:

- Q: How do I reset my password? — A: Visit myaccount.example.edu and click "Forgot Password." Follow the verification steps. If you do not receive the reset email within 5 minutes, check your spam folder.
- Q: How do I connect to campus Wi-Fi? — A: Select the "CampusNet" network. Open a browser and you will be redirected to the captive portal. Log in with your student ID and password.
- Q: What software is available for free to students? — A: Students can download Microsoft 365, Adobe Creative Cloud, and the VPN client at no charge from the software portal at software.example.edu.

For URL import: find a real university IT FAQ page (any public university's IT services page) and import its URL. Review and edit the auto-extracted pairs for quality.

### Step A4: Add Follow-Up Prompts

Configure at least two multi-turn follow-up prompt chains.

Example chain for password reset:

1. Main answer: "Visit myaccount.example.edu and click Forgot Password..."
2. Follow-up prompt 1: "What if I don't receive the reset email?" → Link to or create answer about checking spam and contacting the help desk.
3. Follow-up prompt 2: "What are the password requirements?" → Link to or create answer listing length, complexity, and history requirements.

### Step A5: Train and Test

1. Click **Save changes**.
2. Click **Test** in the top menu.
3. Test at least five different questions — some that match well, some that are close paraphrases, and one that should not match anything.
4. Record the confidence scores for each test query.

### Deliverable A

1. Screenshot of the knowledge base showing your Q&A pairs list.
2. Screenshot of the Test panel showing at least five test queries with confidence scores.
3. Written answers:

   - Which question received the lowest confidence score? Rephrase the question differently and test again. Did the score improve?
   - Did the URL import extract all questions accurately? What edits did you make?

---

## Part B: Multi-Turn Conversation Walkthrough (15 minutes)

### Step B1: Test the Follow-Up Prompt Chain

1. In the Test panel, type the trigger question for your multi-turn chain (for example, "How do I reset my password?").
2. The first answer should appear with follow-up prompt buttons.
3. Click each follow-up prompt button and verify the linked answer appears.
4. Continue the chain as deep as your prompts go.

### Step B2: Configure the Confidence Threshold

1. Click the **Settings** gear icon in the Test panel.
2. Set the confidence threshold to **0.65**.
3. Test a question that you expect to match at around 0.60–0.70 confidence.
4. Observe whether the answer or the fallback message is returned.
5. Lower the threshold to **0.40** and test the same question again.

### Deliverable B

1. Screenshot of the multi-turn conversation flow in the Test panel showing the prompt chain.
2. Written answer: What happened when you lowered the confidence threshold? What is the trade-off between a high threshold and a low threshold in a production FAQ bot?

---

## Part C: Deploy and Query via REST (20 minutes)

### Step C1: Deploy the Knowledge Base

1. In Language Studio, click **Deploy knowledge base** in the left menu.
2. Click **Deploy** to push the current version to the production slot.
3. After deployment, click **Get prediction URL**.
4. Copy the REST endpoint URL and your API key.

### Step C2: Query the Endpoint with Python

Create `lab09_qa.py`:

```python
import requests
import json

ENDPOINT = "<your-language-endpoint>"
API_KEY  = "<your-key>"
PROJECT  = "lab09-faq"
DEPLOYMENT = "production"

url = (f"{ENDPOINT}/language/:query-knowledgebases"
       f"?projectName={PROJECT}"
       f"&deploymentName={DEPLOYMENT}"
       f"&api-version=2021-10-01")

headers = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "Content-Type": "application/json"
}

questions = [
    "How do I reset my password?",
    "Can I get Microsoft Office for free?",
    "What time does the library close?"
]

for q in questions:
    body = {"question": q, "top": 1, "confidenceScoreThreshold": 0.5}
    response = requests.post(url, headers=headers, json=body)
    result = response.json()
    answer = result["answers"][0]
    print(f"\nQ: {q}")
    print(f"A: {answer['answer']}")
    print(f"Confidence: {answer['confidenceScore']:.2f}")
```

Run the script:

```bash
python lab09_qa.py
```

### Deliverable C

1. Terminal screenshot showing output for all three questions.
2. Written answer: The third question ("What time does the library close?") is likely not in your knowledge base. What did the bot return, and what does this tell you about the confidence threshold you set in the code?

---

## Part D: Bot Framework Emulator Exploration (20 minutes)

### Step D1: Install the Emulator

If not already installed, download the Bot Framework Emulator from `aka.ms/bf-emulator` and install it.

### Step D2: Run a Sample Bot Locally

Microsoft provides sample bots in the BotBuilder-Samples repository on GitHub. For this lab, use the **QnA Maker sample** (sample 11).

1. Clone or download the sample: `https://github.com/microsoft/BotBuilder-Samples`
2. Navigate to `samples/python/11.qnamaker` (or the C# or JS equivalent).
3. Copy your QA endpoint and key into the `config.py` (or appsettings.json) file.
4. Install dependencies: `pip install -r requirements.txt`
5. Run the bot: `python app.py`
6. Open the Bot Framework Emulator.
7. Click **Open Bot** and enter `http://localhost:3978/api/messages`.
8. Type a question from your knowledge base and observe the response.

Note: If local Python setup is not available, screenshot the Emulator interface from the lecture demo and answer the questions below based on the lecture video.

### Step D3: Observe the Activity Log

1. In the Emulator, send three different messages.
2. Click on a message activity in the log panel on the right.
3. Observe the full JSON activity object.

### Deliverable D

1. Screenshot of the Emulator showing a conversation with at least three messages.
2. Screenshot of the JSON activity object for one message.
3. Written answer: What fields in the activity JSON were most surprising or interesting to you? What does the `channelId` field say for Emulator interactions?

---

## Part E: Copilot Studio Exploration (15 minutes)

### Step E1: Access Copilot Studio

Navigate to copilotstudio.microsoft.com. Sign in with your Microsoft account. If your Verizon or university account has Copilot Studio access, use it; otherwise, sign up for a free trial.

### Step E2: Explore a Sample Bot

1. Click **Try a sample** or open one of the pre-built sample bots.
2. Explore the following components:

   - The **Topics** list — note the topic names and trigger phrases
   - Open one topic and trace its conversation flow through message, question, condition, and action nodes
   - Identify the **Fallback** topic and note how it handles unmatched inputs
   - Check the **Settings** panel for connected knowledge sources

### Deliverable E

1. Screenshot of the Topics list for the sample bot.
2. Screenshot of the canvas for one topic showing at least one question node and one condition node.
3. Written answer (100–150 words): How does Copilot Studio's topic-based model compare to the CLU intent-based model you built in Lab 08? What are the advantages and disadvantages of each approach for a non-developer building a customer service bot?

---

## Part F: Responsible AI Reflection (10 minutes)

Answer the following in 150–200 words.

Your FAQ bot is about to go live on your university's website. Before launch, the IT director asks you to review the deployment for responsible AI risks.

1. What disclosure should the bot provide at the start of every conversation?
2. Describe the escalation path: what should happen when a user asks a question the bot cannot answer or when the user explicitly asks to speak to a human?
3. The bot logs every conversation. What data handling steps should be in place before launch to protect user privacy?

---

## Submission Requirements

Submit the following to the course LMS by the posted deadline.

- Part A: Knowledge base screenshot, test panel screenshot, two written answers
- Part B: Multi-turn screenshot, written threshold trade-off answer
- Part C: Terminal output screenshot, written answer about the unmatched question
- Part D: Emulator conversation screenshot, activity JSON screenshot, written answer
- Part E: Topics screenshot, topic canvas screenshot, 100–150-word comparison
- Part F: Responsible AI reflection (150–200 words)

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Part A — Knowledge base | 20 | 10+ Q&A pairs; multi-turn prompts configured; test results documented |
| Part B — Multi-turn and threshold | 15 | Follow-up chain demonstrated; threshold trade-off explained accurately |
| Part C — REST query | 15 | Script runs; output shown; unmatched question analyzed |
| Part D — Emulator | 20 | Conversation screenshot; activity JSON shown; fields discussed |
| Part E — Copilot Studio | 15 | Screenshots show topic list and canvas; comparison is substantive |
| Part F — Reflection | 15 | Disclosure, escalation, and privacy all addressed specifically |
| **Total** | **100** | |

---

## Cleanup

Delete resource groups after submission to avoid charges.

1. In the Azure portal, navigate to **Resource groups**.
2. Select `cis4330-mod09-rg` (or your reused group).
3. Click **Delete resource group**, confirm, and click **Delete**.

---

## Part 9 — Challenge Exercise

### Challenge 1: Active Learning Pipeline Simulation

1. Review the list of 10 user queries you submitted to your knowledge base in Part C of this lab. Identify 3 queries that received a low confidence score (below 0.70) or were unmatched.
2. For each low-confidence query: (a) write the question exactly as the user phrased it, (b) write the answer that should have been returned, and (c) write 2 alternative phrasings of the same question that could be added as alternate question variants in the knowledge base.
3. Add all three Q&A pairs (with alternate questions) to your knowledge base, retrain, and re-run the same three queries. Record the new confidence scores.
4. Explain in 2-3 sentences how the Active Learning workflow in production would automate steps 1-2 of this process, and what role the human reviewer plays in the full loop.

### Challenge 2: Multi-Turn Conversation Design

1. Design a multi-turn conversation for a new topic in your bot that requires at least 3 turns to complete. Example scenarios: a flight booking flow (origin → destination → date), a pizza order (size → toppings → delivery or pickup), or a library book reservation (title → availability check → confirm reservation date).
2. Write out the conversation script as a dialogue between User and Bot for the happy path (user provides correct information each turn).
3. Implement the multi-turn flow in either: (a) Copilot Studio using topics with follow-up prompts, or (b) Question Answering using follow-up prompts linked between Q&A pairs. Provide a screenshot of the conversation flow canvas or Q&A chain.
4. Test the flow in the bot emulator or QA test panel and document one point where the conversation could fail (e.g., unexpected user input) and how you would handle it with a fallback prompt.

### Reflection Questions

1. After completing Challenge 1, explain why the human review step in Active Learning is essential rather than automatically accepting all suggested Q&A pairs. What types of incorrect or harmful suggestions might the system produce that human review would catch?
2. Based on Challenge 2, describe the fundamental difference between a single-turn FAQ bot (Module 09 base lab) and a multi-turn task-completion bot in terms of what the bot must "remember" between conversation turns and how that changes the system design requirements.

---

End of Lab 09
