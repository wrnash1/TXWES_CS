# Quiz: Module 16 — AI-900 Exam Preparation and Capstone

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Instructions

This quiz serves two purposes: (1) it is the Module 16 graded assessment, and (2) it is the answer key for the 20-question timed practice exam in the M16 Lab. Complete the Lab Part 3 simulation BEFORE reviewing this document.

Each question is worth 5 points. The quiz is closed-book and should be completed in 30 minutes. This quiz covers all five AI-900 exam domains.

**Note:** Questions 1–20 in this document correspond exactly to the 20 simulation questions in M16_Lab.md Part 3.

---

## Questions and Answers

**Question 1**

A hospital wants to automatically flag urgent patient records for physician review based on clinical note text. What type of AI workload is this?

A. Computer vision

B. Natural language processing

C. Anomaly detection in time series

D. Generative content creation

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Computer vision processes images. Clinical notes are text documents, not images.
- **B** is correct. Analyzing clinical text to extract urgency signals, diagnoses, or risk factors is natural language processing — specifically text classification or entity extraction applied to medical text.
- **C** is incorrect. Anomaly detection in time series monitors sequential numerical data (sensor readings, transaction streams) for unusual patterns. Clinical text review is not a time series problem.
- **D** is incorrect. Generative content creation produces new content. Flagging records for review is a classification task, not generation.

---

**Question 2**

Which responsible AI principle requires that an AI system's decision-making be understandable to the people it affects?

A. Fairness

B. Accountability

C. Transparency

D. Inclusiveness

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Fairness requires equitable treatment across groups — it concerns outcomes, not understandability.
- **B** is incorrect. Accountability requires that humans are responsible for AI decisions — it concerns responsibility assignment, not understandability of the model itself.
- **C** is correct. Transparency requires that AI systems and their limitations be understandable to the people who use them and are affected by them.
- **D** is incorrect. Inclusiveness requires that AI systems empower all people regardless of ability, geography, or background — it concerns access and participation, not explanation.

---

**Question 3**

A company trains an AI model to predict customer churn. The output is either "Will Churn" or "Will Not Churn." What type of ML task is this?

A. Regression

B. Clustering

C. Classification

D. Anomaly detection

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Regression predicts a continuous numerical value (e.g., probability score from 0.0 to 1.0 would be regression; a discrete "Will/Will Not" binary category is classification).
- **B** is incorrect. Clustering groups similar items without predefined labels. The company has defined output categories, making this supervised classification, not unsupervised clustering.
- **C** is correct. Classification assigns inputs to predefined categories. "Will Churn" / "Will Not Churn" are two discrete categories, making this binary classification.
- **D** is incorrect. Anomaly detection identifies unusual observations that deviate from the norm. Predicting churn from customer features is pattern-based classification, not anomaly detection.

---

**Question 4**

A data scientist wants to try 200 algorithm and hyperparameter combinations to find the best performing model on a tabular dataset. Which Azure ML feature automates this?

A. Azure Machine Learning Designer

B. Azure AutoML

C. Azure Custom Vision

D. Azure AI Foundry

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. The Designer is a visual drag-and-drop pipeline builder for manually constructing training workflows. It does not automatically search algorithm and hyperparameter combinations.
- **B** is correct. AutoML (Automated Machine Learning) in Azure ML automatically searches over algorithms and hyperparameter combinations, selecting the best performer within the defined constraints and time budget.
- **C** is incorrect. Custom Vision is a service for training custom image classification and object detection models. It does not work with tabular data.
- **D** is incorrect. Azure AI Foundry (formerly Azure AI Studio) is a platform for generative AI and LLM development, not tabular ML experimentation.

---

**Question 5**

A retail company needs to deploy a model that scores every customer in their database nightly and writes predictions to a table. Which endpoint type is most appropriate?

A. Managed online endpoint

B. Batch endpoint

C. Compute cluster direct deployment

D. Real-time streaming endpoint

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Managed online endpoints process individual real-time requests synchronously. Nightly bulk scoring of an entire database is not a real-time use case.
- **B** is correct. Batch endpoints process large volumes of data asynchronously. A nightly scoring job that writes predictions to a database table is exactly the batch endpoint use case.
- **C** is incorrect. Direct deployment to a compute cluster is not a supported Azure ML production deployment pattern. Compute clusters are for training, not serving.
- **D** is incorrect. Real-time streaming is not an Azure ML endpoint type. This is a distractor combining streaming and real-time concepts inappropriately.

