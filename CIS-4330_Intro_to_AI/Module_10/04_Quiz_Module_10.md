# Quiz: Module 10 — Generative AI and Azure OpenAI Service

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Domain: Describe features of generative AI workloads on Azure

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Submit through the course LMS.

---

## Question 1

Which of the following best describes the fundamental difference between discriminative AI and generative AI?

A. Discriminative AI works with images; generative AI works with text

B. Discriminative AI classifies or extracts from existing data; generative AI creates new content

C. Discriminative AI requires more training data than generative AI

D. Discriminative AI is always more accurate than generative AI

### Q1 — Correct Answer

B. Discriminative AI classifies or extracts from existing data; generative AI creates new content

### Q1 — Distractor Analysis

- A is incorrect: Both types of AI can work with images, text, audio, and other modalities. The distinction is about task type (classification vs. generation), not data type.
- C is incorrect: Training data requirements depend on the specific model and task, not the discriminative vs. generative distinction. LLMs require enormous training data.
- D is incorrect: Accuracy is task-dependent. Discriminative models may be highly accurate on their specific classification tasks, while generative models are evaluated on different metrics like fluency, coherence, and factual accuracy.

---

## Question 2

A developer is building a customer support application that uses GPT-4. Some users are submitting questions in real time and expect answers within two seconds. The developer sets the temperature parameter to 0.0. What effect does this have?

A. The model will run faster because it skips the sampling process entirely

B. The model will produce the same deterministic response each time for the same input

C. The model will refuse to answer questions outside its training knowledge

D. The model will limit all responses to a maximum of 100 tokens

### Q2 — Correct Answer

B. The model will produce the same deterministic response each time for the same input

### Q2 — Distractor Analysis

- A is incorrect: Temperature 0.0 selects the highest-probability token at each step but does not fundamentally change inference speed. Speed is governed by hardware, model size, and token count.
- C is incorrect: Temperature controls output randomness, not scope or knowledge boundaries. The model can still attempt to answer questions outside its knowledge; it may hallucinate.
- D is incorrect: Temperature has no relationship to response length. Token limits are controlled by the max tokens (max response) parameter.

---

## Question 3

A financial services company uses Azure OpenAI to generate quarterly earnings summaries from internal analyst reports. The output is published directly to investors without human review. Which responsible AI concern does this practice most directly violate?

A. Fairness — the summaries may be biased against certain industry sectors

B. Human oversight — consequential financial communications should have human review before publication

C. Privacy — investor data is being processed without consent

D. Transparency — the company should disclose which model version was used

### Q3 — Correct Answer

B. Human oversight — consequential financial communications should have human review before publication

### Q3 — Distractor Analysis

- A is incorrect: While bias is a concern in generative AI, the primary risk in publishing unreviewed AI-generated financial communications is accuracy and accountability, not sector bias.
- C is incorrect: Generating summaries from internal reports about the company's own performance does not inherently involve investor personal data.
- D is incorrect: Model version disclosure is a transparency consideration, but the most immediate and serious risk is publishing potentially inaccurate financial statements to investors without any human quality check.

---

## Question 4

What is the primary purpose of Retrieval-Augmented Generation (RAG) in an Azure OpenAI application?

A. To reduce the cost of API calls by caching frequently asked questions

B. To inject relevant source documents into the model's context, grounding responses in trusted content and reducing hallucination

C. To train the GPT model on the organization's proprietary data

D. To translate the model's response into multiple languages automatically

### Q4 — Correct Answer

B. To inject relevant source documents into the model's context, grounding responses in trusted content and reducing hallucination

### Q4 — Distractor Analysis

- A is incorrect: RAG is not a caching mechanism. It actively retrieves and injects documents at query time for each user request.
- C is incorrect: RAG does not train or fine-tune the model. It provides context at inference time without modifying the model's weights.
- D is incorrect: Translation is a separate concern handled by Azure AI Translator or by explicitly asking the model to translate. RAG is specifically about grounding factual responses.

---

## Question 5

A developer wants to use Azure OpenAI Service to generate product descriptions from a structured list of product attributes. The outputs need to follow a very specific format: a 50-word description, three bullet points highlighting features, and a call-to-action sentence. Which prompting technique would most reliably produce this consistent format?

A. Zero-shot prompting with a brief description of the desired output

B. Chain-of-thought prompting asking the model to reason step by step

C. Few-shot prompting with two or three fully formatted example outputs

D. Lowering the temperature to 0.0 and increasing max tokens to 2,000

### Q5 — Correct Answer

C. Few-shot prompting with two or three fully formatted example outputs

### Q5 — Distractor Analysis

- A is incorrect: Zero-shot prompting often works for simple tasks but is less reliable for enforcing a specific, detailed multi-element format. Examples make the format expectation explicit.
- B is incorrect: Chain-of-thought is designed for multi-step reasoning tasks such as math and logic. It does not inherently improve adherence to a specific output format.
- D is incorrect: Temperature and token count control randomness and length. They do not enforce a particular content structure.

