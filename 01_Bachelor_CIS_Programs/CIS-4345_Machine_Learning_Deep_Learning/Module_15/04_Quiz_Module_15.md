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

### Question 11 (5 points)

A VAE is trained on MNIST digits. After training, you sample two latent vectors `z_1` and `z_2` corresponding to the encoded representations of a "3" and an "8". You decode 10 evenly spaced points along the straight line between `z_1` and `z_2`. What is this operation called, and what result do you expect in a well-trained VAE?

- A) Latent projection; the decoded images will all look like noise because points off the training manifold are unseen
- B) Latent interpolation; the decoded images should show a smooth visual transition from "3" to "8"
- C) Latent sampling; the decoded images will be random digits from the full prior distribution
- D) Latent clustering; each decoded image will snap to the nearest class centroid

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why A is incorrect:* The VAE's KL regularization encourages a continuous latent space. Points between two encoded examples are not off-manifold — the continuity constraint ensures they decode to plausible images.
  - *Why B is correct:* Latent interpolation is a standard technique for verifying latent space continuity. A well-regularized VAE produces smoothly morphing decoded images along the interpolation path.
  - *Why C is incorrect:* Sampling describes drawing random points from the prior `N(0, I)`, not tracing a path between two specific encoded points.
  - *Why D is incorrect:* VAE latent spaces are not discretized into class clusters; soft continuous blending is what distinguishes them from standard autoencoders.

---

### Question 12 (5 points)

In GAN training, the generator loss using the original minimax formulation saturates early in training. The non-saturating generator loss replaces `log(1 - D(G(z)))` with `-log(D(G(z)))`. What problem does this fix?

- A) It prevents the discriminator from overfitting to the generator distribution
- B) It eliminates mode collapse by encouraging the generator to explore diverse modes
- C) It provides stronger gradients to the generator when the discriminator is confidently rejecting fakes (early training)
- D) It converts the GAN objective to a maximum likelihood problem

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why A is incorrect:* The discriminator loss is unchanged; only the generator loss is reformulated.
  - *Why B is incorrect:* Mode collapse is a separate failure mode not directly addressed by the non-saturating loss.
  - *Why C is correct:* When D(G(z)) ≈ 0 (discriminator rejects all fakes), the original loss `log(1 - D(G(z))) ≈ log(1) = 0` is flat — no gradient. The non-saturating form `-log(D(G(z))) → -log(0) → ∞` has steep gradients that effectively train the generator.
  - *Why D is incorrect:* Maximum likelihood equivalence applies to the WGAN variant, not the non-saturating GAN reformulation.

---

### Question 13 (5 points)

Positional encodings are added to token embeddings at the input of a Transformer. Which property of sinusoidal positional encodings makes them useful for sequences longer than those seen during training?

- A) They are learned jointly with the token embeddings, allowing extrapolation by gradient descent
- B) The sinusoidal functions produce unique and deterministic encodings for any position index, including unseen ones
- C) Each encoding vector has norm 1, preventing the position signal from dominating the embedding
- D) They partition the sequence into fixed-length chunks, enabling attention to scale linearly

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why A is incorrect:* Sinusoidal encodings are not learned — they are computed analytically from the position index using fixed sine and cosine functions.
  - *Why B is correct:* Because the formula uses continuous trigonometric functions of position indices, you can compute a unique encoding for position 10,000 even if training used only positions 0–512. Learned positional embeddings have no representation for unseen positions.
  - *Why C is incorrect:* Sinusoidal encoding vectors are not unit-normed; their norms depend on `d_model`.
  - *Why D is incorrect:* Positional encodings do not segment the sequence or change attention complexity.

---

### Question 14 (5 points)

In a Transformer decoder, there are two attention sub-layers per block. What is the role of the second attention sub-layer?

- A) It applies causal masking to prevent the decoder from attending to future output tokens
- B) It attends to the encoder's output, allowing the decoder to condition its generation on the source representation
- C) It computes self-attention over the decoder's own output tokens without masking
- D) It computes attention over the positional encodings to reinforce position information

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why A is incorrect:* Causal masking is applied in the first sub-layer (masked self-attention over decoder outputs), not the second.
  - *Why B is correct:* The second sub-layer is cross-attention: queries come from the decoder, while keys and values come from the encoder output. This is how the decoder reads the encoded source.
  - *Why C is incorrect:* Unmasked self-attention would allow the decoder to cheat by attending to future output positions during training.
  - *Why D is incorrect:* There is no attention layer dedicated to positional encodings; those are added directly to embeddings before the first layer.

---

### Question 15 (5 points)

Layer normalization is used in Transformers instead of batch normalization. Which reason best justifies this choice?

- A) Layer normalization is computationally cheaper because it requires fewer parameters than batch normalization
- B) Batch normalization requires large batch sizes for stable statistics, while layer normalization normalizes across features within a single example and works well with small batches and variable-length sequences
- C) Layer normalization prevents vanishing gradients more effectively than batch normalization in shallow networks
- D) Batch normalization cannot be applied after an attention layer due to the softmax output

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why A is incorrect:* Both normalization methods have similar parameter counts (gamma and beta per feature). The motivation is statistical, not computational.
  - *Why B is correct:* In NLP, sequences have variable lengths and batches often contain only a few examples. Batch normalization statistics computed across a batch are unstable under these conditions. Layer normalization operates entirely within each example, making it batch-size independent.
  - *Why C is incorrect:* The vanishing gradient claim is not a standard justification for the LayerNorm vs BatchNorm choice in Transformers.
  - *Why D is incorrect:* There is no theoretical barrier to applying batch normalization after softmax outputs; the practical issue is the batch statistics problem.

---

