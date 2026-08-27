# Reading Guide: Module 06 - Computer Vision and Image Recognition

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe features of Computer Vision workloads on Azure (15-20%)

---

## Overview

This reading guide covers computer vision tasks, convolutional neural network concepts, Azure computer vision services, and responsible AI considerations for visual AI systems. The AI-900 exam tests your ability to match vision tasks to Azure services and identify responsible AI implications. Complete the study checklist before the lab.

---

## Section 1: Core Vocabulary

**Computer Vision**
The field of AI that enables machines to interpret and understand visual information — photographs, video, medical images, documents, and more.

**Image Classification**
A computer vision task that assigns a single label (or ranked set of labels) to an entire image. Output: a class label with a confidence score.

**Object Detection**
A computer vision task that identifies and locates all instances of specific object categories within an image. Output: bounding boxes (x, y, width, height) with class labels and confidence scores for each detected object.

**Image Segmentation**
A computer vision task that assigns a label to every pixel in an image. Semantic segmentation assigns all pixels of the same category the same label. Instance segmentation distinguishes individual instances of the same category.

**Optical Character Recognition (OCR)**
Detecting and extracting printed or handwritten text from images, documents, and scanned files.

**Face Detection**
Locating all human faces in an image and returning their bounding box coordinates.

**Face Verification**
Determining whether two face images show the same person. A 1:1 matching task.

**Face Identification**
Determining which known individual a detected face belongs to, from a pre-enrolled database. A 1:N matching task. Access to this capability in Azure Face API is restricted due to responsible AI concerns.

**Convolutional Neural Network (CNN)**
A deep learning architecture designed for image data. Convolutional layers apply learned filters to detect local visual features (edges, shapes, textures) while preserving spatial relationships.

**Convolutional Layer**
A neural network layer that applies learned filters to input images or feature maps, producing new feature maps that represent detected local patterns.

**Filter (Kernel)**
A small grid of learned weights in a convolutional layer. Each filter detects a specific local pattern. CNNs learn many filters per layer.

**Feature Map**
The output of applying a filter to an image. Each element of the feature map represents how strongly the filter's pattern appears at that image location.

**Pooling Layer**
A layer that reduces the spatial dimensions of feature maps by taking the maximum or average value in small regions. Reduces computation and provides translational robustness.

**Transfer Learning (computer vision)**
Using a CNN pretrained on a large dataset (such as ImageNet) as the starting point for training a new model on a smaller domain-specific dataset. The early layers retain general visual features; the final layers are retrained.

**Azure Computer Vision**
A prebuilt Azure Cognitive Service that analyzes images to return tags, object detection results, text (via Read API), image captions, color analysis, and content flags. No custom training required.

**Azure Custom Vision**
An Azure service that enables users to train custom image classifiers and object detectors using their own labeled images, powered by transfer learning.

**Azure Face API**
An Azure Cognitive Service that detects human faces in images, returns face attributes (age estimate, emotion, accessories), and supports face verification. Face identification requires approved access.

**Azure Form Recognizer / Document Intelligence**
An Azure Applied AI Service that extracts structured data from documents, forms, receipts, and invoices using intelligent OCR and document layout understanding.

**Bounding Box**
A rectangle defined by x-coordinate, y-coordinate, width, and height that locates a detected object within an image.

**Confidence Score (computer vision)**
A value between 0 and 1 representing the model's certainty that a detected object or classification label is correct.

**Content Moderation**
A computer vision application that automatically classifies images as containing adult content, violence, or other policy-violating material.

---

## Section 2: Comparison Tables

### Table 1: Core Computer Vision Tasks

| Task | Input | Output | Key Difference from Similar Tasks | Azure Service |
|---|---|---|---|---|
| Image Classification | Image | One or more class labels with confidence scores | Describes the whole image, no location | Azure Computer Vision / Custom Vision |
| Object Detection | Image | Bounding boxes + class labels for each detected object | Locates and classifies multiple objects | Azure Computer Vision / Custom Vision |
| Image Segmentation | Image | Per-pixel class label map | Pixel-level precision; more granular than detection | Azure ML (custom) |
| OCR / Text Extraction | Image / document | Extracted text with bounding polygons | Handles printed and handwritten text | Azure Computer Vision (Read API) |
| Face Detection | Image | Face bounding boxes + attributes | Detects faces specifically, not general objects | Azure Face API |
| Face Verification | Two images | Match/no-match with confidence | 1:1 comparison only | Azure Face API |
| Video Analysis | Video stream | Objects/activities over time | Adds temporal dimension | Azure Video Indexer |