---

## Question 6

Which Azure OpenAI model is specifically designed to generate images from a text description?

A. GPT-4 Turbo

B. Whisper

C. DALL-E 3

D. Ada text-embedding

### Q6 — Correct Answer

C. DALL-E 3

### Q6 — Distractor Analysis

- A is incorrect: GPT-4 Turbo is a language model capable of processing text and image inputs, but it generates text, not images.
- B is incorrect: Whisper is a speech recognition model that converts audio to text. It does not generate images.
- D is incorrect: Ada text-embedding converts text into vector representations for semantic search and clustering. It does not generate images or any visual content.

---

## Question 7

Azure OpenAI Service content filters screen both prompts and completions for harmful content across four categories. Which list correctly identifies all four categories?

A. Hate, violence, misinformation, and copyright infringement

B. Hate, sexual content, violence, and self-harm

C. Profanity, hate, spam, and self-harm

D. Sexual content, violence, misinformation, and privacy violations

### Q7 — Correct Answer

B. Hate, sexual content, violence, and self-harm

### Q7 — Distractor Analysis

- A is incorrect: Misinformation and copyright infringement are important concerns but are not the four designated content filter categories in Azure OpenAI Service.
- C is incorrect: Profanity and spam are not among the four designated filter categories, though profanity may be caught incidentally.
- D is incorrect: Misinformation and privacy violations are not part of the four built-in content filter categories, though other Azure mechanisms address privacy.

---

## Question 8

A developer provides this system prompt to a GPT-3.5 Turbo deployment: "You are a helpful cooking assistant. Only answer questions about recipes, ingredients, and cooking techniques. If asked about anything else, say you can only help with cooking questions." A user then sends: "What is the weather in Dallas today?" What should the well-designed bot do?

A. Answer the weather question because GPT-3.5 is capable of answering it

B. Decline and redirect the user as instructed by the system prompt

C. Generate a hallucinated weather forecast since it cannot access real-time data

D. Return an error because the question is outside the model's training data

### Q8 — Correct Answer

B. Decline and redirect the user as instructed by the system prompt

### Q8 — Distractor Analysis

- A is incorrect: A well-configured system prompt should override the model's general capability. Following the system prompt's scope restriction is the correct behavior.
- C is incorrect: A well-designed system prompt prevents the model from generating out-of-scope responses. The model should follow the instruction to redirect, not hallucinate an answer.
- D is incorrect: The model does not return errors for out-of-scope questions. It generates text; the system prompt is what directs it to redirect rather than attempt an answer.

---

## Question 9

A company is considering using the direct OpenAI API for a healthcare application that processes patient information. Their compliance officer requires HIPAA coverage. Which action should they take?

A. Use the direct OpenAI API since all major cloud providers are HIPAA compliant

B. Use Azure OpenAI Service, which offers HIPAA-eligible services under the Azure compliance framework

C. Build a private LLM from scratch to avoid third-party data handling entirely

D. HIPAA does not apply to AI systems, so either service can be used

### Q9 — Correct Answer

B. Use Azure OpenAI Service, which offers HIPAA-eligible services under the Azure compliance framework

### Q9 — Distractor Analysis

- A is incorrect: The direct OpenAI API does not currently offer a HIPAA Business Associate Agreement. Azure OpenAI Service does, under Microsoft's enterprise compliance program.
- C is incorrect: Building a private LLM from scratch is technically possible but is an enormous undertaking requiring billions of dollars in compute and data. It is not the practical answer for a compliance requirement.
- D is incorrect: HIPAA applies to all systems that process protected health information, including AI applications. Compliance is not optional.

---

## Question 10

A journalist asks a GPT-4 deployment: "What happened in the Contoso Corporation board meeting last Tuesday?" The model responds with a detailed, confident-sounding description of the meeting, including names and decisions. What is the most likely explanation for this response?

A. The model accessed a live news database to retrieve the meeting details

B. The model hallucinated the response, generating plausible-sounding but fabricated content

C. The model summarized its training data which included the meeting transcript

D. The model retrieved the response from its content filter cache

### Q10 — Correct Answer

B. The model hallucinated the response, generating plausible-sounding but fabricated content

### Q10 — Distractor Analysis

- A is incorrect: Standard GPT-4 in Azure OpenAI Service does not have real-time internet access by default. It cannot retrieve live news or recent events.
- C is incorrect: A specific internal corporate board meeting from last Tuesday almost certainly was not in the model's training data, which has a knowledge cutoff and would not include private corporate meeting minutes.
- D is incorrect: Content filter caches are not a source of meeting information. Content filters screen for harmful content; they do not store or retrieve information.

---

End of Quiz — Module 10