### Question 16 (5 points)

In a VAE, the KL divergence term `D_KL(q(z|x) || p(z))` acts as a regularizer. What happens to the generated samples if the KL weight is set to zero (i.e., training with reconstruction loss only)?

- A) The model degenerates to a standard autoencoder with an unstructured latent space, making random sampling from the prior produce poor images
- B) The model converges faster because the gradient has fewer conflicting terms
- C) The KL term being zero forces the encoder to output the prior distribution exactly
- D) The VAE becomes equivalent to a GAN because the decoder alone generates samples

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* Without the KL penalty, the encoder is free to place encoded points anywhere in latent space without regard to the prior `N(0, I)`. Decoding random samples from `N(0, I)` will miss most of the actual data encodings, producing blurry or incoherent outputs.
  - *Why B is incorrect:* Training may converge in terms of reconstruction loss, but the latent space is unstructured, making the model useless for generation.
  - *Why C is incorrect:* Setting the KL weight to zero removes the incentive to match the prior — the encoder will drift away from `N(0, I)`, not toward it.
  - *Why D is incorrect:* A VAE without KL regularization resembles a standard autoencoder, not a GAN. A GAN has an entirely different training objective.

---

### Question 17 (5 points)

An attention mechanism is described as having `O(n^2)` complexity where `n` is the sequence length. Which specific operation causes this quadratic scaling?

- A) The softmax normalization over the attention weights
- B) The projection of queries, keys, and values through dense layers
- C) Computing pairwise dot products between every query and every key, producing an n × n score matrix
- D) The final multiplication of attention weights with value vectors

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why A is incorrect:* Softmax is applied row-wise on an already-computed n × n matrix; it is `O(n^2)` but the score matrix computation is the root cause.
  - *Why B is incorrect:* Linear projections are `O(n · d_model)` — linear in sequence length, not quadratic.
  - *Why C is correct:* `Q @ K^T` produces an n × n matrix where each of the n queries is dotted with all n keys. This is fundamentally quadratic in the sequence length.
  - *Why D is incorrect:* `weights @ V` is also `O(n^2 · d)` but follows from the already-computed quadratic score matrix.

---

### Question 18 (5 points)

You are fine-tuning BERT for a named entity recognition (NER) task, where each token must be assigned a label (e.g., PERSON, ORG, O). How does this differ from the standard BERT classification setup?

- A) You use the `[CLS]` token output and replicate it to all token positions
- B) You attach a classification head to every token's final hidden state instead of only the `[CLS]` token output
- C) You replace the BERT encoder with a bidirectional LSTM for token-level prediction
- D) You remove the `[CLS]` token and use mean pooling over all token outputs

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why A is incorrect:* Replicating the `[CLS]` vector provides no position-specific information; each token's prediction needs its own contextual representation.
  - *Why B is correct:* NER is a token classification task. BERT's final hidden states for each token position are passed to a per-token classifier head (a dense layer applied independently at each position).
  - *Why C is incorrect:* Replacing BERT's encoder with an LSTM would discard the pretrained representations — the opposite of transfer learning.
  - *Why D is incorrect:* Mean pooling collapses sequence-level information and is used for sentence embedding, not token classification.

---

### Question 19 (5 points)

A DCGAN generator uses `Conv2DTranspose` layers. What does `Conv2DTranspose` do that regular `Conv2D` cannot?

- A) It applies learned upsampling, increasing the spatial dimensions of the feature map
- B) It transposes the kernel matrix to make the convolution reversible
- C) It clips pixel values to the range [0, 1] during the forward pass
- D) It computes the inverse of the discriminator's convolutional features

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* `Conv2DTranspose` (also called fractionally strided convolution or deconvolution) inserts learnable fractional strides between input elements, expanding spatial resolution. It is used in generators to go from a small latent feature map to a full-resolution image.
  - *Why B is incorrect:* The "transpose" in the name refers to the transpose of the convolution operation (which is a property of gradient computation), not matrix transposition of the kernel.
  - *Why C is incorrect:* No clipping occurs; the output activation (e.g., `tanh`) handles value range.
  - *Why D is incorrect:* `Conv2DTranspose` has no relationship to the discriminator's computations at inference time.

---

### Question 20 (5 points)

You train a standard autoencoder on Fashion MNIST with a 2D bottleneck. At test time you sample a point `z = [5.0, 5.0]` — far outside the region where training data was encoded — and decode it. What is the most likely result?

- A) The decoder produces an image that clearly belongs to one of the 10 Fashion MNIST classes
- B) The decoder produces a blurry or nonsensical image because the latent region was never visited during training
- C) The decoder raises a dimension mismatch error because the input is outside the valid range
- D) The decoder produces a clean reconstruction because the sigmoid output activation constrains pixel values to [0, 1]

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why A is incorrect:* The standard autoencoder has no constraint that fills the latent space uniformly. Regions far from encoded training data were never associated with any meaningful output.
  - *Why B is correct:* Without the KL regularization of a VAE, the decoder's weights are only optimized for the compact region of latent space actually visited during training. Decoding a distant point extrapolates in an unpredictable way, typically producing noise or blurred artifacts.
  - *Why C is incorrect:* The latent vector `[5.0, 5.0]` is dimensionally valid (shape matches the decoder's `input_shape=(2,)`); no error occurs.
  - *Why D is incorrect:* The sigmoid output ensures values are in [0, 1] but does not ensure the decoded image is meaningful — it may be uniformly gray or noisy.

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
| 11 | B |
| 12 | C |
| 13 | B |
| 14 | B |
| 15 | B |
| 16 | A |
| 17 | C |
| 18 | B |
| 19 | A |
| 20 | B |