### Table 2: Azure Computer Vision Services

| Service | Custom Training | Primary Use Case | Key Capability | Responsible AI Note |
|---|---|---|---|---|
| Azure Computer Vision | No | General image analysis, OCR | Tags, captions, objects, Read API | Content safety filters available |
| Azure Custom Vision | Yes | Custom image classification / object detection | Transfer learning from 15+ images/class | Model accuracy varies with dataset quality |
| Azure Face API | No | Face detection, verification, attributes | Bounding boxes, age estimate, emotion | Face identification requires gated access |
| Azure Form Recognizer | Partially | Document and form data extraction | Field extraction, table recognition | PII handling requires attention |
| Azure Video Indexer | Partially | Video content analysis | Transcription, face detection, scene detection | Face identification gated |

### Table 3: Image Classification vs Object Detection vs Segmentation

| Dimension | Image Classification | Object Detection | Image Segmentation |
|---|---|---|---|
| Output granularity | One label per image | One bounding box per detected instance | One label per pixel |
| Spatial information | None | Object location (bounding box) | Precise object shape |
| Use case | "What is in this image overall?" | "Where are all the objects in this image?" | "Which pixels belong to each object?" |
| Compute requirement | Low | Moderate | High |
| Labeled data requirement | Labels per image | Bounding boxes per image | Pixel masks per image |
| Azure Custom Vision | Yes (classification project) | Yes (object detection project) | Requires Azure ML |

### Table 4: CNN Layer Functions

| Layer Type | What It Does | Analogy |
|---|---|---|
| Convolutional layer | Applies learned filters to detect local patterns | Sliding a spotlight across the image to find specific features |
| ReLU activation | Introduces non-linearity after each conv layer | Keeps useful signal; discards negative activations |
| Pooling layer | Reduces spatial dimensions; provides robustness | Compressing the image while preserving what was found |
| Flatten layer | Converts 3D feature map to 1D vector | Unrolling the spatial map into a feature list |
| Fully connected layer | Combines all features for final classification | Standard neural network inference on extracted features |
| Softmax output | Converts scores to class probabilities | Normalizes the confidence across all possible classes |

---

## Section 3: Azure Custom Vision Workflow

Azure Custom Vision follows a consistent five-step workflow for both classification and object detection projects.

**Step 1 — Create project:** Select project type (classification or object detection) and domain (general, food, retail, medical, logo, etc.). Domain selection initializes the pretrained CNN for the closest matching visual domain.

**Step 2 — Upload and label images:** For classification, add images and assign one or more class tags. For object detection, add images and draw bounding boxes around each instance. Minimum: 15 images per class for classification; 50 images per class for object detection.

**Step 3 — Train:** Click Train. Custom Vision runs transfer learning — it freezes the early layers of the pretrained CNN and fine-tunes the final layers on your labeled images. Training takes seconds to minutes.

**Step 4 — Evaluate:** Review precision and recall per class on the test set. The Performance tab shows where the model struggles. Add more labeled images to weak classes and retrain to improve.

**Step 5 — Publish and call:** Publish the trained iteration to a prediction endpoint. Call the endpoint via REST API with an image, and receive JSON output containing class predictions (classification) or bounding box detections (object detection) with confidence scores.

---

## Section 4: Responsible AI in Computer Vision

The AI-900 exam addresses responsible AI specifically in the context of facial recognition.

**Facial recognition and privacy:** Systems that identify individuals by face in public spaces enable mass surveillance. Microsoft has committed to not selling real-time facial recognition to police in the United States and has made face identification in Azure Face API a gated access capability, requiring customers to submit a use case for approval.

**Bias and demographic disparities:** Studies — including the Gender Shades research by Joy Buolamwini and Timnit Gebru — demonstrated that commercial face analysis systems had error rates up to 34% higher for darker-skinned women than for lighter-skinned men. These disparities reflect imbalances in training data. The Microsoft Fairness principle requires teams to audit models across demographic groups.

**Content safety:** Computer vision used for content moderation must balance sensitivity (catching harmful content) against specificity (not over-flagging legitimate content). Azure Content Safety is a dedicated service for this purpose.

