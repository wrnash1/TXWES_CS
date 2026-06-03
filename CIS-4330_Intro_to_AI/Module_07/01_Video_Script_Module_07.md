# Video Script: Module 07 — Computer Vision with Azure

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Microsoft Azure AI Fundamentals (AI-900)

---

## INTRO SEGMENT (0:00 – 1:30)

Welcome back to CIS-4330. I'm Professor Nash, and today we are diving into one of the most visually compelling areas of artificial intelligence: computer vision.

By the end of this module you will be able to explain what computer vision is, describe the Azure services that enable it, demonstrate key capabilities including image classification, object detection, OCR, and facial analysis, and discuss responsible use considerations — all of which map directly to AI-900 exam objectives.

Let's start with a question: how does a machine "see"?

---

## SECTION 1: What Is Computer Vision? (1:30 – 4:00)

Human vision seems effortless. You glance at a photo and instantly know there is a dog, a park bench, afternoon sunlight. But teaching a machine to do that requires mathematics, data, and a lot of training examples.

Computer vision is the branch of AI that trains models to interpret and understand visual information from the world — images, video frames, documents, and live camera feeds.

At a high level, computer vision works in three steps.

**Step one: Image input.** The system receives pixel data — a grid of numbers representing color channels, usually red, green, and blue.

**Step two: Feature extraction.** A deep learning model, typically a convolutional neural network (CNN), scans the image in overlapping windows, detecting edges, textures, shapes, and patterns at increasing levels of abstraction.

**Step three: Prediction.** The model outputs a label, a bounding box, extracted text, or some structured insight depending on the task.

The key insight is that none of this requires hand-crafted rules. The model learns features automatically from thousands or millions of labeled training images.

Modern computer vision is powered almost entirely by deep learning. Earlier techniques relied on hand-engineered features like SIFT or HOG descriptors. Today, CNNs and vision transformers learn features directly from data, which is why performance has improved so dramatically over the past decade.

---

## SECTION 2: Azure Computer Vision API (4:00 – 7:30)

Microsoft packages computer vision capabilities into managed cloud services so you do not need to build or train models from scratch.

**[SHOW DEMO]** Open the Azure portal at portal.azure.com. Navigate to Create a Resource, search for "Computer Vision," and show the resource creation blade. Point out the Pricing Tier options: Free F0 allows 20 calls per minute. Standard S1 charges per 1,000 transactions.

The Azure Computer Vision API — now unified under the brand Azure AI Vision — exposes pre-built models through a simple REST interface. You send an HTTP POST request with an image URL or binary image data, and the service returns structured JSON.

The core capabilities are as follows.

**Image analysis.** The service returns tags with confidence scores, a dense caption describing the image in natural language, dominant colors, detected objects with bounding boxes, and content categories aligned to a taxonomy.

**Optical Character Recognition.** The service reads printed and handwritten text in images and documents, returning text content with bounding polygon coordinates.

**Spatial analysis.** Using video feeds, the service can count people in defined zones, detect when people cross virtual lines, and monitor occupancy — primarily in retail and workplace safety scenarios.

**Dense captions.** This feature generates multiple descriptive captions for different regions of an image, not just a single overall caption.

**[SHOW DEMO]** Navigate to Vision Studio at vision.cognitive.azure.com. Select "Image analysis." Upload a sample photo of a city street. Show the JSON response panel. Walk through the response structure:

```json
{
  "tags": [
    { "name": "outdoor", "confidence": 0.998 },
    { "name": "building", "confidence": 0.991 }
  ],
  "objects": [
    { "object": "car", "confidence": 0.87,
      "rectangle": { "x": 120, "y": 200, "w": 180, "h": 95 } }
  ],
  "readResult": {
    "content": "STOP"
  }
}
```

The REST endpoint for image analysis follows this pattern:

```http
POST https://<your-endpoint>/computervision/imageanalysis:analyze
     ?api-version=2023-02-01-preview
     &features=tags,caption,objects,read
```

You pass your subscription key in the `Ocp-Apim-Subscription-Key` header. The image can be sent as a JSON body with a URL or as raw binary in the request body with content type `application/octet-stream`.

---

## SECTION 3: Image Classification (7:30 – 10:00)

Image classification answers a single question: what is in this image?

It assigns one or more labels from a fixed set of categories to the entire image. This is a classification problem — multi-class when exactly one label applies, or multi-label when several can apply simultaneously.

Pre-built models like those in the Computer Vision API are trained on millions of general images. But many real-world scenarios require domain-specific categories — for example, classifying types of manufacturing defects, identifying plant diseases, or categorizing insurance claim photos.

That is where **Azure Custom Vision** comes in. Custom Vision lets you build and train your own image classification model with as few as a few dozen images per class.

The workflow has four steps.

**Step one: Create a project.** At customvision.ai, choose Classification as the project type and select a domain. General domains work for most use cases; specialized domains like Food or Retail optimize for those contexts.

