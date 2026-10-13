# Reading Guide: Module 07 — Computer Vision with Azure

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4330 &BULL; INTRODUCTION TO ARTIFICIAL INTELLIGENCE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Domain: Describe features of computer vision workloads on Azure

---

## Overview

This reading guide consolidates key concepts, service comparisons, and exam preparation material for Module 07. Work through each section after watching the video lecture and before attempting the quiz. Estimated reading time: 45–60 minutes.

---

## Section 1: Computer Vision Fundamentals

### How Machines Process Images

Digital images are stored as arrays of pixel values. A standard color image is a three-dimensional array with dimensions height × width × 3 (red, green, blue channels). Each channel value typically ranges from 0 to 255.

A convolutional neural network (CNN) processes an image by sliding small filter kernels across the pixel grid. Each kernel learns to detect a specific pattern — an edge at a particular angle, a color gradient, a texture. Deeper layers combine these primitive detections into increasingly abstract concepts: corners become shapes, shapes become objects.

This hierarchical feature learning is what makes CNNs so effective for vision tasks. Unlike traditional image processing that requires manually designed filters, CNNs learn which filters are useful directly from labeled training data.

### Core Vision Task Types

| Task | Question Answered | Output |
|------|------------------|--------|
| Image Classification | What category is the whole image? | Class label + confidence score |
| Object Detection | What objects are present and where? | Bounding boxes + labels + scores |
| Image Segmentation | Which pixels belong to each object? | Per-pixel class map |
| OCR | What text is in the image? | Transcribed text + positions |
| Facial Analysis | Are there faces? Who are they? | Face rectangles + attributes |

---

## Section 2: Azure AI Vision Services — Capability Matrix

### Service Overview

| Service | Best For | Training Required | Access Policy |
|---------|----------|------------------|---------------|
| Azure AI Vision (Analyze Image) | General-purpose image analysis, tags, captions, objects | No (pre-built) | Public |
| Azure AI Vision (Read API) | OCR on documents, mixed print/handwriting | No (pre-built) | Public |
| Azure Custom Vision — Classification | Domain-specific image categories | Yes (your data) | Public |
| Azure Custom Vision — Object Detection | Locating custom objects in images | Yes (your labeled data) | Public |
| Azure Face API | Face detection, verification, identification, liveness | Optional (PersonGroups) | Limited Access |
| Azure AI Document Intelligence | Form extraction, invoices, receipts, structured docs | Optional (custom models) | Public |

### What Azure AI Vision Analyze Image Returns

| Feature | Description |
|---------|-------------|
| Tags | Objects, scenes, concepts with confidence scores |
| Caption | Natural-language sentence describing the image |
| Dense Captions | Multiple region-level captions |
| Objects | Detected objects with bounding rectangles |
| Read | Extracted text with bounding polygons |
| Smart Crops | Suggested crop coordinates for different aspect ratios |
| People | Detected persons with bounding boxes (no identification) |

---

## Section 3: Azure Custom Vision — Training Deep Dive

### Project Types

Custom Vision supports two project types. Classification assigns a category label to the whole image. Object Detection locates individual instances of objects within the image.

Both project types share the same portal workflow but differ in how you label data and in the output format of predictions.

### Classification Output Formats

Two output formats apply to Custom Vision Classification projects.

**Multiclass** (Single label): Exactly one tag applies to each image. The model returns all tag probabilities that sum to 1.0.

**Multilabel**: Multiple tags can apply to one image. The model returns independent probabilities for each tag, not summing to 1.0.

### Recommended Minimum Images per Tag

| Scenario | Minimum Images per Tag | Recommended |
|----------|----------------------|-------------|
| Quick prototype | 15 | 30 |
| Production model | 50 | 100+ |
| High-confidence production | 100 | 200+ |

More diverse images — different lighting, angles, backgrounds — improve generalization more than simply duplicating similar images.

### Performance Metrics

| Metric | Definition | Ideal Value |
|--------|-----------|-------------|
| Precision | True positives ÷ (true positives + false positives) | High (close to 1.0) |
| Recall | True positives ÷ (true positives + false negatives) | High (close to 1.0) |
| Average Precision (AP) | Area under the Precision-Recall curve | High (close to 1.0) |

There is a trade-off between precision and recall controlled by the probability threshold. Raising the threshold increases precision (fewer false positives) but decreases recall (more false negatives).

### Export Formats for Edge Deployment

| Format | Target Platform |
|--------|----------------|
| TensorFlow (SavedModel) | Android, general ML pipelines |
| CoreML | iOS and macOS applications |
| ONNX | Windows ML, .NET ONNX Runtime, cross-platform |
| Docker (TensorFlow) | Linux containers, Kubernetes edge nodes |
| VAIDK | Vision AI Dev Kit hardware |

---

