# Lab: Module 09 — Natural Language Processing with TensorFlow

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Overview

In this lab you will build two text classification models for IMDB sentiment analysis. The first uses a bag-of-embeddings approach (`GlobalAveragePooling1D`). The second uses a Bidirectional LSTM. You will then extend the pipeline to accept raw strings using `TextVectorization` embedded in the model.

**Estimated time:** 75–90 minutes

**Environment:** Google Colab (recommended) or local Python 3.9+ with TensorFlow 2.12+

---

## Learning Outcomes

After completing this lab you will be able to:

- Tokenize text and pad sequences using the legacy `Tokenizer` API
- Build and train an `Embedding` + `GlobalAveragePooling1D` classifier
- Build and train an `Embedding` + Bidirectional LSTM classifier
- Compare the two architectures by plotting accuracy and loss curves
- Build a portable model using `TextVectorization` that accepts raw strings

---

## Setup

### Part A — Imports and Data Loading

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

print(f"TensorFlow version: {tf.__version__}")

# Load IMDB — already integer-encoded, vocabulary of 10,000 words
VOCAB_SIZE = 10000
(x_train_raw, y_train), (x_test_raw, y_test) = tf.keras.datasets.imdb.load_data(
    num_words=VOCAB_SIZE
)

print(f"Training samples : {len(x_train_raw)}")
print(f"Test samples     : {len(x_test_raw)}")
print(f"Sample sequence  : {x_train_raw[0][:20]}")
print(f"Label             : {y_train[0]}")   # 1 = positive, 0 = negative
```

### Part B — Pad Sequences

```python
MAXLEN = 200

# TODO: Pad x_train_raw and x_test_raw to MAXLEN using pad_sequences
# Use padding='post' and truncating='post'

x_train = tf.keras.preprocessing.sequence.pad_sequences(
    x_train_raw,
    maxlen=______,
    padding=______,
    truncating=______
)

x_test = tf.keras.preprocessing.sequence.pad_sequences(
    x_test_raw,
    maxlen=MAXLEN,
    padding='post',
    truncating='post'
)

print(f"x_train shape: {x_train.shape}")   # Expected: (25000, 200)
print(f"x_test shape : {x_test.shape}")    # Expected: (25000, 200)
```

---

## Part 1 — Bag-of-Embeddings Classifier

### Step 1.1 — Build the Model

```python
EMBED_DIM = 64

def build_bow_model():
    model = tf.keras.Sequential([
        # TODO: Add Embedding layer
        # input_dim = VOCAB_SIZE + 1  (reserve index 0 for padding)
        # output_dim = EMBED_DIM
        # input_length = MAXLEN
        tf.keras.layers.Embedding(
            input_dim=_______ + 1,
            output_dim=_______,
            input_length=_______
        ),

        # TODO: Add GlobalAveragePooling1D to aggregate over sequence positions
        tf.keras.layers._______________(),

        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.4),

        # TODO: Add output layer for binary classification
        # activation = 'sigmoid', output units = 1
        tf.keras.layers.Dense(_______, activation=_______)
    ])
    return model

bow_model = build_bow_model()
bow_model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
bow_model.summary()
```

### Step 1.2 — Train

```python
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', patience=3, restore_best_weights=True
)

bow_history = bow_model.fit(
    x_train, y_train,
    epochs=20,
    batch_size=128,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=1
)

bow_loss, bow_acc = bow_model.evaluate(x_test, y_test, verbose=0)
print(f"BOW Test Accuracy: {bow_acc:.4f}")
```

---

## Part 2 — Bidirectional LSTM Classifier

### Step 2.1 — Build the Model

```python
def build_lstm_model():
    model = tf.keras.Sequential([
        # Embedding with mask_zero=True to ignore padding tokens in the LSTM
        tf.keras.layers.Embedding(
            input_dim=VOCAB_SIZE + 1,
            output_dim=EMBED_DIM,
            input_length=MAXLEN,
            mask_zero=True         # <-- propagate padding mask to LSTM
        ),

        # TODO: Add a Bidirectional LSTM layer with 64 units
        tf.keras.layers.Bidirectional(
            tf.keras.layers.LSTM(_______)
        ),

        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.4),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

lstm_model = build_lstm_model()
lstm_model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
lstm_model.summary()
```

### Step 2.2 — Train

```python
lstm_history = lstm_model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=128,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=1
)

lstm_loss, lstm_acc = lstm_model.evaluate(x_test, y_test, verbose=0)
print(f"LSTM Test Accuracy: {lstm_acc:.4f}")
```

---

## Part 3 — TextVectorization Inside the Model

### Step 3.1 — Decode IMDB Back to Text and Build a String-Input Model

```python
# The IMDB dataset comes pre-encoded; we need the word index to decode it
word_index = tf.keras.datasets.imdb.get_word_index()
# IDs 1-3 are reserved; actual words start at index 4
index_to_word = {v + 3: k for k, v in word_index.items()}
index_to_word[0] = "<PAD>"
index_to_word[1] = "<START>"
index_to_word[2] = "<UNK>"
index_to_word[3] = "<UNUSED>"

