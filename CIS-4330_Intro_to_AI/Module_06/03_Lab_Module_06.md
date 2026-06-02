# Lab Activity: Module 06 - Computer Vision and Image Recognition

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe features of Computer Vision workloads on Azure
**Points:** 100
**Submission:** Canvas LMS — Module 06 Lab Assignment

---

## Objectives

By the end of this lab, you will be able to:

- Identify the computer vision task type described in a given scenario.
- Match computer vision scenarios to the correct Azure service.
- Interpret sample Azure Computer Vision API output including tags, objects, and confidence scores.
- Evaluate responsible AI implications of facial recognition deployment scenarios.
- Distinguish between image classification and object detection use cases.

---

## Prerequisites

No Azure subscription is required. All exercises are analysis and interpretation tasks. You will need:

- Module 06 video lecture (completed).
- Module 06 reading guide (completed), including Table 1 and Table 2.

---

## Part A: Computer Vision Task Classification (30 points)

For each scenario, identify the computer vision task from this list: Image Classification, Object Detection, Image Segmentation, OCR (Text Extraction), Face Detection, Face Verification, Video Analysis, Content Moderation.

Each task may be used at most twice. Provide a one-sentence justification.

### Scenario 1

An insurance company receives photos of vehicle damage filed with claims. The system needs to automatically identify what parts of the car are damaged (hood, door, bumper) and locate each damaged area within the photo.

Computer vision task: ________________
Justification: ________________

### Scenario 2

A security system at a hospital entrance takes two photos at different times of day and needs to determine whether the person entering at 11 PM is the same person whose badge photo is on file.

Computer vision task: ________________
Justification: ________________

### Scenario 3

A social media platform needs to automatically screen all uploaded images to determine whether each one contains adult content or violent imagery, and flag policy violations before the content is published.

Computer vision task: ________________
Justification: ________________

### Scenario 4

An agricultural technology company wants to classify each aerial drone photograph of a field as one of four categories: healthy crop, drought stress, pest damage, or flooding.

Computer vision task: ________________
Justification: ________________

### Scenario 5

A logistics company receives thousands of handwritten package labels daily. The company needs to extract the recipient address text from photographs of each label so the information can be entered into their routing system.

Computer vision task: ________________
Justification: ________________

### Scenario 6

A medical imaging company analyzes brain MRI scans. Their system needs to precisely outline the boundary of a tumor in each scan — not just draw a bounding box around it, but delineate the exact shape at the pixel level.

Computer vision task: ________________
Justification: ________________

### Scenario 7

A retail store's camera system analyzes continuous video footage to detect when a customer has been standing in the same location for more than five minutes without moving toward a checkout lane, triggering an alert for staff to offer assistance.

Computer vision task: ________________
Justification: ________________

### Scenario 8

A mobile app for plant enthusiasts needs to determine whether a photo uploaded by a user shows a healthy plant, a plant with a specific fungal disease, or a plant with a nutrient deficiency.

Computer vision task: ________________
Justification: ________________

---

## Part B: Azure Service Matching (20 points)

For each scenario, identify the most appropriate Azure service: Azure Computer Vision, Azure Custom Vision, Azure Face API, Azure Form Recognizer (Document Intelligence).

Each service may be used more than once.

### Scenario 9

A startup wants to add an automatic image tagging feature to their photo sharing app. They want to identify general objects — trees, cars, buildings, animals — in user-uploaded photos. They have no custom training data and need fast deployment.

Azure service: ________________
Justification: ________________

### Scenario 10

A wine distributor wants to build a mobile app that identifies wine bottle labels from photos. The standard Computer Vision service does not recognize the hundreds of specific winery labels the company carries. They have 50 labeled photos per label variety.

Azure service: ________________
Justification: ________________

### Scenario 11

A bank processes thousands of printed loan application forms daily. They need to automatically extract the applicant's name, address, loan amount, and signature date from scanned form images and populate their database.

Azure service: ________________
Justification: ________________

### Scenario 12

A concert venue wants to implement a system that checks whether a person's face at the entrance matches their ticket photo to verify event access and prevent ticket fraud.

Azure service: ________________
Justification: ________________

### Scenario 13

A publishing company needs to extract all text from thousands of scanned historical newspaper pages — including both printed headlines and handwritten margin notes — to create a searchable digital archive.

Azure service: ________________
Justification: ________________

---

## Part C: Interpreting Computer Vision API Output (30 points)

The following JSON represents the response from Azure Computer Vision for an analyzed image of an outdoor park scene.

```json
{
  "tags": [
    {"name": "tree", "confidence": 0.997},
    {"name": "grass", "confidence": 0.994},
    {"name": "person", "confidence": 0.961},
    {"name": "dog", "confidence": 0.876},
    {"name": "path", "confidence": 0.743},
    {"name": "bench", "confidence": 0.511}
  ],
  "objects": [
    {
      "object": "person",
      "confidence": 0.941,
      "rectangle": {"x": 102, "y": 88, "w": 85, "h": 210}
    },
    {
      "object": "dog",
      "confidence": 0.863,
      "rectangle": {"x": 310, "y": 240, "w": 120, "h": 95}
    },
    {
      "object": "bench",
      "confidence": 0.502,
      "rectangle": {"x": 540, "y": 300, "w": 190, "h": 80}
    }
  ],
  "description": {
    "captions": [
      {"text": "a person walking a dog in a park", "confidence": 0.887}
    ]
  }
}
```

