# Quiz: Module 06 - Computer Vision and Image Recognition

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe features of Computer Vision workloads on Azure
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A retail company wants to automatically identify all products visible in shelf photographs and determine the location of each product on the shelf. Which computer vision task is most appropriate?

- A) Image Classification
- B) Object Detection
- C) Image Segmentation
- D) Face Detection

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Object detection identifies and locates multiple instances of objects in an image by providing bounding boxes with class labels and confidence scores. Knowing both what is on the shelf and where it is located requires object detection.
- *Why A is incorrect:* Image classification assigns one label to the entire image. It would say "this image contains products" but would not identify each product's type or location.
- *Why C is incorrect:* Segmentation provides pixel-level labels — precise for shape outlines but overkill for shelf analysis. Object detection bounding boxes are sufficient for product location.
- *Why D is incorrect:* Face detection is specifically for human faces. It does not detect retail products.

---

## Question 2

An organization wants to add image analysis to its application but has no machine learning expertise and no custom training data. The application needs to identify common objects, generate image captions, and extract tags from user-uploaded photos. Which Azure service is most appropriate?

- A) Azure Custom Vision
- B) Azure Face API
- C) Azure Computer Vision
- D) Azure Form Recognizer

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Computer Vision is a prebuilt service requiring no custom training. It provides tagging, object detection, image captioning, and more via REST API.
- *Why A is incorrect:* Azure Custom Vision requires users to upload and label training images. The scenario explicitly states no training data is available.
- *Why B is incorrect:* Azure Face API is specifically for detecting and analyzing human faces. It does not identify general objects or generate scene captions.
- *Why D is incorrect:* Azure Form Recognizer (Document Intelligence) extracts structured data from forms and documents. It is not designed for general image tagging or captioning.

---

## Question 3

A food safety company wants to train a model to classify aerial photographs of agricultural fields as one of five crop disease categories specific to their client base. Standard image recognition services do not include these disease categories. Which Azure service should they use?

- A) Azure Computer Vision with no training
- B) Azure Custom Vision with labeled training images
- C) Azure Face API with domain adaptation
- D) Azure Form Recognizer with custom model training

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Custom Vision enables custom image classification training using the customer's own labeled images. Transfer learning means only 15+ images per class are needed to start. Domain-specific categories require custom training.
- *Why A is incorrect:* Prebuilt Azure Computer Vision does not recognize domain-specific agricultural disease categories that are not in its training data.
- *Why C is incorrect:* Azure Face API is for human face analysis. Domain adaptation is not a feature of this service for general image classification.
- *Why D is incorrect:* Azure Form Recognizer processes structured documents and forms. It does not perform general image classification.

---

## Question 4

What is the primary architectural reason that convolutional neural networks (CNNs) are more effective for image recognition than standard feedforward neural networks?

- A) CNNs use sigmoid activation in all hidden layers, which is more effective for pixel data.
- B) CNNs apply learned filters that detect local spatial patterns, preserving spatial relationships and reducing the number of parameters compared to fully connected layers.
- C) CNNs process images in grayscale only, which reduces computational complexity.
- D) CNNs are trained using unsupervised learning, allowing them to learn from unlabeled images.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Convolutional layers use weight sharing — the same filter is applied across the entire image. This dramatically reduces parameters compared to fully connected layers (which would need a separate weight for every pixel-to-neuron connection) and explicitly models local spatial structure.
- *Why A is incorrect:* Modern CNNs use ReLU in hidden layers, not sigmoid. Sigmoid causes vanishing gradients in deep networks.
- *Why C is incorrect:* CNNs process full-color RGB images (3 channels) and can handle any number of input channels.
- *Why D is incorrect:* CNNs for image classification are trained with supervised learning on labeled image datasets.

---

## Question 5

A hospital wants to build a system that extracts specific text fields — patient name, diagnosis code, admission date, and prescribing physician — from scanned paper medical forms. Which Azure service is best suited for this task?

