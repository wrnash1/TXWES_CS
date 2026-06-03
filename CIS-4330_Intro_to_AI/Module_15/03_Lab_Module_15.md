# Lab Activity: Module 15 — Emerging AI Technologies

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Lab Overview

**Lab Title:** Multimodal AI, Edge Deployment, and Federated Learning Simulation

**Duration:** 90–120 minutes

**Format:** Individual (Azure free-tier account required for Part 3; Parts 1–2 run locally)

**Objectives:**

- Query a multimodal AI model through the Azure OpenAI Vision API and analyze its cross-modal reasoning
- Simulate model compression through quantization and measure the accuracy-size tradeoff
- Simulate a two-client federated learning round and observe convergence behavior
- Reflect on the practical deployment implications of each technology

**Prerequisites:** Module 14 lab environment; Python 3.9+; Azure free-tier account with Azure OpenAI resource

---

## Part 1: Multimodal AI with Azure OpenAI Vision (30 minutes)

### Step 1.1 — Set Up Azure OpenAI Vision Access

Log into the Azure Portal at portal.azure.com. Navigate to your Azure OpenAI resource (or create a free-tier resource in East US). In Azure AI Studio, confirm that the **gpt-4o** or **gpt-4-vision-preview** model is deployed to your resource. Copy your endpoint URL and API key.

Create a file named `lab15_config.py` with the following content, replacing the placeholder values with your actual credentials.

```python
AZURE_OPENAI_ENDPOINT = "https://YOUR-RESOURCE-NAME.openai.azure.com/"
AZURE_OPENAI_KEY      = "YOUR_API_KEY_HERE"
DEPLOYMENT_NAME       = "gpt-4o"   # or gpt-4-vision-preview
API_VERSION           = "2024-02-01"
```

### Step 1.2 — Install Required Packages

```bash
pip install openai pillow requests matplotlib scikit-learn torch torchvision
```

### Step 1.3 — Build the Multimodal Query Script

Create `lab15_multimodal.py` with the following code.

```python
import base64
import urllib.request
from openai import AzureOpenAI
from lab15_config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, DEPLOYMENT_NAME, API_VERSION

client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    api_version=API_VERSION
)

def encode_image_from_url(url: str) -> str:
    """Download an image and return it as a base64-encoded string."""
    with urllib.request.urlopen(url) as response:
        return base64.b64encode(response.read()).decode("utf-8")

def ask_about_image(image_url: str, question: str) -> str:
    """Send an image + text question to the multimodal model."""
    b64 = encode_image_from_url(image_url)
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[{
            "role": "user",
            "content": [
                {"type": "text",  "text": question},
                {"type": "image_url",
                 "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}
            ]
        }],
        max_tokens=400
    )
    return response.choices[0].message.content
```

### Step 1.4 — Run Three Multimodal Queries

Add the following test harness to `lab15_multimodal.py` and run it.

```python
if __name__ == "__main__":
    # Query 1: Object recognition and scene description
    img1 = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/320px-Cat03.jpg"
    q1   = "Describe this image in detail. What objects are present, and what is the mood or atmosphere?"
    print("=== Query 1: Scene Description ===")
    print(ask_about_image(img1, q1))

    # Query 2: Text extraction from an image (OCR-style)
    img2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/A-small-cup-of-coffee.JPG/320px-A-small-cup-of-coffee.JPG"
    q2   = "If there is any text visible in this image, transcribe it exactly. Then describe what you see."
    print("\n=== Query 2: Text Extraction ===")
    print(ask_about_image(img2, q2))

    # Query 3: Reasoning about a chart or diagram
    img3 = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Simple_pie_chart.png/320px-Simple_pie_chart.png"
    q3   = "This image contains a chart. Describe the type of chart, estimate the values shown, and explain what insight a viewer would take away."
    print("\n=== Query 3: Chart Reasoning ===")
    print(ask_about_image(img3, q3))
```

### Step 1.5 — Reflection Questions

Record the model's responses in your lab report and answer the following (2–3 sentences each):

1. For Query 3, how accurate was the model's chart interpretation? What might cause errors in visual data extraction?
2. How does the multimodal API differ from calling the Azure AI Vision OCR endpoint separately and then asking a language model about the extracted text? What are the tradeoffs?
3. Describe one real-world application in your intended career field where this multimodal capability would provide meaningful value.

