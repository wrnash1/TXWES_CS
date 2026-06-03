# Discussion Forum: Module 13 — Time Series Forecasting with TensorFlow

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Overview

This discussion has three scenarios. Respond to **one** scenario with an original post of 175–225 words, then provide **two peer responses** of 75–100 words each. Peer responses must add new analysis or constructive critique — agreement without elaboration does not earn full credit.

**Due dates:** Original post by Wednesday 11:59 PM; peer responses by Sunday 11:59 PM.

---

## Scenario A — The Leaky Pipeline

A data science intern at a logistics company builds a demand-forecasting model for daily package shipments. She splits the 3-year dataset randomly into 80% training and 20% validation, trains a stacked LSTM, and reports a validation MAE of 1.2 — far below the company benchmark of 3.0. Her manager, a senior ML engineer, is skeptical and asks her to re-run the experiment with a temporal split. The new validation MAE is 4.7, worse than the naive baseline.

Discuss what went wrong in the original experiment. Why did the random split produce such a misleadingly low MAE? What specific form of data leakage occurred? If you were the senior engineer, what steps would you walk the intern through to diagnose and fix the pipeline? Consider whether the temporal-split MAE of 4.7 necessarily means the model is bad, or whether additional context would change your assessment.

**Sample response (for instructor reference — do not post):**

The intern's random split allowed future shipment data to appear in the training set, giving the LSTM implicit knowledge of outcomes it should not have access to at inference time. This is temporal data leakage — the model effectively memorized associations between training windows and validation labels that do not respect causal time order. The 1.2 MAE was illusory. After the temporal split, the 4.7 MAE reflects genuine out-of-sample difficulty. However, 4.7 is not necessarily damning — the senior engineer should compare it to the naive baseline (last-day forecast). If the naive baseline is also around 4–5, the model is learning nothing useful and needs architectural changes or better features. If the naive baseline is 8+, then 4.7 represents real value. Steps to fix: enforce temporal split, inspect for other leakage sources (normalization stats from full series, any target-encoded features), and plot residuals over time to diagnose systematic bias. The intern's mistake is common and instructive.

---

## Scenario B — CNN vs. LSTM: Architecture Selection

A team at a utility company is building a model to forecast hourly electricity demand 24 hours ahead. They have two years of hourly data and seven candidate features: temperature, humidity, day of week, hour of day, holiday flag, previous 24-hour load, and previous week's same-hour load. One engineer argues that a 1D CNN is sufficient and will train 10x faster. Another argues that an LSTM is necessary to capture the weekly and seasonal dependencies. A third suggests a hybrid CNN-LSTM model.

Taking a position, argue which architecture you would choose for this problem and justify your reasoning. Address: (1) the relevant dependency structure in the data, (2) the computational tradeoffs, and (3) how you would validate your choice empirically using the metrics and baseline approaches from Module 13.

**Sample response (for instructor reference — do not post):**

I would start with the CNN for practical reasons. Electricity demand exhibits strong local patterns — the shape of demand within a 24-hour window is highly predictive regardless of what happened two weeks ago. A Conv1D stack with kernel sizes of 3–7 can capture morning-peak and evening-peak shapes efficiently. The 10x training speed advantage matters when iterating hyperparameters. However, the weekly dependency (previous same-hour load) is a manually engineered lag feature, not something the CNN needs to model implicitly. By including `lag_168` (previous week's same hour) as an explicit input feature in the multivariate design, I can give the model the long-range context it needs without requiring LSTM memory. I would validate the choice by establishing the naive baseline (predict last week's same-hour demand), then comparing CNN, LSTM, and CNN-LSTM MAE/RMSE on a temporal validation set covering at least one full seasonal cycle. The winner is the one that beats the baseline by the largest margin while meeting latency requirements for production inference.

---

## Scenario C — Evaluation in Context

A student finishes the Module 13 lab and reports the following results:

| Model | MAE | RMSE |
|-------|-----|------|
| Naive Baseline | 5.21 | 7.14 |
| Dense | 4.88 | 6.73 |
| 1D CNN | 4.15 | 5.92 |
| Stacked LSTM | 4.22 | 6.01 |

She is confused because the CNN slightly outperforms the LSTM — she expected the LSTM to win because it has memory. She is also unsure whether a 20% improvement over the naive baseline justifies deploying a deep learning model in a real system.

Explain why the CNN may have outperformed the LSTM on this particular dataset. What characteristics of the synthetic time series (short seasonal cycles, moderate noise, limited sequence length) might favor convolutional over recurrent architectures? Then address the deployment question: what criteria beyond raw MAE should factor into the decision to use a deep learning model over a simple baseline?

**Sample response (for instructor reference — do not post):**

CNNs outperforming LSTMs on short-window tasks is common and well-documented. The synthetic series has a 7-day weekly cycle and a 365-day annual cycle, but neither requires the LSTM to integrate information from more than 30 steps back (our window size). Within that window, the CNN's local pattern detection is just as powerful as the LSTM's gated memory — and the CNN has fewer parameters to fit, reducing overfitting risk on limited data. The LSTM also requires sequential computation across time steps, making it more susceptible to suboptimal learning rates on this scale. On the deployment question: raw MAE is necessary but insufficient. Decision-makers need to weigh inference latency (can the model serve predictions in real time?), retraining frequency (how often does the series distribution shift?), interpretability requirements (is a neural network explainable to stakeholders?), and operational cost (cloud compute for serving). A 20% improvement over the naive baseline has economic value only if the forecasting task drives decisions where that accuracy difference changes outcomes — such as inventory ordering or staffing schedules. If the business impact is small, a simple moving average may be preferable due to lower maintenance burden.

---

## Peer Response Guidelines

Strong peer responses will do at least one of the following:

- Introduce a counterargument or edge case the original post did not consider
- Connect the scenario to a real-world domain or industry application
- Provide a specific code-level example that supports or challenges a claim
- Identify a logical gap in the original post's reasoning

Responses that only say "Great point, I agree" or paraphrase the original without adding substance will receive 0 points on the Peer Response criterion.

---

## Grading Rubric (10 points total)

| Criterion | Points |
|-----------|--------|
| Original post addresses the scenario directly | 2 |
| Technical accuracy of claims | 2 |
| Depth of reasoning (not surface-level restatement) | 2 |
| Word count within 175–225 range | 1 |
| Peer response 1 — substantive addition | 1.5 |
| Peer response 2 — substantive addition | 1.5 |
| **Total** | **10** |
