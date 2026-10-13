# Video Script: Module 09 — Natural Language Processing with TensorFlow

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: TensorFlow Developer Certificate

---

### [00:00 – 01:30] Opening and Module Overview

**Visual:** Title card — "Module 09: Natural Language Processing with TensorFlow"

**Audio:**
Welcome back, everyone. I'm Professor Nash, and in Module 09 we step out of the image domain and into the world of text. Natural Language Processing — NLP — is one of the most impactful application areas in machine learning today, and it is a major section of the TensorFlow Developer Certificate exam.

Here is our agenda for today:

- How computers represent text as numbers
- Text tokenization with Keras `Tokenizer` and `TextVectorization`
- Word embeddings and the Keras `Embedding` layer
- Building a text classification model end-to-end
- Sentiment analysis: a classic NLP task
- Preprocessing best practices for text data

Every one of these topics appears on the TF Developer Certificate. Let's get into it.

---

### [01:30 – 04:00] The Text Representation Problem

**Visual:** Diagram showing "the food was terrible" being converted to integers and then to embedding vectors.

**Audio:**
Before any neural network can process text, we have to solve a fundamental problem: neural networks work with numbers, not words. So how do we turn the sentence "the food was terrible" into something a network can learn from?

The pipeline has three stages:

**Stage 1 — Tokenization:** Split the text into tokens (usually words or subwords) and assign each unique token an integer ID. "the" might become ID 1, "food" becomes ID 2, "was" becomes ID 3, and "terrible" becomes ID 4.

**Stage 2 — Sequence encoding:** Convert each piece of text into a list of integer IDs, then pad or truncate all lists to the same length so they form a regular 2D array that a neural network can consume.

**Stage 3 — Embedding:** Map each integer ID to a dense vector of real numbers — for example, a 64-dimensional vector. These embedding vectors are learned during training. Words used in similar contexts end up with similar vectors.

Each stage is critical. If you get tokenization wrong, the rest of the pipeline breaks. If you skip embeddings and feed raw integers to the network, you are treating word IDs as ordinal numbers, which is semantically meaningless.

---

### [04:00 – 07:30] Tokenizer — The Legacy API

**Visual:** Code editor showing `Tokenizer` being fit and applied.

**Audio:**
Keras provides a `Tokenizer` class in `tf.keras.preprocessing.text`. Like `ImageDataGenerator` for images, this is the legacy API — you will see it on the exam and in older codebases.

```python
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    "the food was amazing",
    "the service was terrible",
    "i loved the atmosphere",
    "never going back there"
]

# OOV token handles words not seen during fit
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)

# Inspect the word index
word_index = tokenizer.word_index
print(word_index)
# {'<OOV>': 1, 'the': 2, 'was': 3, 'food': 4, ...}

# Convert sentences to integer sequences
sequences = tokenizer.texts_to_sequences(sentences)
print(sequences)
# [[2, 4, 3, 5], [2, 6, 3, 7], ...]

# Pad to uniform length
padded = pad_sequences(sequences, maxlen=10, padding='post', truncating='post')
print(padded.shape)
# (4, 10)
```

Key parameters to know:

- `num_words` — vocabulary size cap; only the top N most frequent words are kept
- `oov_token` — the special token substituted for any word not in the vocabulary
- `padding='post'` — pad with zeros at the end; `padding='pre'` pads at the start
- `truncating='post'` — cut long sequences from the end

The `oov_token` is crucial. Without it, words not seen during `fit_on_texts` are simply dropped from the sequence — you lose information silently.

---

### [07:30 – 11:00] TextVectorization — The Modern API

**Visual:** Code editor showing `TextVectorization` layer integrated into a Keras model.

**Audio:**
The modern TensorFlow approach is the `TextVectorization` layer. It does everything `Tokenizer` does but operates as a Keras layer, which means it can be embedded in the model graph and run on GPU.