- A) Azure Computer Vision (image tagging)
- B) Azure Custom Vision (image classification)
- C) Azure Form Recognizer (Document Intelligence)
- D) Azure Face API (attribute extraction)

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Form Recognizer is designed specifically for extracting structured field data from documents, forms, receipts, and invoices — including recognizing field labels and matching them to their values. This goes beyond raw OCR to understand document structure.
- *Why A is incorrect:* Azure Computer Vision's Read API extracts raw text from images but does not understand form structure or map values to named fields.
- *Why B is incorrect:* Custom Vision performs image classification or object detection. It cannot extract structured text fields from document images.
- *Why D is incorrect:* Azure Face API is for detecting and analyzing human faces. It does not process document text.

---

## Question 6

Microsoft has restricted access to face identification capabilities in Azure Face API. Which responsible AI principle most directly explains this policy decision?

- A) Reliability and Safety — face identification causes hardware failures
- B) Inclusiveness — face identification only works for certain demographics
- C) Fairness and Privacy — face identification enables mass surveillance with potential for discriminatory outcomes
- D) Transparency — face identification models cannot be explained to end users

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Microsoft restricted face identification specifically because 1:N identification of individuals in public spaces enables mass surveillance, violates privacy expectations, and has demonstrated bias against certain demographic groups. Both Privacy/Security and Fairness principles drove this decision.
- *Why A is incorrect:* Face identification does not cause hardware failures. Reliability and Safety addresses system errors, not surveillance risk.
- *Why B is incorrect:* While demographic bias is a concern, Inclusiveness focuses on making AI accessible to all people — it is not the primary principle cited for restricting surveillance capability.
- *Why D is incorrect:* Transparency addresses explainability. While face identification is not easily explained, the restriction is driven by surveillance and bias risks, not explainability.

---

## Question 7

Azure Computer Vision returns confidence scores for each detected tag. A developer receives a tag "bicycle" with confidence 0.43. What does this score indicate about the detection?

- A) The model is 43% confident the object is a bicycle; the remaining 57% confidence is distributed across other possible tags.
- B) The bicycle tag should be automatically discarded because scores below 0.5 are always incorrect.
- C) The image contains exactly 0.43 bicycles.
- D) The bicycle was detected in the top-left 43% of the image.

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Confidence scores represent the model's probability estimate for that specific tag. A score of 0.43 means the model has moderate uncertainty — it is possible a bicycle is present but the model is not highly confident. Developers typically set a minimum threshold (0.5-0.9) and filter below it.
- *Why B is incorrect:* Scores below 0.5 are not automatically wrong; some accurate detections have low confidence. The threshold depends on the application's tolerance for false positives vs. false negatives.
- *Why C is incorrect:* Confidence scores are probabilities, not counts. Object count is determined by the number of detected instances.
- *Why D is incorrect:* Bounding box coordinates represent location, not confidence scores. These are separate fields in the API response.

---

## Question 8

Which of the following best describes the difference between face detection and face verification?

- A) Face detection identifies who a person is; face verification draws a bounding box around faces.
- B) Face detection locates faces in an image; face verification determines if two faces show the same person.
- C) Face detection requires a database of known individuals; face verification uses public images only.
- D) Face detection is available in Azure; face verification requires on-premises hardware.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Face detection finds and localizes faces in images (bounding boxes). Face verification is a 1:1 comparison — given two face images, it determines whether they show the same individual. These are distinct tasks with different inputs and outputs.
- *Why A is incorrect:* This inverts the definitions. Face identification (not detection) determines who a person is. Face detection finds where faces are.
- *Why C is incorrect:* Face verification does not require a database — it compares exactly two images. Face identification requires a database of enrolled individuals.
- *Why D is incorrect:* Both face detection and face verification are available in Azure Face API as cloud services.

---

## Question 9

A developer uploads 25 photos of damaged car bumpers (labeled "damaged") and 25 photos of undamaged bumpers (labeled "normal") to Azure Custom Vision. After training, the model achieves 90% precision and 72% recall on the test set. What does a recall of 72% mean in this context, and why might this recall level be problematic for a manufacturing quality control application?

