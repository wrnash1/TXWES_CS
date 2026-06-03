# Quiz: Module 12 — AI in Business: Use Cases and ROI

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe AI workloads and considerations (15-20%)

**Instructions:** Select the best answer for each question.

---

## Question 1

A utility company deploys an AI system that analyzes 10 years of equipment sensor readings and identifies which transformers are statistically most likely to fail in the next 90 days. Maintenance crews then schedule inspections based on this output. Which AI use case category does this represent?

A. Automation — the AI is replacing the task of inspecting transformers

B. Enhancement — the AI is augmenting inspection crews with better scheduling information

C. Insights — the AI is extracting actionable patterns from data at a scale humans cannot match

D. New Products — the AI is enabling a service that did not previously exist

Correct Answer: C

Distractor analysis: A is incorrect because no inspection task is replaced — humans still perform all inspections. B is incorrect; Enhancement describes AI that augments the human while they perform a task, but the transformative value here is in the prediction itself (pattern extraction from data), not in helping a worker do their job faster. D is incorrect because predictive maintenance is an optimization of an existing process, not an entirely new product or revenue stream. C is correct because the value is evidence-based prediction derived from data patterns that humans could not identify manually at this scale.

---

## Question 2

A retail company uses Azure AI Language to analyze the sentiment of customer product reviews and classify them as positive, negative, or neutral. A product manager reviews a daily summary report. Previously, two analysts spent 4 hours per day manually reading and coding reviews. Which AI use case category does this most accurately represent?

A. Enhancement, because the product manager still reviews the output

B. Automation, because the AI performs a task previously done by human analysts

C. Insights, because the AI is extracting patterns from customer data

D. New Products, because sentiment analysis was not previously possible manually

Correct Answer: B

Distractor analysis: A is incorrect; Enhancement applies when AI augments a human doing the same task, not when AI replaces the task and a different human reviews aggregated output. C is partially plausible since sentiment analysis produces data insights, but the primary value described is the elimination of manual coding labor — the definition of Automation. D is incorrect because manual sentiment review was already happening; AI did not create a new capability, it automated an existing one. B is correct: AI is performing a task previously done by humans at lower cost and higher speed.

---

## Question 3

A company is evaluating whether to use Azure Cognitive Services or build a custom Azure Machine Learning model for a new AI initiative. According to the build-versus-buy decision framework, which factor most strongly favors building a custom model?

A. The task is a standard language task such as translation or sentiment analysis

B. No labeled training data is available and the timeline is four weeks

C. The task involves proprietary categories specific to the company's business domain

D. The company wants to deploy quickly without ML engineering resources

Correct Answer: C

Distractor analysis: A describes a scenario that favors prebuilt Cognitive Services, not a custom model. B also favors prebuilt services — without labeled data, custom model training is not feasible. D also favors prebuilt services because custom models require ML engineering. C is correct: when the task involves categories, entities, or patterns that are proprietary and not covered by any prebuilt model, a custom model with domain-specific training data is required.

---

## Question 4

An organization is calculating the ROI of its first AI deployment. Before launch, the team measured the current process performance to have a reference point for comparison. What is this pre-deployment measurement called, and why is it essential to ROI calculation?

A. A performance benchmark — it documents what the AI system should achieve in production

B. A baseline metric — it establishes the pre-AI performance level so that improvement can be quantified

C. A model evaluation score — it confirms the model is accurate before deployment

D. A data audit — it ensures the training data is representative before the model is trained

Correct Answer: B

Distractor analysis: A is incorrect; a benchmark can describe what is desired, but the pre-deployment measurement of actual performance is specifically called a baseline. C describes model evaluation metrics (accuracy, F1 score) which are measured against test data during development, not against production process performance. D describes data quality assessment, which happens before training, not before deployment. B is correct: a baseline metric captures the current state of the process before AI is introduced; without it, there is no reference point to calculate how much the AI improved things.

---

## Question 5

A hospital network's AI-900 study group debates which Azure service to recommend for a scenario where clinicians need to extract patient name, date of birth, diagnosis code, and insurance provider from scanned medical intake forms. Which service is most appropriate?

A. Azure Machine Learning AutoML — because form extraction is a supervised classification problem

B. Azure AI Document Intelligence — because it is purpose-built for extracting structured fields from unstructured documents

C. Azure AI Language — because medical text extraction is a named entity recognition task

D. Azure OpenAI — because GPT-4 can read and interpret document content

Correct Answer: B

Distractor analysis: A is incorrect; AutoML is used for tabular prediction tasks, not document field extraction. C is partially plausible since NER is related, but Azure AI Language NER is for entity extraction from free text, not for structured layout extraction from scanned form images. D is technically possible but not the recommended architecture; GPT-4 is not purpose-built for document processing at scale and lacks the structured output and prebuilt form models that Document Intelligence provides. B is correct: Azure AI Document Intelligence (formerly Form Recognizer) is the designated Azure service for extracting structured data from document images and PDFs.

---

## Question 6

