# Quiz: Module 15 — Advanced Topics: Generative Models and Transformers

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Instructions

This quiz contains 10 multiple-choice questions worth 10 points each. Select the single best answer. Distractors are analyzed for each question to support deeper understanding.

**Time limit:** 20 minutes

---

## Question 1

An autoencoder is trained to minimize the difference between its input and output. Why is the bottleneck (low-dimensional latent layer) essential to this objective?

- A) It prevents the network from memorizing training data by removing parameters
- B) It forces the encoder to learn a compressed representation that captures essential structure
- C) It ensures the decoder and encoder have matching weight dimensions
- D) It adds regularization equivalent to L2 weight decay

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. Removing parameters via bottleneck does constrain capacity, but the purpose is not memorization prevention — it is to force information compression.
- **B:** Correct. Without the bottleneck, the identity function (copying input to output) is trivially achievable. The bottleneck creates an information constraint that forces the encoder to distill essential features.
- **C:** Incorrect. The encoder and decoder architectures are typically mirrored but their weight dimensions are independent.
- **D:** Incorrect. L2 regularization penalizes large weights; the bottleneck constrains representational capacity — these are different mechanisms.

---

## Question 2

In a variational autoencoder, the encoder outputs `mu` and `log_var` instead of a single latent vector. What is the primary reason for using `log_var` instead of `var` (variance) directly?

- A) `log_var` is dimensionally smaller and reduces parameter count
- B) The log transform ensures numerical stability since variance is always positive and log variance can be any real number
- C) `log_var` is required by the TensorFlow API for sampling layers
- D) Using variance directly would prevent backpropagation through the encoder

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. `log_var` and `var` have the same dimensionality.
- **B:** Correct. Variance must be non-negative, but directly outputting a raw network activation can produce negative values. Predicting `log_var` (which is unconstrained) and then taking `exp(log_var)` to recover variance guarantees positivity and improves numerical stability.
- **C:** Incorrect. The reparameterization is a custom design choice, not a TF API requirement.
- **D:** Incorrect. The issue with backpropagation in VAEs is the sampling step itself, not the variance parameterization — that is addressed by the reparameterization trick.

---

## Question 3

The reparameterization trick in a VAE rewrites the sample `z ~ N(mu, exp(log_var))` as:

```python
z = mu + tf.exp(0.5 * log_var) * epsilon
```

where `epsilon ~ N(0, I)`. What problem does this solve?

- A) It prevents the KL divergence from dominating the loss during early training
- B) It makes the sampling step differentiable, enabling gradients to flow through mu and log_var
- C) It constrains the latent space to a unit hypercube
- D) It doubles the effective batch size by using random augmentation

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. KL annealing (gradually increasing KL weight) addresses the KL domination problem, not the reparameterization trick.
- **B:** Correct. Direct sampling from `N(mu, sigma^2)` is a stochastic node; gradients cannot flow through it. Reparameterizing moves the randomness to `epsilon`, which is independent of the parameters, making the remaining computation fully differentiable.
- **C:** Incorrect. The reparameterization does not constrain the latent space geometry; that is the role of the KL divergence term.
- **D:** Incorrect. Reparameterization has nothing to do with batch size.

---

## Question 4

In GAN training, **mode collapse** occurs when:

- A) The generator loss and discriminator loss both converge to zero
- B) The generator produces only a limited subset of the data distribution, ignoring diversity
- C) The discriminator achieves 100% accuracy on real vs fake classification
- D) The gradient of the generator loss explodes during backpropagation

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. Both losses converging to zero would indicate the generator has learned the full data distribution and the discriminator is at chance — the ideal outcome.
- **B:** Correct. Mode collapse means the generator converges to producing only a few types of outputs (modes). For MNIST, this might mean generating only digits "1" and "7" regardless of the noise input.
- **C:** Incorrect. A discriminator with perfect accuracy is actually an early training phase problem (the generator is too weak), but it is not called mode collapse.
- **D:** Incorrect. Gradient explosion is a separate training instability, not mode collapse.

---

## Question 5

In the scaled dot-product attention formula:

```python
scores = tf.matmul(Q, K, transpose_b=True) / tf.math.sqrt(d_k)
```

Why is the division by `sqrt(d_k)` necessary?

- A) To normalize the output values to the range [0, 1]
- B) To ensure the softmax receives well-scaled inputs — without scaling, large d_k causes extremely small gradients
- C) To make the attention weights sum to d_k rather than 1
- D) To prevent the key vectors from dominating the query vectors in the dot product

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. Softmax (not the scaling) normalizes to [0, 1]. Dividing by `sqrt(d_k)` does not directly constrain the range of scores before softmax.
- **B:** Correct. When `d_k` is large, the dot products `Q @ K^T` grow in magnitude because they sum `d_k` independent random terms. Large scores push softmax into near-zero gradient regions (saturation). Dividing by `sqrt(d_k)` keeps scores in a regime where softmax gradients are healthy.
- **C:** Incorrect. Softmax still normalizes weights to sum to 1 regardless of the scaling.
- **D:** Incorrect. The scaling affects the magnitude of all scores uniformly; it does not selectively affect keys vs queries.

