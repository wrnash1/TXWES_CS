# Video Script: Module 16 — AI-900 Exam Preparation and Capstone

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Segment 1: Introduction and Exam Overview (Lines 1–30)

[SLIDE: Module 16 Title Card — AI-900 Exam Preparation and Capstone]

Welcome to Module 16 — the final module of CIS-4330. I'm Professor Nash, and this session is entirely focused on getting you ready to pass the Microsoft Azure AI Fundamentals AI-900 exam and to think about what comes next in your AI career.

You have spent fifteen modules building a comprehensive foundation: from the basics of machine learning and neural networks through computer vision, natural language processing, generative AI, responsible AI, security and privacy, and the emerging frontier of the field. This module ties it all together.

[SLIDE: About the AI-900 Exam]

Let me start with the practical details you need to know.

The AI-900 exam is administered by Microsoft and Pearson VUE. It consists of 40 to 60 questions. The passing score is 700 out of 1000. The exam is available in English and several other languages, and it can be taken in person at a Pearson VUE test center or online with remote proctoring.

The cost is $165 USD, though Microsoft frequently offers discounted or free vouchers through academic programs, Microsoft Learn challenges, and virtual training events. Check the Microsoft Learn website and your academic institution's Microsoft partnership for current offers.

[SLIDE: The Five Exam Domains]

The AI-900 exam is organized into five domains, each covering a specific slice of AI knowledge. Here are the domains with their approximate weight in the exam:

- Domain 1: Describe AI workloads and considerations — 15 to 20 percent
- Domain 2: Describe fundamental principles of machine learning on Azure — 20 to 25 percent
- Domain 3: Describe features of computer vision workloads on Azure — 15 to 20 percent
- Domain 4: Describe features of natural language processing workloads on Azure — 15 to 20 percent
- Domain 5: Describe features of generative AI workloads on Azure — 15 to 20 percent

We will spend the bulk of this video reviewing each domain in depth.

---

## Segment 2: Domain 1 — AI Workloads and Considerations (Lines 31–60)

[SLIDE: Domain 1 Overview]

Domain 1 asks you to identify appropriate AI workloads for given scenarios and to describe the principles of responsible AI.

[SLIDE: Identify AI Workload Types]

The exam will present you with business scenarios and ask which type of AI workload is most appropriate. The key workload categories you must know are:

**Machine learning**: building predictive models from data. Use cases include churn prediction, demand forecasting, fraud detection, and price optimization.

**Computer vision**: analyzing image and video content. Use cases include defect detection, facial recognition, object counting, and medical imaging.

**Natural language processing**: understanding and generating human language. Use cases include sentiment analysis, entity extraction, document summarization, and chatbots.

**Conversational AI**: building dialog systems. Use cases include customer service bots, FAQ assistants, and virtual agents.

**Document intelligence**: extracting structured data from unstructured documents. Use cases include invoice processing, contract review, and form digitization.

[SLIDE: Responsible AI Principles]

Microsoft's six Responsible AI Principles appear repeatedly in Domain 1. You must know all six and be able to match them to scenarios.

**Fairness**: AI systems should treat all people equitably and not discriminate based on protected characteristics.

**Reliability and Safety**: AI systems should perform reliably and safely under expected and unexpected conditions.

**Privacy and Security**: AI systems should protect personal data and be resistant to attack.

**Inclusiveness**: AI systems should empower everyone and engage people broadly.

**Transparency**: AI systems should be understandable, and their purpose and limitations should be communicated clearly.

**Accountability**: People should be accountable for AI systems and their outcomes.

A common exam question pattern: given a scenario where an AI system produces biased outputs against a demographic group, which principle is most directly violated? The answer is fairness.

---

## Segment 3: Domain 2 — Machine Learning Principles on Azure (Lines 61–100)

[SLIDE: Domain 2 Overview]

Domain 2 is the most technically dense exam domain. It covers the core concepts of machine learning and how Azure ML implements them.

[SLIDE: Types of Machine Learning]