**Medical imaging accuracy:** Computer vision deployed for medical diagnosis (tumor detection, retinal disease screening) has high-stakes consequences. Errors — missed diagnoses or false alarms — directly affect patient outcomes. The Reliability and Safety and Accountability principles both apply.

---

## Section 5: AI-900 Exam Tips

1. Image classification assigns one label to the whole image. Object detection assigns labels and bounding boxes to each detected object within the image. Segmentation goes pixel-by-pixel. Know these distinctions precisely — they are directly tested.

2. Azure Computer Vision is prebuilt and requires no training. Azure Custom Vision requires labeled training images but enables custom categories. The exam uses scenario clues like "custom objects," "domain-specific," or "company's own products" to signal Custom Vision.

3. Azure Face API is specifically for faces. For general object detection, use Azure Computer Vision or Custom Vision. Do not confuse them.

4. The Read API (OCR) is part of Azure Computer Vision. When a scenario describes extracting text from an image or document, the answer is Azure Computer Vision Read API or Azure Form Recognizer, depending on whether the input is a photograph or a structured form/document.

5. Azure Form Recognizer (Document Intelligence) is an Applied AI Service, not a standard Cognitive Service. It handles structured document extraction — receipts, invoices, forms — not just raw text from images.

6. Face identification (1:N matching to a database of known individuals) requires approved access in Azure and is treated differently from face detection and face verification.

7. Transfer learning is why Azure Custom Vision works with small datasets. The pretrained CNN already knows how to detect edges, shapes, and textures; you only need to teach it the specific categories that matter for your application.

8. The Fairness principle and bias in facial recognition datasets are directly tested on AI-900. Know that commercial face analysis systems have been shown to have higher error rates for darker-skinned and female individuals.

---

## Section 6: Required Reading

**Microsoft Learn — Analyze images with Azure AI Vision**
learn.microsoft.com/en-us/training/modules/analyze-images-computer-vision/

Covers Azure Computer Vision capabilities: tagging, objects, captions, Read API, and smart crops.

**Microsoft Learn — Classify images with Azure AI Custom Vision**
learn.microsoft.com/en-us/training/modules/classify-images-custom-vision/

Covers the Custom Vision training workflow for image classification with hands-on exercises.

**Microsoft Learn — Detect objects in images with Azure AI Custom Vision**
learn.microsoft.com/en-us/training/modules/detect-objects-images-custom-vision/

Covers object detection projects in Custom Vision including labeling and evaluation.

---

## Section 7: Study Checklist

- [ ] Write the definitions of image classification, object detection, segmentation, OCR, and face verification from memory.
- [ ] Study Table 1 until you can describe the output format of each computer vision task.
- [ ] Study Table 2 and match each Azure service to its correct use case.
- [ ] Explain why Azure Custom Vision works with small datasets, referencing transfer learning.
- [ ] Describe the responsible AI concern with face identification and explain Microsoft's response to it.
- [ ] Complete the Microsoft Learn module: Analyze images with Azure AI Vision.
- [ ] Complete the Microsoft Learn module: Classify images with Azure AI Custom Vision.
- [ ] Review all eight AI-900 exam tips in Section 5.
- [ ] Complete the Module 06 quiz.
- [ ] Complete the Module 06 lab.
- [ ] Post initial discussion by Wednesday 11:59 PM and respond to two peers by Sunday 11:59 PM.

## 9. Supplemental Resources

**1. Papers with Code — Image Classification Benchmarks**
<https://paperswithcode.com/task/image-classification>
A real-time leaderboard tracking the state-of-the-art on major computer vision benchmarks (ImageNet, CIFAR-10, etc.) with links to papers and code. Provides context for understanding where Azure Computer Vision and Custom Vision sit relative to cutting-edge research models.

**2. OpenCV University — Free Computer Vision Course**
<https://opencv.org/university/>
Free introductory courses from the team behind the OpenCV library covering image processing fundamentals, object detection, and face recognition. Provides practical background for the Python-based lab exercises throughout this course.

**3. MIT OpenCourseWare — 6.869: Advances in Computer Vision (lecture notes)**
<https://ocw.mit.edu/courses/6-869-advances-in-computer-vision-spring-2022/>
Freely available lecture notes and slides from MIT's advanced computer vision course. Covers CNNs, segmentation, detection, and generative models at a rigorous level — useful for students who want to understand the underlying techniques that power Azure Computer Vision.