---

**Question 6**

What is the primary purpose of OCR in Azure AI Vision?

A. Detect faces in photographs

B. Classify whether an image contains prohibited content

C. Extract text from images and documents

D. Translate text from one language to another

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Face detection is a separate capability in Azure AI Vision and Azure Face API. OCR specifically deals with text in images, not facial features.
- **B** is incorrect. Content moderation (detecting prohibited content) is a separate capability. OCR reads text; it does not classify visual content as appropriate or inappropriate.
- **C** is correct. OCR (Optical Character Recognition) extracts printed or handwritten text from images, scanned documents, PDFs, and photographs.
- **D** is incorrect. Translation is a separate capability handled by Azure AI Translator. OCR extracts text; it does not translate between languages.

---

**Question 7**

A company wants to train an image classifier using 200 labeled photographs of their own industrial equipment to detect malfunctions. Which Azure service should they use?

A. Azure AI Vision (pre-built analysis)

B. Azure Custom Vision (train custom classifier)

C. Azure Machine Learning AutoML

D. Azure Face API

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Azure AI Vision's pre-built analysis uses Microsoft's general-purpose models. It cannot recognize company-specific industrial equipment malfunction patterns without training on custom data.
- **B** is correct. Azure Custom Vision enables users to train a custom image classifier or object detector using their own labeled images. 200 labeled photos is appropriate for Custom Vision's few-shot learning capability.
- **C** is incorrect. Azure ML AutoML handles tabular data classification and regression. It does not provide a specialized custom image training interface like Custom Vision.
- **D** is incorrect. Azure Face API specifically analyzes human faces. It is not applicable to industrial equipment image classification.

---

**Question 8**

A user asks a chatbot: "I want to book a flight to Dallas for next Friday." The chatbot must identify that the user intends to book a flight (intent) and extract "Dallas" and "next Friday" (entities). Which Azure service handles this?

A. Azure AI Translator

B. Azure AI Vision

C. Azure AI Language — Conversational Language Understanding

D. Azure AI Speech — speech translation

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Azure AI Translator translates text between languages. It does not perform intent classification or entity extraction.
- **B** is incorrect. Azure AI Vision analyzes images and video. It does not process natural language text for intent and entity extraction.
- **C** is correct. Conversational Language Understanding (CLU), part of Azure AI Language, is specifically designed for chatbot and voice assistant scenarios — classifying user intent and extracting named entities from conversational utterances.
- **D** is incorrect. Azure AI Speech speech translation converts spoken audio from one language to another. It does not classify user intent in text.

---

**Question 9**

A contact center wants to transcribe customer service phone calls in real time. Which Azure service performs this function?

A. Azure AI Language

B. Azure AI Speech — speech-to-text

C. Azure AI Translator

D. Azure OpenAI Whisper deployment

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Azure AI Language performs text analysis (sentiment, entities, key phrases) on text that has already been transcribed. It does not convert audio to text.
- **B** is correct. Azure AI Speech provides a speech-to-text capability that transcribes spoken audio — including real-time streaming audio from phone calls — to text.
- **C** is incorrect. Azure AI Translator translates text between languages. It does not transcribe audio.
- **D** is incorrect. While Azure OpenAI Service does provide access to the Whisper model for transcription, Whisper is designed for file-based audio transcription, not real-time streaming transcription. Azure AI Speech is the service designed for real-time call transcription.

---

**Question 10**

Which Azure service would you use to translate a customer review written in Portuguese into English?

A. Azure AI Language — sentiment analysis

B. Azure AI Speech — speech translation

C. Azure AI Translator

D. Azure OpenAI GPT-4

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Azure AI Language sentiment analysis classifies the tone of text as positive, negative, or neutral. It does not translate between languages.
- **B** is incorrect. Azure AI Speech speech translation converts spoken audio in one language to text in another. A written customer review is text, not audio.
- **C** is correct. Azure AI Translator is the dedicated text translation service, supporting 100+ languages. Translating a written Portuguese review to English is its primary use case.
- **D** is incorrect. While GPT-4 can translate text, Azure AI Translator is the purpose-built, cost-effective service for translation workflows. Using GPT-4 for translation would be technically possible but architecturally inappropriate and cost-inefficient.

---

**Question 11**

A company deploys GPT-4 via Azure OpenAI Service. They want the model to answer questions using only information from their internal policy documents, rather than the model's general training knowledge. What pattern should they implement?

A. Fine-tuning the model on the policy documents