## Section 4: OCR — Read API vs. Image Analysis

### Choosing the Right OCR Path

| Scenario | Recommended Service |
|----------|-------------------|
| Multi-page scanned PDF | Read API (Document Intelligence) |
| Handwritten notes | Read API |
| Photo of a street sign | Image Analysis (OCR feature) |
| Invoice with tables and line items | Document Intelligence (Invoice model) |
| Single-line text label on a product | Image Analysis (OCR feature) |

### Read API Response Hierarchy

The Read API returns a structured hierarchy:

```text
AnalyzeResult
└── pages[]
    ├── width, height, angle
    └── lines[]
        ├── content (full line text)
        ├── boundingPolygon (4 or more x,y points)
        └── words[]
            ├── content (single word)
            ├── boundingPolygon
            └── confidence (0.0 – 1.0)
```

### Supported Languages and Scripts

The Read API supports over 150 printed languages and 9 handwritten languages, including Latin script, Chinese (Simplified and Traditional), Japanese, Korean, Arabic, Hindi, and others.

---

## Section 5: Face API — Capabilities and Restrictions

### Capability Summary

| Capability | Description | Access |
|-----------|-------------|--------|
| Face Detection | Locate faces; return bounding rect + attributes | Public |
| Attribute Analysis | Age estimate, emotion, glasses, head pose, hair | Public |
| Face Verification | Compare two faces for same-person determination | Limited Access |
| Face Identification | Match face to PersonGroup | Limited Access |
| Similar Face Search | Find similar faces in a FaceList | Limited Access |
| Liveness Detection | Determine if face is real/present | Limited Access |

### Limited Access Policy

Microsoft requires an application for access to identification and verification features. Approved use cases include:

- Account creation identity verification (matching selfie to ID document)
- Liveness detection for financial services authentication
- Access control for employees with explicit consent
- Accessibility features (for example, describing a room to a visually impaired user)

Use cases that are generally NOT approved include law enforcement, public surveillance without consent, and tracking individuals across public spaces.

### Responsible AI Considerations for Facial Analysis

Several documented risks apply to facial analysis systems.

**Demographic bias**: Error rates vary across demographic groups. Systems trained on non-representative datasets show systematically higher error rates for women, darker-skinned individuals, and older and younger age groups.

**Consent and notice**: People should know when their face is being analyzed. Covert surveillance raises ethical and legal concerns.

**Consequential decision making**: Decisions affecting liberty, employment, or housing should never rely solely on automated facial analysis.

---

## Section 6: Service Comparison Tables for AI-900

### When to Use Each Vision Service

| Use Case | Service to Use |
|----------|---------------|
| Add tags and captions to product images automatically | Azure AI Vision — Analyze Image |
| Extract invoice data from scanned PDFs | Azure AI Document Intelligence |
| Classify industrial defect photos into custom categories | Azure Custom Vision — Classification |
| Count cars in a parking lot from live video | Azure AI Vision — Spatial Analysis |
| Detect whether a login selfie matches an ID photo | Face API (Limited Access) |
| Find and locate custom objects in drone footage | Azure Custom Vision — Object Detection |
| Read text from a photo of a whiteboard | Azure AI Vision — Image Analysis (OCR) |

### Pricing Model (Reference Tiers)

| Service | Free Tier | Standard Tier (approx.) |
|---------|-----------|------------------------|
| Azure AI Vision | 5,000 transactions/month | $1.00 per 1,000 transactions |
| Custom Vision Training | 1 hour/month | $10 per compute hour |
| Custom Vision Prediction | 10,000 transactions/month | $2.00 per 1,000 transactions |
| Face API Detection | 30,000 transactions/month | $1.00 per 1,000 transactions |

*Pricing is approximate and subject to change. Always verify current pricing at azure.microsoft.com/pricing.*

---

## Section 7: AI-900 Exam Tips

### High-Frequency Exam Topics

The following topics appear frequently in AI-900 questions related to computer vision.

**Topic 1 — Service selection.** Exam questions present a scenario and ask which Azure service is most appropriate. The key distinction is pre-built versus custom: use Custom Vision when you have domain-specific categories; use Azure AI Vision for general-purpose analysis.

**Topic 2 — Classification vs. object detection.** Classification labels the whole image. Object detection returns bounding boxes for individual instances. Know this distinction precisely.

**Topic 3 — Read API use cases.** Multi-page documents and handwriting route to the Read API. Simple scene text routes to Image Analysis.

**Topic 4 — Face API access.** AI-900 tests whether you understand that identification features require Limited Access approval. General face detection (bounding box, attributes) is public.

**Topic 5 — Custom Vision export.** Know the export formats: TensorFlow, CoreML, ONNX, Docker. Know that export enables offline/edge deployment.