def decode_review(encoded):
    return " ".join([index_to_word.get(i, "?") for i in encoded])

# Decode first 500 training reviews to strings
train_strings = [decode_review(seq) for seq in x_train_raw[:500]]
train_labels_sub = y_train[:500]

# Create TextVectorization layer
vectorize_layer = tf.keras.layers.TextVectorization(
    max_tokens=VOCAB_SIZE,
    output_mode='int',
    output_sequence_length=MAXLEN
)

# TODO: Call adapt() on the training strings (list of strings)
vectorize_layer.adapt(______)

print(f"Vocabulary size: {len(vectorize_layer.get_vocabulary())}")
```

### Step 3.2 — Build the String-Input Model

```python
def build_string_model():
    # Input: raw string tensors
    string_input = tf.keras.Input(shape=(1,), dtype=tf.string)

    # Step 1: vectorize (string → integer sequence)
    x = vectorize_layer(string_input)

    # Step 2: embed
    x = tf.keras.layers.Embedding(
        input_dim=len(vectorize_layer.get_vocabulary()) + 1,
        output_dim=EMBED_DIM
    )(x)

    # Step 3: aggregate
    x = tf.keras.layers.GlobalAveragePooling1D()(x)

    # Step 4: classify
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    x = tf.keras.layers.Dropout(0.3)(x)
    output = tf.keras.layers.Dense(1, activation='sigmoid')(x)

    return tf.keras.Model(string_input, output)

string_model = build_string_model()
string_model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train on decoded strings (subset)
train_ds = tf.data.Dataset.from_tensor_slices(
    (train_strings, train_labels_sub.astype(np.float32))
).batch(32).prefetch(tf.data.AUTOTUNE)

string_history = string_model.fit(train_ds, epochs=5, verbose=1)

# Predict directly from raw strings
test_reviews = tf.constant([
    "This movie was absolutely brilliant. I loved every moment.",
    "Terrible film. Boring plot and terrible acting. Waste of time."
])
preds = string_model.predict(test_reviews, verbose=0)
for review, pred in zip(test_reviews.numpy(), preds):
    sentiment = "positive" if pred[0] > 0.5 else "negative"
    print(f"Sentiment: {sentiment} ({pred[0]:.3f})")
    print(f"  Review: {review.decode()[:60]}...")
```

---

## Part 4 — Visualization and Comparison

### Step 4.1 — Plot Training Curves

```python
def plot_nlp_comparison(bow_hist, lstm_hist):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for hist, name in [(bow_hist, "BOW"), (lstm_hist, "Bi-LSTM")]:
        axes[0].plot(hist.history['accuracy'],     label=f"{name} train")
        axes[0].plot(hist.history['val_accuracy'], label=f"{name} val", linestyle='--')
        axes[1].plot(hist.history['loss'],         label=f"{name} train")
        axes[1].plot(hist.history['val_loss'],     label=f"{name} val", linestyle='--')

    axes[0].set_title("Accuracy Comparison")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Accuracy")
    axes[0].legend()

    axes[1].set_title("Loss Comparison")
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("Loss")
    axes[1].legend()

    plt.suptitle("Module 09 — Bag-of-Embeddings vs Bidirectional LSTM")
    plt.tight_layout()
    plt.savefig("module09_results.png", dpi=120)
    plt.show()

plot_nlp_comparison(bow_history, lstm_history)
```

### Step 4.2 — Print Results Summary

```python
print("=" * 50)
print(f"{'Model':<25} {'Test Accuracy':>15}")
print("=" * 50)
print(f"{'BOW (GAP1D)':<25} {bow_acc:>14.4f}")
print(f"{'Bidirectional LSTM':<25} {lstm_acc:>14.4f}")
print("=" * 50)
```

---

## Deliverables

Submit the following to Canvas:

1. Your completed Jupyter notebook (`.ipynb`) with all cells executed and outputs visible.
2. The saved plot `module09_results.png` showing both model accuracy curves.
3. A written response (150–200 words) answering:
   - Which model achieved higher test accuracy — BOW or Bi-LSTM?
   - Did either model overfit? How did you identify this from the curves?
   - What was the predicted sentiment for each of the two hard-coded test reviews in Part 3?
   - Explain in one sentence why `input_dim = VOCAB_SIZE + 1` rather than `VOCAB_SIZE`.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Sequences padded to correct shape `(25000, 200)` | 10 |
| BOW model builds, compiles, and trains without errors | 20 |
| LSTM model with Bidirectional wrapper builds and trains | 20 |
| TextVectorization model accepts raw strings and predicts | 20 |
| Comparison plot generated and saved | 10 |
| Written analysis with specific accuracy numbers | 20 |
| **Total** | **100** |

---

Texas Wesleyan University — CIS-4345 Machine Learning and Deep Learning

Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.