B. Retrieval Augmented Generation (RAG)

C. Increasing the model's temperature parameter

D. Using the DALL-E model instead of GPT-4

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Fine-tuning changes the model's learned weights using training examples. It can bias the model toward a style or domain, but it does not reliably restrict the model to only using specific documents for specific answers. RAG provides more precise grounding.
- **B** is correct. RAG retrieves relevant document chunks at inference time and provides them to the model as context. The model generates responses grounded in the retrieved content. This directly addresses the requirement of using only internal policy documents.
- **C** is incorrect. Temperature controls output randomness and creativity. Lowering temperature makes the model more deterministic, but it still draws on its general training knowledge — it does not restrict it to policy documents.
- **D** is incorrect. DALL-E generates images from text. It cannot answer text questions about policy documents.

---

**Question 12**

What does the temperature parameter control in an Azure OpenAI text generation request?

A. The number of tokens in the output

B. The randomness and creativity of the model's output

C. The speed of inference on the compute cluster

D. The maximum context length the model can process

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Output token count is controlled by the `max_tokens` parameter, not temperature.
- **B** is correct. Temperature controls the probability distribution over possible next tokens. Low temperature (close to 0) makes the model choose the most probable token consistently, producing deterministic output. High temperature (close to 2) increases randomness, enabling more creative and varied outputs.
- **C** is incorrect. Inference speed is determined by compute resources and model size. Temperature is a generation parameter that has no direct impact on inference latency.
- **D** is incorrect. Maximum context length is a property of the model architecture and is not configurable via temperature. It is controlled by model selection.

---

**Question 13**

A customer uses DALL-E 3 via Azure OpenAI Service. What type of output does DALL-E generate?

A. Audio files from text descriptions

B. Images generated from text descriptions

C. Code generated from natural language specifications

D. Summaries of uploaded documents

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. DALL-E generates images, not audio. Audio generation is a separate modality handled by other models.
- **B** is correct. DALL-E 3 is a text-to-image model. Given a natural language description ("a photorealistic image of a red fox in a snowy forest"), DALL-E generates a corresponding image.
- **C** is incorrect. Code generation is a capability of GPT-4 and similar language models, not DALL-E. DALL-E is specifically for image generation.
- **D** is incorrect. Document summarization is a text-to-text task performed by GPT-4. DALL-E generates images from text, not text from text.

---

**Question 14**

Which of the following best describes Azure OpenAI content filtering?

A. A tokenizer that limits the length of prompts sent to the model

B. An encryption layer that prevents unauthorized access to model weights

C. Classifiers applied to inputs and outputs to prevent harmful or inappropriate content

D. A pricing control that limits the number of API calls per subscription

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. A tokenizer converts text to tokens for model processing. Content filtering evaluates the safety of content, not its length or format.
- **B** is incorrect. Model weight protection is a security infrastructure concern. Content filtering specifically evaluates the substance of prompts and responses for harmful content.
- **C** is correct. Azure OpenAI content filtering applies classifiers to both the input prompt and the generated output to detect and block harmful categories: hate speech, violence, self-harm, and sexual content.
- **D** is incorrect. API call limits are a rate-limiting and billing control, not content filtering. Content filtering operates on the content of each request, not on request volume.

---

**Question 15**

An AI-powered hiring tool consistently recommends male candidates over female candidates with equal qualifications. Which responsible AI principle is most directly violated?

A. Transparency

B. Accountability

C. Fairness

D. Reliability

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Transparency concerns the understandability of the AI system's decision-making. The issue here is discriminatory outcomes, not opacity.
- **B** is incorrect. Accountability concerns whether humans are responsible for AI impacts. While accountability is also relevant (no human review of biased outcomes), the primary principle directly violated by discriminatory hiring outcomes is fairness.
- **C** is correct. Fairness requires that AI systems treat all people equitably and do not produce systematically different outcomes for demographic groups with equal underlying qualifications.
- **D** is incorrect. Reliability concerns whether the system performs consistently as expected. The system is performing consistently — consistently in a biased manner. The root issue is fairness, not unreliable performance.

---

**Question 16**

A medical imaging AI achieves 95% accuracy in testing but performs at only 78% accuracy on patients over age 75 in production. Which responsible AI principle failure does this illustrate?

A. Privacy and Security

B. Fairness and Inclusiveness

C. Accountability

