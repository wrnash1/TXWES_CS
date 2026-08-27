# Lab Activity: Module 14 — AI Security and Privacy

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Lab Overview

**Lab Title:** Exploring Adversarial Robustness and Differential Privacy in Azure ML

**Duration:** 90–120 minutes

**Format:** Individual (Azure free-tier account required)

**Objectives:**

- Demonstrate a basic adversarial example against a pre-trained image classifier
- Apply input preprocessing as a defense and observe the effect on accuracy
- Implement a differentially private query using the SmartNoise/OpenDP toolkit
- Document findings in a structured security analysis report

**Prerequisites:** Completion of Module 13 lab; Python 3.9+ with pip; Azure free-tier account

---

## Part 1: Environment Setup (15 minutes)

### Step 1.1 — Create a Python Virtual Environment

Open a terminal or Azure Cloud Shell and run the following commands.

```bash
python -m venv ai_security_lab
source ai_security_lab/bin/activate        # macOS/Linux
# ai_security_lab\Scripts\activate         # Windows
pip install torch torchvision numpy pillow matplotlib opendp
```

### Step 1.2 — Download the Lab Starter Script

Create a new file named `lab14_starter.py` in your working directory. All code in Parts 2–4 will be added to this file in the sections indicated.

### Step 1.3 — Verify Imports

Add the following imports to the top of `lab14_starter.py` and run the file to confirm no errors.

```python
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
import opendp.prelude as dp
```

If any import fails, re-run the pip install command for the missing package.

---

## Part 2: Adversarial Example with FGSM (35 minutes)

### Step 2.1 — Load a Pre-Trained Model

Add the following code block to `lab14_starter.py`. This loads a pre-trained ResNet-18 model from PyTorch's model zoo and sets it to evaluation mode.

```python
# Load pre-trained ResNet-18
model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
model.eval()

# ImageNet normalization parameters
mean = [0.485, 0.456, 0.406]
std  = [0.229, 0.224, 0.225]

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean, std=std)
])
```

### Step 2.2 — Download and Classify a Clean Image

Add the following block to download a sample image and classify it.

```python
# Download a sample image (tabby cat from ImageNet)
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/320px-Cat_November_2010-1a.jpg"
urllib.request.urlretrieve(url, "cat.jpg")

# Load and preprocess
img = Image.open("cat.jpg").convert("RGB")
img_tensor = preprocess(img).unsqueeze(0)  # shape: (1, 3, 224, 224)
img_tensor.requires_grad = True

# Forward pass
output = model(img_tensor)
pred_class = output.argmax(dim=1).item()

# Load ImageNet class labels
labels_url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
urllib.request.urlretrieve(labels_url, "imagenet_classes.txt")
with open("imagenet_classes.txt") as f:
    classes = [line.strip() for line in f.readlines()]

print(f"Clean prediction: {classes[pred_class]} (class {pred_class})")
```

Run the file. Record the clean prediction label in your lab report.

### Step 2.3 — Apply FGSM to Generate an Adversarial Example

Add the following FGSM attack code.

```python
# FGSM attack
epsilon = 0.02   # perturbation magnitude

# Compute loss with respect to the true label
criterion = torch.nn.CrossEntropyLoss()
true_label = torch.tensor([pred_class])
loss = criterion(output, true_label)

# Backpropagate to get gradient w.r.t. input
model.zero_grad()
loss.backward()
data_grad = img_tensor.grad.data

# Create adversarial example
adv_tensor = img_tensor + epsilon * data_grad.sign()
adv_tensor = adv_tensor.detach()

# Classify adversarial example
adv_output = model(adv_tensor)
adv_class = adv_output.argmax(dim=1).item()
print(f"Adversarial prediction (ε={epsilon}): {classes[adv_class]} (class {adv_class})")
```

### Step 2.4 — Visualize the Perturbation

Add the visualization block.

```python
# De-normalize for display
def denormalize(tensor, mean, std):
    t = tensor.clone().squeeze(0)
    for c, m, s in zip(t, mean, std):
        c.mul_(s).add_(m)
    return t.permute(1, 2, 0).numpy().clip(0, 1)

clean_img_disp = denormalize(img_tensor.detach(), mean, std)
adv_img_disp   = denormalize(adv_tensor, mean, std)
perturbation    = np.abs(adv_img_disp - clean_img_disp) * 10  # amplified

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(clean_img_disp); axes[0].set_title(f"Clean: {classes[pred_class][:20]}")
axes[1].imshow(perturbation);   axes[1].set_title("Perturbation (10x)")
axes[2].imshow(adv_img_disp);   axes[2].set_title(f"Adversarial: {classes[adv_class][:20]}")
for ax in axes: ax.axis("off")
plt.tight_layout()
plt.savefig("lab14_fgsm.png", dpi=120)
print("Saved lab14_fgsm.png")
```

