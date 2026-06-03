# Quiz: Module 07 — Computer Vision with Azure

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Domain: Describe features of computer vision workloads on Azure

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Submit your answers through the course LMS.

---

## Question 1

A retail company wants to automatically generate descriptive tags and a natural-language caption for thousands of product images stored in Azure Blob Storage. No custom training is needed. Which Azure service is most appropriate?

A. Azure Custom Vision — Classification project

B. Azure AI Vision — Analyze Image API

C. Azure Face API — Attribute Detection

D. Azure AI Document Intelligence — Read model

### Q1 — Correct Answer

B. Azure AI Vision — Analyze Image API

### Q1 — Distractor Analysis

- A is incorrect: Custom Vision requires you to upload and label training data. This scenario explicitly says no custom training is needed, and the task is a general-purpose capability already built into Azure AI Vision.
- C is incorrect: Face API is specialized for human faces. It does not generate general image tags or captions.
- D is incorrect: Document Intelligence extracts structured text from documents and forms, not descriptive tags or captions for product images.

---

## Question 2

A developer is building a mobile app that needs to count and locate cars in parking lot photos. The app must work offline without any internet connection. Which approach best meets these requirements?

A. Call the Azure AI Vision Analyze Image API from the mobile app at runtime

B. Train an Azure Custom Vision object detection model and export it in CoreML format

C. Use the Azure Face API Liveness Detection endpoint

D. Train an Azure Custom Vision classification model and publish a prediction endpoint

### Q2 — Correct Answer

B. Train an Azure Custom Vision object detection model and export it in CoreML format

### Q2 — Distractor Analysis

- A is incorrect: Calling a cloud API requires internet connectivity; the requirement is offline operation.
- C is incorrect: Face API Liveness Detection determines whether a face is real, not for detecting or counting vehicles.
- D is incorrect: A classification model labels the whole image — it does not locate individual objects. A published prediction endpoint also requires internet connectivity.

---

## Question 3

What does a confidence score of 0.94 returned by the Azure AI Vision Analyze Image API mean?

A. The image contains exactly 94 recognizable objects

B. The model estimates a 94% probability that the predicted tag or label is correct

C. The API call consumed 94% of the available quota for the billing period

D. The image quality is rated 94 out of 100 by the service

### Q3 — Correct Answer

B. The model estimates a 94% probability that the predicted tag or label is correct

### Q3 — Distractor Analysis

- A is incorrect: Confidence scores are probabilities between 0.0 and 1.0, not counts of objects.
- C is incorrect: Confidence scores are per-prediction quality estimates, not quota consumption metrics.
- D is incorrect: Azure AI Vision does not return an image quality rating.

---

## Question 4

A company's quality control team needs to detect three specific types of manufacturing defects in photos taken on an assembly line. The defect categories are proprietary. Which service and project type should they use?

A. Azure AI Vision — Analyze Image API with the `objects` feature

B. Azure Custom Vision — Classification project with three tags

C. Azure Custom Vision — Object Detection project with three tags

D. Azure AI Document Intelligence — Custom model

### Q4 — Correct Answer

C. Azure Custom Vision — Object Detection project with three tags

### Q4 — Distractor Analysis

- A is incorrect: The Analyze Image API uses pre-built models that do not know proprietary defect categories.
- B is incorrect: Classification assigns a label to the whole image. Locating individual defects within an image requires bounding boxes, which is object detection.
- D is incorrect: Document Intelligence extracts text and structured data from documents and is not designed for visual defect detection.

---

## Question 5

Which of the following best describes the difference between Precision and Recall in Custom Vision model evaluation?

A. Precision measures how fast the model runs; Recall measures how much memory it uses

B. Precision is the fraction of positive predictions that are correct; Recall is the fraction of actual positives the model correctly identified

C. Precision measures image resolution requirements; Recall measures the number of training images used

D. Precision and Recall are identical metrics calculated on different subsets of the data

### Q5 — Correct Answer

B. Precision is the fraction of positive predictions that are correct; Recall is the fraction of actual positives the model correctly identified

### Q5 — Distractor Analysis

