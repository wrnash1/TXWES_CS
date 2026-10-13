# Lab: Module 14 — AI Security and Privacy

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Lab Overview

**Title:** AI Security Threat Modeling and Privacy-Preserving Analysis

**Estimated Time:** 90–120 minutes

**Skill Level:** Intermediate (combination of analysis and hands-on exploration)

**Prerequisites:**

- Completed Module 14 video lecture and reading guide
- Python environment (Anaconda or Google Colab)
- Azure free account (for Part 4)

**Learning Objectives:**

1. Construct a threat model for a realistic AI deployment scenario
2. Observe adversarial attack behavior in a controlled environment
3. Analyze differential privacy noise impact on query accuracy
4. Apply a GDPR/CCPA compliance checklist to an AI use case
5. Review Microsoft Responsible AI toolkits in Azure

---

## Part 1 — AI Threat Modeling Exercise (25 minutes)

### Task 1.1 — Select a Deployment Scenario

Choose ONE of the following AI deployment scenarios for your threat model. You will use this scenario throughout Parts 1 and 5.

**Scenario A — Hospital Patient Triage AI**
An NLP model reads incoming patient complaint text from an online triage portal and assigns a priority score (low / medium / high) that determines wait time. The model is accessed via a web portal used by patients directly.

**Scenario B — Bank Loan Approval AI**
A gradient boosting model scores mortgage applications and returns Approve/Review/Deny decisions within 30 seconds. Loan officers see the decision but cannot override it without a supervisor.

**Scenario C — Retail Shoplifting Detection AI**
A computer vision model processes real-time camera feeds in a retail store. When it detects behavior matching known shoplifting patterns, it alerts a loss prevention officer via mobile notification.

**Record:** Your selected scenario and a one-sentence description.

### Task 1.2 — STRIDE Threat Modeling

STRIDE is a threat modeling framework used in software security, adapted here for AI systems. For each STRIDE category, identify at least one specific AI-relevant threat for your scenario.

| STRIDE Category | Definition | Your AI-Specific Threat |
|---|---|---|
| Spoofing | Attacker impersonates a legitimate input or user | |
| Tampering | Attacker modifies data, model, or pipeline | |
| Repudiation | Actions cannot be traced or audited | |
| Information Disclosure | Sensitive data is exposed through model outputs | |
| Denial of Service | Model or system is made unavailable | |
| Elevation of Privilege | Attacker gains unauthorized capabilities | |

### Task 1.3 — Attack Scenario Narratives

For TWO of the six STRIDE threats you identified, write a 100–150 word attack scenario narrative. Each narrative should include:

- Who the attacker is (external adversary, disgruntled employee, competitor, etc.)
- What specific action they take
- What AI-specific vulnerability they exploit
- What the real-world impact is on individuals or the organization

### Task 1.4 — Countermeasure Mapping

For each of the two attack narratives from Task 1.3, propose two specific countermeasures. For each countermeasure, specify:

1. What layer of the defense-in-depth stack it operates at (infrastructure / model / data / API / monitoring)
2. How it mitigates the specific attack
3. Any tradeoff or limitation of this countermeasure

---

## Part 2 — Adversarial Examples Demonstration (25 minutes)

### Task 2.1 — Setup

Open Google Colab (`https://colab.research.google.com`) or your local Python environment.

Install required packages by running:

```python
!pip install torch torchvision matplotlib numpy
```

### Task 2.2 — Load a Pretrained Model and Run Normal Inference

Paste and run the following code block:

```python
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import urllib.request
import matplotlib.pyplot as plt
import json
import numpy as np

# Load pretrained ResNet18
model = models.resnet18(pretrained=True)
model.eval()

# Load ImageNet class labels
url = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
with urllib.request.urlopen(url) as f:
    labels = json.load(f)

# Load sample image
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/320px-Cat_November_2010-1a.jpg"
urllib.request.urlretrieve(img_url, "cat.jpg")

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

img = Image.open("cat.jpg")
img_tensor = transform(img).unsqueeze(0)
img_tensor.requires_grad = True

# Normal inference
with torch.no_grad():
    output = model(img_tensor)
    probs = torch.softmax(output, dim=1)
    top5 = torch.topk(probs, 5)

print("Top 5 predictions (no attack):")
for i in range(5):
    idx = top5.indices[0][i].item()
    prob = top5.values[0][i].item()
    print(f"  {labels[idx]}: {prob:.4f}")
```

**Record:** The top predicted class and its confidence score.

### Task 2.3 — Apply FGSM Adversarial Attack

Paste and run the following code:

```python
# FGSM Attack
img_tensor_adv = transform(img).unsqueeze(0)
img_tensor_adv.requires_grad = True

# Forward pass
output_adv = model(img_tensor_adv)
# Target: class 907 (French bulldog) as attack target
target = torch.tensor([907])
loss = torch.nn.CrossEntropyLoss()(output_adv, target)
model.zero_grad()
loss.backward()

# FGSM perturbation
epsilon = 0.03  # small perturbation
perturbation = epsilon * img_tensor_adv.grad.sign()
img_adversarial = img_tensor_adv + perturbation
img_adversarial = torch.clamp(img_adversarial, -3, 3)  # keep in valid range

# Inference on adversarial image
with torch.no_grad():
    output_attacked = model(img_adversarial)
    probs_attacked = torch.softmax(output_attacked, dim=1)
    top5_attacked = torch.topk(probs_attacked, 5)

print(f"\nTop 5 predictions (FGSM attack, epsilon={epsilon}):")
for i in range(5):
    idx = top5_attacked.indices[0][i].item()
    prob = top5_attacked.values[0][i].item()
    print(f"  {labels[idx]}: {prob:.4f}")

# Visualize perturbation magnitude
perturbation_np = perturbation.squeeze().detach().numpy()
print(f"\nPerturbation L-inf norm: {np.abs(perturbation_np).max():.6f}")
print(f"Perturbation L-2 norm: {np.linalg.norm(perturbation_np):.4f}")
```

