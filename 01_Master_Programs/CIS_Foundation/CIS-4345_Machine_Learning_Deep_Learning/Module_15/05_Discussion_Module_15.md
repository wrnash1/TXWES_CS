# Discussion Forum: Module 15 — Advanced Topics: Generative Models and Transformers

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Overview

This discussion has three scenarios exploring generative models and Transformers in applied contexts. Respond to **one** scenario with an original post of 175–225 words, then provide **two peer responses** of 75–100 words each. Peer responses must add substantive new analysis, not merely restate or agree.

**Due dates:** Original post by Wednesday 11:59 PM; peer responses by Sunday 11:59 PM.

---

## Scenario A — Autoencoder vs. VAE for Anomaly Detection

A cybersecurity team at a financial institution wants to detect fraudulent network traffic by training an unsupervised model on normal traffic logs. One engineer proposes a standard dense autoencoder; a second proposes a VAE. The team has 500,000 samples of normal traffic and zero labeled fraud examples.

Compare the autoencoder and VAE for this specific use case. Which architecture would you choose and why? Address: how each model defines "anomaly," whether the structured latent space of the VAE provides a real advantage over the standard autoencoder for detection, and what threshold-setting strategy you would use to decide when reconstruction error is high enough to flag traffic as suspicious.

**Sample response (for instructor reference — do not post):**

For anomaly detection on unlabeled data, I would choose the standard autoencoder over the VAE for this use case. Both models flag anomalies using reconstruction error — inputs that deviate from normal patterns cannot be reconstructed well. However, the VAE's KL divergence term regularizes the latent space toward `N(0, I)`, which is valuable for controlled generation but adds no practical benefit for detection. In fact, the KL term can slightly increase reconstruction error on normal samples to maintain the prior constraint, potentially reducing the signal-to-noise ratio of the detection threshold. The standard autoencoder maximizes reconstruction fidelity on the training distribution, which is exactly what you want for anomaly scoring. For threshold setting, I would use the training reconstruction error distribution: compute the 99th or 99.9th percentile of training errors and flag any test sample exceeding that percentile. This calibrates the false positive rate to approximately 0.1–1% on normal traffic, which a human analyst can review. The threshold should be validated against any available fraud samples (even a handful) before production deployment.

---

## Scenario B — GAN Training Instability

A student is training a DCGAN on a dataset of 10,000 product images (shoes, bags, and clothing) to generate synthetic product photos for data augmentation. After 20 epochs she observes: the discriminator loss is near zero and the generator loss is increasing. All generated images look identical — a blurry gray average of all shoes.

Diagnose what has gone wrong in this training run. Is the problem mode collapse, discriminator dominance, both, or something else? What specific architectural and training changes would you recommend to stabilize training? Your response should reference at least two specific GAN stabilization techniques from the reading guide.

**Sample response (for instructor reference — do not post):**

This is discriminator dominance combined with the early stages of mode collapse. When the discriminator loss approaches zero, it has learned to distinguish real from fake with near-perfect accuracy, providing the generator with a useless gradient — essentially a flat loss landscape where the generator cannot learn which direction to improve. The generator then collapses to a single safe output (the mean image) that at least does not actively fool no one, because improving from it seems equally pointless in all directions. Two targeted fixes: first, apply **label smoothing** — replace real labels of 1.0 with 0.9. This softens the discriminator's confidence ceiling, preserving a useful gradient signal to the generator. Second, increase the generator's learning rate relative to the discriminator's (or reduce the discriminator's) so the generator keeps pace. If these fail, consider switching to **Wasserstein loss with gradient penalty** (WGAN-GP), which provides a more informative gradient signal even when the discriminator is strong, and directly prevents the zero-gradient problem of the original minimax loss. With 10,000 images across three categories, the student should also ensure training data is well-shuffled and apply BatchNorm throughout the generator.

---

## Scenario C — BERT vs. Simpler NLP for a Business Problem

A regional hospital network wants to classify incoming patient complaint emails into six categories: billing, wait time, staff behavior, facility cleanliness, medical outcome, and other. They have 2,400 labeled complaint emails (400 per category) and a team of two junior ML engineers with no NLP experience. The CIO asks them to recommend the best approach.

Argue whether fine-tuning a pretrained BERT model is appropriate for this problem, or whether a simpler approach (TF-IDF + logistic regression, or a small LSTM + word embeddings) would serve the hospital better. Consider: dataset size, team expertise, inference latency requirements (emails are processed overnight in batch), interpretability needs for compliance, and total cost of ownership.

**Sample response (for instructor reference — do not post):**

BERT fine-tuning is appropriate here, and the team should use it. With 2,400 balanced labeled examples across six categories, this is exactly the regime where pretrained models shine: the dataset is too small to train a strong LSTM from scratch but large enough for effective fine-tuning. BERT-base fine-tuned for 3–5 epochs with `lr=2e-5` will likely achieve 85–92% accuracy; a TF-IDF classifier on this size dataset typically tops out at 75–82% on informal email language. The "no NLP experience" concern is mitigated by TensorFlow Hub — the preprocessing and encoder are packaged layers requiring only a classification head to be written, which is straightforward. Latency is not a concern because processing is overnight batch; BERT inference on 2,400 emails takes minutes. For compliance interpretability, attention weight visualization and LIME/SHAP explanations work with BERT. Total cost of ownership is low: the model can be retrained quarterly as new labeled complaints accumulate. If the team is still uncertain, the pragmatic path is to build both, evaluate on a held-out test set of 300 emails, and choose based on accuracy and maintenance simplicity.

---

## Peer Response Guidelines

Strong peer responses will do at least one of the following:

- Identify a constraint or edge case the original post overlooked
- Challenge a recommendation with a specific counterexample
- Introduce a relevant paper, technique, or real-world deployment that supports or complicates the post's conclusion
- Provide a precise quantitative argument (model size, training time, expected accuracy)

Generic agreement or paraphrase receives 0 points on the Peer Response criteria.

---

## Grading Rubric (10 points total)

| Criterion | Points |
|-----------|--------|
| Original post directly addresses the scenario | 2 |
| Technical accuracy of generative/Transformer claims | 2 |
| Depth of reasoning — tradeoffs considered | 2 |
| Word count within 175–225 range | 1 |
| Peer response 1 — substantive addition | 1.5 |
| Peer response 2 — substantive addition | 1.5 |
| **Total** | **10** |