---

## Question 6

In multi-head attention with H heads, the query, key, and value matrices are each projected into H separate subspaces before computing attention. What is the primary benefit of this design?

- A) It reduces the `O(n^2)` complexity of self-attention to `O(n log n)`
- B) It allows the model to jointly attend to information from different representation subspaces at different positions
- C) It eliminates the need for positional encodings
- D) It allows attention weights to be cached between layers for faster inference

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. Multi-head attention does not reduce the quadratic complexity; it runs H attention functions, each on `d_model / H` dimensions.
- **B:** Correct. Different heads can specialize in different types of relationships — syntactic dependencies, semantic similarities, coreference — simultaneously, then the concatenated outputs are projected back.
- **C:** Incorrect. Multi-head attention is order-agnostic; positional encodings remain necessary regardless of the number of heads.
- **D:** Incorrect. Attention weight caching between layers is not a property of multi-head attention.

---

## Question 7

A Transformer encoder block contains two sub-layers wrapped in residual connections and layer normalization. Which two sub-layers are present?

- A) Conv1D and MaxPooling1D
- B) Multi-head self-attention and position-wise feed-forward network
- C) LSTM and dense projection
- D) Cross-attention and causal masked self-attention

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. Conv1D and pooling are CNN components; Transformers do not use them in the standard encoder.
- **B:** Correct. The encoder block applies multi-head self-attention (each token attends to all tokens) followed by a two-layer dense FFN applied identically to each position.
- **C:** Incorrect. LSTMs are recurrent; Transformers specifically replace recurrence with attention.
- **D:** Incorrect. Cross-attention (attending to encoder output) and causal masking are features of the Transformer decoder, not the encoder.

---

## Question 8

BERT is pretrained using masked language modeling (MLM). Which description correctly defines MLM?

- A) The model predicts the next token in a sequence given all previous tokens
- B) The model predicts which of two sentences is more likely in natural language
- C) 15% of input tokens are randomly replaced with [MASK]; the model predicts the masked tokens using bidirectional context
- D) The model learns to match sentence embeddings to their paraphrase pairs

**Correct Answer:** C

**Distractor Analysis:**

- **A:** Incorrect. Predicting the next token from all previous tokens is causal language modeling — the GPT family's pretraining objective.
- **B:** Incorrect. Predicting which sentence is more likely describes a natural language inference task, not MLM.
- **C:** Correct. In MLM, 15% of tokens are masked; the model sees the full sequence (with masked positions) and predicts the original tokens using context from both directions.
- **D:** Incorrect. Sentence pair matching is used in contrastive learning approaches like SimCSE; it is not BERT's pretraining objective.

---

## Question 9

You want to use BERT for a binary sentiment classification task. Where do you attach the classification head?

- A) To the output embedding of every token, then average across positions
- B) To the output of the last token in the sequence
- C) To the `[CLS]` token's output from the final encoder layer
- D) To the `[SEP]` token's output, which marks the end of the sentence

**Correct Answer:** C

**Distractor Analysis:**

- **A:** Incorrect. Averaging across all token outputs is a valid feature extraction approach (mean pooling) used in some BERT variants, but the standard BERT classification approach uses the `[CLS]` token.
- **B:** Incorrect. The last token in BERT sequences is `[SEP]` (a separator token), not the classification token.
- **C:** Correct. BERT prepends a special `[CLS]` token whose final hidden state is designed to aggregate sequence-level information for classification.
- **D:** Incorrect. `[SEP]` marks boundaries between sentence segments and is not used for classification.

---

## Question 10

An autoencoder trained on manufacturing sensor data achieves low reconstruction error on normal operation logs. A new sensor reading produces reconstruction error 8 standard deviations above the training mean. What is the most appropriate interpretation?

- A) The autoencoder has overfit to the training data
- B) The sensor reading likely represents an anomaly that differs from normal operating patterns
- C) The autoencoder needs to be retrained with a larger bottleneck dimension
- D) The reconstruction loss function should be changed to mean absolute error

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. Overfitting would cause low reconstruction error on training data but the described behavior (high error on a new reading) is consistent with anomaly detection working correctly.
- **B:** Correct. Autoencoders learn to reconstruct normal patterns efficiently. Inputs that deviate significantly from training patterns cannot be reconstructed well, resulting in high error — the signature of anomalies.
- **C:** Incorrect. A larger bottleneck gives the encoder more capacity, which may actually reduce anomaly detection sensitivity by allowing it to reconstruct unusual patterns.
- **D:** Incorrect. Changing the loss function would not explain the observation or improve the interpretation; the high reconstruction error is informative.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | B |
| 3 | B |
| 4 | B |
| 5 | B |
| 6 | B |
| 7 | B |
| 8 | C |
| 9 | C |
| 10 | B |
