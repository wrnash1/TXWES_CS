# Discussion Forum: Module 02 - Supervised vs Unsupervised Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Due Dates:** Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM
**Total Points:** 10

---

## Instructions

Read all three scenarios below. Choose one scenario for your initial post. Identify your scenario choice (A, B, or C) at the top of your post.

---

## Scenario A: The Loan Approval Model

A regional bank wants to use machine learning to automate its personal loan approval process. The data science team has access to five years of historical loan applications — 120,000 records — with features including credit score, income, employment type, loan amount requested, and debt-to-income ratio. Each record is labeled with the outcome: approved or denied. The team initially trains a logistic regression model, which achieves 84% accuracy. A manager suggests switching to a more powerful gradient boosting model, which achieves 91% accuracy. However, the bank's compliance officer notes that federal lending law requires the bank to explain the reason for any denial to the applicant.

In your initial post (175-225 words), address all of the following:

- Classify this problem as supervised or unsupervised, and as regression or classification. Explain your reasoning.
- The compliance officer's concern creates a tension between accuracy and interpretability. Which model — logistic regression or gradient boosting — should the bank use, and why? Reference the algorithm comparison concepts from the reading guide.
- Identify one responsible AI principle that is relevant to this scenario and explain why it applies.

---

## Scenario B: The Product Recall Detection System

A consumer electronics manufacturer wants to use machine learning to identify products at risk of failure before customers report issues. The quality assurance team has sensor data from the manufacturing line for 2 million units — temperature, voltage, pressure, and vibration readings at various production stages. No failures have been recorded yet for the products currently on the market, and no historical failure labels are available. The team must decide between two approaches: (1) use unsupervised anomaly detection on the sensor data to flag unusual production readings, or (2) wait until some failures accumulate, then train a supervised classification model.

In your initial post (175-225 words), address all of the following:

- Explain why option 1 (unsupervised) is or is not the correct initial approach given the data available.
- What are the limitations of the unsupervised approach in this context? What does the model not know that a supervised model would know?
- Under what conditions would the team be ready to transition to a supervised model, and what would that transition require?

---

## Scenario C: The Student Performance Predictor

A university's institutional research office wants to build a machine learning model to identify students at risk of academic failure early enough in the semester to intervene. The office has five years of student records with features including high school GPA, SAT scores, attendance rate, number of late assignments, and financial aid status. Each student's record is labeled with their final status: in good standing or academic probation. The model will be used to trigger outreach from academic advisors.

In your initial post (175-225 words), address all of the following:

- Identify the learning paradigm and task type. Explain why this is not an unsupervised problem even though the university is trying to "discover" which students are at risk.
- The model correctly identifies 78% of at-risk students (recall = 0.78) but also flags 35% of students who are actually in good standing (false positive rate = 0.35). Is this trade-off acceptable in this context? Defend your answer.
- Propose one feature that is currently in the dataset that could introduce bias and explain which responsible AI principle that risk relates to.

---

## Peer Response Guidelines

Reply to at least two classmates who chose different scenarios than you. Each peer response must be at least 50 words and must add substantive analysis beyond simple agreement.

Suggested peer response approaches:

- Challenge the algorithm choice made in your peer's initial post using evidence from the reading guide.
- Propose an alternative solution to the business problem they analyzed.
- Identify a responsible AI principle they did not mention that also applies to their scenario.
- Ask a probing follow-up question and provide your own tentative answer.

---

## Grading Rubric (10 Points Total)

### Initial Post (6 Points)

- **6 pts:** Addresses all required sub-questions with accurate use of course vocabulary (paradigm, task type, algorithm characteristics, responsible AI). Meets the 175-225 word requirement. Demonstrates original reasoning.
- **4-5 pts:** Addresses most sub-questions. Minor vocabulary errors or one sub-question is underdeveloped. Word count met.
- **2-3 pts:** Fewer than half the sub-questions addressed, or significant factual errors present. May not meet word count.
- **0-1 pts:** Post is missing or does not engage substantively with the chosen scenario.

### Peer Responses (4 Points)

- **4 pts:** Substantive responses to at least two peers from different scenarios. Each response adds new analysis or challenges an assumption. Minimum 50 words each.
- **2-3 pts:** Responds to two peers with limited added substance. Or responds to only one peer.
- **0-1 pts:** No responses, or all responses are superficial.

---

## Professor Nash Note

Scenario B is intentionally the most challenging of the three because it asks you to reason about when unsupervised learning is a reasonable starting point and when you need to pivot toward a supervised approach. Strong posts will engage honestly with both the strengths and the limitations of the approach they recommend, rather than presenting one method as universally correct.
