# Video Script: Module 15 — Advanced Topics: Generative Models and Transformers

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Production Notes

- **Runtime target:** 22–24 minutes
- **Format:** Screencast with Colab walkthroughs; whiteboard diagrams for attention mechanism and Transformer architecture
- **Visual aids:** Autoencoder bottleneck diagram; GAN adversarial loop diagram; self-attention heatmap
- **Code environment:** Google Colab, TensorFlow 2.x / Keras

---

## SEGMENT 1 — Introduction and Roadmap (0:00–2:00)

Welcome to Module 15 — our deepest dive yet into the frontier of deep learning. In the previous modules we covered the core supervised learning pipeline: training classifiers, sequence models, and deploying them to production. Today we explore models that go beyond classification and regression. We are going to look at models that generate new data, models that compress information into a structured latent space, and the Transformer architecture that sits underneath virtually every state-of-the-art NLP system you interact with today.

By the end of this module you will understand:

- Autoencoders — architecture, bottleneck, and applications
- Variational autoencoders — latent space interpolation and generative sampling
- Generative adversarial networks — the adversarial training loop
- The attention mechanism — the mathematical core of modern NLP
- The Transformer encoder — multi-head self-attention and positional encoding
- BERT — what it is, how it was trained, and when to use it

This is a survey module. We are building conceptual fluency and implementing lightweight versions of each architecture. Research depth on any of these topics could fill an entire graduate course. Our goal is to understand enough to use these tools intelligently in your own work.

---

## SEGMENT 2 — Autoencoders (2:00–6:00)

[SLIDE: Autoencoder architecture — encoder, bottleneck, decoder]

An **autoencoder** is a neural network trained to reconstruct its own input. It consists of two halves: an **encoder** that maps the input to a low-dimensional **latent code** (the bottleneck), and a **decoder** that maps the latent code back to the original input space.

Why would you train a network to reproduce its input? The constraint at the bottleneck forces the encoder to learn a compressed representation that captures the most essential structure. This is unsupervised — no labels needed.

Here is a minimal autoencoder for MNIST:

```python
import tensorflow as tf

LATENT_DIM = 32

# Encoder
encoder_input = tf.keras.Input(shape=(28, 28, 1))
x = tf.keras.layers.Flatten()(encoder_input)
x = tf.keras.layers.Dense(256, activation='relu')(x)
latent = tf.keras.layers.Dense(LATENT_DIM, activation='relu')(x)
encoder = tf.keras.Model(encoder_input, latent, name='encoder')

# Decoder
decoder_input = tf.keras.Input(shape=(LATENT_DIM,))
x = tf.keras.layers.Dense(256, activation='relu')(decoder_input)
x = tf.keras.layers.Dense(28 * 28, activation='sigmoid')(x)
output = tf.keras.layers.Reshape((28, 28, 1))(x)
decoder = tf.keras.Model(decoder_input, output, name='decoder')

# Autoencoder
ae_input = tf.keras.Input(shape=(28, 28, 1))
encoded = encoder(ae_input)
decoded = decoder(encoded)
autoencoder = tf.keras.Model(ae_input, decoded, name='autoencoder')

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
```

[PAUSE — show the model summary]

We use binary cross-entropy as the loss because pixel values are normalized to [0, 1] and we can treat reconstruction as a per-pixel prediction problem.

Applications of autoencoders include:

- **Anomaly detection**: train on normal data; high reconstruction error signals anomaly
- **Denoising**: train with noisy inputs and clean targets
- **Dimensionality reduction**: use the encoder as a feature extractor

---

## SEGMENT 3 — Variational Autoencoders (6:00–10:30)

[SLIDE: VAE architecture — encoder outputs mu and log_var; reparameterization trick; decoder]

The standard autoencoder has a problem: the latent space is unstructured. You cannot easily sample from it to generate new data. A **variational autoencoder** (VAE) fixes this by forcing the encoder to output a probability distribution rather than a single point.

Instead of outputting a latent vector directly, the encoder outputs two vectors: `mu` (mean) and `log_var` (log variance). A latent sample is then drawn from the distribution `N(mu, exp(log_var))`. The reparameterization trick makes this differentiable:

```python
z = mu + tf.exp(0.5 * log_var) * epsilon
```

where `epsilon ~ N(0, I)`. This enables gradients to flow through the sampling operation.

Here is the VAE sampling layer:

```python
class Sampling(tf.keras.layers.Layer):
    def call(self, inputs):
        mu, log_var = inputs
        epsilon = tf.random.normal(shape=tf.shape(mu))
        return mu + tf.exp(0.5 * log_var) * epsilon

# VAE Encoder
enc_input = tf.keras.Input(shape=(28, 28, 1))
x = tf.keras.layers.Flatten()(enc_input)
x = tf.keras.layers.Dense(256, activation='relu')(x)
mu = tf.keras.layers.Dense(LATENT_DIM)(x)
log_var = tf.keras.layers.Dense(LATENT_DIM)(x)
z = Sampling()([mu, log_var])
vae_encoder = tf.keras.Model(enc_input, [mu, log_var, z], name='vae_encoder')
```

The VAE loss adds a **KL divergence** term that penalizes the encoder if its distribution deviates from `N(0, I)`:

```
Total loss = Reconstruction loss + beta * KL divergence
KL divergence = -0.5 * sum(1 + log_var - mu^2 - exp(log_var))
```

The KL term regularizes the latent space. With a well-trained VAE, you can sample any point in the latent space and decode it to get a plausible new image. You can also interpolate between two latent codes to smoothly morph one image into another.

[VISUAL: Grid of VAE-generated MNIST digits sampled from a 2D latent space]

---

## SEGMENT 4 — Generative Adversarial Networks (10:30–14:30)

[SLIDE: GAN game — Generator and Discriminator adversarial loop]

A **generative adversarial network** (GAN) takes a completely different approach to generation. Two networks compete in a minimax game:

- The **Generator** takes random noise `z` and outputs a fake image
- The **Discriminator** takes an image (real or fake) and outputs the probability that it is real

The Generator tries to fool the Discriminator; the Discriminator tries to tell real from fake. At equilibrium, the Generator produces images indistinguishable from real data.

Here is a minimal DCGAN (Deep Convolutional GAN) for MNIST:

```python
# Generator
def build_generator(latent_dim=100):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(7 * 7 * 128, activation='relu',
                              input_shape=(latent_dim,)),
        tf.keras.layers.Reshape((7, 7, 128)),
        tf.keras.layers.Conv2DTranspose(64, (4, 4), strides=2,
                                        padding='same', activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2DTranspose(1, (4, 4), strides=2,
                                        padding='same', activation='tanh')
    ])
    return model

# Discriminator
def build_discriminator():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(64, (4, 4), strides=2,
                               padding='same', input_shape=(28, 28, 1)),
        tf.keras.layers.LeakyReLU(0.2),
        tf.keras.layers.Conv2D(128, (4, 4), strides=2, padding='same'),
        tf.keras.layers.LeakyReLU(0.2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model
```

GAN training is notoriously unstable. Key techniques to stabilize training:

- **Label smoothing**: use 0.9 for real labels instead of 1.0
- **Leaky ReLU** in the discriminator
- **BatchNormalization** in the generator
- Train the discriminator and generator in alternating steps with separate optimizers

GANs require patience and experimentation. For a course project, aim to see recognizable digits after 10–20 epochs of training on MNIST.

---

## SEGMENT 5 — The Attention Mechanism (14:30–17:30)

[SLIDE: Query, Key, Value diagram]

The attention mechanism is the mathematical engine of modern NLP. At its core, attention asks: for each position in a sequence, which other positions are most relevant?

Attention computes three projections from the input: **Queries (Q)**, **Keys (K)**, and **Values (V)**. The attention score between position i and position j is:

```
Attention(Q, K, V) = softmax(Q @ K^T / sqrt(d_k)) @ V
```

where `d_k` is the key dimension. The `sqrt(d_k)` factor prevents extremely small gradients when `d_k` is large.

Intuitively: Q is "what am I looking for," K is "what do I have," and V is "what I will return if matched." The dot product `Q @ K^T` computes how well each query matches each key; softmax normalizes these into attention weights; the output is a weighted sum of values.

