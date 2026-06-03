# Discussion Forum: Module 04 — Neural Networks and Deep Learning Foundations

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Instructions

Post your **initial response** to one of the three scenarios below by **Wednesday at 11:59 PM**. Your initial post must be **175–225 words** written in complete sentences. Respond to **at least two classmates** by **Sunday at 11:59 PM** with a minimum of **60 words each**. Peer responses must add substance — extend the argument, offer a counterexample, or connect the idea to a different application.

---

## Scenario A — Activation Function Consequences in Production

A data science team at a logistics company builds a neural network to predict whether a shipment will arrive on time (binary classification). The network has six hidden layers and uses sigmoid activation throughout — including all hidden layers. The model trains for 100 epochs but validation accuracy never climbs above 53%, barely better than random guessing. A junior engineer suggests the problem is "not enough training data." A senior engineer disagrees.

Explain what is most likely happening in this network from a mathematical standpoint. Identify the specific failure mode by name, explain why sigmoid causes it in deep networks, and describe the change you would make to fix it. Then explain why that fix works at the gradient level. Your response should reference at least one specific activation function property (such as gradient range or saturation behavior) to support your reasoning.

---

## Scenario B — Choosing the Right Loss Function

You are consulting for a university admissions department building a model to classify applications into one of four categories: Strong Accept, Likely Accept, Likely Reject, and Strong Reject. A graduate student on the team proposes using Mean Squared Error as the loss function because "it minimizes the difference between predicted and actual values." Another team member argues this is the wrong choice.

Evaluate both positions. Explain why MSE is or is not appropriate for this classification task and what the correct loss function choice should be. Describe what output layer activation function pairs with your recommended loss function and explain the mathematical property that makes them work together. If you were setting up this model in Keras, describe what the final two lines of your `model.compile()` call would look like and why.

---

## Scenario C — Gradient Descent and Learning Rate Decisions

A machine learning engineer is training a deep network to detect fraudulent transactions. She runs three experiments with identical architectures and data, varying only the learning rate: `lr=0.1`, `lr=0.001`, and `lr=0.00001`. After 50 epochs, she observes the following: the first run has wildly oscillating loss that never converges, the second run shows steady smooth improvement, and the third run barely moves from its initial loss.

Explain what is happening in each of the three runs using gradient descent theory. For each run, name the problem and describe what is happening geometrically on the loss surface. Recommend a practical strategy for finding a good learning rate without running dozens of full training experiments. Your response should demonstrate understanding of the relationship between learning rate, step size, and convergence.

---

## Peer Response Requirements

Your two peer responses must each:

- Be at least 60 words in complete sentences
- Add a new idea, counterexample, or alternative interpretation — not just agreement
- Reference a specific technical concept from the module (activation functions, gradient descent, loss functions, backpropagation, or weight initialization)

Responses that only say "Good point" or restate what the peer wrote will receive no credit.

---

## Grading Rubric (10 Points Total)

| Criterion | Points |
|---|---|
| Initial post is 175–225 words in complete sentences | 1 |
| Correctly identifies and names the relevant technical concept | 2 |
| Explanation demonstrates accurate understanding of the mechanism | 3 |
| Response connects theory to the practical scenario described | 2 |
| Two peer responses, each 60+ words with substantive new content | 2 |
| **Total** | **10** |

---

## Professor Nash — Closing Note

The three scenarios in this discussion are not hypothetical edge cases — they represent real mistakes I have seen in production ML systems. Sigmoid hidden layers in deep networks, wrong loss functions for classification tasks, and misconfigured learning rates are among the most common reasons a neural network fails to learn despite appearing to be correctly assembled.

The goal of this discussion is not to give a textbook definition. It is to reason through a broken system and explain why it is broken, which is exactly what you will need to do when debugging your own models. By the time you complete the TensorFlow Developer Certificate, these patterns should be instinctive.

Read your classmates' posts carefully. You will often find that someone else reasoned about the same scenario from a different angle — and that different angle is worth more than any single correct answer.
