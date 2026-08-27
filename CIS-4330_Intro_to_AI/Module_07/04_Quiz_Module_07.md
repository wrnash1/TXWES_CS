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

---

## Question 11 (5 points)

A developer calls the Azure AI Vision Analyze Image API with the `objects` feature enabled. How does the output of the `objects` feature differ from the `tags` feature?

A. The `objects` feature returns bounding box coordinates for each detected item; the `tags` feature returns a list of keyword labels with no location information.

B. The `objects` feature lists the dominant colors in the image; the `tags` feature counts the total number of objects.

C. The `objects` feature applies sentiment analysis to the image; the `tags` feature identifies the image type.

D. There is no difference — both features return identical results.

### Q11 — Correct Answer

A. The `objects` feature returns bounding box coordinates for each detected item; the `tags` feature returns a list of keyword labels with no location information.

### Q11 — Distractor Analysis

- B is incorrect: Dominant color analysis is a separate feature (`color`). Neither `objects` nor `tags` counts items or analyzes colors.
- C is incorrect: Azure AI Vision does not perform sentiment analysis on images. The `tags` feature identifies objects and concepts, not image type.
- D is incorrect: The two features return different data structures. `tags` gives keyword-confidence pairs; `objects` gives label-bounding-box-confidence structures.

---

## Question 12 (5 points)

A developer trains a Custom Vision object detection model and notices that the model's Recall is much lower than its Precision. Which action is most likely to improve Recall without retraining the model?

A. Add more training images to the dataset and retrain.

B. Lower the probability threshold so the model flags more predictions as positive.

C. Raise the probability threshold so only high-confidence detections are accepted.

D. Switch from an object detection project to a classification project.

### Q12 — Correct Answer

B. Lower the probability threshold so the model flags more predictions as positive.

### Q12 — Distractor Analysis

- A is incorrect: Adding images requires retraining, which the question explicitly excludes from the solution.
- C is incorrect: Raising the threshold further increases Precision but reduces Recall — the opposite of what is needed.
- D is incorrect: Switching project types would discard all annotated bounding box training data and does not address the threshold issue.

---

## Question 13 (5 points)

Which of the following scenarios requires the Azure AI Document Intelligence Layout model rather than the Read model?

A. Extracting all words and lines from a single-page handwritten letter.

B. Extracting table structure, reading order of multi-column text, and paragraph positions from a complex multi-page annual report.

C. Converting an audio recording of a speech into a transcript.

D. Classifying a scanned document as either an invoice or a contract.

### Q13 — Correct Answer

B. Extracting table structure, reading order of multi-column text, and paragraph positions from a complex multi-page annual report.

### Q13 — Distractor Analysis

- A is incorrect: Simple full-text extraction from a single page is well-served by the Read model; the Layout model's structural analysis is not needed.
- C is incorrect: Audio transcription is handled by Azure AI Speech Service, not Document Intelligence.
- D is incorrect: Document classification is handled by the Document Intelligence Custom Classification model, not the Layout model.

---

## Question 14 (5 points)

A security system needs to determine whether a face presented to a camera is a real person physically present or a printed photograph being held up. Which Azure Face API capability addresses this?

A. Face Identification

B. Liveness Detection

C. Face Grouping

D. Attribute Analysis (age, emotion)

### Q14 — Correct Answer

B. Liveness Detection

### Q14 — Distractor Analysis

- A is incorrect: Face Identification matches a face to a database of enrolled individuals. It does not determine whether the face is physically present or a photo.
- C is incorrect: Face Grouping organizes detected faces into clusters of similar appearance. It does not verify physical presence.
- D is incorrect: Attribute analysis (age, smile, glasses) describes facial characteristics. It does not detect whether the face is physically real or a spoofed image.

---

## Question 15 (5 points)

An e-commerce platform wants to automatically generate alt-text descriptions for all product images to comply with accessibility standards. Which Azure AI Vision feature generates a human-readable sentence describing the content of an image?

A. Tags — returns keyword labels like "chair," "wood," "indoor."

B. Objects — returns bounding boxes for detected items.

C. Captions — returns a natural language sentence such as "a wooden rocking chair on a white background."

D. Read — returns any text printed on the image.

### Q15 — Correct Answer

C. Captions — returns a natural language sentence such as "a wooden rocking chair on a white background."

### Q15 — Distractor Analysis

- A is incorrect: Tags return keyword-confidence pairs that are not grammatically structured sentences suitable for alt-text.
- B is incorrect: Objects return detection results with coordinates — useful for locating items but not for generating readable descriptions.
- D is incorrect: The Read feature extracts text printed in the image. If a product photo has no printed text, the Read feature returns nothing useful.

---

## Question 16 (5 points)

A fashion retailer wants to enable shoppers to search for products by uploading a photo of a similar item they already own. The retailer has a catalog of 50,000 product images. Which Azure AI Vision feature is most appropriate for this use case?

A. Image Captioning — generate a text description of the uploaded photo and use it as a search query.

B. Image Embeddings / Visual Search — compare the embedding of the uploaded photo against catalog image embeddings to find similar items.

C. Face API Liveness Detection — verify the shopper is a real person before allowing the search.

D. Custom Vision Classification — classify the uploaded photo into one of 50,000 individual product categories.