### Step 2.5 — Experiment with Epsilon Values

Modify the epsilon value to 0.005, 0.01, 0.05, and 0.10. Re-run each time and record:

- The predicted class at each epsilon value
- Whether the prediction changed from the clean prediction
- Your subjective assessment of whether the perturbation is visible

Record your results in a table in your lab report with columns: Epsilon | Predicted Class | Changed? | Perturbation Visible?

---

## Part 3: Input Preprocessing Defense (20 minutes)

### Step 3.1 — JPEG Compression Defense

Add the following defense code.

```python
import io

def jpeg_compress_defense(tensor, quality=75):
    """Apply JPEG compression to strip adversarial perturbation."""
    img_disp = denormalize(tensor, mean, std)
    pil_img = Image.fromarray((img_disp * 255).astype(np.uint8))

    buffer = io.BytesIO()
    pil_img.save(buffer, format="JPEG", quality=quality)
    buffer.seek(0)
    defended_pil = Image.open(buffer).convert("RGB")

    defended_tensor = preprocess(defended_pil).unsqueeze(0)
    return defended_tensor

# Apply defense to adversarial example
defended_tensor = jpeg_compress_defense(adv_tensor, quality=75)
defended_output = model(defended_tensor)
defended_class  = defended_output.argmax(dim=1).item()
print(f"Post-defense prediction: {classes[defended_class]} (class {defended_class})")
```

### Step 3.2 — Test Defense at Multiple Epsilon Values

For each epsilon value from Step 2.5, apply the JPEG compression defense and record whether the prediction is restored to the correct class. Add a "Defended Prediction" column to your results table.

### Step 3.3 — Reflection Questions

Answer the following in your lab report (2–3 sentences each):

1. At what epsilon value did the adversarial example first change the prediction? What does this tell you about the robustness of ResNet-18?
2. Did JPEG compression successfully defend against all epsilon levels? Why might it fail at high epsilon?
3. How would you design a more robust defense for a production image classification API?

---

## Part 4: Differential Privacy with OpenDP (20 minutes)

### Step 4.1 — Simulated Salary Dataset

Add the following code to create a simulated sensitive dataset.

```python
import opendp.prelude as dp
dp.enable_features("contrib")

# Simulated salary data (in thousands USD) — 500 employees
np.random.seed(42)
salaries = np.random.normal(loc=75, scale=20, size=500).clip(20, 200).tolist()
print(f"True mean salary: ${np.mean(salaries):.2f}K")
```

### Step 4.2 — DP Mean with the Laplace Mechanism

Add the differentially private mean computation.

```python
# Define bounds (domain knowledge: salaries between $20K and $200K)
lower, upper = 20.0, 200.0
sensitivity = (upper - lower) / len(salaries)  # L1 sensitivity of mean

def dp_mean(data, epsilon):
    """Compute differentially private mean using Laplace mechanism."""
    true_mean = np.mean(data)
    noise_scale = sensitivity / epsilon
    dp_noise = np.random.laplace(0, noise_scale)
    return true_mean + dp_noise

# Compare across epsilon values
print("\nDifferential Privacy — Mean Salary Estimation")
print(f"{'Epsilon':>10} | {'DP Mean':>12} | {'True Mean':>12} | {'|Error|':>10}")
print("-" * 52)
for eps in [0.01, 0.1, 0.5, 1.0, 5.0, 10.0]:
    dp_est = dp_mean(salaries, eps)
    error  = abs(dp_est - np.mean(salaries))
    print(f"{eps:>10.2f} | {dp_est:>12.2f} | {np.mean(salaries):>12.2f} | {error:>10.2f}")
```

### Step 4.3 — Observe the Privacy-Utility Tradeoff

Run the code and record the output table. In your lab report, answer:

1. At ε = 0.01, how far is the DP estimate from the true mean? Is this useful for business decisions?
2. At ε = 5.0 or ε = 10.0, is the DP estimate reasonably accurate? What privacy risk does this level represent?
3. If you were advising a healthcare organization releasing aggregate statistics from patient data, what epsilon value would you recommend? Justify your answer.

---

## Part 5: Lab Report (10 minutes)