---

## Part 2: Model Quantization — Accuracy vs. Size Tradeoff (30 minutes)

### Step 2.1 — Load and Evaluate a Full-Precision Model

Create `lab15_quantization.py` and add the following code.

```python
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import time

# Load full-precision MobileNetV2
model_fp32 = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.IMAGENET1K_V1)
model_fp32.eval()

# Download a small validation subset (CIFAR-10 as proxy)
transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

dataset = datasets.CIFAR10(root="./data", train=False, download=True, transform=transform)
loader  = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=False, num_workers=0)

def evaluate(model, loader, max_batches=10):
    correct, total, elapsed = 0, 0, 0.0
    with torch.no_grad():
        for i, (imgs, _) in enumerate(loader):
            if i >= max_batches:
                break
            start = time.perf_counter()
            out   = model(imgs)
            elapsed += time.perf_counter() - start
            # Top-1 accuracy against ImageNet classes (proxy only)
            correct += (out.argmax(1) < 10).sum().item()  # count valid top-class
            total   += imgs.size(0)
    return total, elapsed

total, t_fp32 = evaluate(model_fp32, loader)
size_fp32 = sum(p.numel() * p.element_size() for p in model_fp32.parameters()) / 1e6
print(f"FP32 — Params: {sum(p.numel() for p in model_fp32.parameters())/1e6:.1f}M "
      f"| Size: {size_fp32:.1f} MB | Inference time ({total} imgs): {t_fp32:.3f}s")
```

### Step 2.2 — Apply Dynamic INT8 Quantization

Add the following quantization block.

```python
# Dynamic quantization — converts Linear layers to INT8 at runtime
model_int8 = torch.quantization.quantize_dynamic(
    model_fp32,
    {torch.nn.Linear},
    dtype=torch.qint8
)

total, t_int8 = evaluate(model_int8, loader)
size_int8 = sum(
    p.numel() * p.element_size() for p in model_int8.parameters()
) / 1e6

print(f"INT8 — Size: {size_int8:.1f} MB | Inference time ({total} imgs): {t_int8:.3f}s")
print(f"Size reduction: {(1 - size_int8/size_fp32)*100:.1f}%")
print(f"Speed change:   {(t_fp32 - t_int8)/t_fp32*100:.1f}% {'faster' if t_int8 < t_fp32 else 'slower'}")
```

### Step 2.3 — Record Results and Reflect

Run the script and record the FP32 and INT8 size, inference time, and computed reduction percentages in your lab report. Answer:

1. What size reduction did quantization achieve? Does this align with the expected 4x reduction discussed in the reading guide?
2. Did inference speed improve or worsen after quantization? What hardware-level factors might explain this result on your machine?
3. If you were deploying this model to a Raspberry Pi with 1 GB of RAM, would INT8 quantization alone be sufficient? What additional compression techniques would you consider?

---

## Part 3: Federated Learning Simulation (25 minutes)

### Step 3.1 — Simulate a Two-Client Federated Round

Create `lab15_federated.py` with the following complete simulation.

