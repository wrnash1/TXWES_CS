# Reading Guide: Module 01 - Introduction to AI & Machine Learning
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 01 - Introduction to AI & Machine Learning**! This module introduces the foundational concepts of Artificial Intelligence and Machine Learning as framed by the **AI-900 (Microsoft Azure AI Fundamentals)** certification. You will learn what distinguishes traditional programming from ML-based systems, how Azure categorizes AI workloads, and where deep learning fits within the broader AI landscape.

As a student, you will explore how AI systems learn from data rather than explicit rules, recognize the three major ML paradigm types (supervised, unsupervised, reinforcement), and understand how Microsoft Azure provides cloud-based AI services that abstract model training complexity. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Artificial intelligence**: The simulation of human cognitive capabilities — such as reasoning, learning, and perception — by computer systems. In the AI-900 framework, AI encompasses ML, computer vision, NLP, and conversational AI workloads that can all be built on Azure services.
*   **Machine learning vs deep learning**: Machine learning is a subset of AI in which algorithms learn statistical patterns directly from labeled or unlabeled data to make predictions. Deep learning is a further subset of ML that uses multi-layer neural networks to automatically extract hierarchical features, enabling breakthroughs in image recognition and NLP.
*   **Predictive modeling workloads**: AI tasks where a trained model forecasts outcomes for new, unseen data based on patterns learned during training. Azure ML supports regression (continuous value prediction), classification (categorical label assignment), and forecasting (time-series) as the three primary predictive workload types tested on AI-900.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** The exam distinguishes between AI workloads (computer vision, NLP, conversational AI, anomaly detection, knowledge mining) and ML concepts. Know which Azure service maps to each workload — for example, Azure Cognitive Services for vision/language, Azure Machine Learning for custom model training.
*   **Common AI-900 Trap:** Do not confuse "deep learning" with all of machine learning. The exam may present a scenario where a shallow algorithm (like logistic regression) is the better answer because the dataset is small and interpretability is required.
*   **Study Resource:** The official Microsoft AI-900 learning path on [Microsoft Learn: AI Fundamentals](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/) covers all exam objectives for free, including interactive modules on AI concepts and Azure services. Start with the "Explore fundamental AI concepts" module.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the introductory chapter on AI and machine learning fundamentals in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). Focus on Chapters 1–2, which cover agent-based reasoning and the role of learning.
*   **Required Video:** Watch the introductory lecture on AI and ML concepts in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video maps directly to the AI-900 "Describe Artificial Intelligence workloads and considerations" domain.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Set up Python development folder**: Create a project directory and a virtual environment (`python -m venv venv`) to isolate your AI experiment dependencies.
*   **Install NumPy and Pandas: `pip install numpy pandas`**: These libraries are the foundation for data manipulation in every subsequent ML lab in this course.
*   **Create basic script to verify packages import successfully**: Write a short Python script that imports `numpy` and `pandas` and prints their version numbers, confirming the environment is correctly configured.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the introductory chapters on AI in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
- [ ] Watch the video lecture on Introduction to AI & Machine Learning in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