### Deliverable

Compile a lab report in PDF or Word format containing the following sections.

**Section 1 — Adversarial Examples:**
Include your epsilon results table and the saved `lab14_fgsm.png` visualization. Answer the three reflection questions from Step 3.3.

**Section 2 — Differential Privacy:**
Include the DP mean output table. Answer the three questions from Step 4.3.

**Section 3 — Azure AI Security Reflection:**
In 150–200 words, describe how the techniques you practiced today relate to real-world AI deployment. Specifically address: How would a company deploying an Azure AI Vision API protect against adversarial inputs? How would a company releasing aggregate model statistics comply with GDPR's data minimization principle using differential privacy?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Part 2: FGSM attack runs successfully; epsilon table completed | 25 |
| Part 3: Defense applied; reflection questions answered thoroughly | 25 |
| Part 4: DP table completed; privacy-utility questions answered | 25 |
| Part 5: Lab report complete, professional, and coherent | 25 |
| **Total** | **100** |

---

## Troubleshooting

**"No module named torch"** — ensure your virtual environment is activated before running pip install and before running the script.

**Image download fails** — replace the URL with any JPEG image of your choice. The FGSM attack works on any valid ImageNet-preprocessed image.

**CUDA errors** — add `model = model.cpu()` and ensure `img_tensor = img_tensor.cpu()` if no GPU is available.

**OpenDP import error** — run `pip install opendp --upgrade` to ensure version 0.9 or higher is installed.

---

## Part 9 — Challenge Exercise

### Challenge 1: Targeted vs. Untargeted FGSM and Defense Effectiveness

1. Extend the FGSM experiment from Part 2 of this lab. Select an image that your ResNet-50 model classifies correctly with confidence above 0.90. Generate adversarial examples at five epsilon values: 0.005, 0.01, 0.02, 0.05, 0.10. For each epsilon, record: (a) the original class, (b) the adversarial prediction, (c) the adversarial confidence score, and (d) whether the perturbation is visually detectable.
2. Implement a targeted FGSM attack: choose a specific wrong target class and modify the sign of the gradient to push the prediction toward that target. Compare the epsilon required to achieve the targeted misclassification versus the untargeted misclassification at the same confidence level.
3. Apply two defenses to the adversarial examples: (a) Gaussian blur (sigma=1.0) using `scipy.ndimage.gaussian_filter`, and (b) JPEG compression at quality=50 using PIL. For each defense, test whether the defended image restores the correct classification. Record success/failure for each combination of epsilon and defense.
4. Build a comparison table: Epsilon | Original Class | Adversarial Class | Untargeted Success | Targeted Class | Targeted Success | Blur Defense Restores | JPEG Defense Restores. Write a 3–4 sentence analysis of which epsilon range and which defense combination is most practical for a production computer vision pipeline.

### Challenge 2: Membership Inference Attack Simulation

1. Train two identical `RandomForestClassifier` models on the Breast Cancer Wisconsin dataset (`sklearn.datasets.load_breast_cancer`): Model A trained on 80 percent of the data (training set), Model B trained on 20 percent (test set). Both models have access to the full feature set.
2. Implement a simple membership inference attack: for each sample in the full dataset, query Model A's `predict_proba` output and record the confidence for the true class. Repeat for Model B. Compute the mean confidence on samples that were in training vs. samples that were not in training for each model.
3. A membership inference signal: training set samples typically receive higher confidence from the model they were trained on. Compute the AUC of a binary classifier that uses confidence score to predict "was this sample in the training set?" Plot the ROC curve.
4. Apply a mitigation: retrain Model A with `max_depth=3` (a regularization constraint that reduces overfitting). Recompute the membership inference AUC. Write a 2–3 sentence explanation of why regularization reduces membership inference risk and what this reveals about the connection between overfitting and privacy.

### Reflection Questions

1. After completing Challenge 1, explain why JPEG compression and Gaussian blur can partially defend against FGSM adversarial examples, even though they are not designed as adversarial defenses. What property of adversarial perturbations makes them vulnerable to these preprocessing operations, and why does this defense fail at very high epsilon values?

2. Based on Challenge 2, explain why membership inference attacks are more dangerous for models trained on small, sensitive datasets (such as a clinical trial dataset with 500 patients) than for models trained on large general datasets (such as an ImageNet model). What does this imply about the relationship between dataset size, overfitting risk, and the need for differential privacy?

---

Lab Line Count: 175 | Module 14 — AI Security and Privacy
