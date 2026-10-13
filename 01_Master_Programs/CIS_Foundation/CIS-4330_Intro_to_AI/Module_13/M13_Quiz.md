# Quiz: Module 13 — AI Applications in Business

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. The quiz is closed-book and should be completed in 20 minutes.

---

## Questions

**Question 1**

A hospital system wants to automatically extract patient diagnoses, medications, and dosages from unstructured clinical notes to populate a structured database. Which Azure AI service is most appropriate?

A. Azure Machine Learning AutoML

B. Azure AI Language — Text Analytics for Health

C. Azure Computer Vision

D. Azure AI Personalizer

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. AutoML is for training custom classification or regression models, not for extracting structured data from clinical text. It has no built-in clinical NLP.
- **B** is correct. Azure AI Language's Text Analytics for Health is specifically designed to extract and structure clinical entities — diagnoses, medications, dosages, body locations — from unstructured medical text.
- **C** is incorrect. Computer Vision analyzes images, not text documents.
- **D** is incorrect. Azure Personalizer is a recommendation and reinforcement learning service for product/content personalization, unrelated to clinical text extraction.

---

**Question 2**

A bank wants to detect fraudulent credit card transactions in real time as they occur. The model must return a decision in under 200 milliseconds. Which deployment architecture is most appropriate?

A. Batch endpoint scoring transactions nightly

B. Managed online endpoint with low-latency real-time inference

C. AutoML experiment running on a compute cluster

D. Designer pipeline with manual trigger

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Batch endpoints process large datasets asynchronously. Nightly scoring would mean fraudulent transactions go undetected for hours.
- **B** is correct. Managed online endpoints handle synchronous, low-latency inference. Transactions can be scored in real time as they are submitted.
- **C** is incorrect. An AutoML experiment is a training workflow, not a production deployment mechanism.
- **D** is incorrect. A manually triggered Designer pipeline is a training tool, not a real-time inference service.

---

**Question 3**

According to the ROI framework presented in Module 13, what is the most commonly underestimated cost category in AI projects?

A. Cloud infrastructure compute costs

B. Data scientist salaries

C. Integration with existing systems and ongoing maintenance

D. Licensing fees for Azure AI services

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Cloud compute costs are highly visible and typically well-scoped in project budgets.
- **B** is incorrect. Data scientist salaries are personnel costs that organizations typically budget accurately.
- **C** is correct. Integration costs (connecting the AI model to existing enterprise systems) and ongoing maintenance (monitoring, retraining, support) are consistently the most underestimated components — often by a factor of 3–5x relative to the initial estimate.
- **D** is incorrect. Azure AI service licensing is a straightforward, transparent consumption-based pricing model.

---

**Question 4**

A retail company attributes 35% of its revenue to which AI capability?

A. Computer vision for automated checkout

B. Demand forecasting for inventory optimization

C. Product recommendation engine

D. Customer sentiment analysis

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Automated visual checkout (Amazon Go style) reduces friction and theft but is not the largest revenue driver in retail AI.
- **B** is incorrect. Demand forecasting reduces costs and improves supply chain efficiency but is not directly attributed to 35% of revenue.
- **C** is correct. Amazon attributes approximately 35% of its revenue to its recommendation engine — the highest-ROI AI application in retail history.
- **D** is incorrect. Sentiment analysis is a customer intelligence tool that informs product and service decisions but is not tied to a 35% revenue attribution.

---

**Question 5**

In the CRISP-DM framework, a team discovers during Phase 2 (Data Understanding) that the available training data is missing values for 40% of the most important features. What should the team do?

A. Proceed to modeling with the available data and note the limitation in the final report.

B. Skip to Phase 4 (Modeling) and let the algorithm handle missing values automatically.

C. Loop back to Phase 1 (Business Understanding) to assess whether the project goal is achievable and explore additional data sources.

D. Move directly to Phase 6 (Deployment) and collect better data post-deployment.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Proceeding with severely missing data almost guarantees an unacceptable model and wastes significant development investment.
- **B** is incorrect. Skipping data preparation and hoping the model handles missing values is a methodological error. Most algorithms require explicit handling of missing data. Skipping does not address the root cause.
- **C** is correct. CRISP-DM is explicitly iterative. Discovering that data is insufficient in Phase 2 requires looping back to Phase 1 to reassess the problem definition, adjust success criteria, or identify alternative data sources.
- **D** is incorrect. Deploying a model known to have poor data quality creates real business risk and is irresponsible.

---

**Question 6**