- A) The model correctly classifies 72% of all uploaded images; the remaining 28% failed to process.
- B) 72% of the damaged bumpers in the test set were correctly identified; 28% of actual defects were missed.
- C) The model is 72% confident in its predictions on average.
- D) 72% of the model's "damaged" predictions were correct; the remaining 28% were false alarms.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Recall = TP / (TP + FN). In this context, a recall of 72% means 28% of genuinely damaged bumpers were classified as normal (false negatives). Missing defects in manufacturing quality control can result in defective products reaching customers — a serious problem.
- *Why A is incorrect:* This describes accuracy of image processing, not recall. Recall is specifically about the true positive rate among actual positives.
- *Why C is incorrect:* This describes average confidence, not recall. Recall is computed from the confusion matrix, not from score magnitudes.
- *Why D is incorrect:* This describes precision (proportion of positive predictions that are correct), not recall.

---

## Question 10

Which of the following scenarios is best served by Azure Form Recognizer rather than Azure Computer Vision?

- A) Identifying whether a user-uploaded photo contains a cat or a dog.
- B) Generating an automatic caption describing a street scene photograph.
- C) Extracting the vendor name, invoice date, line items, and total amount from a scanned invoice PDF.
- D) Detecting whether a person appears in a security camera image.

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Form Recognizer is designed to extract structured field data from documents (invoices, receipts, forms) — understanding document layout, matching labels to values, and returning structured JSON with field names and extracted values.
- *Why A is incorrect:* This is image classification — best handled by Azure Computer Vision or Custom Vision, not Form Recognizer.
- *Why B is incorrect:* Automatic image captioning is a feature of Azure Computer Vision, not Form Recognizer.
- *Why D is incorrect:* Detecting people in security footage is an object detection or video analysis task, not a document extraction task.

---

### Question 11 (5 points)

What is the key output difference between semantic segmentation and instance segmentation in computer vision?

- A) Semantic segmentation labels each pixel with a class; instance segmentation additionally distinguishes between separate individual objects of the same class.
- B) Semantic segmentation works only on video; instance segmentation works on still images.
- C) Semantic segmentation requires custom training; instance segmentation is prebuilt in Azure Computer Vision.
- D) Semantic segmentation draws bounding boxes; instance segmentation draws pixel masks.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* Semantic segmentation assigns a class label (e.g., "car") to every pixel but treats all cars as one region. Instance segmentation goes further — it distinguishes between Car 1, Car 2, and Car 3 as separate objects, each with its own pixel mask.
  - *Why B is incorrect:* Both semantic and instance segmentation can be applied to still images and video frames. The distinction is not based on media type.
  - *Why C is incorrect:* Both segmentation types are available through prebuilt and custom services. The difference is in what they output, not in training requirements.
  - *Why D is incorrect:* Bounding boxes are produced by object detection, not segmentation. Both segmentation types produce pixel-level masks, not boxes.

---

### Question 12 (5 points)

A logistics company wants to automate package label reading at sorting facilities. The labels contain printed barcodes, handwritten notes, and typed addresses on a variety of backgrounds. Which Azure capability is most appropriate?

- A) Azure Face API — attribute detection
- B) Azure Computer Vision — Read API (OCR)
- C) Azure Custom Vision — image classification
- D) Azure Form Recognizer — receipt model

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The Azure Computer Vision Read API is designed for Optical Character Recognition (OCR) — extracting printed and handwritten text from images at scale. It handles diverse backgrounds and text orientations, making it ideal for package label reading.
  - *Why A is incorrect:* Azure Face API analyzes human faces. It does not read text from package labels.
  - *Why C is incorrect:* Custom Vision classifies images into categories. It cannot read or extract text content from labels.
  - *Why D is incorrect:* The Form Recognizer receipt model extracts structured fields from receipts (vendor, total, items). Package labels are not receipts and do not have the same structure.

---

### Question 13 (5 points)

Transfer learning enables Azure Custom Vision to achieve good results with relatively few training images (as few as 15 per class). What is the underlying reason this is possible?

- A) Custom Vision uses data augmentation to generate millions of synthetic images from the 15 provided.
- B) The model reuses feature representations learned from millions of images during pretraining, so only the final classification layer needs significant training on the new data.
- C) Custom Vision reduces the image resolution to make the problem simpler, requiring less data.
- D) Microsoft's servers provide unlimited unlabeled images to supplement the 15 user-provided images.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Transfer learning carries over the general visual feature detectors (edges, textures, shapes, object parts) learned from large datasets like ImageNet. The user's 15 labeled images only need to tune the final classification layer, which is far less data-hungry than training all layers from scratch.
  - *Why A is incorrect:* While Custom Vision may apply some augmentation, this alone does not explain the small-data capability. The key mechanism is the pretrained feature extractor, not augmentation alone.
  - *Why C is incorrect:* Reducing image resolution degrades classification quality rather than improving it. Custom Vision processes images at full resolution.
  - *Why D is incorrect:* Microsoft does not supplement user-provided training data with third-party images. The pretrained model weights — not additional unlabeled data — are what make small-dataset training feasible.

