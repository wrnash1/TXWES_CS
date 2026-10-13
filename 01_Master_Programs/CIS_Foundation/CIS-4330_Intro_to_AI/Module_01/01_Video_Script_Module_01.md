# Video Script: Module 01 - Introduction to AI and Machine Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AI-900 Domain:** Describe Artificial Intelligence workloads and considerations (15-20%)

---

## [00:00 - 01:30] Opening and Welcome

Good morning, good afternoon, or good evening — wherever you are joining from, welcome to CIS-4330, Introduction to Artificial Intelligence, here at Texas Wesleyan University. I am Professor Nash, and I am genuinely excited to work through this material with you.

Before we dive in, I want to frame exactly what this course is. CIS-4330 is designed with one clear target on the horizon: the Microsoft AI-900 certification, also called Azure AI Fundamentals. That certification is a recognized industry credential that signals you understand the core concepts of AI, machine learning, and how Microsoft Azure delivers AI services at scale.

Every module in this course maps directly to an AI-900 exam domain. Today's module covers the first and most foundational domain: describing AI workloads and the core concepts behind machine learning. You will not need prior experience with calculus or statistics to follow this lecture. What you do need is curiosity and careful attention to vocabulary — because on the AI-900 exam, precise terminology is everything.

Let us get started.

---

## [01:30 - 04:00] What Is Artificial Intelligence?

The term artificial intelligence has been used since 1956, when computer scientist John McCarthy coined it at the Dartmouth Conference. But the concept has evolved dramatically. For our purposes — and specifically for the AI-900 exam — here is the definition you need to internalize:

Artificial intelligence is the capability of a computer system to perform tasks that would normally require human intelligence.

That definition comes directly from Microsoft's learning framework, and it is important because it is deliberately broad. AI is not one algorithm or one technology. It is an umbrella term that covers a wide range of capabilities.

Microsoft organizes AI into five major workload categories on the AI-900 exam. Write these down:

- Machine learning
- Computer vision
- Natural language processing
- Conversational AI
- Anomaly detection and knowledge mining

We will spend dedicated modules on each of these. For today, the key insight is this: all of these are forms of AI, but they work in fundamentally different ways and they serve different business purposes.

Here is an analogy I use. Think of AI as the category "vehicle." Under that category, you have cars, trucks, motorcycles, and bicycles. They are all vehicles, but they operate differently and you would use them for different tasks. Machine learning is like the engine inside many of those vehicles — it is the core mechanism that powers a large portion of modern AI.

---

## [04:00 - 07:00] The AI, Machine Learning, and Deep Learning Hierarchy

[SHOW DIAGRAM: Three concentric circles. Outermost circle labeled "Artificial Intelligence." Middle circle labeled "Machine Learning." Innermost circle labeled "Deep Learning."]

This nested diagram is one of the most tested visuals on the AI-900 exam. Let me walk through each layer.

The outermost circle is Artificial Intelligence. It encompasses every approach where a machine mimics cognitive functions. This includes rule-based expert systems from the 1980s, which did not learn at all — they simply followed programmed if-then rules. AI does not require learning; it requires intelligent-seeming behavior.

The middle circle is Machine Learning. Machine learning is a subset of AI in which the system learns from data rather than following hand-coded rules. The programmer does not write explicit decision logic. Instead, the programmer provides examples — labeled data — and an algorithm finds the patterns automatically. This shift from rule-writing to data-driven learning is the defining characteristic of the ML era.

The innermost circle is Deep Learning. Deep learning is a subset of machine learning that uses artificial neural networks with many layers — hence the word "deep." These networks are inspired by the structure of the human brain, though they are mathematical approximations, not biological replicas. Deep learning excels at unstructured data: images, audio, text.

Here is the AI-900 trap I want you to avoid. The exam sometimes presents scenarios where deep learning seems like the best answer because it sounds more powerful. But deep learning requires enormous amounts of labeled data and significant computing resources. For small, structured datasets with clear features, a simpler machine learning algorithm like logistic regression or a decision tree will outperform a neural network and will be far easier to interpret and audit. Always match the tool to the task.

---

## [07:00 - 10:30] How Machine Learning Actually Works

[SHOW DIAGRAM: ML Workflow diagram with five boxes connected by arrows: "Training Data" → "Feature Extraction" → "Algorithm Training" → "Trained Model" → "Predictions on New Data"]

Let me walk through this workflow because it underpins everything we do in this course.

Step one is training data. A machine learning model learns from examples. Those examples are called training data. If we are building a model to detect spam email, our training data would be thousands of emails already labeled as "spam" or "not spam."

Step two is feature extraction. A feature is a measurable property of the data. In the spam example, features might include the number of exclamation points, whether the word "urgent" appears, the length of the email, and whether the sender's domain is recognized. The quality of features dramatically affects model performance.

Step three is algorithm training. We feed the features and labels into a machine learning algorithm. The algorithm adjusts its internal parameters — its weights — to minimize the difference between its predictions and the correct labels. This minimization process is called optimization, and it is the mathematical core of ML.

Step four is the trained model. Once training is complete, we have a model: a mathematical function that takes new, unseen inputs and produces predictions. The model has encoded the patterns it found in the training data.

Step five is prediction. We deploy the model and feed it new emails it has never seen. It applies the learned patterns and classifies each email as spam or not spam.