**Supervised learning** trains on labeled data — inputs paired with correct outputs. Two subcategories: classification (predicting a category) and regression (predicting a number).

**Unsupervised learning** trains on unlabeled data. Key techniques include clustering (grouping similar data points) and dimensionality reduction.

**Reinforcement learning** trains an agent through reward signals for desired behaviors. Used in robotics, game playing, and sequential decision-making.

**Semi-supervised learning** uses a small amount of labeled data combined with a large amount of unlabeled data. Useful when labeling is expensive.

**Self-supervised learning** creates labels automatically from the data itself — for example, predicting masked words in a sentence. This is how large language models are pre-trained.

[SLIDE: Model Evaluation Metrics]

Know these evaluation metrics cold for the exam.

For classification: **accuracy** (correct predictions divided by total predictions), **precision** (true positives divided by predicted positives), **recall** (true positives divided by actual positives), **F1 score** (harmonic mean of precision and recall), and **AUC-ROC** (area under the receiver operating characteristic curve).

For regression: **mean absolute error (MAE)**, **root mean squared error (RMSE)**, and **R-squared (coefficient of determination)**.

The exam frequently asks: which metric is most important when the cost of false negatives is very high? The answer is recall — because recall measures how many actual positives you correctly identified.

[SLIDE: Azure Machine Learning]

Azure ML is Microsoft's managed platform for the full ML lifecycle. Key components you must know:

**Azure ML Studio**: the web UI for creating, training, and deploying models.

**Automated ML (AutoML)**: automatically tries multiple algorithms and hyperparameters and selects the best-performing model.

**Azure ML Designer**: a drag-and-drop visual pipeline builder for no-code ML workflows.

**Compute clusters and instances**: managed compute for training and inference.

**Experiments and runs**: logging and tracking of training jobs.

**Model registry**: version-controlled storage for trained models.

**Inference endpoints**: real-time and batch deployment targets.

[SLIDE: Overfitting and Underfitting]

Two concepts that appear consistently in exam questions:

**Overfitting** occurs when a model learns the training data too well, including noise, and fails to generalize to new data. The model has high training accuracy but low validation accuracy. Remediated by regularization, dropout, cross-validation, and more training data.

**Underfitting** occurs when a model is too simple to capture the patterns in the data. Both training and validation accuracy are low. Remediated by using a more complex model or adding more features.

---

## Segment 4: Domain 3 — Computer Vision on Azure (Lines 101–130)

[SLIDE: Domain 3 Overview]

Domain 3 covers computer vision workloads and the Azure services that implement them.

[SLIDE: Core Computer Vision Tasks]

**Image classification**: assigns a single label to an entire image. Example: classifying chest X-rays as normal or abnormal.

**Object detection**: locates and labels multiple objects within an image using bounding boxes. Example: detecting pedestrians and vehicles in traffic camera footage.

**Semantic segmentation**: assigns a class label to every pixel. Example: identifying road surfaces, sidewalks, and buildings in satellite imagery.

**Instance segmentation**: like semantic segmentation but distinguishes between individual instances of the same class.

**Image generation**: creates new images from text prompts or reference images.

**Optical character recognition (OCR)**: extracts text from images and documents.

[SLIDE: Azure AI Vision Services]

**Azure AI Vision** (formerly Cognitive Services Computer Vision) provides pre-built APIs for image analysis, object detection, OCR, face detection, and spatial analysis.

**Azure AI Custom Vision** allows you to train custom image classification and object detection models without writing ML code, using a web-based labeling and training interface.

**Azure AI Face** provides face detection, verification, identification, and emotion analysis.

**Azure AI Document Intelligence** (formerly Form Recognizer) extracts structured fields from invoices, receipts, contracts, and custom document formats.

**Azure AI Video Indexer** analyzes video content for transcription, face identification, scene segmentation, and content moderation.

[SLIDE: Convolutional Neural Networks]

The foundational architecture behind computer vision is the **convolutional neural network (CNN)**. A CNN applies learned filters (convolutions) across an image to detect increasingly complex patterns: edges in early layers, shapes in middle layers, and object-level features in deep layers. Pooling layers reduce spatial dimensions, and fully connected layers produce the final classification.

