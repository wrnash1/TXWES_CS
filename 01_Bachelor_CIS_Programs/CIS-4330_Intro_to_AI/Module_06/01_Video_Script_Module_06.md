# Video Script: Module 06 - Computer Vision and Image Recognition

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AI-900 Domain:** Describe features of Computer Vision workloads on Azure (15-20%)

---

## [00:00 - 01:30] Opening

Welcome back. Professor Nash here, and this is Module 06. In the last module we covered NLP — how machines understand language. Today we turn to a different kind of perception: computer vision, specifically how machines understand images and video. Computer vision is one of the most mature and commercially deployed areas of AI, and the AI-900 exam dedicates a full domain to it. Let us get started.

---

## [01:30 - 05:00] What Is Computer Vision?

Computer vision is the field of AI that enables machines to interpret and understand visual information from the world — photographs, video, medical scans, satellite imagery, and more. The human visual system makes this look effortless, but teaching machines to interpret visual scenes requires solving fundamentally hard problems.

Consider a photograph of a crowded city street. A person looking at the photo can immediately identify: dozens of individual people (person detection), the cars and buses on the road (object detection), the stop signs and traffic lights (object recognition), the words on a storefront (text recognition, also called OCR), the approximate age and emotional state of the people visible (face analysis), and the general scene context of an urban intersection (scene classification).

Each of these is a distinct computer vision task, and Azure provides prebuilt capabilities for all of them through Azure Computer Vision.

The breakthrough enabling modern computer vision was the convolutional neural network, or CNN, combined with large labeled image datasets. AlexNet's victory in the 2012 ImageNet competition — dramatically outperforming all traditional computer vision methods — marked the beginning of the deep learning era in computer vision. Today, CNNs trained on millions of labeled images can recognize thousands of object categories with accuracy exceeding human performance on standardized benchmarks.

---

## [05:00 - 09:00] Core Computer Vision Tasks

[SHOW DIAGRAM: Six panels showing different computer vision task types. Panel 1: a dog labeled "Image Classification." Panel 2: same dog with a bounding box labeled "Object Detection." Panel 3: dog with pixel-level mask labeled "Image Segmentation." Panel 4: document with highlighted text "OCR / Text Extraction." Panel 5: face with emotion overlay "Face Analysis." Panel 6: video frames with motion arrows "Video Analysis."]

Let me walk through the six core computer vision tasks you need to know for AI-900.

**Image Classification** is the simplest task: given an image, assign it a single label. Is this image a cat or a dog? Is this chest X-ray normal or abnormal? The model outputs a label (or set of labels) for the entire image.

**Object Detection** goes further: it identifies and locates all instances of specific object categories within an image. The output is a set of bounding boxes — rectangles drawn around each detected object — along with the object's class label and a confidence score. An autonomous vehicle system uses object detection to locate all pedestrians, vehicles, and traffic signs in each camera frame.

**Image Segmentation** is the most detailed spatial task. Instead of bounding boxes, segmentation assigns a label to every individual pixel in the image. Semantic segmentation assigns each pixel to a category: road, sky, car, pedestrian. Instance segmentation goes further, distinguishing individual instances of the same category. Medical imaging systems use segmentation to precisely delineate tumor boundaries.

**Optical Character Recognition (OCR)** detects and extracts text from images. Azure Computer Vision's Read API can extract printed and handwritten text from photographs, scanned documents, and PDFs, including text in complex layouts.

**Face Analysis** detects human faces in images and extracts attributes: estimated age, detected emotion, whether glasses are present, and face landmarks (key points like eye corners and mouth edges). Face verification determines if two face images show the same person.

**Video Analysis** extends these capabilities to video streams. This includes motion detection, activity recognition (identifying what people are doing), and tracking objects across frames over time.

---

## [09:00 - 12:30] How CNNs Process Images

[SHOW DIAGRAM: A CNN pipeline. Input image on the left. A series of "Convolutional Layer + ReLU" blocks extract feature maps. A "Pooling Layer" reduces spatial dimensions. After several conv-pool pairs, a "Flatten" layer converts to a 1D vector. "Fully Connected Layers" produce class scores. Softmax outputs class probabilities.]

Let me explain conceptually how a convolutional neural network processes an image. You do not need to implement this for AI-900, but understanding the architecture helps you reason about when computer vision is appropriate and why it works.

An image is a three-dimensional grid of numbers: width x height x color channels (3 channels for RGB images). A 224x224 pixel RGB image is represented as a tensor with 224 x 224 x 3 = 150,528 numbers.

A convolutional layer applies a set of learnable filters — small grids of weights — that slide across the image. Each filter detects a specific local pattern: a vertical edge, a horizontal edge, a color gradient, a texture. The output of applying all filters to an image is a set of feature maps — one feature map per filter — where each value represents how strongly that filter's pattern appears at that location.

After each convolutional layer, a pooling layer reduces spatial dimensions by taking the maximum or average value in each small region. This makes the representation more compact and gives the network translational robustness — the ability to recognize a pattern regardless of exactly where it appears in the image.