---

### Question 14 (5 points)

An Azure Computer Vision analysis of an outdoor scene returns the following bounding box for a detected object: `{"left": 245, "top": 120, "width": 180, "height": 90}`. What does this bounding box describe?

- A) The detected object begins 245 pixels from the left edge, 120 pixels from the top, and spans 180 pixels wide and 90 pixels tall.
- B) The detected object has a confidence score of 245 with 120 training examples.
- C) The image was resized to 180x90 pixels before analysis.
- D) The object was detected in 245 separate image frames.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* Azure Computer Vision object detection returns bounding boxes in pixel coordinates relative to the top-left corner of the image. The bounding box defines a rectangle: starting point (left, top) and dimensions (width, height).
  - *Why B is incorrect:* These are spatial coordinates and dimensions, not scores or training counts. Confidence is a separate field in the API response.
  - *Why C is incorrect:* The API does not resize images and report the output dimensions as bounding box fields. The image dimensions are separate metadata.
  - *Why D is incorrect:* Bounding boxes apply to single images, not video frame counts. The "left" value is a horizontal pixel coordinate, not a frame count.

---

### Question 15 (5 points)

A security team wants to verify that the person entering a restricted facility matches the employee badge photo on file. They need a 1:1 match — not a search against a database. Which Azure Face API capability is most appropriate?

- A) Face Detection
- B) Face Identification
- C) Face Verification
- D) Face Grouping

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Face Verification is a 1:1 comparison that answers "Is Face A the same person as Face B?" It is designed precisely for access control scenarios where a live capture is compared against a single stored reference image.
  - *Why A is incorrect:* Face Detection locates faces in images (bounding boxes and landmarks) but does not compare identities between images.
  - *Why B is incorrect:* Face Identification is a 1:N search — it finds which person from a group of enrolled individuals matches a query face. The scenario explicitly needs 1:1, not a database search.
  - *Why D is incorrect:* Face Grouping organizes detected faces from a collection of images into groups of similar-looking individuals. It does not verify identity against a specific known person.

---

### Question 16 (5 points)

An autonomous vehicle perception system uses a deep learning model that correctly detects pedestrians 98% of the time in good daylight conditions but drops to 67% accuracy in heavy rain. Which responsible AI principle is most directly violated?

- A) Fairness
- B) Reliability and Safety
- C) Transparency
- D) Accountability

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Reliability and Safety requires that AI systems perform consistently across a range of conditions, especially in high-stakes applications. A 31-percentage-point accuracy drop in adverse weather in a system that controls vehicle behavior represents a critical safety failure.
  - *Why A is incorrect:* Fairness addresses equitable treatment across demographic groups. Variation in performance by weather conditions is a reliability and safety concern, not a demographic bias issue.
  - *Why C is incorrect:* Transparency addresses explainability. While the system's degraded performance should be disclosed, the primary principle violated by performance degradation that endangers passengers and pedestrians is Reliability and Safety.
  - *Why D is incorrect:* Accountability addresses organizational responsibility for AI outcomes. While accountability is implicated, the immediate principle violated by unsafe degraded performance is Reliability and Safety.

---

### Question 17 (5 points)

Which metric would be MOST important to monitor for a medical imaging AI that screens chest X-rays for pneumonia, given that missing a case of pneumonia is far more dangerous than a false alarm?

- A) Precision
- B) Accuracy
- C) Specificity
- D) Recall (Sensitivity)

