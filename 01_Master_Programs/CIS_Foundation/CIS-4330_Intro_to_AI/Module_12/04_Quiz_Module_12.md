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
| 11 | B |
| 12 | C |
| 13 | A |
| 14 | D |
| 15 | B |
| 16 | C |
| 17 | A |
| 18 | D |
| 19 | B |
| 20 | C |

---

## Question 11

A news media company wants to use AI to generate first-draft headlines for breaking news stories. Editors review and approve every headline before publication. Which AI use case category does this represent?

A. Automation, because the AI produces the headline without human intervention

B. Enhancement, because the AI augments the editor's work while humans retain final approval

C. New Products, because AI-generated headlines are a new publishing capability

D. Insights, because the AI is extracting patterns from prior successful headlines

Correct Answer: B

Distractor analysis: A is incorrect; Automation implies the AI completes the task end-to-end without a human in the loop. Here, editors review every headline — the human decision is retained. C is incorrect; Enhancement does not become New Products simply because AI is used in a publishing workflow — no new revenue stream or product experience is being created. D is incorrect; the AI is generating content, not extracting patterns from data to inform decisions. B is correct: Enhancement is the category for AI that assists a human performing a task while the human retains decision authority.

---

## Question 12

An organization wants to deploy an AI model to help customer service agents respond to complex billing disputes. The agents read the AI's suggested response and then decide whether to send it as-is, edit it, or discard it. According to responsible AI best practices, what design pattern does this represent?

A. Full automation, because the AI generates the final customer response

B. Bias mitigation, because human review reduces the chance of biased AI outputs reaching customers

C. Human-in-the-loop, because humans review and approve AI outputs before they are acted on

D. RAG architecture, because the AI retrieves billing data before generating a response

Correct Answer: C

Distractor analysis: A is incorrect; full automation would require the AI to send the response without any human review. B describes a potential benefit but is not the name of this design pattern. D describes how the AI may be retrieving context, not the governance pattern for how humans interact with the output. C is correct: Human-in-the-loop (HITL) is the design pattern in which an AI system's outputs are reviewed and approved by a human before being acted on — exactly the pattern described.

---

## Question 13

A company has a deployed machine learning model that was trained on 18 months of sales data and accurately predicted sales volume for the first six months after deployment. In month seven, prediction accuracy drops sharply following a major market disruption. No changes were made to the model itself. What most likely explains the accuracy drop?

A. Data drift — the statistical distribution of production data has shifted away from the training data distribution

B. Overfitting — the model memorized the training data and cannot generalize to new inputs

C. Model bias — the model was trained on a biased sample that excluded certain customer segments

D. Context window overflow — the model ran out of memory when processing recent transaction volumes

Correct Answer: A

Distractor analysis: B is incorrect; overfitting would have caused poor accuracy from the start, not after six months of good performance. C is incorrect; bias describes systematic skew in predictions affecting specific groups, not a sudden accuracy drop following an external market event. D is incorrect; context window is a property of large language models, not of the regression or forecasting models used for sales prediction. A is correct: data drift describes the phenomenon where the real-world data distribution changes after model training, causing models that were accurate on historical patterns to degrade on new data — exactly what happens during economic or market disruptions.

---

## Question 14

An enterprise wants to deploy AI to process incoming invoices automatically. Invoices arrive from hundreds of different vendors, each using a different layout. The company needs to extract vendor name, invoice number, line items, and total amount. Which Azure service is purpose-built for this use case?

A. Azure Machine Learning AutoML — trained on tabular invoice data with labeled fields

B. Azure AI Language — because invoice fields are entities extractable via named entity recognition

C. Azure OpenAI — because GPT-4 can read and parse any document layout

D. Azure AI Document Intelligence — because it provides prebuilt and custom models for structured field extraction from documents

Correct Answer: D

Distractor analysis: A is incorrect; AutoML is designed for tabular classification and regression, not for extracting fields from unstructured document images. B is incorrect; Azure AI Language NER works on plain text, not on scanned document images or PDFs with complex layouts. C is technically possible but not the enterprise-recommended architecture; GPT-4 lacks the structured output models and scale-optimized pricing designed for document processing pipelines. D is correct: Azure AI Document Intelligence (formerly Form Recognizer) provides both prebuilt invoice models and custom models trained to extract specific fields from vendor-specific layouts — the exact combination needed.

---

## Question 15

A company is presenting an AI business case to its board. The financial team asks how they will know whether the AI system created value after deployment. The data science lead says they measured the current process performance before starting the project. What has the team done correctly?

A. They have defined the AI success metric, which determines what accuracy threshold the model must reach

B. They have established a baseline metric, which enables quantitative comparison between pre-AI and post-AI performance

C. They have completed the model evaluation, which confirms the model's accuracy on held-out test data

D. They have performed a data audit, which ensures the training data is sufficient for model development

Correct Answer: B

Distractor analysis: A is incorrect; a success metric defines a target, but pre-deployment measurement of actual current performance is the baseline, not the target. C is incorrect; model evaluation uses test data during development — it is not the same as measuring production process performance before deployment. D is incorrect; a data audit assesses training data quality, not production process performance. B is correct: establishing a baseline captures the pre-AI state of the process so that after deployment the organization can calculate the measurable improvement and quantify ROI.

---

## Question 16

A hospital network's AI-900 study group is discussing the cost structure of a new AI initiative. One team member says "We should include the cost of labeling 50,000 training images" and another says "We should not forget the cost of GPU compute for running predictions after deployment." Which ROI cost categories do these two items respectively represent?

A. Implementation cost; data infrastructure cost

B. Training cost; monitoring cost

C. Data preparation cost; ongoing operational cost

