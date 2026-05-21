# Reading Guide: Module 08 - Azure Machine Learning Studio
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 08 - Azure Machine Learning Studio**! This module covers Microsoft's cloud-based platform for building, training, and deploying machine learning models at scale. Azure Machine Learning Studio is a core service tested on the **AI-900 (Microsoft Azure AI Fundamentals)** exam, and understanding when to use its no-code, low-code, and code-first approaches is essential for both the exam and real-world AI project work.

As a student, you will also deepen your understanding of deep learning and neural networks — the model architecture that powers Azure Cognitive Services and Azure OpenAI Service under the hood. You will learn how neurons process inputs through activation functions, how layers are organized (input, hidden, output), and how backpropagation trains the network by adjusting weights. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Azure Machine Learning Studio (AutoML and Designer)**: Microsoft's cloud-based workspace for the full ML lifecycle — data preparation, model training, evaluation, and deployment. AutoML automatically tries many algorithms and hyperparameters to find the best model without writing code. The Designer provides a drag-and-drop canvas for building ML pipelines visually. Code-first Jupyter notebooks are also available for experienced data scientists.
*   **Neurons and layers (input, hidden, output)**: A neural network is organized into layers of artificial neurons. The input layer receives raw feature data; one or more hidden layers learn increasingly abstract representations by applying weighted sums and activation functions; the output layer produces the final prediction (a class probability for classification, or a numeric value for regression). Depth — the number of hidden layers — is what makes a network "deep."
*   **Activation functions (ReLU and Sigmoid)**: Mathematical functions applied at each neuron to introduce non-linearity into the network. ReLU (Rectified Linear Unit) outputs max(0, x) — it passes positive values unchanged and zeros out negatives, which prevents vanishing gradients in deep networks. Sigmoid outputs 1 / (1 + e^-x) — it squashes any value to a probability between 0 and 1, making it suitable for binary output neurons but prone to vanishing gradients in hidden layers.
*   **Backpropagation**: The training algorithm that adjusts neural network weights by calculating the gradient of the loss function with respect to each weight, then propagating the error signal backward from the output layer to the input layer. Combined with gradient descent, backpropagation enables a network to minimize prediction error over many training iterations (epochs).

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** Azure Machine Learning Studio has three authoring experiences. The exam tests which to recommend: **AutoML** (no-code, finds the best algorithm automatically), **Designer** (drag-and-drop pipeline builder, low-code), and **Notebooks** (code-first, full control with Python/R). If a scenario says "data scientist with no coding experience" or "quickest path to a model," AutoML or Designer is the answer. If a scenario says "custom Python training script," Notebooks is the answer.
*   **Common AI-900 Trap:** The exam distinguishes between **Azure Machine Learning** (custom model training with your own data) and **Azure Cognitive Services** (pre-built models called via REST API with no training required). If a scenario describes training a model on company-specific data, the answer is Azure Machine Learning. If the scenario describes calling an existing AI capability without training, the answer is Azure Cognitive Services. Mixing these up is the most frequently tested trap in the Azure AI workload section.
*   **Study Resource:** The Microsoft Learn module [Use Automated Machine Learning in Azure Machine Learning](https://learn.microsoft.com/en-us/training/modules/use-automated-machine-learning/) walks through creating an AutoML experiment from scratch in Azure ML Studio. It is free, hands-on, and directly maps to AI-900 exam objectives. A companion module, [Create a regression model with Azure Machine Learning designer](https://learn.microsoft.com/en-us/training/modules/create-regression-model-azure-machine-learning-designer/), covers the visual Designer experience.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters on neural networks, deep learning, and machine learning platforms in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). This freely available textbook by Poole and Mackworth covers neuron models, layered network architectures, and the gradient descent learning algorithm that underpins all neural network training.
*   **Required Video:** Watch the Azure Machine Learning Studio and neural network segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video covers the AutoML, Designer, and Notebooks authoring paths and explains how deep learning neural networks power the advanced AI capabilities available on Azure.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Define a basic neural network layer layout using scikit-learn's MLPClassifier**: Configure an `MLPClassifier(hidden_layer_sizes=(64, 32))` to create a two-hidden-layer network, then call `model.fit(X_train, y_train)` and `model.predict(X_test)` to train and evaluate it.
*   **Examine activation function behavior**: Compare ReLU and Sigmoid outputs by plotting both functions over the range [-5, 5] using NumPy and Matplotlib, observing how ReLU avoids saturation in negative regions and why it is preferred in hidden layers.
*   **Trace forward propagation through a small network**: Manually compute the output of a two-layer network (2 inputs → 3 hidden → 1 output) using NumPy matrix multiplication and a ReLU activation, verifying that the math matches the model's prediction.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapters on neural networks and deep learning in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on Azure Machine Learning Studio in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