### Q16 — Correct Answer

B. Image Embeddings / Visual Search — compare the embedding of the uploaded photo against catalog image embeddings to find similar items.

### Q16 — Distractor Analysis

- A is incorrect: Text-based search after captioning loses the visual nuances (color, texture, shape) that make visual similarity search valuable and would produce imprecise results.
- C is incorrect: Liveness Detection checks whether a face is real. It has no relevance to product similarity search.
- D is incorrect: Training 50,000 separate Custom Vision categories (one per product) is not a scalable or practical approach. Similarity search via embeddings does not require per-product classification.

---

## Question 17 (5 points)

A city traffic management department deploys an AI Vision system to count vehicles by type (car, truck, bus, motorcycle) at major intersections. After six months, the city discovers the system undercounts motorcycles by 40% compared to manual counts. What is the most likely cause?

A. The Azure AI Vision API has a known bug that skips every fifth vehicle detection.

B. The training or prebuilt model data contained fewer motorcycle examples, resulting in lower recall for that class.

C. Motorcycles travel faster than other vehicles, and the API cannot process moving objects.

D. The Free pricing tier limits motorcycle detection to 100 vehicles per month.

### Q17 — Correct Answer

B. The training or prebuilt model data contained fewer motorcycle examples, resulting in lower recall for that class.

### Q17 — Distractor Analysis

- A is incorrect: There is no documented bug causing periodic skips in Azure AI Vision detection results.
- C is incorrect: Computer vision object detection analyzes individual video frames or still images. The speed of objects does not prevent detection — image blur from motion can affect quality, but the scenario points to a systematic 40% undercount suggestive of training data imbalance.
- D is incorrect: Pricing tier affects transaction throughput and quota, not per-class detection accuracy.

---

## Question 18 (5 points)

An Azure Custom Vision model is trained to classify satellite images as one of three land-cover types: forest, urban, and water. A developer publishes the model and calls the prediction endpoint with a new satellite image. The response shows: `forest: 0.62, urban: 0.31, water: 0.07`. How should the developer interpret this result?

A. The image contains 62% forest, 31% urban areas, and 7% water by pixel area.

B. The model predicts forest as the most likely land-cover type with 62% confidence; the image is assigned the "forest" label when the threshold is set to 0.5 or below 0.62.

C. The model is defective because the three scores should each equal exactly 0.33.

D. The image must be retaken because scores below 0.70 are invalid.

### Q18 — Correct Answer

B. The model predicts forest as the most likely land-cover type with 62% confidence; the image is assigned the "forest" label when the threshold is set to 0.5 or below 0.62.

### Q18 — Distractor Analysis

- A is incorrect: Classification scores are class probabilities, not pixel area percentages. Segmentation would be needed for pixel-level land-cover proportions.
- C is incorrect: Scores only equal 1/N when the model has equal confidence across all classes, which is rare. Softmax distributes probability mass based on the model's learned patterns.
- D is incorrect: There is no 0.70 validity threshold. The developer sets a threshold based on the application's precision-recall trade-off requirements.

---

## Question 19 (5 points)

Which of the following is a responsible AI concern specific to deploying Azure AI Vision Spatial Analysis in a workplace environment?

A. Spatial Analysis requires a minimum of 100 cameras before it can produce accurate results.

B. Continuous video monitoring of employees raises privacy concerns about consent, data retention, and potential discriminatory use of behavioral analytics data.

C. Spatial Analysis is only accurate in outdoor environments with natural lighting.

D. Spatial Analysis requires Custom Vision training before it can detect people in a space.

### Q19 — Correct Answer

B. Continuous video monitoring of employees raises privacy concerns about consent, data retention, and potential discriminatory use of behavioral analytics data.

### Q19 — Distractor Analysis

- A is incorrect: Spatial Analysis can operate with a single camera. There is no 100-camera minimum requirement.
- C is incorrect: Spatial Analysis is designed for indoor environments such as retail stores, offices, and warehouses, as well as outdoor spaces. Lighting conditions affect accuracy but are not a blanket limitation.
- D is incorrect: Spatial Analysis is a prebuilt capability that detects and tracks people without requiring Custom Vision training.

---

## Question 20 (5 points)

A developer needs to read text from a receipt image taken with a smartphone. The receipt has slightly tilted text and some areas are smudged. Which Azure AI Vision feature handles this scenario, and what is a realistic expectation about output quality?

A. The Image Analysis `tags` feature; it will label the receipt as a document type.

B. The Read API; it is designed for real-world image OCR including tilted and low-quality text, but accuracy may be reduced in heavily smudged areas.

C. The Face API `attributes` feature; it will extract numbers and dates from the image.

D. Custom Vision classification; it will categorize the image as a receipt versus non-receipt.

### Q20 — Correct Answer

B. The Read API; it is designed for real-world image OCR including tilted and low-quality text, but accuracy may be reduced in heavily smudged areas.

### Q20 — Distractor Analysis

- A is incorrect: The `tags` feature identifies objects and concepts in images. It does not extract text content from receipts.
- C is incorrect: The Face API is for analyzing human faces. It has no text extraction capability.
- D is incorrect: Custom Vision classification categorizes the whole image into predefined classes. It does not extract text content.

---

End of Quiz — Module 07
