# Reading Guide: Module 15 — Advanced Topics: Generative Models and Transformers

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Overview

Module 15 surveys five of the most influential deep learning architectures developed since 2013: autoencoders, variational autoencoders (VAEs), generative adversarial networks (GANs), the Transformer, and BERT. The goal is conceptual fluency and hands-on exposure, not exhaustive mathematical derivation. Each section includes the core idea, the key architectural choices, a Keras implementation sketch, and practical guidance on when to use the technique.

**Estimated study time:** 3–3.5 hours

---

## Learning Objectives

After completing this guide you will be able to:

1. Describe the encoder-bottleneck-decoder structure of an autoencoder
2. Explain the reparameterization trick in a VAE and why it is necessary
3. Describe the minimax game in GAN training and common stabilization strategies
4. Explain scaled dot-product attention mathematically and in code
5. Identify the components of a Transformer encoder block
6. Describe how BERT is pretrained and how fine-tuning works

---

## Section 1 — Autoencoders

### 1.1 Architecture and Objective

An autoencoder is trained to minimize reconstruction error:

```text
Loss = ||x - decoder(encoder(x))||^2
```

The encoder compresses the input `x` into a latent code `z` of dimension `d_z << d_x`. Because the bottleneck forces information loss, the encoder must learn to preserve the most informative structure. This is representation learning without labels.

### 1.2 Keras Implementation Pattern

The functional API allows building encoder and decoder as separate models, then composing them:

```python
import tensorflow as tf

LATENT_DIM = 32

encoder_input = tf.keras.Input(shape=(784,))
x = tf.keras.layers.Dense(256, activation='relu')(encoder_input)
latent = tf.keras.layers.Dense(LATENT_DIM)(x)
encoder = tf.keras.Model(encoder_input, latent)

decoder_input = tf.keras.Input(shape=(LATENT_DIM,))
x = tf.keras.layers.Dense(256, activation='relu')(decoder_input)
reconstructed = tf.keras.layers.Dense(784, activation='sigmoid')(x)
decoder = tf.keras.Model(decoder_input, reconstructed)

ae_in = tf.keras.Input(shape=(784,))
autoencoder = tf.keras.Model(ae_in, decoder(encoder(ae_in)))
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
```

Keeping encoder and decoder as separate models is important: you can use `encoder.predict(X)` to extract latent codes for downstream tasks.

### 1.3 Applications

- **Anomaly detection**: Train on normal data; inputs with high reconstruction error are anomalies
- **Denoising autoencoders**: Pass noisy inputs, target clean outputs; the model learns to denoise
- **Feature extraction**: Use encoder output as a feature vector for downstream classifiers

### 1.4 Limitations

The standard autoencoder's latent space has no guaranteed structure. Two nearby points in latent space may not decode to similar-looking outputs, making it unsuitable for controlled generation.

---

## Section 2 — Variational Autoencoders

### 2.1 The Core Idea

A VAE imposes structure on the latent space by constraining the encoder to output a distribution rather than a point. The encoder outputs `mu` and `log_var` parameterizing `q(z|x) = N(mu, exp(log_var))`. The decoder learns `p(x|z)` — how to reconstruct x from a sample z.

### 2.2 The Reparameterization Trick

Sampling from `N(mu, sigma^2)` is not differentiable with respect to `mu` or `sigma`. The trick rewrites the sample as:

```python
z = mu + tf.exp(0.5 * log_var) * tf.random.normal(shape=tf.shape(mu))
```

Now `mu` and `log_var` are deterministic parameters in the computation graph; only `epsilon` is random. Gradients flow through `mu` and `log_var` normally.

### 2.3 The ELBO Loss

The VAE training objective is the Evidence Lower BOund (ELBO), which decomposes into two terms:

- **Reconstruction loss**: `||x - x_hat||^2` or binary cross-entropy — measures how well the decoder reconstructs x
- **KL divergence**: `D_KL(q(z|x) || p(z))` — regularizes the latent distribution toward the prior `N(0, I)`

