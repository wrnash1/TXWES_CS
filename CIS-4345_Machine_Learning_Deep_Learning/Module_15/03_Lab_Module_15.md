# Lab Activity: Module 15 — Generative Models and Transformers

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Lab Overview

**Title:** Autoencoders, VAEs, and a Minimal Transformer

**Duration:** 90–120 minutes

**Platform:** Google Colab (GPU runtime recommended for Part 3)

**Deliverable:** Completed Colab notebook (`.ipynb`) submitted to Canvas

**Points:** 100

---

## Learning Objectives

By the end of this lab you will have:

- Built and trained a dense autoencoder on Fashion MNIST
- Visualized latent space structure using 2D PCA projections
- Built a VAE with the reparameterization trick and compared generated samples to autoencoder reconstructions
- Implemented scaled dot-product attention from scratch
- Built a minimal Transformer text classifier on a toy sentiment dataset

---

## Prerequisites

Review the Module 15 video and reading guide. You need a working understanding of the Keras functional API and custom `Layer` subclassing before beginning Part 4.

---

## Part 1 — Dense Autoencoder on Fashion MNIST (25 minutes)

### Step 1.1 — Setup

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

tf.random.set_seed(42)
np.random.seed(42)
print("TF:", tf.__version__)
```

### Step 1.2 — Load and Normalize Data

```python
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train_flat = x_train.reshape(-1, 784)
x_test_flat = x_test.reshape(-1, 784)

CLASS_NAMES = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
```

### Step 1.3 — Build the Autoencoder

```python
LATENT_DIM = 2  # 2D for visualization

# Encoder
enc_in = tf.keras.Input(shape=(784,))
x = tf.keras.layers.Dense(256, activation='relu')(enc_in)
x = tf.keras.layers.Dense(64, activation='relu')(x)
latent = tf.keras.layers.Dense(LATENT_DIM)(x)
encoder = tf.keras.Model(enc_in, latent, name='encoder')

# Decoder
dec_in = tf.keras.Input(shape=(LATENT_DIM,))
x = tf.keras.layers.Dense(64, activation='relu')(dec_in)
x = tf.keras.layers.Dense(256, activation='relu')(x)
recon = tf.keras.layers.Dense(784, activation='sigmoid')(x)
decoder = tf.keras.Model(dec_in, recon, name='decoder')

# Full autoencoder
ae_in = tf.keras.Input(shape=(784,))
autoencoder = tf.keras.Model(ae_in, decoder(encoder(ae_in)), name='autoencoder')
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
autoencoder.summary()
```

### Step 1.4 — Train

```python
history_ae = autoencoder.fit(
    x_train_flat, x_train_flat,
    epochs=30, batch_size=256,
    validation_split=0.1,
    callbacks=[tf.keras.callbacks.EarlyStopping(patience=4)],
    verbose=1
)
```

### Step 1.5 — Visualize Reconstructions

```python
def plot_reconstructions(model, x, n=10):
    recons = model.predict(x[:n], verbose=0)
    fig, axes = plt.subplots(2, n, figsize=(15, 3))
    for i in range(n):
        axes[0, i].imshow(x[i].reshape(28, 28), cmap='gray')
        axes[0, i].axis('off')
        axes[1, i].imshow(recons[i].reshape(28, 28), cmap='gray')
        axes[1, i].axis('off')
    axes[0, 0].set_ylabel("Original", fontsize=8)
    axes[1, 0].set_ylabel("Reconstructed", fontsize=8)
    plt.tight_layout()
    plt.show()

plot_reconstructions(autoencoder, x_test_flat)
```

### Step 1.6 — Visualize the 2D Latent Space

```python
z_test = encoder.predict(x_test_flat, verbose=0)
plt.figure(figsize=(8, 6))
scatter = plt.scatter(z_test[:, 0], z_test[:, 1],
                      c=y_test, cmap='tab10', alpha=0.4, s=5)
plt.colorbar(scatter, ticks=range(10), label='Class')
plt.title("2D Autoencoder Latent Space — Fashion MNIST")
plt.xlabel("z[0]")
plt.ylabel("z[1]")
plt.show()
```

**Question 1.1 (Markdown cell):** Do different clothing classes form distinct clusters? What does this tell you about what the autoencoder learned?

---

## Part 2 — Variational Autoencoder (30 minutes)

### Step 2.1 — Sampling Layer

```python
class Sampling(tf.keras.layers.Layer):
    """Reparameterization: z = mu + exp(0.5 * log_var) * epsilon"""
    def call(self, inputs):
        mu, log_var = inputs
        epsilon = tf.random.normal(shape=tf.shape(mu))
        return mu + tf.exp(0.5 * log_var) * epsilon