This five-step workflow applies whether you are predicting housing prices, diagnosing medical images, or translating languages. The data changes. The algorithm changes. The workflow stays the same.

---

## [10:30 - 13:30] The Three Learning Paradigms

Machine learning is typically divided into three paradigms, and the AI-900 exam tests all three.

The first paradigm is supervised learning. In supervised learning, the training data includes both input features and correct output labels. The algorithm learns to map inputs to outputs. Examples include email spam detection, predicting house prices, and classifying whether a tumor is benign or malignant. The word "supervised" reflects the fact that the model is supervised — guided — by the correct answers during training.

The second paradigm is unsupervised learning. In unsupervised learning, the training data contains only inputs — no labels. The algorithm must find structure on its own. The most common unsupervised task is clustering: grouping similar data points together without being told the group names in advance. Customer segmentation is a classic example. A retailer might cluster customers into groups based on purchasing behavior, then name those groups afterward based on what patterns emerge.

The third paradigm is reinforcement learning. In reinforcement learning, an agent learns by interacting with an environment and receiving rewards or penalties based on its actions. The agent's goal is to maximize cumulative reward over time. This is how AI systems learn to play chess, control robots, and optimize real-time bidding in advertising systems. Reinforcement learning is the least tested of the three on AI-900 but appears in scenarios about autonomous decision-making.

The AI-900 exam will present you with a scenario and ask which learning paradigm applies. Practice this skill: read the scenario, identify whether labeled data is present, and determine whether the system learns from feedback.

---

## [13:30 - 16:30] How Azure Delivers AI

[SHOW DIAGRAM: Three-tier pyramid. Bottom tier: "Azure Machine Learning (custom models)." Middle tier: "Azure Cognitive Services (prebuilt APIs)." Top tier: "Azure Applied AI Services (task-specific solutions)."]

Microsoft Azure organizes its AI offerings into three tiers, and understanding this hierarchy is essential for AI-900.

The bottom tier is Azure Machine Learning. This is the platform for data scientists and engineers who want to build, train, and deploy custom models from scratch. Azure ML provides the compute infrastructure, experiment tracking, model registry, and deployment pipelines. We will cover Azure ML in depth in Module 08.

The middle tier is Azure Cognitive Services. These are prebuilt AI APIs that you can call with a few lines of code. You do not need to train any model. You send an image to the Vision API and receive object labels back. You send text to the Language API and receive sentiment scores back. Cognitive Services covers vision, speech, language, and decision capabilities. Module 07 is dedicated to these services.

The top tier is Azure Applied AI Services. These combine Cognitive Services and custom logic to address specific end-to-end business scenarios. Examples include Azure Form Recognizer for document processing, Azure Cognitive Search for knowledge mining, and Azure Bot Service for conversational applications.

The key insight for AI-900: when a scenario describes a business problem, ask yourself which tier is the right fit. Custom model needed? Azure Machine Learning. Prebuilt capability with no training? Cognitive Services. End-to-end business solution? Applied AI Services.

---

## [16:30 - 19:00] Responsible AI — An Introduction

AI-900 devotes an entire exam domain to responsible AI, and we will cover it fully in Module 10. But I want to introduce the framework now because it should inform how you think about every module in this course.

Microsoft has defined six responsible AI principles:

- Fairness: AI systems should treat all people equitably.
- Reliability and safety: AI systems should perform reliably and safely.
- Privacy and security: AI systems should be secure and respect privacy.
- Inclusiveness: AI systems should empower everyone and engage people.
- Transparency: AI systems should be understandable.
- Accountability: People should be accountable for AI systems.

These principles are not just philosophical. They appear directly in AI-900 exam questions. You will be asked to identify which principle is violated when a hiring algorithm rejects more applications from one demographic group. You will be asked which principle is served when a model provides an explanation for its decision.

Memorize these six principles by name. Understand what each one means in a concrete scenario.

---

## [19:00 - 21:00] Module 01 Summary and Lab Preview

Let us recap what we covered today.

Artificial intelligence is the broad capability of machines to perform tasks requiring human-like intelligence. Machine learning is a subset of AI that learns patterns from data. Deep learning is a subset of ML that uses multi-layered neural networks. The three ML paradigms are supervised, unsupervised, and reinforcement learning. Azure delivers AI through Azure Machine Learning for custom models, Azure Cognitive Services for prebuilt APIs, and Azure Applied AI Services for end-to-end solutions. Responsible AI is guided by six principles: fairness, reliability, privacy, inclusiveness, transparency, and accountability.

In this week's lab, you will classify real-world scenarios as AI, ML, or DL, and determine whether each scenario represents supervised learning, unsupervised learning, or reinforcement learning. You will also practice identifying which Azure service tier applies to each scenario. This classification skill is directly tested on the AI-900 exam.

Before the next lecture, complete the reading guide and the quiz. The reading guide contains comparison tables and AI-900 exam tips that reinforce what we covered here.

For additional study, visit learn.microsoft.com and search for "AI-900 study guide." The official Microsoft learning paths are free, well-structured, and map directly to every topic we will cover.

I will see you in the next module, where we dig into supervised versus unsupervised learning in detail. Great work today.

---

## References

- Microsoft Learn — Azure AI Fundamentals certification overview: learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/
- Microsoft Learn — Explore fundamental AI concepts: learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/