For the exam, understand conceptually that CNNs learn hierarchical features through convolution and pooling — you will not be asked to implement one.

---

## Segment 5: Domain 4 — Natural Language Processing on Azure (Lines 131–165)

[SLIDE: Domain 4 Overview]

Domain 4 covers NLP workloads: understanding, analyzing, and generating human language using Azure AI services.

[SLIDE: Core NLP Tasks]

**Text classification**: assigns categories to text documents. Applications include sentiment analysis and topic classification.

**Named entity recognition (NER)**: identifies and classifies named entities — people, organizations, locations, dates, and quantities — in text.

**Key phrase extraction**: identifies the most important phrases in a document.

**Language detection**: identifies the language of a text sample.

**Sentiment analysis**: determines whether text expresses positive, negative, neutral, or mixed sentiment, typically at document and sentence level.

**Entity linking**: connects recognized entities to a knowledge base (such as Wikipedia).

**Translation**: converts text from one language to another.

**Summarization**: condenses a long document into a shorter representation while preserving key information.

**Question answering**: retrieves or generates answers to natural language questions from a document or knowledge base.

[SLIDE: Azure AI Language Services]

**Azure AI Language** (formerly Text Analytics and Language Understanding) provides pre-built NLP capabilities through REST APIs:

- Sentiment analysis and opinion mining
- Key phrase extraction
- Named entity recognition and entity linking
- Language detection
- Summarization (extractive and abstractive)
- Custom text classification
- Custom NER

**Azure AI Translator** provides neural machine translation across 100+ languages, with document translation and custom translation model support.

**Azure AI Speech** provides speech-to-text, text-to-speech, speaker recognition, and real-time translation.

**Azure AI Language Understanding (LUIS)** — now integrated into Azure AI Language as Conversational Language Understanding (CLU) — enables building custom intent recognition models for conversational applications.

**Azure AI Bot Service** provides managed infrastructure for deploying conversational bots connected to Azure AI Language.

[SLIDE: Transformers and Attention]

The foundational architecture behind modern NLP is the **transformer** (Vaswani et al., 2017). The key innovation is the **self-attention mechanism**, which allows every token in a sequence to attend to every other token, capturing long-range dependencies that earlier RNN-based models struggled with.

BERT (Bidirectional Encoder Representations from Transformers) pre-trains a transformer encoder on masked language modeling, producing general-purpose text representations that can be fine-tuned for downstream NLP tasks.

GPT (Generative Pre-trained Transformer) pre-trains a transformer decoder on next-token prediction, producing a model that can generate fluent text and be fine-tuned for many tasks.

---

## Segment 6: Domain 5 — Generative AI on Azure (Lines 166–200)

[SLIDE: Domain 5 Overview]

Domain 5 was added to the AI-900 exam in 2023 to reflect the rapid rise of generative AI. It covers large language models, Azure OpenAI Service, and responsible generative AI practices.

[SLIDE: What Is Generative AI?]

**Generative AI** refers to AI systems that create new content — text, images, code, audio, or video — rather than classifying or predicting from existing data.

Large language models are trained on massive text corpora using self-supervised learning — predicting the next token given all preceding tokens. Through this process, they develop broad knowledge and reasoning capabilities that can be applied to a wide variety of tasks.

[SLIDE: Azure OpenAI Service]

**Azure OpenAI Service** provides enterprise-grade access to OpenAI models — including GPT-4, GPT-4o, DALL-E 3, and the Embeddings API — through Azure's infrastructure with:

- Private network deployment options
- Azure Active Directory authentication
- Content filtering and safety features
- Compliance with Azure's regulatory certifications

Key concepts for the exam:

**Prompt engineering**: crafting inputs to guide model behavior. Techniques include zero-shot prompting, few-shot prompting with examples, chain-of-thought prompting for step-by-step reasoning, and system messages that establish model persona and constraints.

**Tokens**: the units of text that LLMs process. Models have context window limits measured in tokens (e.g., GPT-4 Turbo supports 128,000 tokens).