**Step two: Upload and tag images.** You upload training images and assign category labels. Azure recommends at least 50 images per tag for reliable training.

**Step three: Train.** Custom Vision trains a model on your data, typically in a few minutes using Quick Training or a longer compute-budgeted Advanced Training.

**Step four: Publish and consume.** You publish the trained iteration to a prediction endpoint and call it via REST, exactly like any other Azure cognitive service.

**[SHOW DEMO]** Navigate to customvision.ai. Show an existing project with tags "apple," "banana," and "orange." Click Train, then navigate to the Performance tab. Show the Precision, Recall, and Average Precision metrics for each tag.

Explain: Precision means of all images labeled as Apple, what fraction actually were apple? Recall means of all actual apple images, what fraction did the model correctly identify?

Classification output returns a JSON array:

```json
{
  "predictions": [
    { "tagName": "apple", "probability": 0.97 },
    { "tagName": "banana", "probability": 0.02 }
  ]
}
```

---

## SECTION 4: Object Detection (10:00 – 12:30)

Image classification tells you what is in an image. Object detection goes further — it tells you what is in the image AND where each object is located.

The output of object detection is a set of bounding boxes, each paired with a class label and a confidence score.

Bounding boxes are typically expressed as normalized coordinates: left, top, width, height — all values between 0 and 1 relative to image dimensions. This normalization means the coordinates work regardless of the original image resolution.

Azure supports object detection in two ways.

The **Computer Vision Analyze Image API** returns an `objects` array with bounding boxes and class labels for common objects recognized by the pre-built model.

**Azure Custom Vision** also supports a custom object detection project type. In this workflow you upload images and manually draw bounding boxes around each instance of each object class you want to detect — this process is called annotation or labeling. After training, the model can locate those objects in new images.

Real-world applications include the following scenarios.

In retail, shelf monitoring systems detect products and verify planogram compliance — is the right product in the right slot?

In transportation, traffic analysis systems count and classify vehicles at intersections.

In healthcare, object detection models locate anomalies in X-ray or pathology slide images.

In security, surveillance systems detect and track people or vehicles in camera feeds.

**[SHOW DEMO]** In Custom Vision, create or open an Object Detection project. Show the annotation interface where you draw bounding boxes with the mouse. Label a few boxes as "hard hat" and "no hard hat" for a safety scenario. Show the trained model's performance summary.

---

## SECTION 5: Optical Character Recognition (12:30 – 14:30)

Optical Character Recognition — OCR — is the process of extracting text from images and documents.

This capability covers an enormous range of practical scenarios: reading scanned documents, extracting data from receipts and invoices, parsing license plates, digitizing historical manuscripts, enabling search over image archives, and powering accessibility features for visually impaired users.

Azure offers two OCR paths, optimized for different scenarios.

The **Read API**, now part of Azure AI Document Intelligence, is optimized for dense text, multi-page documents, mixed print and handwriting, and complex layouts including tables and form fields. It is asynchronous — you submit a job, poll for completion, and retrieve results.

The **Image Analysis OCR** feature is built into the general Computer Vision service and handles simpler text extraction from natural scene images — signs, labels, product packaging. It returns results synchronously.

The Read API response is hierarchical: documents contain pages, pages contain lines, lines contain words, and each word has bounding polygon coordinates and a confidence score.

```json
{
  "pages": [
    {
      "lines": [
        {
          "content": "Invoice #1042",
          "boundingPolygon": [
            { "x": 50, "y": 100 },
            { "x": 250, "y": 100 },
            { "x": 250, "y": 125 },
            { "x": 50, "y": 125 }
          ]
        }
      ]
    }
  ]
}
```

**[SHOW DEMO]** In Vision Studio, select "Extract text from images." Upload an image of a printed receipt. Walk through the OCR output JSON and show how text content maps back to bounding polygons on the image overlay.

---

## SECTION 6: Face API (14:30 – 16:30)

The Azure Face API detects human faces in images and performs several types of analysis.

**Face detection** locates faces and returns bounding rectangles, plus optional attributes: estimated age, apparent emotion (happiness, sadness, surprise, and so on), head pose as Euler angles, the presence of glasses, hair color, and facial hair.

**Face verification** answers a binary question: are these two face images the same person? It returns a confidence score and a boolean result based on a configurable threshold.

**Face identification** compares a detected face against a trained group of known individuals — called a PersonGroup — and returns the closest match with a confidence score. This powers employee attendance systems, access control, and security applications.

**Liveness detection** determines whether the face in a video or image represents a real person present at the time of capture, or a spoof such as a printed photograph held in front of the camera or a deepfake video.

However, Microsoft has implemented strict responsible AI policies around Face API. As of June 2023, new customers must apply for access through the Limited Access program. General-purpose face identification and verification features are approved only for specific use cases: verifying identity for account creation, detecting liveness for financial transactions, and similar high-value, consent-based scenarios.

This is a direct example of AI governance in practice. We will return to this theme at the end of this module and more deeply in Module 11.