A manufacturing company wants to predict equipment failures before they occur, using vibration, temperature, and current draw data from sensors on production floor machinery. This is an example of which AI use case?

A. Visual quality inspection

B. Supply chain disruption prediction

C. Predictive maintenance

D. Demand forecasting

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Visual quality inspection uses camera images to detect defects in manufactured products, not sensor telemetry to predict equipment failure.
- **B** is incorrect. Supply chain disruption prediction models external supply and logistics factors, not internal equipment condition data.
- **C** is correct. Predictive maintenance uses sensor telemetry (vibration, temperature, current) to predict equipment failures before they occur, enabling just-in-time maintenance scheduling.
- **D** is incorrect. Demand forecasting predicts product demand for inventory planning, not equipment condition.

---

**Question 7**

A credit scoring AI model produces significantly lower approval rates for applicants in one demographic group compared to another, even when controlling for financial factors. This is an example of which concern?

A. Data drift in the production model

B. Concept drift in the training algorithm

C. Disparate impact — a fairness and regulatory compliance issue

D. Overfitting to the training dataset

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Data drift is a distribution shift in live inference data — a model monitoring concept, not a fairness problem.
- **B** is incorrect. Concept drift is a change in the true relationship between inputs and labels over time — also a monitoring concept, not a demographic disparity issue.
- **C** is correct. Disparate impact occurs when an AI model produces systematically different (and worse) outcomes for a protected demographic group. This violates fair lending laws (ECOA, FCRA) in the United States and is a core responsible AI concern.
- **D** is incorrect. Overfitting is a training problem where the model learns noise rather than signal. It does not inherently produce demographic disparities.

---

**Question 8**

A startup is deciding whether to build a custom recommendation model or use Azure Personalizer. The startup has no AI engineering team, needs a working system in two months, and sells a standard consumer product. What is the recommended approach?

A. Build a custom model to maintain full control of the recommendation logic.

B. Buy / use Azure Personalizer as the managed recommendation service.

C. Wait until the company can hire an AI team before deploying any recommendation capability.

D. Use a rule-based system (manual rules) instead of AI to avoid complexity.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Without an AI engineering team, building a custom recommendation model is not feasible in two months. The build option requires expertise the company does not have.
- **B** is correct. Azure Personalizer is a managed recommendation service requiring no ML expertise to deploy. It handles model training and serving. This matches the criteria: no internal talent, fast timeline, standard product.
- **C** is incorrect. Waiting foregoes competitive advantage. The company can use managed services now and hire AI talent later.
- **D** is incorrect. Rule-based systems for recommendations do not scale or personalize effectively. They require ongoing manual maintenance and produce inferior results.

---

**Question 9**

What percentage of an organization's annual revenue did Amazon attribute to its AI-powered recommendation engine, as discussed in Module 13?

A. 5%

B. 15%

C. 25%

D. 35%

**Correct Answer: D**

**Distractor Analysis:**

- **A** is incorrect. 5% would make the recommendation engine a modest contributor, not the dominant revenue driver it is.
- **B** is incorrect. 15% would be significant but understates the actual reported figure.
- **C** is incorrect. 25% is closer but still below the widely cited 35% attribution.
- **D** is correct. Amazon has reported that approximately 35% of its revenue comes from product recommendations generated by its AI systems, making it one of the most financially impactful AI deployments in commercial history.

---

**Question 10**

A data science team completes model training and achieves 96% accuracy on their held-out test set. They present this result to business stakeholders, who are unimpressed. The stakeholders say they need to understand "what this means for the business." What is the most appropriate next step?

A. Retrain the model with more data to improve accuracy above 96%.

B. Convert the accuracy metric into business impact — show how 96% accuracy translates to specific cost savings, revenue gains, or error reductions.

C. Deploy the model immediately since 96% accuracy meets any reasonable standard.

D. Replace the accuracy metric with AUC, which is a more sophisticated evaluation measure.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. 96% accuracy is already high. The problem is not model performance — it is communication. Stakeholders do not understand model accuracy; they understand business outcomes.
- **B** is correct. Bridging the gap between model metrics and business outcomes is a core AI project management skill. The team should show: "96% accuracy means 4% of transactions are misclassified. That translates to $X in annual fraud losses vs. the current 12% misclassification rate, which costs $Y."
- **C** is incorrect. Deploying without stakeholder understanding and buy-in creates organizational resistance and reduces the chance of successful adoption.
- **D** is incorrect. Switching metrics does not address the communication problem. AUC is even less interpretable to non-technical stakeholders than accuracy.

---

*Quiz prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
