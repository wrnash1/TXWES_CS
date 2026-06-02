# Discussion Forum: Module 04 - Neural Networks and Deep Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Due Dates:** Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM
**Total Points:** 10

---

## Instructions

Read all three scenarios below. Choose one scenario for your initial post. Identify your scenario choice (A, B, or C) at the top of your post.

---

## Scenario A: The Medical Diagnosis Black Box

A hospital system deploys a deep neural network that analyzes patient lab results, vital signs, and medical history to predict the risk of sepsis within the next 12 hours. The model achieves 94% accuracy and significantly outperforms the hospital's existing clinical scoring tools. However, the intensive care physicians push back against using the model in clinical decisions. "We cannot recommend interventions based on a system we cannot explain," one physician states. "If the model flags a patient and we act on it, and something goes wrong, we need to be able to explain why."

In your initial post (175-225 words), address all of the following:

- Explain why deep neural networks are inherently difficult to interpret, referencing the role of hidden layers and learned weights.

- Which Microsoft responsible AI principle does the physicians' concern most directly invoke? Explain how it applies in this clinical context.

- The hospital considers replacing the deep learning model with a decision tree that achieves 88% accuracy. Is this a reasonable trade-off? Defend your answer by weighing interpretability against predictive performance in a high-stakes medical context.

---

## Scenario B: The Autonomous Vehicle Training Dilemma

An autonomous vehicle startup is training a deep convolutional neural network to detect pedestrians from dashcam footage. Their dataset contains 500,000 labeled video frames collected in suburban settings in California and Texas during daytime. After training, the model achieves 96% accuracy on the test set drawn from the same dataset. When the startup tests the model in a pilot program in Seattle during winter, accuracy drops to 71%.

In your initial post (175-225 words), address all of the following:

- Explain why a convolutional neural network is the appropriate architecture for this task, referencing the properties of CNNs that make them suited to image data.

- Identify the root cause of the performance drop in Seattle. Use the ML concepts of training data distribution and generalization to explain what went wrong.

- Propose two concrete changes to the training pipeline that would improve the model's robustness to different geographic and weather conditions.

---

## Scenario C: The Small Dataset Fine-Tuning Decision

A museum wants to build an AI system that classifies uploaded photos of ancient coins into one of 40 historical categories. Their collection contains 1,200 labeled coin photos — 30 per category. A contractor proposes two options:

Option 1: Train a custom CNN from scratch using only the 1,200 museum images.
Option 2: Use transfer learning by fine-tuning a pretrained ResNet-50 model on the 1,200 images.

The contractor estimates Option 1 would take 3 weeks of GPU compute and likely result in poor generalization due to the small dataset. Option 2 would take 4 hours of fine-tuning on a single GPU.

In your initial post (175-225 words), address all of the following:

- Explain the concept of transfer learning and why it is particularly effective when labeled training data is scarce.

- Which layers of the pretrained ResNet-50 should be frozen during fine-tuning, and which should be updated? Explain the rationale.

- Beyond compute time, what are two other reasons Option 2 is likely to produce a better model than Option 1 for this specific use case?

---

## Peer Response Guidelines

Reply to at least two classmates who chose different scenarios than you. Each peer response must be at least 50 words and must add analysis beyond simple agreement.

Suggested peer response approaches:

- Challenge the responsible AI analysis in your peer's post with a counter-argument.

- Suggest a different architectural choice or technical solution than your peer proposed.

- Raise an edge case or limitation that your peer did not address.

- Connect the scenario to a real-world AI deployment story you have encountered.

---

## Grading Rubric (10 Points Total)

### Initial Post — 6 Points

**6 pts:** Addresses all required sub-questions with accurate course vocabulary. Meets 175-225 word requirement. Demonstrates original reasoning.

**4-5 pts:** Addresses most sub-questions with generally correct analysis. Minor vocabulary errors or one sub-question underdeveloped. Word count met.

**2-3 pts:** Fewer than half the sub-questions addressed, or significant factual errors. May not meet word count.

**0-1 pts:** Post missing or does not substantively engage with the scenario.

### Peer Responses — 4 Points

**4 pts:** Substantive responses to at least two peers from different scenarios. Each response adds new analysis or a counterpoint. Minimum 50 words each.

**2-3 pts:** Responds to two peers with limited substance, or responds to only one peer.

**0-1 pts:** No responses or all responses are superficial.

---

## Professor Nash Note

Scenario A raises a tension that is not going away: the most accurate AI models are often the least interpretable. This is not a hypothetical dilemma — healthcare organizations, lenders, and courts are actively wrestling with when algorithmic accuracy justifies reduced transparency. There is no universally correct answer here, and strong posts will engage honestly with the trade-offs rather than declaring one priority always wins.
