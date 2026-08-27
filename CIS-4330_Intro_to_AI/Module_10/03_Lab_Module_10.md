# Lab 10 — Generative AI and Azure OpenAI Service

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Alignment: Describe features of generative AI workloads on Azure

---

## Lab Overview

In this lab you will access the Azure AI Studio Playground, engineer prompts for summarization and code generation, apply few-shot and chain-of-thought techniques, test the content filtering system, and evaluate how grounding affects output quality. You will document your experiments with screenshots and written analysis.

### Learning Objectives

By completing this lab you will be able to:

- Navigate Azure AI Studio and the Playground interface
- Write and iterate prompts to improve output quality
- Apply zero-shot, few-shot, and chain-of-thought prompting
- Observe the effect of temperature and max tokens on output
- Test content filters by submitting borderline inputs
- Demonstrate the hallucination problem and the effect of grounding
- Articulate one responsible AI concern raised by your lab work

### Prerequisites

- Azure OpenAI Service access (instructor-provided or approved personal subscription)
- Web browser access to oai.azure.com (Azure AI Studio / Azure OpenAI Studio)
- No local Python setup required for core parts; optional for bonus API section

### Time Estimate

Approximately 90–120 minutes.

---

## Part A: Azure AI Studio Orientation (15 minutes)

### Step A1: Access the Playground

1. Navigate to oai.azure.com and sign in with your Azure credentials.
2. Select your Azure OpenAI resource from the dropdown if prompted.
3. In the left navigation, click **Chat** under Playground.
4. Confirm that a GPT-3.5 Turbo or GPT-4 deployment is available in the deployment selector.

### Step A2: Explore the Interface

Identify and locate each of these interface elements:

- The **System message** field (where you write the system prompt)
- The **Chat session** area (the conversation thread)
- The **Temperature** parameter slider (under Configuration or Parameters)
- The **Max response** (max tokens) parameter
- The **Clear chat** button

### Deliverable A

Screenshot of the Azure AI Studio Chat Playground with a GPT deployment loaded. Annotate or describe the location of each of the five interface elements listed above.

---

## Part B: Prompt Engineering Experiments (35 minutes)

### Experiment B1: Zero-Shot Prompting

Clear the system message field. Set temperature to 0.7.

In the chat input, type:

```text
Classify the following customer review as Positive, Negative, or Neutral.
Return only the label, nothing else.

Review: "The laptop is incredibly fast and the battery lasts all day,
but the keyboard feels cheap and the trackpad is unresponsive."
```

Note the output. Then ask the same question a second time without clearing the chat. Does the model give a consistent answer?

Record what label the model returned. Was the classification accurate for a mixed review?

### Experiment B2: Few-Shot Prompting

Clear the chat. In the system message, write:

```text
You classify customer reviews as Positive, Negative, or Neutral.
Return only the label. No explanation.
```

In the chat, send this message:

```text
Review: "The product arrived early and exceeded expectations." → Positive
Review: "Completely broken out of the box. Terrible quality." → Negative
Review: "It works. Nothing special." → Neutral
Review: "The laptop is incredibly fast and the battery lasts all day,
but the keyboard feels cheap and the trackpad is unresponsive." →
```

Note the output. Did the few-shot examples change the model's behavior compared to B1?

### Experiment B3: Chain-of-Thought

Clear the chat. Set temperature to 0.

Prompt:

```text
A store sells apples for $0.75 each and bananas for $0.40 each.
Sarah buys 4 apples and some bananas. She pays $4.70 total.
How many bananas did she buy?
Think step by step before giving the final answer.
```

Observe how the model reasons through the problem. Then repeat the same prompt but remove "Think step by step before giving the final answer." Compare the two responses.

### Experiment B4: System Prompt Scoping

Clear the chat. Write this system message:

```text
You are a helpful assistant for a university library.
You answer questions about library hours, book availability, and borrowing policies only.
If asked about anything outside these topics, politely say:
"I can only help with library-related questions. Please contact the main university help desk
for other inquiries."
```

Now test the following messages in sequence:

1. "What are the library hours on weekends?"
2. "Can I borrow DVDs?"
3. "Can you help me write my essay on climate change?"
4. "What is the capital of France?"

Record what the model said for messages 3 and 4.

### Deliverable B

For each of the four experiments, provide:

- A screenshot of the chat showing the prompt and response
- 2–3 sentences analyzing what you observed: did the technique work as expected? What surprised you?

---

## Part C: Temperature and Creativity (15 minutes)

### Step C1: Low Temperature Output

Clear the chat. Set temperature to 0.0. Write this system message: "You are a creative writing assistant."

Send this prompt five times (use the regenerate button if available, or resend):

```text
Write one sentence describing a sunset over the ocean.
```

Record all five responses. Are they identical or similar?

### Step C2: High Temperature Output

Change temperature to 1.2 (or the maximum available). Send the same prompt five times.

Record all five responses. How do they differ from the low-temperature responses?

### Deliverable C

1. List the five low-temperature responses and the five high-temperature responses.
2. Written answer (3–5 sentences): What does temperature control, and when would you want low temperature vs. high temperature in a real application?

---

## Part D: Hallucination and Grounding (20 minutes)

### Step D1: Induce a Hallucination

Clear the chat. Set temperature to 0.3. Clear the system message or use a generic "You are a helpful assistant."

Send this prompt:

```text
What were the main findings of the 2024 Contoso University Annual AI Research Report?
```

This report does not exist. Record what the model says.

### Step D2: Demonstrate Grounding

Now send this prompt (providing the "document" inline):

```text
Use only the following document to answer the question. If the answer is not in the document,
say "This information is not in the provided document."

---
DOCUMENT:
Texas Wesleyan University AI Research Summary — Spring 2026
The Computer Science department completed three AI research projects this semester:
(1) A computer vision system for campus parking lot occupancy monitoring using Custom Vision.
(2) A sentiment analysis pipeline for student feedback survey processing using Azure AI Language.
(3) A retrieval-augmented generation chatbot for the library reference desk using Azure OpenAI Service.
---

Question: What AI project did the library reference desk implement?
```

Record the response.

Now ask: "What projects did the chemistry department complete?" — the answer is not in the document. Record what the model says.

### Deliverable D

1. Screenshot of the hallucination response from Step D1.
2. Screenshots of both grounded responses from Step D2.
3. Written answer (4–6 sentences): Explain the difference between the hallucinated and grounded responses. Why is grounding important for enterprise AI applications? What does the Step D2 example demonstrate about RAG architecture?

---

## Part E: Content Filtering (15 minutes)

### Step E1: Observe Normal Filtering

Clear the chat with a neutral system message.

Send a message asking about a benign but somewhat sensitive topic — for example, safety procedures for handling household chemicals, medication dosages for common conditions, or historical events involving violence.

Note whether the model responds normally, adds safety caveats, or declines.

### Step E2: Explore Filter Boundaries

Attempt prompts that approach but do not cross the content filter boundaries. The goal is to understand where the filters activate, not to generate harmful content. Acceptable test prompts include:

- A fictional story scene involving a character in a dangerous situation
- A question about the effects of alcohol on the human body (medical/educational framing)
- A request to write a villain's threatening monologue for a stage play

Note which prompts receive unfiltered responses, which receive responses with safety language, and which are blocked.

### Deliverable E

1. Screenshots of at least three prompt-response pairs from this experiment.
2. Written answer (4–6 sentences): Describe your observations about where the content filters activated. Were any responses more restrictive than you expected? Less restrictive? What does this tell you about the trade-offs in content filter calibration?

---

## Part F: Code Generation (10 minutes)

### Step F1: Generate and Evaluate Code

Clear the chat. Use this system message:

```text
You are an expert Python developer. Write clean, well-documented code.
```

Send this prompt:

```text
Write a Python function called `find_duplicates` that takes a list as input
and returns a new list containing only the elements that appear more than once.
Preserve the order of first occurrence. Include a docstring, type hints,
and three example test cases in the docstring.
```

Review the generated code carefully.

### Deliverable F