**Topic 6 — Responsible AI.** Be able to explain why bias in training data is a risk, why consent matters for facial analysis, and what Microsoft's Limited Access policy is designed to prevent.

### Common Distractors

Watch out for these traps in exam questions.

- "Use Custom Vision for OCR" is wrong. Custom Vision is for image classification and object detection, not text extraction.
- "Face API can identify anyone in a public photo" is wrong. Identification requires a trained PersonGroup and Limited Access approval.
- "Confidence score of 1.0 means the model is always correct" is wrong. Confidence is the model's estimated probability, not ground truth.

---

## Section 8: Key Term Glossary

| Term | Definition |
|------|-----------|
| Convolutional Neural Network (CNN) | Deep learning architecture that applies learned filters to detect visual features |
| Bounding box | Rectangle (left, top, width, height) locating an object in an image |
| Confidence score | Model's estimated probability that a prediction is correct (0.0–1.0) |
| Precision | Of all positive predictions, the fraction that are truly positive |
| Recall | Of all actual positives, the fraction the model correctly identified |
| Average Precision (AP) | Area under the Precision-Recall curve; overall model quality metric |
| PersonGroup | Named set of known individuals used for Face API identification |
| Limited Access | Microsoft governance program requiring application approval for sensitive AI features |
| ONNX | Open Neural Network Exchange; portable model format for cross-platform deployment |
| Spatial analysis | Computer vision capability that analyzes movement and presence in physical spaces |
| Liveness detection | Determining whether a face image represents a real person present at capture time |
| Annotation | Process of labeling training images with bounding boxes or category tags |

---

## Section 9: Study Checklist

Work through this checklist before taking the quiz.

- [ ] I can name the five core tasks in computer vision (classification, detection, segmentation, OCR, facial analysis)
- [ ] I can describe the difference between image classification and object detection
- [ ] I know what Azure AI Vision returns in its Analyze Image response (tags, caption, objects, read)
- [ ] I can explain when to use Custom Vision vs. Azure AI Vision
- [ ] I know the Custom Vision training workflow: create project → upload + tag → train → publish
- [ ] I understand Precision and Recall and know how the probability threshold affects the trade-off
- [ ] I can list at least three Custom Vision export formats
- [ ] I can describe what the Read API returns and when to use it vs. Image Analysis OCR
- [ ] I can list Face API capabilities and explain which require Limited Access
- [ ] I can explain at least two responsible AI concerns specific to computer vision
- [ ] I know why Microsoft restricts general-purpose facial identification
- [ ] I can select the correct Azure service for a given computer vision scenario

---

## Section 10: Recommended Practice

### Microsoft Learn Modules (Free)

Work through these modules on Microsoft Learn before the lab:

1. **Analyze images with Azure AI Vision** — hands-on with the Analyze Image API
2. **Classify images with Azure AI Custom Vision** — full Custom Vision classification workflow
3. **Detect objects in images with Azure AI Custom Vision** — object detection annotation and training
4. **Detect and analyze faces with Azure AI Face** — Face detection and attribute analysis
5. **Read text with Azure AI Vision** — OCR using the Read API

Search for each title at learn.microsoft.com. All modules are free and include sandboxed Azure environments.

### Self-Test Questions

Before taking the graded quiz, answer these practice questions on paper or in your notes.

1. A company wants to automatically tag product photos with relevant keywords. Which service is most appropriate?

2. A quality control system needs to locate and count specific types of defects in manufacturing photos. The defect types are proprietary and not in any pre-built model. Which service and project type should be used?

3. An application needs to extract line items from scanned invoices that include tables. Which Azure service is best?

4. A developer wants to verify that a customer's selfie matches their profile photo. Which Face API capability is needed? What access level is required?

5. A Custom Vision model achieves 0.95 precision and 0.72 recall. What does this mean in plain language, and how might you adjust the probability threshold?

---

## 11. Supplemental Resources

**1. Microsoft Azure — Computer Vision Documentation (official)**
<https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/>
The complete official documentation for Azure AI Vision, Custom Vision, Face API, and Document Intelligence. Includes quickstarts, API references, and best practice guides directly relevant to the Module 07 lab exercises.

**2. Roboflow — How to Annotate Images for Computer Vision (free guide)**
<https://blog.roboflow.com/tips-for-how-to-label-images/>
A practical guide to image annotation best practices — bounding box drawing, labeling consistency, and managing annotation quality. Directly useful for the Custom Vision object detection portions of the lab where annotation quality drives model performance.

**3. GitHub — Microsoft Responsible AI Transparency Reports**
<https://github.com/microsoft/responsible-ai-toolbox>
Microsoft's open-source Responsible AI Toolbox repository, which provides tools for model interpretability, fairness assessment, and error analysis for computer vision and other AI models. Relevant to the Module 07 discussion of bias in visual recognition systems.

---

End of Reading Guide — Module 07
