# Reading Guide: Module 16 - Final Exam Prep and Microsoft AI-900 Certification
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 16 - Final Exam Prep and Microsoft AI-900 Certification**! This final module consolidates everything covered across the course and prepares you to sit the **Microsoft Azure AI Fundamentals (AI-900)** certification exam with confidence. The AI-900 exam tests your ability to describe AI workloads, identify appropriate Azure AI services for given scenarios, explain how machine learning works, and apply Microsoft's Responsible AI principles — all of which have been covered in detail throughout this course.

As a student, you will use this module to review key exam domains, identify any remaining knowledge gaps, practice with realistic scenario-based questions, and understand the exam registration and testing process. Complete the glossary review and checklist before your final exam attempt.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **AI-900 exam domain summary**: The AI-900 exam covers five knowledge domains: (1) AI workloads and considerations (15–20% of exam — what AI can do, Responsible AI principles); (2) Fundamental principles of machine learning on Azure (20–25% — supervised, unsupervised, Azure ML tools); (3) Computer vision workloads on Azure (15–20% — Azure AI Vision, Custom Vision, Face API); (4) Natural language processing on Azure (15–20% — Azure AI Language, Translator, CLU, Speech); (5) Generative AI workloads on Azure (15–20% — Azure OpenAI Service, prompt engineering, embeddings). Each domain maps to modules covered in this course.
*   **Azure AI service selection decision rules**: The most commonly tested skill is choosing the right Azure service for a scenario. Use these rules: "pre-built image analysis" → Azure AI Vision. "Train with my own images" → Azure Custom Vision. "Extract text from documents" → Azure AI Vision (OCR) or Azure Form Recognizer. "Analyze sentiment / key phrases" → Azure AI Language. "Translate text" → Azure Translator. "Understand user intent in conversation" → CLU. "Build a bot" → Azure Bot Service. "Generate text / code" → Azure OpenAI Service. "Detect anomalies in time-series" → Azure Anomaly Detector.
*   **Microsoft Responsible AI principles — complete set**: Fairness (equitable treatment, no discriminatory bias), Reliability and Safety (consistent, fail-safe behavior), Privacy and Security (data rights, consent, protection), Inclusiveness (serves all people including those with disabilities), Transparency (explainable AI, clear capability disclosures), Accountability (humans remain responsible; oversight mechanisms required). All six are tested by name and by scenario on the AI-900 exam.
*   **Generative AI key concepts for AI-900**: Know the distinction between **foundation models** (large pre-trained models like GPT-4), **prompt engineering** (guiding output without changing weights), **fine-tuning** (adapting weights with domain-specific data), and **Retrieval-Augmented Generation / RAG** (grounding LLM responses in retrieved source documents to reduce hallucination). The exam also tests that **Azure OpenAI Service** provides enterprise access to these models with data residency, compliance, and content safety controls.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area — exam registration and format**: The AI-900 exam consists of 40–60 multiple-choice and scenario-based questions, completed in 60 minutes with a passing score of 700/1000. It can be taken online with a remote proctor or at a Pearson VUE test center. Register at [Microsoft Learn Certifications](https://learn.microsoft.com/en-us/certifications/exams/ai-900/) — students often qualify for exam discounts through Microsoft Imagine or academic programs. The exam is not adaptive; all questions carry equal weight.
*   **Common AI-900 Trap — service confusion on scenario questions**: The highest-error-rate questions ask you to match a business scenario to a service. Review these high-confusion pairs one final time: Azure AI Vision vs. Azure Custom Vision (pre-built vs. train-your-own). Azure AI Language vs. Azure Translator (understand meaning vs. translate language). CLU vs. Custom Question Answering (intent from conversation vs. answers from a FAQ document). Azure Machine Learning vs. Azure Cognitive Services (custom training vs. pre-built API). Azure Anomaly Detector vs. Azure Monitor (ML-based pattern deviation vs. threshold-based alerting).
*   **Study Resource:** The Microsoft Learn AI-900 exam preparation page [Exam AI-900: Microsoft Azure AI Fundamentals](https://learn.microsoft.com/en-us/certifications/exams/ai-900/) lists all official study materials, links to free practice assessments, and the complete exam skills outline. Complete the free [AI-900 practice assessment](https://learn.microsoft.com/en-us/certifications/exams/ai-900/practice/assessment?assessmentId=26&assessment-type=practice) on Microsoft Learn before your exam — it uses retired exam questions and is the most accurate predictor of your readiness.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the full table of contents and chapter summaries of the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). Focus your review on the sections most directly mapped to AI-900: supervised learning (Modules 2–3), neural networks (Module 4), NLP (Modules 5 and 10), computer vision (Modules 6 and 9), Responsible AI (Module 10), and generative AI (Module 11). This freely available textbook by Poole and Mackworth provides the theoretical grounding behind every Azure AI service on the exam.
*   **Required Video:** Watch the full AI-900 exam review and certification prep segment of the official preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video includes a comprehensive final review of all five AI-900 exam domains with sample questions, common pitfalls, and last-minute exam strategy — the most efficient use of your final study hours before sitting the certification exam.

---

### Lab & Command Integration
In this module's final lab activity, you will consolidate and demonstrate mastery of the complete Python ML pipeline covered across the course:
*   **End-to-end pipeline review**: Starting from `pd.read_csv()` data loading through feature engineering, `model.fit()` training, `model.predict()` inference, and `accuracy_score()` / `classification_report()` evaluation — run the complete pipeline on a new dataset, documenting each step and its purpose in a Jupyter notebook.
*   **Azure service scenario mapping exercise**: For each of the 10 Azure AI services covered in the course (Azure AI Vision, Custom Vision, Face API, Azure AI Language, Translator, CLU, Azure Bot Service, Azure Machine Learning, Azure OpenAI Service, Azure Anomaly Detector), write one realistic business scenario where that service is the correct answer — then write one scenario where each is a distractor.
*   **Mock AI-900 exam practice**: Complete the Microsoft Learn free practice assessment at [AI-900 Practice Assessment](https://learn.microsoft.com/en-us/certifications/exams/ai-900/practice/assessment?assessmentId=26&assessment-type=practice), record your score, identify the question categories you missed, and revisit the corresponding module reading guides before your certification exam date.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and review all definitions from Modules 1–15.
*   [ ] Complete the final chapters review in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the full AI-900 exam review video in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Complete the Microsoft Learn [AI-900 Practice Assessment](https://learn.microsoft.com/en-us/certifications/exams/ai-900/practice/assessment?assessmentId=26&assessment-type=practice).
*   [ ] Register for your AI-900 exam at [Microsoft Learn Certifications](https://learn.microsoft.com/en-us/certifications/exams/ai-900/).
*   [ ] Proceed to the final course exam activity.