**[SHOW DEMO]** Show the Face API Quick Start in the Azure portal. Demonstrate a basic face detection call returning bounding box and attributes JSON. Point out the Limited Access notice in the documentation.

---

## SECTION 7: Azure Custom Vision — Advanced Topics (16:30 – 18:30)

Let's go deeper on Custom Vision because it is directly tested on AI-900.

Custom Vision is a managed AutoML service for images. You do not write model training code. You provide labeled images, click Train, and Azure handles feature extraction, model architecture selection, and hyperparameter tuning internally.

Two training options exist.

**Quick Training** uses a subset of your data and completes in minutes. This is suitable for rapid iteration and experimentation.

**Advanced Training** allows you to specify a compute budget in hours. Azure uses that budget to search for a better model configuration. This typically improves performance by 2 to 5 percentage points compared to Quick Training.

After training, Custom Vision provides performance metrics broken down by tag, including the full Precision-Recall curve and the Average Precision score.

You can export trained models in several formats for offline or edge deployment.

- TensorFlow for Android applications
- CoreML for iOS applications
- ONNX for Windows ML and cross-platform runtimes
- Docker containers for Linux edge devices and Kubernetes

This export capability is significant. It means your custom model can run on-device without an internet connection — critical for manufacturing shop floors with network restrictions, medical devices in clinical environments, or remote field applications.

The exported model is quantized and optimized for inference speed, so it runs efficiently even on devices without a dedicated GPU.

**[SHOW DEMO]** In Custom Vision, navigate to a published iteration. Click Export. Show the format selection dialog. Show the downloaded ONNX model file and describe its portability.

---

## SECTION 8: Responsible Use of Computer Vision (18:30 – 21:00)

Computer vision is powerful, and with that power comes responsibility.

Several risk areas deserve careful attention before deploying any computer vision system.

**Bias in training data.** If your training images do not represent the full diversity of people, environments, and conditions the model will encounter in production, the model will perform unevenly across subgroups. Documented examples include facial analysis systems with higher error rates on darker-skinned faces, and medical imaging models that underperform on images from equipment brands not represented in training.

**Privacy.** Capturing and analyzing images of people — especially in public spaces without consent — raises serious privacy concerns. Multiple jurisdictions have enacted or are developing regulations that restrict automated facial recognition.

**Misidentification consequences.** In high-stakes scenarios like law enforcement, a false positive identification can result in wrongful arrest or serious harm to an innocent person. The stakes are asymmetric: the cost of a mistake is borne entirely by the misidentified individual.

**Surveillance misuse.** Spatial analysis capabilities — counting people, tracking movement through zones — can be misused for discriminatory monitoring of employees or targeted communities.

Microsoft's Responsible AI guidelines for Computer Vision recommend the following practices.

First, conduct a human rights impact assessment before deployment. Second, involve affected communities in the design and testing process. Third, apply the principle of minimum necessary data — do not collect more visual data than the task requires. Fourth, ensure meaningful human oversight for consequential decisions. Fifth, be transparent with people when AI vision systems are in use.

The Face API Limited Access policy is a direct implementation of these principles. Microsoft determined that identification at scale is too high risk for unrestricted commercial access.

For the AI-900 exam, you should be able to explain why these guardrails exist and what categories of harm they prevent.

---

## SECTION 9: AI-900 Exam Alignment and Recap (21:00 – 23:30)

Let's connect everything we have covered to AI-900 exam objectives.

The exam tests your ability to identify appropriate use cases for each Computer Vision service, distinguish between classification (what) and object detection (what and where), describe OCR capabilities and the difference between the Read API and Image Analysis, explain Face API capabilities alongside its access restrictions, and describe Custom Vision's training workflow and export options.

Key terms and their definitions for the exam:

- **Azure AI Vision** — the unified brand for Computer Vision API services in Azure
- **Custom Vision** — trainable service for domain-specific image classification and object detection
- **Face API** — detection, verification, identification, and liveness; subject to Limited Access policy
- **Read API** — OCR optimized for dense text and multi-page documents
- **Bounding box** — rectangle coordinates that locate an object within an image
- **Confidence score** — the model's estimated probability that a prediction is correct
- **Precision** — of all positive predictions, the fraction that are truly positive
- **Recall** — of all actual positives, the fraction the model correctly identified
- **Limited Access** — Microsoft's governance framework requiring application approval for sensitive AI features
- **ONNX** — open format for exporting trained models for cross-platform deployment

For the exam, remember this key distinction: use Custom Vision when you need a model trained on your own domain-specific categories. Use the standard Computer Vision API when you need general-purpose pre-built capabilities without additional training.

---

## OUTRO (23:30 – 24:00)

In the lab this week you will provision an Azure Computer Vision resource, call the Analyze Image endpoint with real images, and build a simple Custom Vision classifier. The quiz covers the key terms and concepts from this lecture.

Next week we move into natural language processing — teaching machines to read and understand text. I will see you in Module 8.

---

*Script ends. Total estimated delivery time: 22 minutes with demos.*
