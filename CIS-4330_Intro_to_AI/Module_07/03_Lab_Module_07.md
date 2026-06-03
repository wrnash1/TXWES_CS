# Lab 07 — Computer Vision with Azure

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Alignment: Describe features of computer vision workloads on Azure

---

## Lab Overview

In this lab you will provision an Azure AI Vision resource, call the Analyze Image REST endpoint programmatically, perform OCR on a document image, and build and test a Custom Vision image classifier. You will document your findings and submit screenshots and written responses.

### Learning Objectives

By completing this lab you will be able to:

- Create and configure an Azure AI Vision resource
- Call the Analyze Image API and interpret the JSON response
- Use the Read API to extract text from an image
- Build a Custom Vision classifier with at least three categories
- Evaluate model performance using Precision, Recall, and Average Precision
- Explain one responsible use consideration raised by your lab work

### Prerequisites

- Active Azure for Students subscription (free at azure.microsoft.com/en-us/free/students/)
- A web browser and access to the Azure portal (portal.azure.com)
- Python 3.8+ installed locally, OR use Azure Cloud Shell
- Basic familiarity with REST APIs and JSON

### Time Estimate

Approximately 90–120 minutes.

---

## Part A: Provision Azure AI Vision (20 minutes)

### Step A1: Create the Resource

1. Sign in to the Azure portal at portal.azure.com.
2. Select **Create a resource** from the left navigation or the home page.
3. In the search box type **Computer Vision** and press Enter.
4. Select **Computer Vision** from the results and click **Create**.
5. Fill in the creation form with the following values:

   - **Subscription**: Your Azure for Students subscription
   - **Resource group**: Click **Create new** and name it `cis4330-mod07-rg`
   - **Region**: East US (or the region nearest to you)
   - **Name**: `cis4330-vision-<your-initials>` (must be globally unique)
   - **Pricing tier**: Free F0

6. Click **Review + create**, then **Create**.
7. Wait for deployment to complete (typically 30–60 seconds).
8. Click **Go to resource**.

### Step A2: Retrieve Your Credentials

1. On the resource overview page, click **Keys and Endpoint** in the left menu.
2. Copy **KEY 1** to a text file — you will use this as your API key.
3. Copy the **Endpoint** URL — it will look like `https://eastus.api.cognitive.microsoft.com/`.
4. Keep this tab open; you will need these values throughout the lab.

### Deliverable A

Take a screenshot of the **Keys and Endpoint** page showing your endpoint URL (you may blur or crop the key value for security). Label this screenshot **Lab07-A-Credentials**.

---

## Part B: Analyze Image API (30 minutes)

### Step B1: Prepare a Test Image

Choose any publicly accessible image URL from the web. Good options include:

- A photo of a city street (tests object detection, OCR on signs)
- A photo of a kitchen (tests object and scene recognition)
- A photo of a document with visible text (tests OCR alongside analysis)

Note your image URL — you will use it in the API call.

### Step B2: Call the Analyze Image API

You can make this call using Python, curl, or the Azure Cloud Shell. The instructions below use Python.

Create a file named `lab07_analyze.py` with the following content, replacing the placeholder values:

```python
import requests
import json

ENDPOINT = "https://<your-endpoint>/"
API_KEY  = "<your-key-1>"
IMAGE_URL = "<your-image-url>"

url = (
    ENDPOINT
    + "computervision/imageanalysis:analyze"
    + "?api-version=2023-02-01-preview"
    + "&features=tags,caption,objects,read"
    + "&language=en"
    + "&gender-neutral-captions=true"
)

headers = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "Content-Type": "application/json"
}

body = {"url": IMAGE_URL}

response = requests.post(url, headers=headers, json=body)
response.raise_for_status()

result = response.json()
print(json.dumps(result, indent=2))
```

Run the script:

```bash
python lab07_analyze.py
```

### Step B3: Interpret the Response

Review the JSON output and answer the following questions in your lab write-up.

1. What are the top three tags returned, and what are their confidence scores?
2. What caption did the service generate for the image?
3. How many objects were detected? List the object names and their bounding box coordinates.
4. If any text was detected, what was it?

### Deliverable B

Paste the full JSON response into your lab document (truncate if longer than 100 lines). Answer the four questions above.

---

## Part C: OCR with the Read API (20 minutes)

### Step C1: Choose a Document Image

Find or create an image that contains printed text. Good options:

- A scanned or photographed page of text
- A screenshot of a web article
- A photo of a printed sign or poster

Upload the image to a publicly accessible URL, or use a local file path.

### Step C2: Call the Read API

The Read API is asynchronous. You first submit the image, then poll for results. Add the following to a new file named `lab07_ocr.py`:

