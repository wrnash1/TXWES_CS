# Video Script: Module 16 — AI-900 Exam Preparation and Capstone

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Production Notes

- **Runtime Target:** 30–35 minutes
- **Slide Deck:** M16_Slides.pptx
- **Graphics:** Domain percentage wheel; exam strategy checklist; concept maps for each domain
- **Tone:** Confident, energizing, direct; this is the pre-game speech

---

## SEGMENT 1 — Welcome and Context (Slides 1–3) [3 min]

[ON CAMERA]

Welcome to Module 16 — the final module of CIS-4330. You have worked through 15 modules covering the breadth of artificial intelligence, from fundamental concepts to cutting-edge emerging technologies. Everything in this final module is designed to do one thing: make sure you walk into the AI-900 exam with maximum confidence and maximum preparation.

Let me give you the facts about this exam. The AI-900 is a 45-minute, 40–60 question multiple choice exam. It is designed as a foundational certification — not an expert-level test. Microsoft describes it as appropriate for people who are just beginning to work with AI-based solutions and services. If you have engaged with this course, you are more than prepared.

[SLIDE 1: Title — "AI-900 Exam Preparation and Capstone"]

[SLIDE 2: Exam Overview Facts]

The key facts:

- **Exam code:** AI-900
- **Duration:** 45 minutes (but registered through Pearson VUE; arrive 30 minutes early)
- **Question count:** 40–60 questions
- **Passing score:** 700 out of 1000
- **Cost:** $165 USD (discounted for students; check Microsoft's student resources)
- **Format:** Multiple choice, drag-and-drop, yes/no answer sets, ordering
- **Delivery:** Online proctored or in-person testing center

[SLIDE 3: This Is Achievable]

I want to say this directly: if you have completed the labs, watched the lectures, and done the quizzes in this course, you are prepared to pass this exam. The AI-900 tests understanding, not memorization of API parameters or code syntax. The questions look very much like what we have practiced throughout the semester.

---

## SEGMENT 2 — Domain Breakdown (Slides 4–7) [6 min]

[SLIDE 4: The Five Exam Domains]

The AI-900 exam covers five content domains. Let me give you each one with its approximate weighting and which modules in our course covered it.

[SLIDE 5: Domain 1 — AI Workloads and Considerations (15–20%)]

This domain asks: what kinds of problems can AI solve, and what considerations must be kept in mind when deploying AI?

Key topics:

- Identifying appropriate AI workload types (prediction, computer vision, NLP, generative AI)
- Recognizing responsible AI principles (fairness, reliability, privacy, inclusiveness, transparency, accountability)
- Identifying whether a scenario requires AI versus rule-based logic

Our course coverage: Modules 1–3 (foundational concepts), Module 13 (AI in business), Module 14 (responsible AI).

**Exam Tip:** Know the six responsible AI principles by name and be able to identify which principle is at risk in a given scenario.

[SLIDE 6: Domain 2 — Fundamental Machine Learning Principles on Azure (20–25%)]

This is the most technically substantive domain. Topics include:

- Supervised vs. unsupervised vs. reinforcement learning
- Regression, classification, and clustering
- Training vs. validation vs. test datasets
- Model evaluation metrics (accuracy, precision, recall, AUC)
- Azure Machine Learning workspace components
- AutoML and the Designer
- Feature engineering concepts

Our course coverage: Modules 4–7 (ML fundamentals), Module 12 (MLOps, AML workspace).

**Exam Tip:** Know the difference between classification (predicting a category) and regression (predicting a number), and be able to match each to a business scenario.

[SLIDE 7: Domains 3, 4, and 5]

**Domain 3 — Computer Vision Features on Azure (15–20%)**

Topics:

- Image classification, object detection, image segmentation
- Face detection and recognition
- Optical character recognition
- Azure AI Vision, Custom Vision, Face API
- Responsible use of face recognition

Our course coverage: Modules 8–9.

**Domain 4 — Natural Language Processing Features on Azure (15–20%)**

Topics:

- Text analysis: key phrase extraction, sentiment analysis, entity recognition, language detection
- Speech: speech-to-text, text-to-speech, speech translation
- Language understanding: intent classification, entity extraction (CLU)
- Translation
- Azure AI Language, Azure AI Speech, Language Understanding service

Our course coverage: Modules 10–11.

**Domain 5 — Generative AI Features on Azure (25–30%)**

Topics:

- Large language models and their capabilities
- Prompt engineering concepts
- Azure OpenAI Service and its capabilities (GPT, DALL-E, Whisper, embeddings)
- Responsible generative AI practices
- Retrieval Augmented Generation (RAG)
- Copilot concepts

Our course coverage: Module 11 (generative AI), Module 15 (multimodal AI, agents).

**Exam Tip:** Domain 5 has the highest weighting. Spend the most review time here. Know what Azure OpenAI can do, what DALL-E does, what embeddings are used for, and what RAG means.

---

## SEGMENT 3 — Domain-by-Domain Concept Review (Slides 8–20) [12 min]

[SLIDE 8: Domain 1 Flash Review — AI Types]

Let me run through the key facts you must know for each domain.

**Domain 1 Flash Cards:**

Anomaly detection = identifying unusual patterns (fraud, equipment failure).

Computer vision = extracting meaning from images (classify, detect, segment).

Natural language processing = analyzing and generating text and speech.

Predictive analytics = forecasting future values from historical data.

Generative AI = creating new content — text, images, code, audio.

The responsible AI principle at risk when a credit model produces lower approval rates for a minority group is: **Fairness**.

The responsible AI principle at risk when a medical AI cannot explain why it flagged a patient is: **Transparency**.

[SLIDE 9: Domain 2 Flash Review — ML Fundamentals]

**Supervised learning** = training with labeled data (you know the correct answer).

**Unsupervised learning** = finding patterns in unlabeled data (clustering).

**Reinforcement learning** = learning through reward signals (games, robots).

**Regression** = predicts a continuous number. Example: predict house price.

**Classification** = predicts a category. Example: spam / not spam.

**Clustering** = groups similar items. Example: customer segments.

**Features** = input variables used to make predictions.

**Label** = the correct output the model is trying to predict.

**Overfitting** = model memorizes training data, fails on new data.

**Underfitting** = model is too simple, misses patterns in training data.

[SLIDE 10: Domain 2 Flash Review — Azure ML]

**Azure ML workspace** = top-level resource containing all ML assets.

**Compute instance** = single-node personal dev VM.

**Compute cluster** = auto-scaling pool for training jobs.

**AutoML** = automated algorithm and hyperparameter selection.

**Designer** = drag-and-drop pipeline builder.

**Model registry** = versioned store of trained models.

**Online endpoint** = real-time inference API.

**Batch endpoint** = asynchronous bulk scoring.

**Data drift** = distribution shift in input features over time.

[SLIDE 11: Domain 2 Flash Review — Evaluation Metrics]

These are tested frequently. Know each one.

**Accuracy** = (True Positives + True Negatives) / Total. Good for balanced classes.

**Precision** = True Positives / (True Positives + False Positives). Measures: of all the things the model predicted positive, how many actually were?

**Recall (Sensitivity)** = True Positives / (True Positives + False Negatives). Measures: of all the actual positives, how many did the model find?

**F1 Score** = harmonic mean of Precision and Recall. Use when both matter equally.

**AUC-ROC** = Area Under the ROC Curve. Measures overall classifier performance across all thresholds. Closer to 1.0 = better.

**RMSE (Root Mean Square Error)** = typical error magnitude for regression models. Lower is better.

[SLIDE 12: Domain 3 Flash Review — Computer Vision]

**Image classification** = assign a single label to the whole image.

**Object detection** = identify and locate multiple objects with bounding boxes.

**Semantic segmentation** = classify every pixel into a category.

**Instance segmentation** = segmentation that distinguishes between individual objects.

**OCR** = extract printed or handwritten text from images.

**Face detection** = find faces in an image.

**Face recognition** = identify whose face it is.

**Azure Computer Vision** = pre-built general-purpose image analysis API.

**Custom Vision** = train a custom image classifier or object detector with your own images.

**Face API** = detection, recognition, and verification for human faces.

**Content moderator** = detect offensive or inappropriate image content.

[SLIDE 13: Domain 3 — Responsible Face Recognition]

The exam will include scenarios about responsible use of face recognition. Key principles:

- Face recognition should not be used for real-time surveillance of individuals in public spaces without consent
- Law enforcement use cases require heightened legal authorization and oversight
- Systems must be tested for demographic fairness — error rates must not be higher for any racial or ethnic group
- Users should be informed when facial analysis is in use

Microsoft has published a Responsible AI Standard specifically addressing facial recognition. Know that this service has usage guidelines and that some use cases are explicitly prohibited.

[SLIDE 14: Domain 4 Flash Review — NLP]

**Key phrase extraction** = identify the main topics or concepts in text.

**Sentiment analysis** = determine whether text is positive, negative, or neutral.

**Named entity recognition (NER)** = identify specific entities — persons, organizations, locations, dates, quantities.

**Language detection** = identify which language a text is written in.

**Text summarization** = condense long text into shorter form.

**Question answering** = extract an answer to a natural language question from a document.

**Custom Named Entity Recognition** = train a model to recognize domain-specific entities.

**Azure AI Language** = the primary Azure service for all text analytics capabilities.

[SLIDE 15: Domain 4 Flash Review — Speech and Translation]

**Speech-to-text** = transcribe spoken audio to written text.

**Text-to-speech** = convert text to natural-sounding speech audio.

**Speech translation** = transcribe speech in one language and translate to another.

**Language understanding (CLU)** = extract user intent and named entities from conversational utterances.

**Azure AI Speech** = service providing speech-to-text, text-to-speech, and translation.

**Language Understanding (LUIS / CLU)** = classify user intent in natural language conversation.

**Azure AI Translator** = translate text between 100+ languages.

Common exam scenario: "A company wants to transcribe customer service calls into text and analyze sentiment" → Azure AI Speech + Azure AI Language.

[SLIDE 16: Domain 5 Flash Review — Generative AI]

**Large Language Model (LLM)** = a neural network trained on vast text corpora that can generate, summarize, translate, and analyze text.

**Transformer architecture** = the neural architecture underlying all modern LLMs. Uses self-attention to model relationships between words across long contexts.

**Foundation model** = a large, general-purpose model that can be fine-tuned or prompted for many tasks without retraining from scratch.

**Prompt engineering** = crafting input prompts to guide LLM outputs. Includes few-shot prompting (examples in the prompt), chain-of-thought (asking the model to reason step by step), and system messages.

**Token** = the unit of text processed by an LLM. Roughly 1 token per word.

**Temperature** = controls output randomness. Low temperature = deterministic; high temperature = creative/variable.

[SLIDE 17: Domain 5 Flash Review — Azure OpenAI]

**GPT-4 (and variants)** = text generation, analysis, code, reasoning.

**GPT-4V / GPT-4o** = multimodal; accepts image + text inputs.

**DALL-E 3** = text-to-image generation.

**Whisper** = speech-to-text.

**Embeddings API** = convert text to numerical vector representations for semantic search and similarity.

**Azure OpenAI Service** = Microsoft's managed access to OpenAI models with enterprise security, compliance, and content filtering.

[SLIDE 18: Domain 5 Flash Review — RAG and Copilot]

**Retrieval Augmented Generation (RAG)** = pattern where the LLM's response is grounded by retrieved documents from a knowledge base. Reduces hallucination and enables the model to use up-to-date or proprietary information it was not trained on.

**Vector database** = stores text as embeddings (vectors) to enable semantic similarity search. Used in RAG architectures.

**Azure AI Search** = Azure's vector and keyword search service, commonly used in RAG pipelines.

**Copilot** = Microsoft's branded AI assistant embedded in products (Microsoft 365 Copilot, GitHub Copilot, Bing). Uses Azure OpenAI under the hood.

**Content filtering** = Azure OpenAI applies safety classifiers to inputs and outputs to prevent harmful content. This is a responsible AI control.

[SLIDE 19: Generative AI — Responsible Use]

The exam tests whether you know the responsible use requirements for generative AI.

**Groundedness** = model responses should be based on factual information, not confabulated.

**Transparency** = users should know they are interacting with AI-generated content.

**Harm prevention** = content filters prevent generation of harmful, violent, or illegal content.

**Bias mitigation** = LLMs trained on web data reflect societal biases; responsible deployment requires monitoring and mitigation.

**Avoiding over-reliance** = users should verify AI-generated content, especially for high-stakes decisions.

**Data privacy** = user inputs to LLMs should not be used to train future models without consent.

[SLIDE 20: The Six Responsible AI Principles — Master List]

Memorize these. They appear in multiple domains.

1. **Fairness** — AI systems should treat all people equitably. No disparate impact on protected groups.

2. **Reliability and Safety** — AI systems should perform as expected and fail gracefully. Testing and validation are required.

3. **Privacy and Security** — AI systems must protect personal data and be secure against attacks.

4. **Inclusiveness** — AI systems should empower everyone and engage people of all abilities and backgrounds.

5. **Transparency** — AI systems and their limitations should be understandable to the people who use and are affected by them.

6. **Accountability** — People and organizations should be accountable for AI systems and their impacts.

---

## SEGMENT 4 — Exam Strategy (Slides 21–24) [5 min]

[SLIDE 21: Question Types and How to Approach Each]

**Multiple choice (single best answer)**

Most of the exam. Strategy: eliminate obviously wrong answers first. Often two answers are close — read carefully for the specific context. "Most appropriate" means there may be more than one valid approach, but one is *most* fitting.

**Yes/No / True/False answer sets**

Common format: "For each scenario, select whether the statement is true or false." Treat each independently. Do not let an earlier answer in the set influence later ones.

**Drag and drop / matching**

Match services to scenarios or put steps in order. Know the primary use case for each Azure AI service.

[SLIDE 22: Common Trap Questions]

Watch out for these patterns:

**Trap 1: The almost-right service.** Azure AI Language and Azure AI Speech are separate services. Know which does text analysis (Language) and which does audio (Speech).

**Trap 2: AutoML vs. Designer vs. Custom Vision.** AutoML = tabular data, algorithm search. Designer = pipeline builder. Custom Vision = image classification/detection. Do not mix these up.

**Trap 3: Classification vs. Regression.** Predicting a price = regression. Predicting a category = classification. When the question says "predict whether," it is classification. "Predict how much" is regression.

**Trap 4: Online vs. Batch endpoints.** Online = real-time, low latency. Batch = large volumes, no latency requirement. The question will include timing language — look for it.

**Trap 5: Which responsible AI principle is violated?** The question will describe a scenario and ask which principle is most at risk. Map: unfair outcomes → Fairness. No explanation → Transparency. Privacy violation → Privacy and Security. Unpredictable behavior → Reliability.

[SLIDE 23: Day-Before and Day-Of Strategy]

**Day before:**

- Review your module quizzes — identify any areas where you scored below 80%
- Do the 20 practice questions in the Module 16 Lab (quiz document)
- Review the Domain 5 flash cards (highest weight)
- Do NOT try to learn new material the night before
- Get 8 hours of sleep

**Day of:**

- Eat a real meal before the exam — cognitive performance is affected by hunger
- If testing online: test your internet connection, webcam, and microphone 2 hours before
- Arrive at the testing center 30 minutes early
- Bring a valid government-issued ID
- Do not overthink questions — your first instinct is usually correct on foundational exams

**During the exam:**

- Flag uncertain questions and come back if time allows
- Read every answer choice before selecting — do not stop at the first plausible answer
- If you are genuinely stuck, eliminate two wrong answers and make an educated guess — there is no penalty for wrong answers

[SLIDE 24: Using Microsoft Learn for Final Review]

Microsoft Learn is the official study resource and it is free. The AI-900 learning path is at `https://learn.microsoft.com/en-us/certifications/azure-ai-fundamentals/`.

The learning path covers all five domains with interactive modules, knowledge checks, and sandbox environments. Complete any modules you have not yet touched. The knowledge checks at the end of each section are excellent exam practice.

Also visit `https://examtopics.com/exams/microsoft/ai-900/` for community-submitted practice questions. These are not official, but they reflect the style and difficulty of real exam questions.

---

## SEGMENT 5 — Capstone Reflection and Closing (Slides 25–28) [4 min]

[SLIDE 25: What You Have Accomplished]

Over 16 modules, you have covered:

- The history and foundations of AI
- Machine learning algorithms and principles
- Computer vision and image analysis
- Natural language processing and speech AI
- Generative AI and large language models
- MLOps and the model lifecycle
- AI applications across healthcare, finance, retail, and manufacturing
- AI security: adversarial attacks, differential privacy, compliance
- Emerging technologies: multimodal AI, agents, edge AI, federated learning

That is the full breadth of what the AI-900 tests and significantly more depth than the exam requires.

[SLIDE 26: The Bigger Picture]

But I want to close with something beyond the exam. The technologies we have studied are reshaping every industry and every profession. The question is not whether AI will affect your career — it will. The question is whether you will be the person who understands it, shapes it, and applies it responsibly, or the person to whom it happens.

This course has given you the conceptual foundation. The certification gives you the credential. What you do with that foundation is up to you.

[SLIDE 27: Professor Nash's Final Recommendations]

Three things I want you to do after this course:

First: Take the AI-900 exam within 60 days. The knowledge is fresh now. Every month you wait, you lose retention.

Second: Build something with AI. Any AI. Use Azure AI services to build a small application — even a personal project — that solves a real problem you care about. Nothing consolidates learning like building.

Third: Stay curious. The AI field moves fast. Subscribe to one newsletter, follow one researcher on LinkedIn, and set aside 30 minutes a week to read about what is changing. That habit, sustained for a decade, compounds into expertise.

[SLIDE 28: Closing]

It has been a privilege teaching this course. I genuinely believe that AI literacy — the ability to understand, evaluate, and apply AI thoughtfully — is one of the most important skills of the next 30 years.

You are now AI literate. Go use it well.

[END OF VIDEO]

---

*Script prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