```python
def vae_loss(x, x_hat, mu, log_var):
    recon = tf.reduce_mean(
        tf.keras.losses.binary_crossentropy(x, x_hat)
    )
    kl = -0.5 * tf.reduce_mean(
        1 + log_var - tf.square(mu) - tf.exp(log_var)
    )
    return recon + kl
```

The beta-VAE variant multiplies the KL term by a factor `beta > 1` to encourage more disentangled latent representations.

### 2.4 Sampling and Interpolation

A well-trained VAE supports two generation modes:

- **Random sampling**: draw `z ~ N(0, I)`, decode to get a new sample
- **Latent interpolation**: linearly interpolate between `z_1` and `z_2` (encoded from two real images), decode each point to observe smooth transitions

---

## Section 3 — Generative Adversarial Networks

### 3.1 The Adversarial Game

A GAN consists of two networks:

- **Generator G(z)**: maps random noise `z ~ N(0, I)` to the data space
- **Discriminator D(x)**: outputs the probability that input x is real

The minimax objective is:

```text
min_G max_D E[log D(x_real)] + E[log(1 - D(G(z)))]
```

The discriminator maximizes correct classification; the generator minimizes the discriminator's ability to identify its outputs as fake.

### 3.2 Architecture Choices (DCGAN)

Deep Convolutional GANs use transposed convolutions in the generator and strided convolutions in the discriminator, avoiding pooling layers:

| Component | Key choices |
|-----------|-------------|
| Generator | Dense → Reshape → Conv2DTranspose stacks; BatchNorm; ReLU (tanh output) |
| Discriminator | Conv2D with stride 2; LeakyReLU; no BatchNorm in first layer |

### 3.3 Stabilization Strategies

GAN training is known for mode collapse (generator produces only a few modes) and oscillation. Key strategies:

- **Label smoothing**: use 0.9 instead of 1.0 for real labels
- **Leaky ReLU** in discriminator to avoid dying gradients
- **Separate optimizers** with different learning rates (generator often uses 2e-4, discriminator 1e-4)
- **Gradient clipping** to prevent discriminator from dominating early
- **Wasserstein loss** (WGAN) for better gradient signal — requires weight clipping or gradient penalty

### 3.4 Evaluation Challenges

Unlike supervised models, GANs have no obvious scalar loss to monitor. Metrics include:

- **Visual inspection**: qualitative — are samples diverse and realistic?
- **FID (Fréchet Inception Distance)**: compares statistics of real vs generated feature distributions
- **Inception Score**: measures quality and diversity jointly

For coursework, visual inspection of a grid of generated samples at regular training intervals is standard.

---

## Section 4 — The Attention Mechanism

### 4.1 Scaled Dot-Product Attention

Given query matrix Q, key matrix K, and value matrix V:

```python
import tensorflow as tf
import numpy as np

def scaled_dot_product_attention(Q, K, V, mask=None):
    d_k = tf.cast(tf.shape(K)[-1], tf.float32)
    scores = tf.matmul(Q, K, transpose_b=True) / tf.math.sqrt(d_k)
    if mask is not None:
        scores += mask * -1e9
    weights = tf.nn.softmax(scores, axis=-1)
    return tf.matmul(weights, V), weights
```

The `mask` parameter is used in decoder self-attention to prevent a position from attending to future positions (causal masking).

### 4.2 Multi-Head Attention

Multi-head attention runs scaled dot-product attention `h` times in parallel:

```python
class MultiHeadAttention(tf.keras.layers.Layer):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.W_q = tf.keras.layers.Dense(d_model)
        self.W_k = tf.keras.layers.Dense(d_model)
        self.W_v = tf.keras.layers.Dense(d_model)
        self.W_o = tf.keras.layers.Dense(d_model)

    def split_heads(self, x, batch_size):
        x = tf.reshape(x, (batch_size, -1, self.num_heads, self.d_k))
        return tf.transpose(x, perm=[0, 2, 1, 3])

    def call(self, q, k, v):
        b = tf.shape(q)[0]
        Q = self.split_heads(self.W_q(q), b)
        K = self.split_heads(self.W_k(k), b)
        V = self.split_heads(self.W_v(v), b)
        attn, _ = scaled_dot_product_attention(Q, K, V)
        attn = tf.transpose(attn, perm=[0, 2, 1, 3])
        attn = tf.reshape(attn, (b, -1, self.num_heads * self.d_k))
        return self.W_o(attn)
```

### 4.3 Why Attention Works

Attention allows every token to directly access representations of all other tokens, regardless of their distance in the sequence. RNNs must propagate information through sequential hidden states, which degrades over long distances. Attention has `O(n^2)` complexity in sequence length (all pairs), while RNNs have `O(n)` — but the `O(n^2)` attention is highly parallelizable on GPUs.

---

## Section 5 — The Transformer Encoder

### 5.1 Positional Encoding

Because self-attention treats the input as a set (not a sequence), position information must be injected explicitly. The original Transformer uses sinusoidal encodings:

```python
def positional_encoding(max_len, d_model):
    positions = np.arange(max_len)[:, np.newaxis]
    dims = np.arange(d_model)[np.newaxis, :]
    angles = positions / np.power(10000, (2 * (dims // 2)) / d_model)
    angles[:, 0::2] = np.sin(angles[:, 0::2])
    angles[:, 1::2] = np.cos(angles[:, 1::2])
    return tf.cast(angles[np.newaxis, :, :], tf.float32)
```

Modern models (BERT, GPT) use learned positional embeddings instead.

### 5.2 Transformer Encoder Block

Each block has two sub-layers, each wrapped in residual + layer normalization:

```python
class TransformerEncoderBlock(tf.keras.layers.Layer):
    def __init__(self, d_model, num_heads, dff, dropout=0.1):
        super().__init__()
        self.mha = tf.keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=d_model // num_heads
        )
        self.ffn = tf.keras.Sequential([
            tf.keras.layers.Dense(dff, activation='relu'),
            tf.keras.layers.Dense(d_model)
        ])
        self.norm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.norm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.drop1 = tf.keras.layers.Dropout(dropout)
        self.drop2 = tf.keras.layers.Dropout(dropout)

    def call(self, x, training=False):
        attn = self.mha(x, x, training=training)
        x = self.norm1(x + self.drop1(attn, training=training))
        ffn = self.ffn(x)
        return self.norm2(x + self.drop2(ffn, training=training))
```

### 5.3 Full Transformer Encoder

Multiple encoder blocks are stacked. The original BERT-base uses 12 blocks, `d_model=768`, 12 attention heads, and `dff=3072`.

---

## Section 6 — BERT and Transfer Learning

### 6.1 Pretraining Tasks

BERT is trained on:

- **Masked Language Modeling (MLM)**: 15% of input tokens are randomly masked; the model predicts masked tokens from bidirectional context
- **Next Sentence Prediction (NSP)**: the model predicts whether sentence B naturally follows sentence A

Both tasks use unlabeled text, enabling training on enormous corpora (Wikipedia + BookCorpus, ~16 GB).

### 6.2 Fine-Tuning

For a classification task, add a classification head on top of the `[CLS]` token output:

```python
import tensorflow_hub as hub

preprocess = hub.KerasLayer(
    "https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3"
)
bert = hub.KerasLayer(
    "https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4",
    trainable=True
)

text_in = tf.keras.Input(shape=(), dtype=tf.string)
enc = preprocess(text_in)
out = bert(enc)
pooled = out['pooled_output']
logits = tf.keras.layers.Dense(2, activation='softmax')(pooled)
model = tf.keras.Model(text_in, logits)
model.compile(optimizer=tf.keras.optimizers.Adam(2e-5),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

Fine-tuning for 2–4 epochs at `lr=2e-5` is typical. The small learning rate prevents destroying the pretrained representations.

### 6.3 When to Use BERT vs. Simpler Models

| Scenario | Recommendation |
|----------|----------------|
| Short text, < 10K labeled examples | BERT fine-tuning |
| Long documents (> 512 tokens) | Longformer or chunking strategy |
| Real-time inference latency < 5 ms | DistilBERT or BERT quantization |
| Low resource or research prototype | Word2Vec + LSTM |

---

## Key Terms

- **Autoencoder:** Network trained to reconstruct its input via a compressed bottleneck latent space
- **Latent code:** Compressed representation at the autoencoder bottleneck
- **VAE:** Variational autoencoder; encoder outputs a distribution; reparameterization enables gradients
- **ELBO:** Evidence Lower BOund; VAE training objective = reconstruction loss + KL divergence
- **GAN:** Generative adversarial network; generator vs discriminator minimax game
- **Mode collapse:** GAN failure mode where generator produces only a few output types
- **Attention:** Mechanism that computes weighted sums of values based on query-key similarity
- **Transformer:** Architecture using multi-head self-attention; forms the basis of modern LLMs
- **Positional encoding:** Injecting position information into token embeddings for Transformers
- **BERT:** Bidirectional Encoder Representations from Transformers; pretrained via MLM and NSP

---

## Self-Check Questions

1. What problem does the reparameterization trick solve in VAE training?
2. What is mode collapse in GAN training and what techniques mitigate it?
3. Why does multi-head attention run the attention mechanism multiple times in parallel?
4. What is the purpose of the `[CLS]` token in BERT?
5. Why is layer normalization used in Transformer blocks rather than batch normalization?
6. What makes the KL divergence term necessary in VAE training?

---

## Recommended Resources

- VAE paper: Kingma and Welling, "Auto-Encoding Variational Bayes" (2013) — arXiv:1312.6114
- GAN paper: Goodfellow et al., "Generative Adversarial Networks" (2014) — arXiv:1406.2661
- Transformer paper: Vaswani et al., "Attention Is All You Need" (2017) — arXiv:1706.03762
- BERT paper: Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers" (2018) — arXiv:1810.04805
- Hands-On ML, Chapter 17 — Autoencoders, GANs, and Diffusion Models
- TensorFlow Hub BERT tutorials: [tfhub.dev](https://tfhub.dev)

---

## Next Module Preview

Module 16 is our exam preparation and capstone module. We review all four TensorFlow Developer Certificate exam categories, work through practice problems under timed conditions, and discuss career paths in machine learning. Bring your questions about any topic from Modules 1–15.

---

## 9. Supplemental Resources

**1. [The Illustrated Transformer — Jay Alammar](https://jalammar.github.io/illustrated-transformer/)**
A widely referenced visual walkthrough of the Transformer architecture — covering token embeddings, positional encodings, scaled dot-product attention, multi-head attention, encoder/decoder stacks, and the residual + layer normalization structure. Uses step-by-step diagrams that complement the mathematical treatment in the reading guide and directly support the lab's attention implementation.

**2. [TensorFlow VAE Tutorial — Convolutional VAE](https://www.tensorflow.org/tutorials/generative/cvae)**
Official TensorFlow tutorial building a convolutional VAE on MNIST from scratch, including the ELBO loss derivation, custom training loop with `tf.GradientTape`, latent space visualization, and image generation via decoder sampling. Directly extends the dense VAE built in the lab to convolutional architectures and demonstrates the latent grid visualization technique.

**3. [Hugging Face — Fine-Tuning BERT for Text Classification](https://huggingface.co/docs/transformers/training)**
Practical guide to loading pretrained BERT variants via the Transformers library, tokenizing inputs with `AutoTokenizer`, fine-tuning with the `Trainer` API, and evaluating with standard metrics. Demonstrates the same transfer learning workflow covered in Section 6 of this reading guide using the production-grade Hugging Face ecosystem.
