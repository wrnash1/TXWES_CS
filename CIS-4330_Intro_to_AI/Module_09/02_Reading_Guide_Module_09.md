# Reading Guide: Module 09 - Azure Bot Service and Conversational AI
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 09 - Azure Bot Service and Conversational AI**! This module covers how Microsoft Azure enables developers to build intelligent conversational agents — chatbots and virtual assistants — without writing the underlying NLP infrastructure from scratch. Conversational AI is one of the five core Azure AI workload types tested on the **AI-900 (Microsoft Azure AI Fundamentals)** exam.

As a student, you will learn how Azure Bot Service provides the hosting and channel-integration framework for bots, how Azure AI Language's Conversational Language Understanding (CLU) extracts user intent from natural language, and how the question-answering capability (formerly QnA Maker) builds knowledge-base-driven bots. You will also explore image representation in Python, which underpins how computer vision models ingest and process image data. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Azure Bot Service**: Microsoft's managed platform for building, hosting, and deploying conversational bots across multiple channels (Microsoft Teams, web chat, SMS, email, Slack) from a single codebase. Azure Bot Service uses the Bot Framework SDK and integrates natively with Azure AI Language services to give bots natural language understanding capabilities without requiring manual NLP implementation.
*   **Intent and entity recognition (CLU)**: Conversational Language Understanding (CLU) is the Azure AI Language feature that identifies what a user wants (the intent — e.g., "BookFlight") and extracts the specific details from the utterance (the entities — e.g., "destination: Paris," "date: next Friday"). Intent and entity recognition transforms unstructured natural language input into structured data that a bot can act on.
*   **Image classification**: A computer vision task in which a model assigns a single label (or ranked list of labels) to an entire image — for example, classifying a photo as "cat," "dog," or "bird." In Azure, Custom Vision trains a custom image classifier using labeled example images uploaded to the portal, with no deep ML expertise required.
*   **Object detection**: A computer vision task that goes beyond classification by identifying the location and class of every distinct object within an image, drawing bounding boxes around each one. Azure AI Vision's object detection API and Azure Custom Vision both support this capability — the key distinction from classification is that detection returns coordinates (bounding boxes) in addition to labels.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** Conversational AI questions on the exam center on choosing the right Azure service for a given scenario. Know these clearly: **Azure Bot Service** (builds and hosts the bot), **CLU / Conversational Language Understanding** (understands intent and extracts entities from user input), **Custom Question Answering** (answers questions from a FAQ document or knowledge base), and **Azure AI Speech** (speech-to-text and text-to-speech, used when bots need to handle voice input). A scenario describing a bot that reads a PDF manual to answer employee questions → Custom Question Answering. A scenario describing a bot that books appointments and understands "cancel my meeting tomorrow" → CLU.
*   **Common AI-900 Trap:** The exam frequently confuses **CLU (intent/entity extraction)** with **Azure Translator (language translation)**. CLU understands meaning and structure within one language. Translator converts text from one language to another. If the scenario says "understand what the user is asking," the answer is CLU. If the scenario says "convert Spanish input to English," the answer is Azure Translator. These are tested side-by-side as distractors.
*   **Study Resource:** The Microsoft Learn module [Build a bot with Azure AI Bot Service](https://learn.microsoft.com/en-us/training/modules/build-faq-chatbot-qna-maker-azure-bot-service/) walks through creating a custom question-answering knowledge base and deploying it as a bot using Azure Bot Service. It is free, interactive, and maps directly to AI-900 conversational AI exam objectives.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters on natural language understanding, conversational agents, and computer vision in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). This freely available textbook by Poole and Mackworth covers intent recognition, dialogue management, and image representation — all foundational concepts for the Azure services explored in this module.
*   **Required Video:** Watch the conversational AI and Azure Bot Service segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video maps Azure Bot Service, CLU, and Custom Question Answering to real-world deployment scenarios and explains how each service is tested on the AI-900 exam.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Examine an image array representation in Python**: Load an image using `PIL.Image.open()` and convert it to a NumPy array with `np.array(img)`, then inspect `.shape` to confirm the (height, width, channels) dimensions — this shows how computer vision models receive pixel data as numeric matrices.
*   **Process image matrix dimensions and normalize pixel values**: Divide the image array by 255.0 to scale all pixel values from the [0, 255] range to [0, 1], which is the standard preprocessing step before feeding images to a neural network classifier.
*   **Use pre-trained model APIs to classify an image using Azure Custom Vision**: Send a sample image to an Azure Custom Vision prediction endpoint via an HTTP POST request using the `requests` library, then parse the JSON response to display the top predicted tag and its confidence score.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapters on conversational agents and computer vision in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on Azure Bot Service and Conversational AI in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