### Question 14 (8 points)

The tags array contains both "tree" (0.997) and "bench" (0.511). Explain what the confidence score represents and describe what a score of 0.511 for "bench" tells you about the model's certainty. At what threshold would you typically set a minimum confidence score for a business application, and why?

Your answer: ________________

### Question 15 (8 points)

The objects array includes bounding box rectangles for each detected object. The object "bench" is detected with confidence 0.502. A product manager says they want to filter out any detection below confidence 0.75 for their retail analytics application. If they apply this filter, which objects from this response would be retained and which would be removed? What is the trade-off of setting a high confidence threshold?

Your answer: ________________

### Question 16 (7 points)

The description.captions field returns "a person walking a dog in a park" with confidence 0.887. This caption is generated automatically. Describe a scenario where automatically generated image captions would be a valuable accessibility feature, and identify which Microsoft responsible AI principle this capability supports.

Your answer: ________________

### Question 17 (7 points)

Azure Computer Vision returned the tag "dog" with confidence 0.876 in the tags array, but the objects array also detects a "dog" with confidence 0.863. What is the conceptual difference between a tag result and an object detection result for the same "dog"? When would a developer need the object result but not the tag result?

Your answer: ________________

---

## Part D: Responsible AI Analysis — Facial Recognition (20 points)

Read the following scenario and answer both questions in complete sentences (minimum 4 sentences each).

### Scenario

A city government is considering deploying a real-time facial recognition system on 500 public street cameras. The system would compare faces captured by cameras to a database of outstanding warrants and automatically alert police when a match is detected above 85% confidence. The system vendor claims accuracy of 94% overall on their benchmark test set.

### Question 18 (10 points)

Identify two distinct responsible AI principles that are relevant to this scenario. For each principle, explain specifically how this deployment could violate it, using details from the scenario.

Your answer: ________________

### Question 19 (10 points)

The system claims 94% overall accuracy. A civil rights organization points out that the benchmark test set was primarily composed of lighter-skinned male faces. Explain why overall accuracy can be misleading in this context, what additional evaluation data the city should demand before deployment, and what remediation steps would be needed if disparities are found.

Your answer: ________________

---

## Answer Key and Grading Rubric

### Part A (3-4 points per scenario = 30 points)

Scenario 1: Object Detection. Multiple damaged areas must be located and identified — requires bounding boxes per object, not one label for the whole image.

Scenario 2: Face Verification. 1:1 comparison of two face images to determine if they show the same person.

Scenario 3: Content Moderation. Automatically classifying images by policy-violating content categories.

Scenario 4: Image Classification. One label (from four categories) assigned to the entire aerial photograph.

Scenario 5: OCR (Text Extraction). Extracting printed or handwritten text from images of package labels.

Scenario 6: Image Segmentation. Pixel-level boundary delineation of a tumor is the definition of segmentation.

Scenario 7: Video Analysis. Tracking person position over time in a continuous video stream.

Scenario 8: Image Classification. Single label from three categories (healthy, fungal, nutrient) for each photo.

### Part B (4 points per scenario = 20 points)

Scenario 9: Azure Computer Vision. General object tagging with no custom training.

Scenario 10: Azure Custom Vision. Domain-specific label recognition requires custom classification training with provided images.

Scenario 11: Azure Form Recognizer (Document Intelligence). Structured form field extraction from scanned documents.

Scenario 12: Azure Face API. 1:1 face verification comparing entrance photo to ticket photo.

Scenario 13: Azure Computer Vision (Read API). OCR of printed and handwritten text from scanned images.

### Part C (30 points per rubric above)

Q14: Confidence score = model's probability estimate for that tag. 0.511 means the model is only slightly more confident than random that a bench is present — essentially uncertain. Most applications set thresholds of 0.7-0.9 to balance precision against recall; lower thresholds increase false positives.

Q15: At 0.75 threshold, only "person" (0.941) is retained. "Dog" (0.863) is also above 0.75 and retained. "Bench" (0.502) is filtered out. Trade-off: higher threshold reduces false positives but may miss genuine objects with uncertain detection (true positives lost).

Q16: Auto-captions provide image descriptions for screen reader users who cannot see the image. This supports the Inclusiveness principle — making AI capabilities accessible to people with visual impairments.

Q17: A tag indicates the presence of a concept anywhere in the image (no location). An object detection result provides the bounding box (location and size). A developer needing to count or locate dogs in a scene needs object results; one needing only to know "is there a dog in this photo" needs only tags.

### Part D (10 points each = 20 points)

Q18: Fairness — if the system has higher error rates for darker-skinned or female individuals, it will produce disproportionate false positives from those groups, leading to unwarranted police interactions. Privacy and Security — continuous public facial recognition enables mass surveillance, collecting biometric data from citizens who have not consented to identification.

Q19: Overall accuracy of 94% on a non-representative benchmark does not reveal demographic subgroup performance. The city should require disaggregated accuracy reports by skin tone, gender, and age group. If disparities are found, the vendor must either retrain on balanced datasets, apply demographic-specific threshold adjustments, or the city should not deploy the system until parity is achieved.

---

## Deliverable

Submit a single document (PDF or Word) with all answers and justifications. Include the JSON excerpt inline with your Part C answers to show which portions you are referencing. Include your name, course section, and date at the top. Upload to the Module 06 Lab Assignment in Canvas by the posted due date.