Deep CNNs stack many convolutional and pooling layers. Early layers detect low-level features: edges and corners. Middle layers detect mid-level features: shapes and textures. Final layers detect high-level features: faces, cars, dogs. This hierarchical feature learning is what makes CNNs so powerful for visual recognition.

---

## [12:30 - 15:30] Azure Computer Vision Services

[SHOW DIAGRAM: Table of Azure Computer Vision services with columns: Service Name, Primary Capability, Training Required, Best Use Case.]

Microsoft Azure provides several computer vision services under the Cognitive Services umbrella. Let me walk through the most important ones for AI-900.

**Azure Computer Vision** is the flagship prebuilt image analysis service. Send it an image URL or byte stream and receive back: object tags with confidence scores, detected objects with bounding boxes, extracted text via the Read API, image descriptions in natural language, color scheme analysis, and content moderation flags (adult content, violence, etc.). No custom training required.

**Azure Custom Vision** extends Azure Computer Vision with your own training data. You upload labeled images, train a custom image classifier or object detector, and deploy the model as an endpoint. You need as few as 15 images per class for a basic classifier, thanks to transfer learning. Custom Vision is the answer when the standard Computer Vision service does not recognize your domain-specific objects — for example, classifying specific plant diseases or industrial defect types.

**Azure Face API** provides face detection, verification, and identification. Important AI-900 fact: Microsoft has limited access to certain Face API capabilities — specifically the ability to identify a specific individual by name from images — due to responsible AI concerns about privacy and mass surveillance. This is one of the most direct responsible AI examples in Azure's service portfolio.

**Azure Form Recognizer** (now part of Azure AI Document Intelligence) extracts structured data from documents, forms, receipts, and invoices — essentially intelligent OCR that understands document layouts and field labels, not just raw text.

---

## [15:30 - 18:30] Azure Custom Vision Walkthrough

Custom Vision is the service you will interact with most directly in computer vision labs. Let me walk through the workflow.

Step one: create a Custom Vision project. Specify the project type (classification or object detection) and the domain (general, food, retail, medical, etc.). Choosing a domain-specific model provides better transfer learning initialization.

Step two: upload and label images. For classification, upload images of each class and tag them. For object detection, upload images and draw bounding boxes around each instance of each object.

Step three: train the model. Click "Train" and Azure runs a transfer learning training job. Even with a few dozen images per class, Custom Vision can produce a useful model because it starts from a powerful pretrained CNN.

Step four: evaluate performance. Azure Custom Vision reports precision and recall per class on a held-out test set. The Quick Training option uses a fast but less accurate model; Advanced Training uses a slower but more accurate approach.

Step five: publish and call the endpoint. Once published, your model is available at a REST endpoint. You send an image and receive class labels or bounding boxes with confidence scores.

---

## [18:30 - 20:30] Responsible AI in Computer Vision

Computer vision raises serious responsible AI concerns. The AI-900 exam addresses several of them.

Face recognition and privacy: systems that identify individuals by face in public spaces can enable mass surveillance and have been misused by authoritarian governments. Microsoft has publicly committed not to sell real-time facial recognition systems to law enforcement in certain contexts, and has restricted the Face API's identification capabilities to vetted customers.

Bias in training data: if a training dataset over-represents certain demographic groups, the model may perform significantly worse on underrepresented groups. Studies have shown commercial face recognition systems have higher error rates for darker-skinned and female faces, reflecting imbalances in training data. The Microsoft responsible AI principle of Fairness directly applies.

Content safety: computer vision deployed for content moderation must accurately flag harmful content without censoring legitimate content. False positives (flagging safe content) and false negatives (missing harmful content) both have real consequences.

---

## [20:30 - 22:30] Module Summary and Lab Preview

Let me recap Module 06.

Computer vision enables machines to interpret visual information. Core tasks include image classification, object detection, image segmentation, OCR, face analysis, and video analysis. CNNs are the foundational architecture, learning hierarchical features from pixels.

Azure Computer Vision provides prebuilt image analysis with no training required. Azure Custom Vision enables custom image classification and object detection through transfer learning. Azure Face API provides face detection and verification with responsible AI-guided access restrictions. Azure Form Recognizer handles intelligent document extraction.

Responsible AI in computer vision centers on facial recognition privacy, bias in training data, and content safety.

This week's lab explores image analysis by interpreting sample API output, matching computer vision tasks to scenarios, and evaluating the responsible AI implications of a face recognition deployment scenario.

See you in Module 07, where we do a deep dive into all Azure Cognitive Services for vision, speech, and language.

---

## References

- Microsoft Learn — Analyze images with Azure AI Vision: learn.microsoft.com/en-us/training/modules/analyze-images-computer-vision/
- Microsoft Learn — Classify images with Azure AI Custom Vision: learn.microsoft.com/en-us/training/modules/classify-images-custom-vision/
- Microsoft Learn — Detect objects in images with Azure AI Custom Vision: learn.microsoft.com/en-us/training/modules/detect-objects-images-custom-vision/