1. Screenshot of the generated function.
2. Written answer: Does the code appear correct? Copy it into a Python environment and test it if possible. Did it pass the example test cases? Were there any issues you would flag before using this code in production?

---

## Part G: Responsible AI Reflection (10 minutes)

Answer the following in 175–225 words.

You have spent this lab interacting with a generative AI system. Based on your experience, address all three points below.

1. Describe one specific output from your lab today that illustrated the hallucination problem. Why is this particularly dangerous in a business or healthcare context?
2. The content filters you tested in Part E represent a trade-off: filters that are too aggressive block legitimate use cases; filters that are too permissive allow harmful content. How should organizations decide where to set this threshold?
3. Some companies are deploying generative AI to generate public-facing content — press releases, product descriptions, social media posts — without human review. What responsible AI principle does this violate, and what process would you recommend instead?

---

## Submission Requirements

Submit the following to the course LMS by the posted deadline.

- Part A: Playground orientation screenshot with annotations
- Part B: Four experiment screenshots with 2–3-sentence analysis each
- Part C: Ten sentences from temperature experiments; written analysis
- Part D: Three screenshots; 4–6-sentence written answer
- Part E: Three screenshots; 4–6-sentence written answer
- Part F: Code screenshot; written evaluation
- Part G: Responsible AI reflection (175–225 words)

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Part A — Orientation | 5 | Screenshot correctly shows playground components |
| Part B — Prompt engineering | 30 | All four experiments documented; analysis is specific and accurate |
| Part C — Temperature | 10 | Responses listed; trade-off explanation is accurate |
| Part D — Hallucination and grounding | 20 | Both steps demonstrated; explanation addresses RAG conceptually |
| Part E — Content filtering | 15 | Three prompt-response pairs shown; observation is thoughtful |
| Part F — Code generation | 10 | Code shown; quality evaluation is specific |
| Part G — Reflection | 10 | All three points addressed substantively |
| **Total** | **100** | |

---

## Note on Azure OpenAI Access

If your Azure account does not yet have Azure OpenAI access approved, contact Professor Nash before the lab due date. Alternative access via the Azure AI Studio free tier or instructor-provided credentials may be available. Do not wait until the last day to discover an access issue.

---

## Part 9 — Challenge Exercise

### Challenge 1: Systematic Prompt Engineering Comparison

1. Choose a single task: summarize a 3-paragraph news article of your choice into 3 bullet points. Write four versions of the prompt for the same article: (a) zero-shot with only task instructions, (b) few-shot with one example summary, (c) chain-of-thought asking the model to identify key facts before summarizing, and (d) a detailed system prompt defining the role as "a professional news editor."
2. Submit all four prompts to your Azure OpenAI deployment at the same temperature (0.7). Record the output for each.
3. Build a comparison table with columns: Technique, Output Quality (1-5 rating), Adherence to 3-bullet format (Yes/No), Notable Differences.
4. Write a 3-4 sentence recommendation: for a production news summarization pipeline that processes 10,000 articles per day, which prompting technique would you standardize on and why? Consider cost (tokens), consistency, and quality.

### Challenge 2: RAG vs. Base Model Hallucination Test

1. Choose a narrow factual domain that you know well — for example, the course syllabus, your university's financial aid policies, or a technical specification document you have access to.
2. Identify 5 specific factual questions whose answers appear in your chosen document. Ask all 5 questions to the base GPT model (no document provided in the prompt). Record the answers and evaluate their accuracy.
3. Now paste the relevant sections of your document directly into the user prompt before each question (simulating manual RAG). Ask the same 5 questions and record the answers.
4. Compare accuracy. Calculate the percentage of questions answered correctly in each condition. Write a 2-3 sentence explanation of why providing document context reduces hallucination from the model's perspective.

### Reflection Questions

1. Based on Challenge 1, explain why few-shot prompting generally produces more consistent format compliance than zero-shot prompting, even when the zero-shot instructions are very explicit. What does this reveal about how LLMs learn from in-context examples vs. instructions?
2. Based on Challenge 2, if an organization wanted to deploy a production RAG system for internal policy Q&A, what are the three most important quality and safety checks they should run before going live?

---

End of Lab 10