```

### Step 2.2 — VAE Encoder

```python
VAE_LATENT = 2

vae_enc_in = tf.keras.Input(shape=(784,))
x = tf.keras.layers.Dense(256, activation='relu')(vae_enc_in)
x = tf.keras.layers.Dense(64, activation='relu')(x)
mu = tf.keras.layers.Dense(VAE_LATENT, name='mu')(x)
log_var = tf.keras.layers.Dense(VAE_LATENT, name='log_var')(x)
z = Sampling()([mu, log_var])
vae_encoder = tf.keras.Model(vae_enc_in, [mu, log_var, z], name='vae_encoder')

# Reuse same decoder architecture
vae_dec_in = tf.keras.Input(shape=(VAE_LATENT,))
x = tf.keras.layers.Dense(64, activation='relu')(vae_dec_in)
x = tf.keras.layers.Dense(256, activation='relu')(x)
vae_recon = tf.keras.layers.Dense(784, activation='sigmoid')(x)
vae_decoder = tf.keras.Model(vae_dec_in, vae_recon, name='vae_decoder')
```

### Step 2.3 — Custom VAE Model with ELBO Loss

```python
class VAE(tf.keras.Model):
    def __init__(self, encoder, decoder, **kwargs):
        super().__init__(**kwargs)
        self.encoder = encoder
        self.decoder = decoder
        self.total_loss_tracker = tf.keras.metrics.Mean(name='total_loss')
        self.recon_loss_tracker = tf.keras.metrics.Mean(name='recon_loss')
        self.kl_loss_tracker = tf.keras.metrics.Mean(name='kl_loss')

    @property
    def metrics(self):
        return [self.total_loss_tracker, self.recon_loss_tracker,
                self.kl_loss_tracker]

    def train_step(self, data):
        with tf.GradientTape() as tape:
            mu, log_var, z = self.encoder(data)
            reconstruction = self.decoder(z)
            recon_loss = tf.reduce_mean(
                tf.keras.losses.binary_crossentropy(data, reconstruction)
            ) * 784
            kl_loss = -0.5 * tf.reduce_mean(
                1 + log_var - tf.square(mu) - tf.exp(log_var)
            )
            total_loss = recon_loss + kl_loss
        grads = tape.gradient(total_loss, self.trainable_weights)
        self.optimizer.apply_gradients(zip(grads, self.trainable_weights))
        self.total_loss_tracker.update_state(total_loss)
        self.recon_loss_tracker.update_state(recon_loss)
        self.kl_loss_tracker.update_state(kl_loss)
        return {m.name: m.result() for m in self.metrics}

vae = VAE(vae_encoder, vae_decoder)
vae.compile(optimizer=tf.keras.optimizers.Adam(1e-3))
vae.fit(x_train_flat, epochs=30, batch_size=256, verbose=1)
```

### Step 2.4 — Sample from the Latent Space

```python
def plot_latent_grid(decoder, n=15, latent_range=3):
    """Decode a grid of points in 2D latent space."""
    grid_x = np.linspace(-latent_range, latent_range, n)
    grid_y = np.linspace(-latent_range, latent_range, n)[::-1]
    canvas = np.zeros((28 * n, 28 * n))
    for i, yi in enumerate(grid_y):
        for j, xi in enumerate(grid_x):
            z_sample = np.array([[xi, yi]])
            img = decoder.predict(z_sample, verbose=0)[0].reshape(28, 28)
            canvas[i * 28:(i + 1) * 28, j * 28:(j + 1) * 28] = img
    plt.figure(figsize=(10, 10))
    plt.imshow(canvas, cmap='gray')
    plt.title("VAE — Decoded Latent Grid")
    plt.axis('off')
    plt.show()

plot_latent_grid(vae_decoder)
```

**Question 2.1 (Markdown cell):** Compare the latent space grid of the VAE to the scatter plot from the standard autoencoder. What structural difference do you observe, and why does the VAE produce it?

---

## Part 3 — Scaled Dot-Product Attention from Scratch (20 minutes)

### Step 3.1 — Implement Attention

```python
def scaled_dot_product_attention(Q, K, V, mask=None):
    """
    Q, K, V: tensors of shape (batch, seq_len, depth)
    mask: optional additive mask (large negative values block positions)
    Returns: output (batch, seq_len, depth), attention weights
    """
    d_k = tf.cast(tf.shape(K)[-1], tf.float32)
    scores = tf.matmul(Q, K, transpose_b=True) / tf.math.sqrt(d_k)
    if mask is not None:
        scores += mask * -1e9
    weights = tf.nn.softmax(scores, axis=-1)
    output = tf.matmul(weights, V)
    return output, weights