- **Correct Answer:** D
- **Distractor Analysis:**
  - *Why D is correct:* Recall = TP / (TP + FN). In a pneumonia screening scenario, a false negative (missed pneumonia case) is potentially life-threatening. Maximizing recall minimizes missed diagnoses, even at the cost of more false alarms that a physician will review.
  - *Why A is incorrect:* Precision = TP / (TP + FP). High precision minimizes false alarms. While useful for managing physician workload, it is not the primary concern when missing a disease is dangerous.
  - *Why B is incorrect:* Accuracy treats all errors equally. A model that marks all X-rays as normal could achieve high accuracy on a dataset with few pneumonia cases while missing all actual cases.
  - *Why C is incorrect:* Specificity = TN / (TN + FP) measures the true negative rate — how well the model avoids false alarms. While important, maximizing specificity sacrifices recall (more missed cases), which is the wrong priority for this screening application.

---

### Question 18 (5 points)

The "Read API" in Azure Computer Vision is specifically optimized for which use case?

- A) Classifying images into thousands of predefined categories from the ImageNet dataset.
- B) Detecting and reading large volumes of printed and handwritten text from images and PDF documents.
- C) Detecting and identifying specific individuals in surveillance camera feeds.
- D) Generating artistic image descriptions for social media content.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The Read API (formerly OCR) is Azure Computer Vision's purpose-built capability for extracting text from images and documents at scale, supporting printed and handwritten text, multiple languages, and rotated or degraded text.
  - *Why A is incorrect:* ImageNet-based image classification is handled by Azure Computer Vision's general image analysis features, not the Read API specifically.
  - *Why C is incorrect:* Identifying specific individuals is Face Identification — a separate Azure Face API capability with restricted access.
  - *Why D is incorrect:* Azure Computer Vision generates functional captions for accessibility and metadata purposes, not artistic descriptions for social media. The Read API specifically handles text extraction.

---

### Question 19 (5 points)

A streaming service builds a content moderation system that automatically flags uploaded video clips containing graphic violence. The system uses computer vision to analyze frames at 1-second intervals. During a test, the model generates many false positives — flagging action movie clips with non-violent fast motion as violent. Which strategy would MOST directly reduce false positives?

- A) Increase the detection confidence threshold so the model only flags clips where it is highly certain the content is violent.
- B) Reduce the frame sampling rate to 10 seconds per frame to decrease the number of classifications.
- C) Switch from object detection to image classification to change the output format.
- D) Remove all action movies from the training dataset.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* Raising the confidence threshold requires higher certainty before flagging content. This reduces false positives (incorrect violent flags) at the cost of potentially missing some true positives (genuine violent content). For a streaming service, the trade-off may be acceptable if human reviewers handle borderline cases.
  - *Why B is incorrect:* Reducing sampling rate lowers detection frequency but does not address the underlying false positive rate. A model with many false positives at 1-second intervals will still produce false positives at 10-second intervals.
  - *Why C is incorrect:* Switching from object detection to image classification changes the output type (bounding boxes vs. whole-image label) but does not address false positive rate. The core confusion problem is about threshold, not architecture type.
  - *Why D is incorrect:* Removing action movies from training would cause the model to fail on the very content generating false positives. The model needs representative examples of non-violent action to learn the distinction.

---

### Question 20 (5 points)

An insurance company wants to automatically assess vehicle damage from photos submitted through their claims app and estimate repair cost categories (minor, moderate, severe). They have 1,200 labeled damage photos. Which Azure service and workflow is most appropriate?

- A) Azure Computer Vision — prebuilt damage analysis with no training
- B) Azure Custom Vision — train a custom image classification model on the 1,200 labeled photos
- C) Azure Form Recognizer — extract claim form fields from the damage photos
- D) Azure Face API — detect faces in the damage photos to verify the claimant's identity

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The three damage severity categories (minor, moderate, severe) are custom domain-specific labels not available in prebuilt models. Azure Custom Vision enables training a classification model on the 1,200 labeled photos using transfer learning, which is sufficient for this dataset size.
  - *Why A is incorrect:* Azure Computer Vision's prebuilt model does not include insurance damage severity categories. Prebuilt analysis tags common objects and scenes, not domain-specific damage assessments.
  - *Why C is incorrect:* Azure Form Recognizer extracts structured text fields from documents. Vehicle damage photos are not structured forms, and repair cost estimation from visual content is not a document extraction task.
  - *Why D is incorrect:* Identity verification is a separate step from damage assessment. Azure Face API would not analyze vehicle damage or estimate repair costs.