Which of the following best describes data drift and its consequence for deployed AI models?

A. Data drift occurs when a model is trained on too little data, causing it to overfit the training set

B. Data drift occurs when the statistical properties of production data change over time, causing model performance to degrade

C. Data drift occurs when two different models are trained on the same dataset but produce different results

D. Data drift occurs when training data is deliberately modified to manipulate model outputs

Correct Answer: B

Distractor analysis: A describes overfitting, which is a training-time problem unrelated to drift. C describes model variance or non-determinism, not drift. D describes a data poisoning attack, a security concept distinct from drift. B is correct: data drift refers to the natural shift in the distribution of real-world data over time — for example, customer behavior changing after an economic shift — which causes a model trained on older patterns to perform poorly on current data. This is why ongoing monitoring and periodic retraining are required for production models.

---

## Question 7

A company wants to build a chatbot that answers employee questions about HR policies using content from the company's internal HR policy documents. The company does not want the chatbot to generate answers from its general knowledge — it should only answer from approved policy content. Which Azure service combination best addresses this requirement?

A. Azure Machine Learning AutoML + Azure AI Language CLU

B. Azure AI Language Question Answering with a knowledge base built from the policy documents

C. Azure OpenAI GPT-4 with a system message instructing it to answer HR questions

D. Azure Anomaly Detector + Azure AI Language sentiment analysis

Correct Answer: B

Distractor analysis: A is incorrect; AutoML and CLU are not designed for FAQ retrieval from documents. C is technically possible but does not guarantee answers come only from approved documents — a general GPT-4 system message does not prevent the model from drawing on training data. Without grounding (RAG), the model may hallucinate policy content that does not exist. D is nonsensical for this use case. B is correct: Azure AI Language Question Answering is specifically designed to create a knowledge base from documents and answer questions using only that content, which matches the requirement for policy-grounded responses.

---

## Question 8

An organization is at AI Maturity Level 2. Which of the following characteristics most accurately describes their current state?

A. Individual departments are running independent proof-of-concept experiments with no production deployments

B. The organization has deployed AI to production and is beginning to establish MLOps practices such as model monitoring and versioning

C. The organization has a centralized AI platform team, a shared data infrastructure, and formal responsible AI governance

D. AI is embedded in all core business processes and the organization has continuous learning loops from production feedback

Correct Answer: B

Distractor analysis: A describes Level 1 (Experimentation) — proof-of-concept projects with no production deployments and no governance. C describes Level 3 (Scaling) — centralized platform and governance across multiple business units. D describes Level 4 (AI-Native) — AI embedded in core processes with continuous improvement loops. B correctly describes Level 2 (Operationalization): the organization has moved at least one model to production and is establishing the foundational MLOps practices that will scale over time.

---

## Question 9

An AI-900 scenario reads: "A financial services firm wants to predict the probability that a loan applicant will default within 12 months. They have 8 years of historical loan records with labeled outcomes (default or no default). They need high accuracy and control over model updates." Which is the most appropriate Azure service for this scenario?

A. Azure AI Language — because loan default prediction requires text sentiment analysis of applications

B. Azure Cognitive Services prebuilt models — because the task is standard credit analysis

C. Azure Machine Learning — because this is a custom binary classification problem requiring training on proprietary historical data

D. Azure OpenAI — because GPT-4 can evaluate financial risk from application text

Correct Answer: C

Distractor analysis: A is incorrect; loan default prediction is a classification problem using structured financial data, not text sentiment analysis. B is incorrect; there is no prebuilt Cognitive Services model for proprietary credit default prediction — this is a domain-specific problem requiring custom training. D is incorrect; GPT-4 is a language model not suited for binary classification on structured tabular data, and it cannot be trained on proprietary historical records. C is correct: this is a classic supervised binary classification task with available labeled data — the exact scenario where Azure Machine Learning (custom or AutoML) is the recommended approach.

---

## Question 10

Which of the following is an example of cost avoidance as an AI ROI value component?

A. A chatbot handles 2,000 customer inquiries per week, reducing the need for two call center employees

B. An AI-powered personalization engine increases e-commerce conversion rates by 2.4 percent

C. A predictive maintenance model prevents four unplanned factory shutdowns per year, avoiding $180,000 in lost production

D. A fraud detection model processes transactions in 40 milliseconds instead of the previous 8-hour batch review

Correct Answer: C

Distractor analysis: A describes labor cost savings — the primary cost reduction from automating a task performed by human workers. B describes new revenue — incremental income generated by an AI-enabled capability. D describes speed improvement — faster processing that may indirectly generate value. C is correct: cost avoidance is value that comes from preventing a cost that would otherwise have been incurred. No cash is directly generated, but the $180,000 that would have been lost to unplanned downtime is avoided — this is the defining characteristic of the cost avoidance value category.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | C |
| 2 | B |
| 3 | C |
| 4 | B |
| 5 | B |
| 6 | B |
| 7 | B |
| 8 | B |
| 9 | C |
| 10 | C |