```

### Step 3.2 — Test with a Toy Example

```python
tf.random.set_seed(42)
batch, seq_len, depth = 1, 6, 8

Q = tf.random.normal((batch, seq_len, depth))
K = tf.random.normal((batch, seq_len, depth))
V = tf.random.normal((batch, seq_len, depth))

output, weights = scaled_dot_product_attention(Q, K, V)
print("Output shape:", output.shape)
print("Weights shape:", weights.shape)
print("Weights sum to 1 per row:", tf.reduce_sum(weights, axis=-1).numpy())

plt.figure(figsize=(5, 4))
plt.imshow(weights[0].numpy(), cmap='viridis')
plt.title("Attention Weight Matrix")
plt.xlabel("Key position")
plt.ylabel("Query position")
plt.colorbar()
plt.show()
```

**Question 3.1 (Markdown cell):** What does each row of the attention weight matrix represent? What would a uniform weight matrix (all `1/seq_len`) mean about the model's behavior?

---

## Part 4 — Minimal Transformer Text Classifier (25 minutes)

### Step 4.1 — Prepare Toy Sentiment Data

```python
# Toy sentiment data — expand for a real task
sentences = [
    "this movie was absolutely wonderful",
    "great film loved every minute",
    "terrific acting and beautiful story",
    "amazing and heartwarming experience",
    "horrible waste of time",
    "terrible boring and painful to watch",
    "awful film I hated it",
    "worst movie I have ever seen",
]
labels = [1, 1, 1, 1, 0, 0, 0, 0]  # 1=positive, 0=negative

tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=500, oov_token='<OOV>')
tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)
padded = tf.keras.preprocessing.sequence.pad_sequences(
    sequences, maxlen=10, padding='post'
)
x_data = np.array(padded, dtype='float32')
y_data = np.array(labels)
```

### Step 4.2 — Transformer Classifier

```python
VOCAB_SIZE = 500
SEQ_LEN = 10
D_MODEL = 32
NUM_HEADS = 2
DFF = 64
DROPOUT = 0.1

class TransformerBlock(tf.keras.layers.Layer):
    def __init__(self, d_model, num_heads, dff, dropout):
        super().__init__()
        self.mha = tf.keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=d_model // num_heads, dropout=dropout
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

# Build model
inp = tf.keras.Input(shape=(SEQ_LEN,))
emb = tf.keras.layers.Embedding(VOCAB_SIZE, D_MODEL)(inp)
x = TransformerBlock(D_MODEL, NUM_HEADS, DFF, DROPOUT)(emb)
x = tf.keras.layers.GlobalAveragePooling1D()(x)
x = tf.keras.layers.Dense(32, activation='relu')(x)
out = tf.keras.layers.Dense(1, activation='sigmoid')(x)

transformer_model = tf.keras.Model(inp, out)
transformer_model.compile(optimizer='adam',
                           loss='binary_crossentropy',
                           metrics=['accuracy'])
transformer_model.summary()

transformer_model.fit(x_data, y_data, epochs=50, verbose=0)
preds = (transformer_model.predict(x_data, verbose=0) > 0.5).astype(int).flatten()
print("Predictions:", preds)
print("Actual:     ", y_data)
```

---

## Submission Checklist

Before submitting, confirm your notebook contains:

- [ ] Autoencoder trained, reconstructions plotted
- [ ] 2D latent space scatter plot with class color coding
- [ ] VAE trained with ELBO loss (both reconstruction and KL terms reported)
- [ ] VAE latent grid decoded and displayed
- [ ] Attention implementation tested with attention weight heatmap
- [ ] Transformer classifier built, trained, and predictions printed
- [ ] All three Markdown written response cells answered

---

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| Autoencoder trained; reconstructions and latent scatter shown | 25 |
| VAE with correct ELBO loss; latent grid visualization | 30 |
| Attention implementation correct; heatmap displayed | 20 |
| Transformer classifier built and tested | 15 |
| Written responses (Q1.1, Q2.1, Q3.1) | 10 |
| **Total** | **100** |
