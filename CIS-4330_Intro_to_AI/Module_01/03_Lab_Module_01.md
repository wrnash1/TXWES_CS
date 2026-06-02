# Lab Activity: Module 01 - Introduction to AI and Machine Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe Artificial Intelligence workloads and considerations
**Points:** 100
**Submission:** Canvas LMS — Module 01 Lab Assignment

---

## Objectives

By the end of this lab, you will be able to:

- Classify real-world scenarios as AI, machine learning, or deep learning.
- Identify whether a scenario represents supervised, unsupervised, or reinforcement learning.
- Distinguish between regression and classification tasks.
- Match business scenarios to the appropriate Azure AI service tier.
- Apply the responsible AI framework to a scenario and identify the relevant principle.

---

## Prerequisites

No Azure subscription is required for this lab. All exercises are classification and analysis tasks completed in writing. You will need:

- Access to the Module 01 video lecture (completed).
- Access to the Module 01 reading guide (completed).
- A word processor or text editor for your written responses.

---

## Part A: AI, ML, and DL Classification (25 points)

Read each scenario below. For each scenario, write your answer and a one-sentence justification explaining your reasoning. Use the exact label from the provided options.

**Answer options:** Traditional AI (rule-based), Machine Learning, or Deep Learning

### Scenario 1

A bank's fraud detection system was programmed by analysts who wrote hundreds of if-then rules: "Flag the transaction if the amount exceeds $5,000 AND the location differs from the cardholder's home city AND the transaction occurs between midnight and 4 AM." The system applies these rules to every transaction.

**Your classification:** _______________
**Justification:** _______________

### Scenario 2

A retail company trained a model on three years of historical sales data. The model learned to predict next month's inventory demand for each product category. No explicit formulas were written — the system discovered the relationship between seasonality, promotions, and demand on its own.

**Your classification:** _______________
**Justification:** _______________

### Scenario 3

A medical imaging company built a system that analyzes CT scans to detect early-stage tumors. The system was trained on 500,000 labeled scans and uses a convolutional neural network with 50 layers to automatically identify spatial features — edges, shapes, density gradients — without any hand-crafted feature engineering.

**Your classification:** _______________
**Justification:** _______________

### Scenario 4

A chess program uses a minimax search algorithm to evaluate every possible sequence of moves up to 20 steps ahead and selects the move that maximizes its advantage assuming the opponent plays optimally. The program was not trained on game data; the evaluation function was written by programmers.

**Your classification:** _______________
**Justification:** _______________

### Scenario 5

An email platform uses a model trained on 10 million labeled emails to classify incoming messages as spam, promotional, social, or primary. The model analyzes word frequencies, sender reputation scores, and link patterns.

**Your classification:** _______________
**Justification:** _______________

---

## Part B: Learning Paradigm Classification (25 points)

Read each scenario. Classify it as supervised learning, unsupervised learning, or reinforcement learning. Write your answer and a two-sentence justification.

### Scenario 6

A hospital wants to group its patients into segments based on shared health risk factors, without knowing in advance how many groups exist or what characteristics define each group. The hospital plans to use the discovered groups to design targeted wellness programs.

**Your classification:** _______________
**Justification:** _______________

### Scenario 7

A streaming service trained a model to predict whether a user will watch a recommended movie, using historical watch-or-skip labels from millions of users as the training signal.

**Your classification:** _______________
**Justification:** _______________

### Scenario 8

A robotics company is training a robot arm to pick objects off a conveyor belt. The robot receives a positive reward when it successfully picks an object and places it correctly, and a penalty when it drops the object or misses. The robot has no labeled dataset of correct pick trajectories; it learns by trial and error.

**Your classification:** _______________
**Justification:** _______________

### Scenario 9

A cybersecurity team trains a model to detect unusual network traffic patterns. The training data contains only normal traffic — no labeled examples of attacks — and the model must learn what "normal" looks like so it can flag deviations.

**Your classification:** _______________
**Justification:** _______________

### Scenario 10

A mortgage company trains a model to predict the probability that a loan applicant will default within 24 months. The training data includes 100,000 past applications, each labeled with the outcome (defaulted / did not default).

**Your classification:** _______________
**Justification:** _______________

---

## Part C: Regression vs Classification (20 points)

For each scenario, identify whether it is a regression task or a classification task. Write the correct label and a one-sentence justification.

### Scenario 11

A weather service wants to predict the exact temperature in degrees Fahrenheit for a city at 3:00 PM tomorrow.

**Your classification:** _______________
**Justification:** _______________

### Scenario 12

A hospital system wants to determine whether a given patient is likely to be readmitted within 30 days of discharge: yes or no.

**Your classification:** _______________
**Justification:** _______________

### Scenario 13

A real estate platform wants to predict the selling price of a home based on square footage, location, number of bedrooms, and year built.

**Your classification:** _______________
**Justification:** _______________

### Scenario 14

A content moderation platform wants to sort user-submitted images into one of five categories: appropriate, adult content, violence, hate symbols, or misinformation.

**Your classification:** _______________
**Justification:** _______________

---

## Part D: Azure Service Tier Matching (20 points)

