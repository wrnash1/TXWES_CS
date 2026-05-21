# Reading Guide: Module 10 - Responsible AI: Ethics, Fairness, and Transparency
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 10 - Responsible AI: Ethics, Fairness, and Transparency**! This module covers Microsoft's framework for building AI systems that are trustworthy, equitable, and explainable. Responsible AI is directly tested on the **AI-900 (Microsoft Azure AI Fundamentals)** exam as one of its core knowledge areas, and understanding Microsoft's six guiding principles is essential for both the certification and for ethical real-world AI development.

As a student, you will also study NLP text preprocessing fundamentals — tokenization, stop-word removal, lemmatization, and bag-of-words representation — which are the building blocks for every language AI feature you have encountered so far in this course. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Microsoft's Responsible AI principles (Fairness, Reliability, Privacy/Security, Inclusiveness, Transparency, Accountability)**: Microsoft's six-principle framework for ethical AI development. Fairness means AI systems should treat all people equitably without bias based on protected characteristics. Reliability and Safety means systems should perform consistently and fail safely. Privacy and Security means training data and model outputs must respect user data rights. Inclusiveness means AI should serve and benefit all people regardless of ability or background. Transparency means AI decisions and capabilities should be explainable. Accountability means humans must remain responsible for AI system outcomes.
*   **Tokenization**: The NLP preprocessing step that splits a raw text string into a sequence of individual tokens — typically words and punctuation marks. Tokenization is the first step in almost every NLP pipeline because downstream operations (stop-word removal, vectorization, model training) all require text to be in discrete token form before they can process it.
*   **Stop-word removal and lemmatization**: Stop-word removal filters out high-frequency words with little semantic value (e.g., "the," "is," "and") to reduce noise and dimensionality in text feature vectors. Lemmatization reduces each token to its dictionary root form (lemma) — for example, "running," "ran," and "runs" all reduce to "run" — so the model treats morphological variants of the same word as a single feature.
*   **Bag-of-words (BoW) representation**: A text vectorization method that converts a document into a fixed-length numeric vector by counting how many times each vocabulary word appears, ignoring word order and grammar. While simple, BoW is effective for tasks like spam detection and sentiment classification. Its main limitation is that it loses context and meaning conveyed by word sequence.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** Microsoft's six Responsible AI principles are tested by name and by scenario. Know which principle applies to which situation: a hiring algorithm that disadvantages one demographic → **Fairness**. A self-driving system that fails unpredictably in rain → **Reliability and Safety**. A model that collects biometric data without user consent → **Privacy and Security**. A model that cannot explain why it denied a loan → **Transparency**. An AI deployed with no human oversight → **Accountability**. The exam presents scenarios and asks you to identify the principle being violated or upheld.
*   **Common AI-900 Trap:** The exam distinguishes **Transparency** (the AI's decision-making process can be understood and explained) from **Accountability** (humans take responsibility for AI outcomes and maintain oversight). A question about "explaining why an AI made a decision" → Transparency. A question about "who is responsible when AI causes harm" → Accountability. Students frequently swap these two; practice applying them to real scenarios to build the distinction.
*   **Study Resource:** The Microsoft Learn module [Fundamental AI Concepts](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/) includes a dedicated section on Microsoft's Responsible AI principles with scenario-based examples. It is free and maps directly to the AI-900 exam's Responsible AI knowledge area. A companion resource, the [Microsoft Responsible AI Standards](https://www.microsoft.com/en-us/ai/responsible-ai), provides the authoritative documentation behind the principles.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters on ethics in AI, fairness, and natural language processing in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). This freely available textbook by Poole and Mackworth addresses ethical considerations in AI system design as well as the NLP techniques (tokenization, bag-of-words) that are foundational to text-based AI services.
*   **Required Video:** Watch the Responsible AI and NLP fundamentals segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video covers Microsoft's six Responsible AI principles with concrete business examples and explains how they are applied across Azure AI services.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Tokenize a sample paragraph into individual words using NLTK**: Call `nltk.word_tokenize(text)` on a sample paragraph, then print the resulting list of tokens to observe how the library handles punctuation, contractions, and whitespace boundaries.
*   **Filter out common stop words**: Import `stopwords` from `nltk.corpus`, build a set of English stop words, and use a list comprehension to remove them from the token list — comparing word counts before and after to see the vocabulary reduction.
*   **Perform sentiment scoring on text segments using TextBlob or VADER**: Apply `TextBlob(text).sentiment.polarity` (range −1 to +1) to several product review sentences and classify each as positive, negative, or neutral, observing how preprocessing choices affect the final polarity score.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapters on AI ethics and NLP in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on Responsible AI and NLP in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