```python
import tensorflow as tf

# Create and adapt the layer
vectorize_layer = tf.keras.layers.TextVectorization(
    max_tokens=10000,
    output_mode='int',
    output_sequence_length=100
)

# Adapt fits the vocabulary on the training data
train_texts = tf.data.Dataset.from_tensor_slices([
    "the food was amazing",
    "the service was terrible",
    "i loved the atmosphere",
    "never going back there"
])
vectorize_layer.adapt(train_texts)

# Inspect vocabulary
vocab = vectorize_layer.get_vocabulary()
print(vocab[:10])

# Vectorize a sample
sample = tf.constant(["the food was amazing and the service was good"])
print(vectorize_layer(sample))
```

Now let's embed it inside a full model:

```python
def build_text_model(max_tokens=10000, sequence_length=100,
                     embedding_dim=64, num_classes=2):
    inputs = tf.keras.Input(shape=(1,), dtype=tf.string)

    # Step 1: vectorize (string → integer sequence)
    x = vectorize_layer(inputs)

    # Step 2: embed (integers → dense vectors)
    x = tf.keras.layers.Embedding(
        input_dim=max_tokens + 1,
        output_dim=embedding_dim,
        mask_zero=True
    )(x)

    # Step 3: aggregate (sequence → single vector)
    x = tf.keras.layers.GlobalAveragePooling1D()(x)

    # Step 4: classify
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    x = tf.keras.layers.Dropout(0.4)(x)
    outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)

    return tf.keras.Model(inputs, outputs)
```

When this model is saved and deployed, the vectorization logic travels with it. Pass raw text strings directly — no external tokenization needed.

---

### [11:00 – 13:30] The Embedding Layer

**Visual:** Animation showing a lookup table where each row is an embedding vector for one word.

**Audio:**
The `Embedding` layer is the heart of every NLP model in TensorFlow. Understanding it is essential for the certification exam.

```python
embedding_layer = tf.keras.layers.Embedding(
    input_dim=10001,    # vocabulary size + 1 for the mask/padding token
    output_dim=64,      # size of each embedding vector
    input_length=100,   # sequence length (optional in functional API)
    mask_zero=True      # tells downstream layers to ignore padding tokens
)
```

Here is what happens internally:

- The layer maintains a weight matrix of shape `(input_dim, output_dim)` — in this example `(10001, 64)`.
- When integer ID `42` enters, the layer returns row 42 of that matrix.
- This is a differentiable lookup, so the embedding vectors are updated by backpropagation during training.
- Words that appear in similar contexts end up with similar vectors because the loss function pushes them together.

The output shape of an `Embedding` layer is `(batch_size, sequence_length, output_dim)` — a 3D tensor. This is important for understanding what layer comes next.

```python
# Input: batch of integer sequences, shape (32, 100)
# After Embedding(10001, 64): shape (32, 100, 64)
# Each of the 100 positions now has a 64-dimensional vector

# Option 1: Feed to LSTM (processes the sequence)
x = tf.keras.layers.LSTM(64)(embedding_output)   # output: (32, 64)

# Option 2: Global average pooling (averages across positions)
x = tf.keras.layers.GlobalAveragePooling1D()(embedding_output)  # output: (32, 64)

# Option 3: Flatten (concatenates all position vectors)
x = tf.keras.layers.Flatten()(embedding_output)  # output: (32, 6400)
```

For simple text classification, `GlobalAveragePooling1D` is fast and effective. For tasks that require understanding word order, use `LSTM` or `GRU`.

---

### [13:30 – 16:30] Text Classification End-to-End

**Visual:** Full model architecture diagram for sentiment analysis.

**Audio:**
Let me walk you through a complete text classification workflow from raw data to trained model. We will use the IMDB sentiment dataset.

```python
import tensorflow as tf
import numpy as np

# Load built-in IMDB dataset (preprocessed integer sequences)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.imdb.load_data(
    num_words=10000
)

# Pad sequences to uniform length
x_train = tf.keras.preprocessing.sequence.pad_sequences(
    x_train, maxlen=200, padding='post', truncating='post'
)
x_test = tf.keras.preprocessing.sequence.pad_sequences(
    x_test, maxlen=200, padding='post', truncating='post'
)

print(f"Training data shape: {x_train.shape}")   # (25000, 200)
print(f"Labels unique values: {np.unique(y_train)}")  # [0 1]

# Build classifier
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(
        input_dim=10001,
        output_dim=64,
        input_length=200
    ),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

# Train
history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=128,
    validation_split=0.2,
    verbose=1
)
```

