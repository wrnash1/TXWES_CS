# Reading Guide: Module 15 - AI Security and Privacy
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 15 - AI Security and Privacy**! This module covers the security threats specific to AI and machine learning systems and the defensive measures organizations use to protect them. As AI models are increasingly deployed in production environments, understanding how to secure them from adversarial attacks, data leakage, and privacy violations is essential both for the **AI-900 (Microsoft Azure AI Fundamentals)** exam and for responsible real-world deployment.

As a student, you will also learn the technical mechanics of model deployment — serialization, containerization, REST API endpoints, and endpoint monitoring — which form the operational foundation that security controls must protect. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Adversarial examples and adversarial training**: Adversarial examples are inputs that have been deliberately crafted — typically by adding imperceptible noise to images, audio, or text — to fool a trained model into making incorrect predictions with high confidence. Adversarial training is the primary defense: the model is retrained with adversarially perturbed examples included in the training set so it learns to classify both clean and crafted inputs correctly.
*   **Model inversion attacks and differential privacy**: A model inversion attack exploits a public model's output probabilities to reconstruct sensitive data from the training set — for example, recovering patient records from a medical classifier. Differential privacy defends against this by injecting calibrated statistical noise into training data, making it mathematically difficult to extract individual records from the model's learned weights or outputs.
*   **Model serialization (pickle, ONNX) and containerization**: Model serialization saves a trained model's weights and structure to a file so it can be reloaded later without retraining. `pickle` (Python-native) and `joblib` are common for scikit-learn models; ONNX (Open Neural Network Exchange) is an interoperable format for exporting models across frameworks (PyTorch → TensorFlow → Azure ML). Containerization packages the model, its dependencies, and a scoring script into a Docker image that can be deployed consistently across any compute environment.
*   **REST API deployment and endpoint monitoring**: Deploying a model as a REST API endpoint makes it accessible to client applications via HTTP POST requests — the client sends input features as JSON and receives predictions in return. Endpoint monitoring tracks request volume, latency, error rates, and input data statistics over time to detect performance degradation, data drift, or anomalous query patterns that may indicate an attack.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** The exam tests the ability to match an AI security threat to the correct mitigation. Know these pairings precisely: **adversarial examples** (perturbed inputs cause misclassification) → adversarial training + input validation. **Model inversion** (API outputs used to reconstruct training data) → differential privacy + rate limiting. **Data poisoning** (attacker corrupts training data to manipulate model behavior) → data validation and provenance controls. **Prompt injection** (LLM ignores system instructions due to crafted user input) → output filtering + keeping sensitive logic out of the system prompt. The exam presents attack descriptions and asks for the correct countermeasure.
*   **Common AI-900 Trap:** Students frequently confuse **adversarial examples** (attack at inference time — perturb the input to fool the model) with **data poisoning** (attack at training time — corrupt the training data to corrupt the model). The timing distinguishes them: inference-time attacks → adversarial training and input filtering. Training-time attacks → data validation and dataset provenance controls. Both are tested, and the defenses are different.
*   **Study Resource:** The Microsoft Learn module [Identify principles and practices for responsible AI](https://learn.microsoft.com/en-us/training/modules/responsible-ai-principles/) covers the Privacy and Security principle in depth, including how Microsoft applies it to Azure AI services. For practical security controls, the [Azure AI services security baseline](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/cognitive-services-security-baseline) documentation describes the specific network, identity, and data protection controls available for Azure Cognitive Services deployments.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters on AI safety, adversarial machine learning, and system deployment in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). This freely available textbook by Poole and Mackworth addresses both the theoretical foundations of adversarial robustness and the practical deployment considerations needed to operate AI systems securely.
*   **Required Video:** Watch the AI security and model deployment segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video covers adversarial threats, differential privacy, and how Azure Machine Learning's endpoint security controls (authentication, network isolation, monitoring) protect deployed models in production.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Serialize a scikit-learn model using joblib**: Call `joblib.dump(model, 'model.pkl')` to save a trained classifier to disk, then reload it with `joblib.load('model.pkl')` and verify predictions are identical — demonstrating the serialize-deploy-predict lifecycle.
*   **Create a mock Dockerfile for hosting the model**: Write a minimal Dockerfile that installs Python and scikit-learn, copies the serialized model and a `score.py` scoring script into the image, and exposes port 5000 — illustrating how Azure ML packages models for containerized deployment.
*   **Send an input data payload and verify the API output response**: Use Python's `requests` library to POST a JSON feature payload to a local Flask scoring endpoint (`/score`), then parse the returned prediction JSON — replicating exactly how Azure ML real-time endpoints accept and respond to client inference requests.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapters on AI security and system deployment in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on AI Security and Privacy in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