```python
import requests
import time
import json

ENDPOINT = "https://<your-endpoint>/"
API_KEY  = "<your-key-1>"
IMAGE_URL = "<your-document-image-url>"

# Step 1: Submit the read operation
submit_url = ENDPOINT + "computervision/imageanalysis:analyze"
params = {
    "api-version": "2023-02-01-preview",
    "features": "read"
}
headers = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "Content-Type": "application/json"
}
body = {"url": IMAGE_URL}

response = requests.post(submit_url, headers=headers,
                         params=params, json=body)
response.raise_for_status()
result = response.json()

# Step 2: Print extracted text
read_result = result.get("readResult", {})
blocks = read_result.get("blocks", [])
for block in blocks:
    for line in block.get("lines", []):
        print(line.get("text", ""))
```

Run the script and observe the extracted text output.

### Deliverable C

1. Screenshot of the terminal showing the extracted text.
2. Short written answer (3–5 sentences): How accurately did the OCR capture the text in your image? Were there any errors? What do you think caused them?

---

## Part D: Custom Vision Classifier (30 minutes)

### Step D1: Create a Custom Vision Resource

1. Navigate to customvision.ai and sign in with your Azure credentials.
2. Click **New Project**.
3. Fill in the project form:

   - **Name**: `lab07-classifier`
   - **Resource**: Create new → select your resource group `cis4330-mod07-rg` → Free F0 tier
   - **Project Types**: Classification
   - **Classification Types**: Multiclass (Single Tag per Image)
   - **Domains**: General [A2] (recommended for most scenarios)

4. Click **Create project**.

### Step D2: Collect Training Images

Choose a classification scenario with exactly three categories. Suggestions:

- Three types of fruit (apple, banana, orange)
- Three types of weather (sunny, cloudy, rainy)
- Three types of clothing (shirt, pants, shoes)

For each category, collect at least 15 images. You can:

- Search Google Images and download
- Use free image sources such as Unsplash or Pixabay
- Take your own photos

Store images in three separate folders named after their categories.

### Step D3: Upload and Tag Images

1. In your Custom Vision project, click **Add images**.
2. Upload all images for your first category and enter the category name as the tag.
3. Repeat for the remaining two categories.
4. Verify each category shows at least 15 tagged images in the gallery.

### Step D4: Train the Model

1. Click **Train** in the top menu.
2. Select **Quick Training** and click **Train**.
3. Wait for training to complete (typically 2–5 minutes).
4. When the **Performance** tab appears, record the metrics:

   - Overall Precision
   - Overall Recall
   - Mean Average Precision (mAP)
   - Per-tag Precision and Recall

### Step D5: Test the Model

1. Click **Quick Test** in the top menu.
2. Enter the URL of an image you did NOT use in training, from one of your three categories.
3. Observe the prediction and confidence score.
4. Test at least three different images (one per category).

### Deliverable D

1. Screenshot of the Performance tab showing your trained model metrics.
2. Screenshot of at least one Quick Test prediction.
3. Written answers to these questions:

   - Which category had the highest Average Precision? Why do you think that is?
   - Did any category perform poorly? What might be causing the lower performance?
   - How would you improve the model if you had more time?

---

## Part E: Reflection and Responsible AI (10 minutes)

Answer the following in 150–200 words:

Your Custom Vision model classifies images into the categories you chose. Consider a scenario where an organization deploys a computer vision system to classify people's behavior in a workplace — for example, detecting whether workers are wearing safety helmets.

Address the following points:

1. What bias risks exist when training this type of model?
2. What data privacy considerations should the organization address before deployment?
3. How should the organization handle cases where the model's prediction is wrong?

---

## Submission Requirements

Submit to the course LMS by the posted deadline. Include all of the following.

- **Lab07-A-Credentials** screenshot (key blurred or cropped)
- Full JSON response from Part B with written answers to the four interpretation questions
- OCR screenshot and written accuracy assessment from Part C
- Custom Vision Performance tab screenshot and Quick Test screenshot from Part D
- Written answers to the three Part D analysis questions
- Reflection response from Part E (150–200 words)

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Part A — Resource provisioning | 10 | Screenshot shows correct resource type and endpoint |
| Part B — Analyze Image call | 20 | Valid JSON response; all four questions answered with specifics |
| Part C — OCR extraction | 15 | Extracted text shown; accuracy assessment thoughtful |
| Part D — Custom Vision training | 30 | Model trained with 3 tags, 15+ images each; metrics recorded; 3 test predictions shown |
| Part D — Analysis questions | 15 | Specific and accurate explanations referencing actual metrics |
| Part E — Reflection | 10 | Addresses bias, privacy, and error handling substantively |
| **Total** | **100** | |

---

## Cleanup (Important)

To avoid incurring Azure charges beyond the free tier, delete your resource group after submitting the lab.

1. In the Azure portal, navigate to **Resource groups**.
2. Select `cis4330-mod07-rg`.
3. Click **Delete resource group**.
4. Type the resource group name to confirm and click **Delete**.

Custom Vision resources within the group will also be deleted.

---

End of Lab 07
