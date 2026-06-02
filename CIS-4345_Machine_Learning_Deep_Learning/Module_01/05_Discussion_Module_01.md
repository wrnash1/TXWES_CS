# Discussion: Module 01 - ML Fundamentals

Course: CIS-4345 Machine Learning and Deep Learning
Institution: Texas Wesleyan University
Instructor: Professor Nash
Total Points: 10

---

## Instructions

Read all three scenarios below. Choose one scenario to address in your initial post. Your initial post is due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Choosing the Right Learning Paradigm

A hospital system wants to build an AI tool to support clinical decision-making. They have three project proposals on the table. Proposal 1: Predict whether a patient admitted to the emergency department will be readmitted within 30 days (labeled historical records available). Proposal 2: Identify unusual patterns in billing codes that no one has flagged before (no labeled fraud examples exist). Proposal 3: Train a robotic medication dispenser to minimize dispensing errors through trial and feedback over many shifts.

In 175-225 words, identify which learning paradigm — supervised, unsupervised, or reinforcement learning — applies to each proposal and explain your reasoning. Then discuss one practical data challenge the hospital would face implementing Proposal 1, such as class imbalance, missing values, or privacy constraints, and describe a specific strategy to address it. Reference at least one concept from the Module 01 reading guide in your response.

---

## Scenario B: Diagnosing Bias and Variance

A student builds a neural network to classify images of handwritten digits. After 50 training epochs, the training accuracy is 98.7% and the validation accuracy is 64.2%. The student concludes the model is working well because the training accuracy is high.

In 175-225 words, explain why the student's conclusion is incorrect. Use the bias-variance tradeoff framework to diagnose the specific problem and classify it as underfitting or overfitting. Describe two concrete remedies the student could apply in TensorFlow or Keras to address this problem — be specific about the Keras API calls or layer types involved. Then explain what the training and validation accuracy curves should look like after a successful fix, and how the student should use those curves to decide when to stop training.

---

## Scenario C: The ML Pipeline in Practice

A startup is building a product recommendation engine for an e-commerce platform. The engineering team wants to skip the problem-definition and data-preprocessing stages and go straight to model training because they feel those stages are "not real coding." The data science lead pushes back.

In 175-225 words, argue the data science lead's position. Explain why skipping problem definition leads to wasted model-building effort, and give a specific example of how an undefined evaluation metric could cause the team to build the wrong model entirely. Then describe two preprocessing steps that, if skipped, would directly harm model performance — be specific about what goes wrong technically. Close by connecting one of the seven ML pipeline stages to a specific step you will perform in this module's lab.

---

## Discussion Rubric

| Criteria | Points | Description |
|---|---|---|
| Initial post — content accuracy | 3 | Concepts are technically correct and use appropriate ML terminology. |
| Initial post — depth of analysis | 2 | Response goes beyond surface-level description; includes specific Keras or TF API references. |
| Initial post — word count and clarity | 1 | 175-225 words; clearly written with logical structure. |
| Peer response 1 | 2 | Identifies a specific point to build on or challenge; adds new information or a counterexample. |
| Peer response 2 | 2 | Same standard as peer response 1. Responses of fewer than 40 words receive 0 points. |
| Total | 10 | |

---

## Professor Nash Note

Choose the scenario that connects most directly to a career path you are considering. There is no single correct answer — I am evaluating your reasoning process and your use of the vocabulary from this module. When responding to peers, focus on extending the conversation rather than simply agreeing. If a classmate made a claim you would like to push back on, do so respectfully and with evidence from the course material.