In code:

```python
import tensorflow as tf

def scaled_dot_product_attention(q, k, v):
    d_k = tf.cast(tf.shape(k)[-1], tf.float32)
    scores = tf.matmul(q, k, transpose_b=True) / tf.math.sqrt(d_k)
    weights = tf.nn.softmax(scores, axis=-1)
    return tf.matmul(weights, v), weights
```

**Multi-head attention** runs this computation H times in parallel with different weight matrices, then concatenates and projects the results. This allows the model to attend to different aspects of the sequence simultaneously.

---

## SEGMENT 6 — The Transformer Architecture (17:30–20:30)

[SLIDE: Transformer encoder block — Multi-head attention + FFN + LayerNorm + residuals]

The Transformer encoder processes a sequence of token embeddings in parallel. Each encoder block has two sub-layers:

1. **Multi-head self-attention** — each token attends to all other tokens
2. **Position-wise feed-forward network** — two dense layers applied to each position independently

Each sub-layer is wrapped in a residual connection and layer normalization:

```
output = LayerNorm(x + SubLayer(x))
```

Here is a minimal Transformer encoder block in Keras:

```python
class TransformerBlock(tf.keras.layers.Layer):
    def __init__(self, d_model, num_heads, dff, dropout=0.1):
        super().__init__()
        self.attention = tf.keras.layers.MultiHeadAttention(
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
        attn_out = self.attention(x, x, training=training)
        x = self.norm1(x + self.drop1(attn_out, training=training))
        ffn_out = self.ffn(x)
        return self.norm2(x + self.drop2(ffn_out, training=training))
```

Because self-attention is order-agnostic (it treats the sequence as a set), Transformers add **positional encodings** to the input embeddings. The original paper used sinusoidal functions; modern models use learned positional embeddings.

---

## SEGMENT 7 — BERT and Transfer Learning (20:30–22:30)

[SLIDE: BERT pretraining tasks — MLM and NSP]

BERT (Bidirectional Encoder Representations from Transformers) is a large Transformer encoder pretrained on two tasks:

- **Masked Language Modeling (MLM)**: 15% of tokens are masked; the model predicts the masked tokens from context
- **Next Sentence Prediction (NSP)**: the model predicts whether sentence B follows sentence A

Pretraining on hundreds of billions of words gives BERT a deep understanding of language. You then **fine-tune** the pretrained model on a small labeled dataset for your specific task — sentiment analysis, question answering, named entity recognition, and so on.

Using BERT via TensorFlow Hub:

```python
import tensorflow_hub as hub
import tensorflow_text as text

preprocess = hub.KerasLayer(
    "https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3"
)
bert_encoder = hub.KerasLayer(
    "https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4",
    trainable=True
)

text_input = tf.keras.Input(shape=(), dtype=tf.string)
preprocessed = preprocess(text_input)
outputs = bert_encoder(preprocessed)
pooled = outputs['pooled_output']
classifier = tf.keras.layers.Dense(2, activation='softmax')(pooled)
model = tf.keras.Model(text_input, classifier)
```

Fine-tuning BERT requires a GPU and typically runs for 2–5 epochs on a small dataset. The pooled output (the [CLS] token representation) is used as the sentence embedding for classification tasks.

---

## SEGMENT 8 — Wrap-Up (22:30–24:00)

In this module we covered five powerful architectures. Autoencoders learn compact representations without labels. Variational autoencoders add probabilistic structure to enable controlled generation. GANs use adversarial training to generate photorealistic data. The attention mechanism enables models to route information based on relevance rather than position. Transformers build on attention to process sequences in parallel with state-of-the-art effectiveness. BERT pretrains this architecture at massive scale, enabling transfer learning with small labeled datasets.

In Module 16 — our final module — we review all four exam categories for the TensorFlow Developer Certificate, work through practice problems, and discuss career paths in ML. Prepare your questions. See you there.

---

## End of Script

**Total estimated runtime:** 24 minutes

**Key code files referenced:** `module15_generative_transformers.ipynb`

**TF Developer Certificate alignment:** Background knowledge supporting all four certificate categories