D. Transparency

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Privacy and Security concerns protecting personal data and resisting attacks. The issue here is disparate performance across age groups, not a data breach or adversarial attack.
- **B** is correct. Fairness requires equitable outcomes across demographic groups. Inclusiveness requires that AI systems work well for all people including older populations. A 17-percentage-point accuracy gap for elderly patients violates both principles — the system delivers worse outcomes for a specific age group.
- **C** is incorrect. Accountability concerns human responsibility for AI systems. While the organization is accountable for deploying a biased system, the principle that describes the discriminatory outcome itself is fairness and inclusiveness.
- **D** is incorrect. Transparency concerns understandability of decision-making. The problem is not that the model's reasoning is opaque — the problem is that it performs inequitably across age groups.

---

**Question 17**

What does the Azure Machine Learning model registry provide?

A. Real-time inference endpoints for deployed models

B. A versioned store of trained model artifacts with lineage and metadata

C. A visual drag-and-drop interface for building ML pipelines

D. Automated algorithm selection and hyperparameter tuning

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Endpoints (online and batch) are separate Azure ML resources. The model registry stores model artifacts; it does not serve predictions.
- **B** is correct. The model registry is a versioned catalog of trained models. Each entry includes the model artifact, version number, training job lineage (which job produced it), evaluation metrics, and custom tags. It is the handoff point between training and deployment.
- **C** is incorrect. The visual drag-and-drop interface is the Designer. The model registry is a storage and governance component, not a visual authoring tool.
- **D** is incorrect. Automated algorithm and hyperparameter selection is the function of AutoML, not the model registry.

---

**Question 18**

A team deploys an online endpoint for a product recommendation model. Over several months, the model's prediction quality degrades. Investigation reveals that customers' purchasing preferences have changed. What type of drift is this?

A. Data drift — input feature distributions have changed

B. Concept drift — the relationship between features and correct output has changed

C. Model drift — the model weights have changed post-deployment

D. Infrastructure drift — compute resources are insufficient

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Data drift is when the statistical distribution of input features changes. In this scenario, it is not just the distribution of inputs that has changed — the underlying preferences (the correct mapping from customer features to preferred recommendations) have changed.
- **B** is correct. Concept drift occurs when the true relationship between input features and the correct output changes. Customer preferences shifting means the "correct" recommendation for a given customer profile is now different from what it was at training time.
- **C** is incorrect. Model drift is not a standard ML term. Model weights do not change post-deployment unless retraining occurs. The model is unchanged; the world around it has changed.
- **D** is incorrect. Infrastructure drift is not a model quality concept. Insufficient compute would cause latency issues, not reduced recommendation accuracy.

---

**Question 19**

Which Azure service provides the embeddings API used to convert text into semantic vector representations for use in RAG pipelines?

A. Azure AI Language

B. Azure AI Translator

C. Azure OpenAI Service

D. Azure Custom Vision

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Azure AI Language provides text analytics capabilities (sentiment, NER, key phrases). It does not provide a general-purpose semantic embeddings API for RAG pipelines.
- **B** is incorrect. Azure AI Translator converts text between languages. It does not produce semantic vector embeddings.
- **C** is correct. Azure OpenAI Service provides the Embeddings API (e.g., text-embedding-ada-002) that converts text into high-dimensional vector representations. These vectors capture semantic meaning and are used to build vector indexes for RAG retrieval.
- **D** is incorrect. Azure Custom Vision trains image classification and object detection models. It does not process text or produce text embeddings.

---

**Question 20**

Microsoft's responsible AI principles are best described as:

A. Legally mandated requirements for all AI deployments in the European Union

B. Ethical guidelines that must be embedded into AI design, development, and deployment practices

C. Technical specifications for configuring Azure AI services securely

D. Performance benchmarks that AI models must meet before Azure deployment

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Microsoft's responsible AI principles are internal Microsoft guidelines, not EU legal mandates. GDPR and the EU AI Act are EU legal requirements. Microsoft's principles are voluntary ethical commitments.
- **B** is correct. The six responsible AI principles (Fairness, Reliability and Safety, Privacy and Security, Inclusiveness, Transparency, Accountability) are ethical guidelines adopted by Microsoft and recommended to customers as foundational practices throughout the AI development lifecycle.
- **C** is incorrect. Technical security configurations are separate from ethical principles. Security configuration is covered by Azure Security Center, Key Vault, and network controls, not by responsible AI principles.
- **D** is incorrect. Microsoft does not publish performance benchmarks that models must meet before Azure deployment. Responsible AI principles govern ethical and safety considerations, not technical performance thresholds.

---

*Quiz prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