Match each scenario to the most appropriate Azure AI service tier: Azure Machine Learning, Azure Cognitive Services, or Azure Applied AI Services. Write your answer and a one-sentence justification.

### Scenario 15

A startup wants to add image captioning to its mobile app. They have no image training data and no data science team. They need a solution they can integrate with a REST API call in one afternoon.

**Your match:** _______________
**Justification:** _______________

### Scenario 16

A pharmaceutical company has a proprietary dataset of 2 million molecular structures labeled with drug efficacy outcomes. They need to train a custom deep learning model and track 500 experiments to find the best-performing architecture.

**Your match:** _______________
**Justification:** _______________

### Scenario 17

A financial institution wants to automatically extract key fields — date, amount, account number — from scanned paper invoices and route them to the correct accounting department.

**Your match:** _______________
**Justification:** _______________

### Scenario 18

A call center wants to add real-time speech-to-text transcription to customer service calls. They need a scalable API solution and do not need to train a custom speech model.

**Your match:** _______________
**Justification:** _______________

---

## Part E: Responsible AI Application (10 points)

Read the following scenario and answer the two questions below in complete sentences (minimum 3 sentences per answer).

### Scenario

A city government deploys an AI-powered predictive policing system. The system was trained on 15 years of arrest records and uses those patterns to predict which neighborhoods are at high risk for crime each week. Police patrol resources are allocated based on the model's predictions. A civil rights organization audits the system and finds that neighborhoods with historically high minority populations are consistently flagged as high risk, regardless of current crime data, because the historical arrest data reflects past over-policing patterns rather than true crime rates.

**Question 1:** Which of Microsoft's six responsible AI principles is most directly violated in this scenario? Identify the principle by name and explain specifically how it is violated using details from the scenario.

**Your answer:** _______________

**Question 2:** Propose two concrete changes the city could make to better align this AI system with responsible AI principles. For each change, identify which responsible AI principle it addresses.

**Your answer:** _______________

---

## Answer Key and Grading Rubric

### Part A Rubric (5 points per scenario = 25 points)

**Scenario 1 — Traditional AI (rule-based):** The system uses explicit if-then rules written by human analysts. No learning from data occurs.

**Scenario 2 — Machine Learning:** The system discovers patterns in historical data without explicit rules. The relationship between inputs and demand is learned, not programmed.

**Scenario 3 — Deep Learning:** Convolutional neural networks with 50 layers processing unstructured image data is the defining characteristic of deep learning.

**Scenario 4 — Traditional AI (rule-based):** Minimax search with a programmer-written evaluation function is a rule-based AI technique, not machine learning.

**Scenario 5 — Machine Learning:** Training on labeled email data to classify categories is supervised machine learning. A neural network would make this deep learning, but the scenario does not specify architecture.

Scoring per scenario: 5 pts = correct answer with accurate justification. 3 pts = correct answer with incomplete justification. 0 pts = incorrect answer.

### Part B Rubric (5 points per scenario = 25 points)

**Scenario 6 — Unsupervised learning:** No labels. Goal is to discover group structure.

**Scenario 7 — Supervised learning:** Historical watch/skip labels provide the supervision signal.

**Scenario 8 — Reinforcement learning:** Agent, environment, reward signal, and trial-and-error learning define RL.

**Scenario 9 — Unsupervised learning:** Only normal traffic data with no attack labels. The model learns the distribution of normal.

**Scenario 10 — Supervised learning:** Labeled outcomes (defaulted / did not default) provide direct supervision.

### Part C Rubric (5 points per scenario = 20 points)

**Scenario 11 — Regression:** Temperature is a continuous value.

**Scenario 12 — Classification:** Yes/no readmission is a binary classification output.

**Scenario 13 — Regression:** Selling price is a continuous numerical output.

**Scenario 14 — Classification:** Five discrete categories constitute a multi-class classification task.

### Part D Rubric (5 points per scenario = 20 points)

**Scenario 15 — Azure Cognitive Services:** Prebuilt image captioning API, no training required.

**Scenario 16 — Azure Machine Learning:** Custom deep learning model with experiment tracking requires Azure ML.

**Scenario 17 — Azure Applied AI Services:** Azure Form Recognizer (Applied AI) handles document field extraction end-to-end.

**Scenario 18 — Azure Cognitive Services:** Azure Speech Service provides real-time speech-to-text via API without custom model training.

### Part E Rubric (10 points)

**Question 1 (5 pts):** Full credit requires naming Fairness as the primary principle and explaining that historical over-policing data encodes racial bias, causing the model to perpetuate that bias in future patrol allocation decisions.

**Question 2 (5 pts):** Full credit requires two distinct changes, each linked to a named principle. Acceptable examples: audit training data for demographic bias (Fairness); use current crime reporting data instead of arrest records (Fairness/Reliability); require human review before deploying patrol allocations (Accountability); publish the model's methodology and limitations publicly (Transparency).

---

## Deliverable

Submit a single document (PDF or Word) containing:

1. Your answers to all 18 scenarios and questions.
2. Your name, course section, and date at the top of the document.

Upload to the Module 01 Lab Assignment in Canvas by the posted due date.