D. Development cost; hardware procurement cost

Correct Answer: C

Distractor analysis: A is incorrect; "implementation cost" and "data infrastructure cost" are not the specific terms used in the AI ROI cost framework. B is partially plausible but "training cost" is typically a subset of development cost; "monitoring cost" refers to performance monitoring, not inference compute. D is incorrect; "hardware procurement" does not accurately describe cloud-based inference compute charged per API call or per compute hour. C is correct: data labeling falls under data preparation cost (acquiring and annotating the training dataset), and GPU inference compute falls under ongoing operational cost (costs incurred while the model serves production traffic after deployment).

---

## Question 17

An organization has deployed four AI systems across different business units, each with its own data pipeline and deployment process. There is no centralized AI platform team, no shared model registry, and no formal responsible AI governance committee. The organization wants to scale AI across all 15 business units. What does the AI maturity model say is the most important prerequisite for this scaling phase?

A. Establishing a centralized AI platform, shared data infrastructure, and formal responsible AI governance

B. Deploying additional proof-of-concept projects in the remaining 11 business units first

C. Replacing all deployed models with newer foundation model-based architectures

D. Hiring a dedicated data scientist for each of the 15 business units

Correct Answer: A

Distractor analysis: B is incorrect; expanding pilots to more business units while infrastructure and governance remain fragmented would amplify the coordination problems, not solve them. C is incorrect; replacing model architectures is a technical decision unrelated to the organizational and governance barriers to scaling. D is incorrect; hiring is a resource decision, but without shared infrastructure and governance, distributed teams will produce inconsistent, duplicated, and ungovernanced AI systems. A is correct: according to the AI maturity model, progressing from Level 2 (Operationalization) to Level 3 (Scaling) requires exactly these three foundations — centralized platform, shared data infrastructure, and responsible AI governance.

---

## Question 18

An organization is building a business case for deploying an AI-powered customer service chatbot. The sponsor argues the chatbot will deliver value through four mechanisms: (1) handling 60% of tier-1 inquiries without agent involvement, (2) giving agents real-time knowledge base suggestions during complex calls, (3) identifying patterns in complaint volume that predict product defects, and (4) enabling 24/7 self-service for customers in time zones not covered by current staffing. Which mechanisms represent Automation, Enhancement, Insights, and New Products respectively?

A. 1=Automation, 2=Insights, 3=Enhancement, 4=New Products

B. 1=Insights, 2=Enhancement, 3=Automation, 4=New Products

C. 1=New Products, 2=Automation, 3=Insights, 4=Enhancement

D. 1=Automation, 2=Enhancement, 3=Insights, 4=New Products

Correct Answer: D

Distractor analysis: A assigns Insights to mechanism 2, but providing real-time suggestions to agents is Enhancement (AI augments a human performing the task), not Insights. B assigns Automation to mechanism 3, but complaint pattern identification is extracting actionable patterns from data — Insights. C incorrectly assigns New Products to mechanism 1 (handling tier-1 inquiries is automating an existing process, not creating a new product). D is correct: (1) the chatbot replaces agent involvement for tier-1 inquiries = Automation; (2) it augments agents during complex calls = Enhancement; (3) it extracts predictive patterns from complaint data = Insights; (4) it enables 24/7 coverage not previously possible = New Products.

---

## Question 19

A company is choosing between Azure AI Language sentiment analysis and building a custom Azure Machine Learning text classification model for a new use case. The use case is classifying internal IT support tickets into eight proprietary priority categories defined by the company's IT governance policy. Which factor is the most decisive reason to choose a custom model over a prebuilt service?

A. The company wants to deploy faster than a custom model allows

B. The eight priority categories are proprietary and not supported by any prebuilt classification service

C. The company lacks the technical staff to operate a custom model in production

D. The volume of support tickets is too low to justify training a custom model

Correct Answer: B

Distractor analysis: A is incorrect and points in the opposite direction — a prebuilt service is faster to deploy; if speed is the priority, prebuilt services win. C is incorrect; lack of technical staff favors using prebuilt services, not building custom models. D is incorrect; low data volume typically favors prebuilt services since custom models require sufficient labeled training data. B is correct: when the classification categories are proprietary and domain-specific, no prebuilt service can produce the required output because prebuilt models are trained on general categories. Custom training is necessary precisely because of domain specificity.

---

## Question 20

An organization calculates that its AI-powered document processing system cost $80,000 to build and deploy and generates $310,000 in annual value (labor savings plus error reduction). However, the CIO notes that the system processes sensitive employee performance review documents and wants to ensure the system complies with privacy and data minimization requirements. Which AI ROI consideration does the CIO's concern most directly represent?

A. A cost avoidance item — security incidents avoided reduce the total cost of ownership

B. A baseline metric issue — privacy compliance cannot be measured before deployment

C. A build-versus-buy factor — prebuilt services have better compliance certifications than custom models

D. A total cost of ownership element — compliance requirements may add implementation and operational costs not included in the initial ROI calculation

Correct Answer: D

Distractor analysis: A is partially true but is not the most direct representation of the CIO's concern — the CIO is raising the question of whether the ROI calculation is complete, not estimating the monetary value of security incident avoidance. B is incorrect; baseline metrics are about measuring pre-deployment performance, not about compliance requirements. C is partially relevant but the CIO has not raised a build-versus-buy question — the system is already deployed. D is correct: the CIO is identifying a gap in the ROI model — compliance costs (data encryption, access controls, audit logging, privacy reviews) are real costs that must be included in total cost of ownership; if they were omitted from the $80,000 figure, the ROI calculation is incomplete.

---

End of Quiz — Module 12
