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