A few key decisions in this code:

- `Embedding(10001, 64)` — vocabulary size 10,000 plus one extra slot for the OOV/padding index 0.
- `GlobalAveragePooling1D` — averages the 64-dimensional vectors across all 200 positions, yielding one 64-dim vector per review.
- `Dense(1, sigmoid)` — binary output: positive (1) or negative (0) sentiment.

---

### [16:30 – 18:30] Sentiment Analysis with Custom Text

**Visual:** Model predicting sentiment on new review strings.

**Audio:**
After training, making predictions on new text requires applying the same tokenization and padding that was used during training:

```python
# Using the legacy Tokenizer approach
def predict_sentiment(text, tokenizer, model, maxlen=200):
    seq = tokenizer.texts_to_sequences([text])
    padded = tf.keras.preprocessing.sequence.pad_sequences(
        seq, maxlen=maxlen, padding='post'
    )
    prob = model.predict(padded, verbose=0)[0][0]
    label = "positive" if prob > 0.5 else "negative"
    return label, float(prob)

result, confidence = predict_sentiment(
    "This movie was absolutely fantastic, I loved every minute!",
    tokenizer, model
)
print(f"Sentiment: {result} ({confidence:.3f})")
```

When using `TextVectorization` embedded in the model, prediction is even simpler:

```python
# Model accepts raw strings directly
test_texts = tf.constant([
    "This movie was absolutely fantastic!",
    "Boring and predictable. I want my two hours back."
])
predictions = model.predict(test_texts)
for text, pred in zip(test_texts.numpy(), predictions):
    sentiment = "positive" if pred[0] > 0.5 else "negative"
    print(f"{text.decode()}: {sentiment} ({pred[0]:.3f})")
```

This is a major advantage of the `TextVectorization` approach: the deployed model is entirely self-contained.

---

### [18:30 – 20:30] Certification Exam Tips

**Visual:** Bullet list of key facts and common mistakes.

**Audio:**
Here are the exam tips for Module 09:

- **`Embedding` input_dim = vocab_size + 1** — you need an extra slot for the padding/OOV index 0. This is a very common off-by-one error on the exam.
- **`output_shape` of `Embedding`** — always `(batch, sequence_length, output_dim)`. Know this cold.
- **`GlobalAveragePooling1D` vs `Flatten`** — GAP1D averages across positions (handles variable length); `Flatten` concatenates all vectors (input length must be fixed).
- **`mask_zero=True`** — tells downstream layers (LSTM, GRU) to ignore padding positions. Use it whenever padding is present.
- **`oov_token`** — always set this in `Tokenizer`. Without it, unseen words are silently dropped.
- **`adapt()`** — must be called on training data before using `TextVectorization`. Never call it on test data.
- **`pad_sequences` default** — `padding='pre'`, `truncating='pre'`. For most NLP tasks, `padding='post'` is better for LSTM performance.

---

### [20:30 – 22:00] Module Summary and Lab Preview

**Visual:** Summary slide with NLP pipeline checklist.

**Audio:**
Outstanding work today. Here is what you mastered in Module 09:

- Text tokenization with `Tokenizer` (legacy) and `TextVectorization` (modern)
- Sequence padding with `pad_sequences` — uniform length for batching
- The `Embedding` layer — learned dense representations of words
- Text classification architecture: Embed → Pool → Dense → Output
- Sentiment analysis on IMDB using binary classification
- Embedding `TextVectorization` inside the model for portable deployment

In the lab you will train your own sentiment classifier on the IMDB dataset, compare a bag-of-words model (with `GlobalAveragePooling1D`) to an LSTM-based model, and build a pipeline where the model accepts raw strings. Then you will extend it to multi-class classification.

Head over to the Lab file to get started. I will see you in Module 10.

---

End of Module 09 Video Script

Texas Wesleyan University — CIS-4345 Machine Learning and Deep Learning

Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.