**Record:** The new top prediction and its confidence score.

**Lab Question 1:** Did the attack change the top prediction? How confident is the model in its new (incorrect) prediction? What does the perturbation's L-inf norm tell you about how large the modification to each pixel was?

### Task 2.4 — Vary Epsilon and Record Results

Rerun the attack with epsilon values of 0.01, 0.05, 0.10, and 0.20. Record the top predicted class and confidence for each epsilon value.

| Epsilon | Top Predicted Class | Confidence |
|---|---|---|
| 0.01 | | |
| 0.03 | | |
| 0.05 | | |
| 0.10 | | |
| 0.20 | | |

**Lab Question 2:** Describe the relationship between epsilon magnitude and attack success. At what epsilon value does the attack consistently change the prediction? What is the tradeoff an attacker faces when choosing epsilon?

---

## Part 3 — Differential Privacy Simulation (20 minutes)

### Task 3.1 — Simulate a Private Query

Run the following code to observe the effect of differential privacy noise on statistical queries:

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Simulate a dataset of patient ages (sensitive)
n = 1000
true_ages = np.random.normal(loc=52, scale=15, n).clip(18, 95)
true_mean = np.mean(true_ages)
print(f"True mean age: {true_mean:.2f}")

# DP query: add Laplace noise
# Sensitivity of mean query = range / n = (95-18)/1000 = 0.077
sensitivity = (95 - 18) / n

def dp_mean_query(data, epsilon):
    true_val = np.mean(data)
    noise = np.random.laplace(0, sensitivity / epsilon)
    return true_val + noise

# Run 100 queries at each epsilon level
epsilons = [0.01, 0.1, 0.5, 1.0, 5.0, 10.0]
results = {}

print("\nDP Mean Query Results (100 runs each):")
print(f"{'Epsilon':>10} | {'Mean Result':>12} | {'Std Dev':>10} | {'Avg Error':>10}")
print("-" * 50)

for eps in epsilons:
    queries = [dp_mean_query(true_ages, eps) for _ in range(100)]
    mean_result = np.mean(queries)
    std_result = np.std(queries)
    avg_error = np.mean(np.abs(np.array(queries) - true_mean))
    results[eps] = queries
    print(f"{eps:>10.2f} | {mean_result:>12.2f} | {std_result:>10.4f} | {avg_error:>10.4f}")
```

**Record:** The table output from this code.

**Lab Question 3:** As epsilon increases, what happens to the average error? What happens to the standard deviation of results? At which epsilon value would you say the results are "practically useful"? What does this tell you about the tradeoff between privacy and utility?

### Task 3.2 — Reflection on DP in Healthcare

Answer the following in 100–150 words: A hospital wants to publish aggregate statistics about patient demographics, diagnoses, and outcomes to support public health research. They consider using differential privacy. What epsilon value would be appropriate, and why? What kinds of queries would still be accurate enough to be useful to researchers under strong DP?

---

## Part 4 — Compliance Checklist Application (15 minutes)

### Task 4.1 — Apply the Compliance Checklist

Return to the deployment scenario you selected in Task 1.1. Apply the Secure AI Deployment Checklist from the Module 14 Reading Guide.

For each checklist item, mark:

- **Pass:** The scenario as described would satisfy this requirement
- **Fail:** The scenario as described would NOT satisfy this requirement
- **Unknown:** The scenario does not provide enough information to assess

For every **Fail** item, write a 1–2 sentence remediation recommendation.

### Task 4.2 — GDPR/CCPA Risk Identification

For your selected scenario, identify:

1. Does GDPR apply? Why or why not?
2. Does CCPA apply? Why or why not?
3. Does Article 22 automated decision-making apply? If so, what must the organization provide?
4. What specific personal data categories are processed? Are any in the "sensitive" category?
5. What is the most significant compliance gap you identified?

---

## Part 5 — Lab Reflection (10 minutes)

Answer each reflection question in 3–5 sentences:

**Reflection 1:** Based on your threat model from Part 1 and your adversarial attack observation from Part 2, how would you rank the three biggest security risks for your selected scenario? What makes one risk higher priority than another?

**Reflection 2:** The epsilon-accuracy tradeoff in differential privacy is fundamentally a policy decision, not a technical one. Who should make that decision — the data scientist, the legal team, the executive, or a regulatory body? Justify your answer.

**Reflection 3:** A colleague argues that security and privacy controls for AI are just overhead that slows down deployment, and that if an attack has never happened to your organization, the risk is theoretical. How would you respond?

---

## Lab Submission Requirements

Submit a single PDF document containing:

1. **Part 1:** Scenario selection, STRIDE table, two attack narratives, countermeasure mapping
2. **Part 2:** Code output screenshots, epsilon results table, Lab Questions 1–2
3. **Part 3:** DP simulation output table, Lab Question 3, healthcare DP reflection
4. **Part 4:** Compliance checklist with assessments and remediations, GDPR/CCPA risk analysis
5. **Part 5:** Three reflection responses

**Grading Rubric:**

| Component | Points |
|---|---|
| STRIDE threat model complete and scenario-specific | 20 |
| Attack narratives realistic and technically sound | 15 |
| Adversarial attack code runs; results recorded and analyzed | 20 |
| DP simulation results recorded; questions answered correctly | 20 |
| Compliance checklist complete with remediations | 15 |
| Reflection responses show depth and synthesis | 10 |
| **Total** | **100** |

---

*Lab prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
