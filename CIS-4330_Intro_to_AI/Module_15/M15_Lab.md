# Lab: Module 15 — Emerging AI Technologies

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Lab Overview

**Title:** Multimodal AI, Agents, and Emerging Technologies Exploration

**Estimated Time:** 90–120 minutes

**Skill Level:** Intermediate

**Prerequisites:**

- Completed Module 15 video lecture and reading guide
- Azure free account with Azure OpenAI Service access (or use Azure AI Foundry demo portal)
- Python environment (Google Colab acceptable)

**Learning Objectives:**

1. Interact with a multimodal AI model using image and text inputs
2. Build a simple AI agent workflow with tool use
3. Observe model quantization effects on size and performance
4. Evaluate a real-world federated learning deployment case study
5. Map your personal certification pathway

---

## Part 1 — Multimodal AI Exploration (25 minutes)

### Task 1.1 — Access Azure OpenAI Vision

**Option A — Azure OpenAI Playground (Preferred):**

1. Navigate to `https://oai.azure.com/` and sign in.
2. If you have a deployment, select it. If not, use the demo at `https://azure.microsoft.com/en-us/products/ai-services/openai-service` and click "Try Azure OpenAI Service."
3. In the Chat Playground, select a GPT-4V or GPT-4o deployment.

**Option B — Azure AI Foundry Demo:**

Navigate to `https://ai.azure.com/` → Explore deployments → Use the chat playground with vision support.

**Option C — OpenAI API (if Azure access is unavailable):**

Use `https://platform.openai.com/playground` with a GPT-4V model.

### Task 1.2 — Image Analysis Tasks

Complete the following five tasks with the multimodal model. For each task, record the prompt you used and a summary of the model's response.

**Task A — Scene Description**

Upload a photograph from your phone or computer (any photograph without personal identifying information). Ask the model:

"Describe this image in detail. What is the main subject? What details are in the background? What is the overall mood or tone?"

**Task B — Text Extraction from Image**

Find or create a simple image containing text (a screenshot of a menu, a sign, a handwritten note). Ask the model:

"Extract all visible text from this image. Then tell me if there are any spelling errors or formatting inconsistencies."

**Task C — Visual Reasoning**

Upload a chart or graph (a bar chart, line graph, or pie chart — from a news article, textbook, or website). Ask the model:

"Analyze this chart. What does it show? What is the most significant trend or data point? What conclusion would a business analyst draw from this data?"

**Task D — Comparative Analysis**

Upload two photographs of the same type of object (two cars, two buildings, two food dishes — from the web is fine). Ask:

"Compare and contrast these two images. Identify three similarities and three differences. Which would you recommend and why?"

**Task E — Limitation Probing**

Find a complex or ambiguous image (an abstract painting, a dense diagram, a crowded scene). Ask the model to describe it in detail. Deliberately ask a question about something you know is NOT in the image.

Record: Did the model correctly say the object was not present, or did it hallucinate? What does this reveal about the model's reliability?

**Lab Question 1:** Based on your five tests, in which type of task did the multimodal model perform most reliably? Where did it show the most uncertainty or make errors? What real-world use case do your findings suggest would be high-risk to automate with this technology?

---

## Part 2 — AI Agent Workflow (25 minutes)

### Task 2.1 — Understand Agent Tool Calling

Read the Azure AI Agent Service documentation at:

`https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/`

Identify and describe THREE tools that Azure AI Agent Service supports natively. For each tool, write:

1. Tool name
2. What it does
3. One business scenario where this tool would be used by an agent

### Task 2.2 — Design an Agent Workflow

You are designing an AI agent for a small business owner. The business owner wants an agent that can:

1. Monitor their email inbox for any messages from customers containing the word "refund"
2. For each refund request, look up the customer's order in a database
3. If the order is within 30 days, automatically approve the refund and send a confirmation email
4. If the order is older than 30 days, flag for human review and send an acknowledgment email

**Design the agent workflow:**

Draw or describe (in structured text) the complete agent workflow as a flowchart-style narrative. Include:

- Starting trigger
- Each decision point
- Each tool call required
- Human escalation points
- Final outputs/actions taken

**Lab Question 2:** This agent has the ability to send emails and approve refunds autonomously. Apply the principle of least privilege and the human-in-the-loop principle from Module 14 to evaluate this design. What guard rails would you require before deploying this agent in a production business setting?

### Task 2.3 — Agent Risk Assessment

For the refund agent you designed, complete the following risk table:

| Risk | Likelihood (Low/Med/High) | Impact (Low/Med/High) | Mitigation |
|---|---|---|---|
| Agent approves a refund for a fraudulent order | | | |
| Agent sends wrong email to wrong customer | | | |
| Prompt injection via malicious email content | | | |
| Agent actions cannot be audited | | | |
| Customer receives duplicate emails | | | |

---

## Part 3 — Model Quantization Exploration (20 minutes)

### Task 3.1 — Observe Quantization Effects

Run the following code in Google Colab or your Python environment:

```python
!pip install transformers torch

from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import time
import os

model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Load full-precision model
print("Loading full-precision model...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model_fp32 = AutoModelForSequenceClassification.from_pretrained(model_name)

# Check size
import torch

def count_parameters(model):
    return sum(p.numel() for p in model.parameters())

def model_size_mb(model):
    param_size = 0
    for param in model.parameters():
        param_size += param.nelement() * param.element_size()
    return param_size / (1024 ** 2)

print(f"FP32 Model parameters: {count_parameters(model_fp32):,}")
print(f"FP32 Model size: {model_size_mb(model_fp32):.2f} MB")

# Apply dynamic quantization (INT8)
model_int8 = torch.quantization.quantize_dynamic(
    model_fp32,
    {torch.nn.Linear},
    dtype=torch.qint8
)

print(f"\nINT8 Model parameters: {count_parameters(model_int8):,}")
print(f"INT8 Model size: {model_size_mb(model_int8):.2f} MB")

# Test sentences
test_sentences = [
    "This product is absolutely fantastic and I love it!",
    "The service was terrible and I want a refund.",
    "The weather today is neither good nor bad.",
    "I expected more from this experience but it was okay.",
]

# Inference speed comparison
from transformers import pipeline

pipe_fp32 = pipeline("text-classification", model=model_fp32, tokenizer=tokenizer)
pipe_int8 = pipeline("text-classification", model=model_int8, tokenizer=tokenizer)

print("\n--- Inference Results and Speed ---")
for sentence in test_sentences:
    t0 = time.time()
    result_fp32 = pipe_fp32(sentence)[0]
    t1 = time.time()
    result_int8 = pipe_int8(sentence)[0]
    t2 = time.time()

    fp32_match = result_fp32['label']
    int8_match = result_int8['label']
    agreement = "AGREE" if fp32_match == int8_match else "DISAGREE"

    print(f"\nText: {sentence[:50]}...")
    print(f"  FP32: {fp32_match} ({result_fp32['score']:.4f}) | {(t1-t0)*1000:.1f}ms")
    print(f"  INT8: {int8_match} ({result_int8['score']:.4f}) | {(t2-t1)*1000:.1f}ms")
    print(f"  Agreement: {agreement}")
```

**Record:** Model sizes (FP32 vs INT8), inference times, and whether predictions agreed.

**Lab Question 3:** What was the model size reduction ratio from FP32 to INT8? Did quantization change any predictions? What does this experiment tell you about using quantization for edge deployment?

---

## Part 4 — Federated Learning Case Study (15 minutes)

### Task 4.1 — Analyze a Real Deployment

Read the following case summary and answer the questions below.

**Case: NHS Chest X-ray AI (UK)**

The UK National Health Service explored using AI to detect pneumonia and other conditions in chest X-rays. Hospitals had different policies about data sharing. A federated learning approach was proposed: each hospital would train a local model on their patients' X-rays and contribute model updates to a central coordinator. No X-ray images would be shared across hospitals.

Results from a simulated FL experiment showed that the federated model achieved 94% accuracy compared to 96% for a fully centralized model trained on all data combined.

**Questions:**

1. The federated model performed 2 percentage points worse than the centralized model. Is this tradeoff acceptable? What factors would influence this decision?

2. One hospital in the federation has 10x more X-ray data than any other hospital. How might this affect the FedAvg aggregation? Is it fair? How would you modify the aggregation to address this?

3. A privacy researcher suggests adding differential privacy to the NHS case. Would this make the model more or less accurate? How would you decide the appropriate epsilon value for this context?

4. Beyond privacy, what other practical benefit of federated learning applies to this NHS scenario? (Think about data governance, sovereignty, and regulatory compliance.)

---

## Part 5 — Personal Certification Pathway (10 minutes)

### Task 5.1 — Build Your Certification Roadmap

Using the certification pathway from the lecture and reading guide, create a personal certification plan.

Complete the following table:

| Certification | Target Date | Why This Cert | Resources You Will Use |
|---|---|---|---|
| AI-900 (required for this course) | End of this semester | Course requirement; foundational credential | Microsoft Learn, Module 16 practice questions |
| [Your Tier 2 choice] | | | |
| [Your Tier 3 or supplemental choice] | | | |

Then write a 150–200 word reflection:

- What career path are you targeting (technical, non-technical, or hybrid AI role)?
- Why did you choose the Tier 2 certification you selected?
- What skill gaps do you need to fill between now and that certification?
- What resources (courses, projects, jobs) will help you fill those gaps?

---

## Lab Submission Requirements

Submit a single PDF document containing:

1. **Part 1:** Five task records (prompt + response summary), Lab Question 1
2. **Part 2:** Three tool descriptions, agent workflow design, Lab Question 2, risk assessment table
3. **Part 3:** Code output screenshot, Lab Question 3
4. **Part 4:** Four federated learning case questions answered
5. **Part 5:** Certification roadmap table and 150–200 word reflection

**Grading Rubric:**

| Component | Points |
|---|---|
| Multimodal tasks completed; Lab Q1 insightful | 25 |
| Agent workflow realistic; risk table complete; Lab Q2 applies security principles | 25 |
| Quantization code runs; Lab Q3 analyzes results correctly | 20 |
| Federated learning case questions show understanding | 20 |
| Certification plan personalized and realistic | 10 |
| **Total** | **100** |

---

*Lab prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