```python
import numpy as np

# -------------------------------------------------------
# Simulate federated learning of a simple linear model
# predicting house price from square footage.
# Client A: suburban homes (smaller, lower prices)
# Client B: urban homes  (larger, higher prices)
# -------------------------------------------------------

np.random.seed(42)

def generate_client_data(n, x_mean, x_std, slope, intercept, noise_std):
    x = np.random.normal(x_mean, x_std, n)
    y = slope * x + intercept + np.random.normal(0, noise_std, n)
    return x.reshape(-1, 1), y

# Client data — deliberately non-IID
X_A, y_A = generate_client_data(200, x_mean=1200, x_std=200, slope=0.15, intercept=50,  noise_std=20)
X_B, y_B = generate_client_data(200, x_mean=2500, x_std=400, slope=0.12, intercept=100, noise_std=30)

def local_train(X, y, w, b, lr=0.0001, epochs=10):
    """Train a linear model locally for a fixed number of epochs."""
    for _ in range(epochs):
        y_pred = X.squeeze() * w + b
        err    = y_pred - y
        grad_w = 2 * np.mean(err * X.squeeze())
        grad_b = 2 * np.mean(err)
        w -= lr * grad_w
        b -= lr * grad_b
    return w, b

def fedavg(updates, sizes):
    """Weighted average of (w, b) tuples by dataset size."""
    total = sum(sizes)
    w_avg = sum(u[0] * s for u, s in zip(updates, sizes)) / total
    b_avg = sum(u[1] * s for u, s in zip(updates, sizes)) / total
    return w_avg, b_avg

def mse(X, y, w, b):
    return np.mean((X.squeeze() * w + b - y) ** 2)

# -------------------------------------------------------
# Global model initialization
# -------------------------------------------------------
w_global, b_global = 0.0, 0.0

print(f"{'Round':>5} | {'Client A MSE':>14} | {'Client B MSE':>14} | {'Global MSE (A+B)':>18}")
print("-" * 60)

X_all = np.vstack([X_A, X_B])
y_all = np.concatenate([y_A, y_B])

for fed_round in range(1, 11):
    # Each client trains from the current global model
    w_A, b_A = local_train(X_A, y_A, w_global, b_global)
    w_B, b_B = local_train(X_B, y_B, w_global, b_global)

    # FedAvg aggregation
    w_global, b_global = fedavg([(w_A, b_A), (w_B, b_B)], [len(y_A), len(y_B)])

    mse_A      = mse(X_A, y_A, w_global, b_global)
    mse_B      = mse(X_B, y_B, w_global, b_global)
    mse_global = mse(X_all, y_all, w_global, b_global)
    print(f"{fed_round:>5} | {mse_A:>14.2f} | {mse_B:>14.2f} | {mse_global:>18.2f}")

print(f"\nFinal model: w = {w_global:.4f}, b = {b_global:.4f}")
```

### Step 3.2 — Analyze Convergence

Run the simulation and record the MSE table in your lab report. Answer:

1. Does the global MSE decrease consistently across rounds? What does this tell you about FedAvg convergence on non-IID data?
2. After 10 rounds, is the model's performance better for Client A or Client B? Why might the model favor one client's distribution?
3. In a real federated deployment, what would prevent an adversary (e.g., a malicious hospital) from sending manipulated weight updates to steer the global model — and what defenses would you recommend?

---

## Part 4: Lab Report (10 minutes)

### Deliverable

Compile a single PDF or Word lab report with four sections.

**Section 1 — Multimodal AI:** Paste the three model responses from Part 1. Answer the three reflection questions.

**Section 2 — Model Quantization:** Include the FP32 vs. INT8 comparison table. Answer the three reflection questions.

**Section 3 — Federated Learning:** Include the MSE convergence table. Answer the three analysis questions.

**Section 4 — Emerging Technologies Synthesis (150–200 words):** Describe a hypothetical enterprise AI system that combines at least two of the technologies from this lab — multimodal AI, edge deployment, and federated learning — to solve a real business or social problem. Identify one regulatory consideration (from Module 14 or the EU AI Act discussion in Module 15) that the system would need to address.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Part 1: Three multimodal queries executed; reflection questions answered | 25 |
| Part 2: Quantization comparison recorded; three questions answered | 25 |
| Part 3: FL convergence table recorded; three questions answered | 25 |
| Part 4: Synthesis section demonstrates integration of module concepts | 25 |
| **Total** | **100** |

---

## Troubleshooting

**Azure OpenAI 404 error** — verify the deployment name in `lab15_config.py` exactly matches the model deployment name shown in Azure AI Studio.

**Azure OpenAI quota exceeded** — free-tier resources have token-per-minute limits. Wait 60 seconds between queries or reduce `max_tokens`.

**CIFAR-10 download fails** — set `download=False` and manually place the CIFAR-10 dataset in `./data/cifar-10-batches-py/`.

**Quantized model is slower** — dynamic quantization benefits depend on CPU support for INT8 SIMD instructions. On ARM CPUs (Apple Silicon, Raspberry Pi) benefits are more pronounced than on older x86 hardware.

**Federated simulation MSE not decreasing** — reduce the learning rate to 0.00001 and increase epochs to 20 for more stable convergence.

---

*Lab Line Count: 180 | Module 15 — Emerging AI Technologies*