- A is incorrect: Precision and Recall are classification quality metrics, not performance or resource metrics.
- C is incorrect: Neither metric relates to image resolution or training data count.
- D is incorrect: Precision and Recall measure distinct aspects of quality — prediction reliability versus completeness of detection.

---

## Question 6

A developer wants to extract text from a 20-page scanned PDF that contains both printed text and handwritten annotations. Which Azure service and feature is most appropriate?

A. Azure AI Vision — Image Analysis OCR feature (synchronous)

B. Azure AI Vision — Analyze Image API with `tags` feature

C. Azure AI Document Intelligence — Read model (asynchronous)

D. Azure Custom Vision — Classification project

### Q6 — Correct Answer

C. Azure AI Document Intelligence — Read model (asynchronous)

### Q6 — Distractor Analysis

- A is incorrect: The Image Analysis OCR feature handles single images with simple scene text and is less reliable for multi-page documents and mixed handwriting.
- B is incorrect: The `tags` feature identifies objects and scenes; it does not extract text content.
- D is incorrect: Custom Vision handles image classification and object detection. It has no OCR capability.

---

## Question 7

A startup wants to use the Azure Face API to identify customers by comparing their faces against a database of enrolled members. Which statement about this use case is accurate?

A. This capability is available to all Azure customers with a Standard pricing tier and requires no special approval

B. This capability requires applying for and receiving approval under Microsoft's Limited Access program

C. Face identification is not supported in Azure — only face detection with a bounding box is available

D. This capability is available only to government agencies and not to commercial customers

### Q7 — Correct Answer

B. This capability requires applying for and receiving approval under Microsoft's Limited Access program

### Q7 — Distractor Analysis

- A is incorrect: Face identification and verification features moved to Limited Access in June 2023; a paid subscription alone is insufficient.
- C is incorrect: Face identification is technically supported but requires Limited Access approval; it is not absent from the service.
- D is incorrect: Certain commercial use cases such as identity verification are approved; blanket government-only restriction is not the policy.

---

## Question 8

An Azure Custom Vision classification model is trained and published. A developer exports it in ONNX format. What is the primary purpose of this export?

A. To view the model's architecture as a human-readable diagram

B. To run the model locally on a device without an internet connection

C. To move the model to a different Azure subscription

D. To convert the model into a SQL database for querying

### Q8 — Correct Answer

B. To run the model locally on a device without an internet connection

### Q8 — Distractor Analysis

- A is incorrect: ONNX is a portable binary inference format, not a visualization format.
- C is incorrect: Moving between subscriptions does not require ONNX export; the format is specifically for local/edge inference.
- D is incorrect: ONNX models run inference computations; they are not database formats.

---

## Question 9

A computer vision system used to screen job application photos shows significantly higher error rates for women and darker-skinned applicants compared to other groups. What is the most likely root cause?

A. The Azure AI Vision service intentionally applies different rules for different demographic groups

B. The training dataset was not representative of the full diversity of applicants

C. Computer vision models cannot process images of people

D. The Free F0 pricing tier reduces accuracy for certain image types

### Q9 — Correct Answer

B. The training dataset was not representative of the full diversity of applicants

### Q9 — Distractor Analysis

- A is incorrect: Azure AI Vision applies a single uniform model. Differential error rates stem from training data problems, not intentional service rules.
- C is incorrect: Computer vision models process images of people routinely; the Face API is a direct example.
- D is incorrect: Pricing tier governs throughput and quota, not model accuracy or demographic fairness.

---

## Question 10

Which Azure service would you use to analyze live video feeds and generate alerts when more than 50 people are present in a defined floor zone at the same time?

A. Azure AI Vision — Spatial Analysis

B. Azure Custom Vision — Object Detection

C. Azure Face API — Face Identification

D. Azure AI Document Intelligence — Layout model

### Q10 — Correct Answer

A. Azure AI Vision — Spatial Analysis

### Q10 — Distractor Analysis

- B is incorrect: Custom Vision Object Detection processes still images and is not designed for real-time live video occupancy monitoring.
- C is incorrect: Face Identification matches faces to known individuals; it does not perform zone-based headcount monitoring.
- D is incorrect: Document Intelligence analyzes documents and forms; it has no video processing capability.

---

End of Quiz — Module 07
