# Discussion Forum: Module 07 — Convolutional Neural Networks

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Overview

This discussion asks you to connect the CNN concepts from this module to real-world scenarios. You will post an original response to one scenario and reply constructively to at least two classmates. Strong posts demonstrate technical accuracy, connect theory to application, and cite specific Keras constructs or architectural decisions where relevant.

---

## Scenario A — Medical Imaging and Model Interpretability

A hospital system wants to deploy a CNN to assist radiologists in detecting pneumonia from chest X-ray images. A radiologist on the team raises a concern: "We cannot use a model that is a black box — we need to understand why it flagged an image as positive." The data science team proposes using feature map visualization and Grad-CAM (Gradient-weighted Class Activation Mapping) to highlight the regions of the image the network attended to most strongly.

Respond to this scenario in 175–225 words. Address all of the following:

- Explain what feature maps reveal about a CNN's internal processing and why early-layer feature maps differ from late-layer feature maps in terms of what they represent.

- Describe one concrete risk of deploying a CNN in a high-stakes medical setting without interpretability tools, and explain how feature visualization partially mitigates that risk.

- Identify one limitation of feature map visualization alone (compared to techniques like Grad-CAM or LIME) and explain why that limitation matters in a clinical context.

---

## Scenario B — Architecture Design Trade-offs

A startup is building an image classification system to sort recycled materials on a conveyor belt (glass, plastic, metal, paper — 4 classes). They have `10,000` labeled training images at `64x64` pixels and must run inference on an embedded device with limited memory (no GPU). Two engineers disagree: Engineer A wants a deep CNN with six blocks (32→64→128→256→512→512 filters), arguing more layers means better features. Engineer B wants a shallow CNN with three blocks (32→64→128) plus aggressive `GlobalAveragePooling2D`, arguing it will generalize better on limited data.

Respond in 175–225 words. Address all of the following:

- Analyze both engineers' positions using specific arguments about parameter count, overfitting risk, and inference speed.

- Recommend one architecture and justify your choice, citing at least one concrete trade-off (e.g., accuracy vs. latency, capacity vs. regularization need).

- Explain how the choice of `GlobalAveragePooling2D` vs. `Flatten + Dense` affects both parameter count and generalization for a 10,000-image dataset.

---

## Scenario C — Debugging a Poorly Performing CNN

A student trains the following CNN on the CIFAR-10 dataset for 50 epochs and reports that training accuracy reaches 99% while validation accuracy never exceeds 58%. They share their architecture:

```python
model = keras.Sequential([
    keras.layers.Conv2D(256, (3,3), activation='relu', input_shape=(32,32,3)),
    keras.layers.Conv2D(256, (3,3), activation='relu'),
    keras.layers.Conv2D(256, (3,3), activation='relu'),
    keras.layers.Flatten(),
    keras.layers.Dense(1024, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

Respond in 175–225 words. Address all of the following:

- Identify at least three specific architectural or training problems visible in this code that contribute to the 41-percentage-point gap between training and validation accuracy.

- Propose a revised architecture that addresses each problem you identified, naming the specific layers or hyperparameters you would change and why.

- Explain what the training and validation accuracy curves would likely look like for your corrected model compared to the original — and what a healthy curve should look like.

---

## Posting Requirements

**Initial Post (due Wednesday at 11:59 PM)**

Choose one scenario (A, B, or C) and write a response of 175–225 words. Your post must:

- Be written in your own words — do not paste code blocks or bullet-point lists as your entire response.

- Reference at least one specific Keras layer, parameter, or architectural concept from the module content.

- Stay within the 175–225 word target (posts under 150 or over 250 words will lose points).

**Peer Responses (due Sunday at 11:59 PM)**

Reply to at least two classmates who responded to different scenarios than you did. Each reply must be 60–90 words and must:

- Identify one point in their response you agree with and explain why.

- Add one piece of information, counter-argument, or alternative approach they did not mention.

Replies that only say "Great post!" or restate the classmate's argument without adding new content will receive zero peer response points.

---

## Grading Rubric (10 Points Total)

| Criterion | Points |
|---|---|
| Initial post addresses all required sub-questions for the chosen scenario | 3 |
| Technical accuracy — CNN terms and Keras constructs used correctly | 2 |
| Appropriate response length (175–225 words) | 1 |
| Peer response 1 — adds substantive new information or counter-argument | 2 |
| Peer response 2 — adds substantive new information or counter-argument | 2 |

---

## Professor Nash's Closing Note

CNNs are not magic — they are a structured set of engineering decisions. Every choice you make (filter count, kernel size, pooling strategy, regularization) has a measurable effect on accuracy, speed, and generalizability. The best ML engineers do not just build models that work on training data; they ask why the model works, where it will fail, and what it would take to deploy it responsibly.

As you discuss these scenarios, think like an engineer who will eventually hand this model to someone whose job depends on it being right. That mindset is what separates a practitioner from a prototype-builder — and it is what the TensorFlow Developer Certificate is ultimately testing.

See you in the next module.

— Professor Nash