**Temperature**: a parameter controlling output randomness. Temperature 0 produces deterministic, focused outputs; higher temperatures produce more varied and creative outputs.

[SLIDE: Retrieval-Augmented Generation]

**Retrieval-Augmented Generation (RAG)** is an architecture that grounds LLM responses in retrieved documents rather than relying solely on parametric knowledge. The process:

1. User submits a query
2. A retrieval component searches a vector index for relevant document chunks
3. Retrieved chunks are included in the LLM prompt as context
4. The LLM generates a response grounded in the retrieved context

RAG reduces hallucination, enables knowledge cutoff bypass, and allows domain-specific grounding without model fine-tuning. **Azure AI Search** with vector search capabilities is the standard Azure component for RAG retrieval.

[SLIDE: Responsible Generative AI]

The exam emphasizes responsible practices for generative AI systems. Four key considerations:

**Harmful content**: LLMs can generate offensive, dangerous, or misleading content. Azure OpenAI's content filtering layers can block generation of specified content categories.

**Prompt injection**: malicious inputs attempt to override system instructions and cause unintended outputs. Defenses include input validation, system prompt hardening, and monitoring.

**Hallucination**: LLMs confidently generate plausible-sounding but factually incorrect information. RAG grounding, temperature reduction, and output verification pipelines help mitigate this.

**Intellectual property**: generative AI may reproduce copyrighted training content. Microsoft's Copilot Copyright Commitment provides legal protection for enterprise Azure OpenAI customers.

[SLIDE: DALL-E and Image Generation]

**DALL-E 3**, accessible through Azure OpenAI, generates images from natural language text prompts. The model translates textual descriptions into photorealistic or artistic images, enabling applications in marketing, design, education, and accessibility.

For the exam, understand that DALL-E is a text-to-image generative model available through Azure OpenAI Service, distinct from Azure AI Vision's image analysis capabilities.

---

## Segment 7: Exam Strategy and Capstone (Lines 201–220)

[SLIDE: Exam Day Strategy]

Here is my exam-day advice based on the structure of the AI-900 exam.

Read every question carefully. Many questions include a scenario that provides context — do not skip the scenario and jump to the answer choices.

Eliminate obviously wrong answers first. With four choices, eliminating two leaves you with a 50-50 shot if you are genuinely uncertain.

Watch for qualifier words: "most appropriate," "primary," "best describes." These words tell you that multiple answers may be partially correct, and you must identify the best one.

Do not leave questions blank. There is no penalty for wrong answers, so always select your best guess.

Flag uncertain questions and review them at the end, but do not change answers without a concrete reason to do so.

[SLIDE: Study Resources]

**Microsoft Learn**: The official free study path for AI-900 at learn.microsoft.com/certifications/exams/ai-900 covers all five domains with interactive modules, knowledge checks, and hands-on Azure exercises.

**AI-900 Practice Assessment**: Microsoft provides a free official practice assessment through Microsoft Learn. Take it at least twice before your exam date.

**Azure AI Documentation**: Reading the product documentation for Azure AI Vision, Azure AI Language, and Azure OpenAI Service reinforces the service-specific knowledge tested in Domains 3–5.

**This Course**: Everything in Modules 1–15 maps to the five exam domains. Use the reading guides and quiz answer keys as review references.

[SLIDE: Capstone Reflection]

As we close out CIS-4330, I want you to reflect on the full arc of this course.

You started by understanding what intelligence means computationally. You learned how machines learn from data, how they see, how they read and write language, and how they generate entirely new content. You learned how to build and deploy these systems responsibly, how to protect them from attack, and where the field is heading.

The AI-900 exam is one milestone on this journey, not the destination. The practitioners who will shape this field are the ones who combine technical knowledge with ethical reasoning, security awareness, and the ability to communicate clearly to non-technical stakeholders.

You have built that foundation here. Go build something with it.

Good luck on your exam, and I will see you at certification.

---

*Script Line Count: 220 | Estimated Runtime: 26–30 minutes*
