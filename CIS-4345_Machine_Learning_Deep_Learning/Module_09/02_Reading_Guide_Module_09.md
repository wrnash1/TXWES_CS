# Reading Guide: Module 09 — Natural Language Processing with TensorFlow

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4345 &BULL; MACHINE LEARNING & DEEP LEARNING SYSTEMS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Learning Objectives

By the end of this module you will be able to:

1. Tokenize raw text using `Tokenizer` and `TextVectorization`.
2. Pad and truncate integer sequences to a fixed length using `pad_sequences`.
3. Explain how the `Embedding` layer maps integers to dense vectors.
4. Build a complete text classification model from raw text to prediction.
5. Implement a binary sentiment analysis model on the IMDB dataset.
6. Compare bag-of-words (`GlobalAveragePooling1D`) vs. sequential (`LSTM`) text encoders.

---

## Section 1 — The NLP Preprocessing Pipeline

### Why Text Needs Special Handling

Images are already numerical — pixels are integers in [0, 255]. Text is categorical: the word "terrible" is not numerically related to "great" in any meaningful way. To train a neural network on text, we must build a bridge from strings to numbers that preserves semantic information.

The full pipeline is:

```text
Raw text → Tokenize → Integer sequences → Pad/Truncate → Embed → Model
```

Each stage has a specific responsibility. Skipping any stage produces incorrect input shapes or semantically meaningless inputs.

### Why Not One-Hot Encoding?

One-hot encoding assigns each word a vector of length `vocab_size` with a single `1` and all other values `0`. For a vocabulary of 10,000 words, every word becomes a 10,000-dimensional sparse vector. Problems:

- Storage: `25000 * 200 * 10000 = 50 billion` float values for 25,000 IMDB reviews.
- No semantic structure: "good" and "great" have orthogonal vectors with zero similarity.
- Embeddings solve both problems: a 64-dimensional dense vector per word, learned during training.

---

## Section 2 — Tokenizer (Legacy API)

### Building the Vocabulary

```python
from tensorflow.keras.preprocessing.text import Tokenizer

train_sentences = [
    "I loved this movie it was fantastic",
    "This film was terrible and boring",
    "An amazing performance by the entire cast",
    "Complete waste of time do not watch"
]

tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(train_sentences)

# word_index maps every word to an integer ID
print(tokenizer.word_index)
# {'<OOV>': 1, 'was': 2, 'this': 3, 'the': 4, ...}
```

### Key Parameters

| Parameter | Default | Purpose |
|---|---|---|
| `num_words` | None (all words) | Cap vocabulary at N most frequent words |
| `oov_token` | None | Token inserted for words not in vocabulary |
| `lower` | True | Convert text to lowercase before tokenizing |
| `filters` | punctuation chars | Characters removed before tokenizing |

### Converting Text to Sequences

```python
from tensorflow.keras.preprocessing.sequence import pad_sequences

sequences = tokenizer.texts_to_sequences(train_sentences)
# [[3, 4, 5, 6, 7, 2, 8], [3, 9, 2, 10, 11, 12], ...]

padded = pad_sequences(sequences, maxlen=20, padding='post', truncating='post')
print(padded.shape)   # (4, 20)
```

### pad_sequences Parameters

| Parameter | Options | Effect |
|---|---|---|
| `maxlen` | int | Target sequence length |
| `padding` | `'pre'` (default), `'post'` | Where to add zeros |
| `truncating` | `'pre'` (default), `'post'` | Where to cut long sequences |
| `value` | 0 (default) | Value used for padding |

The exam commonly tests whether students know that `padding='pre'` is the default. For LSTM models, `padding='post'` is generally preferred because it places real tokens at the beginning of the sequence where the LSTM processes them first.

### The OOV Token Problem

```python
# Suppose "phenomenal" was not in training data
test_sentence = ["the film was phenomenal"]
test_seq = tokenizer.texts_to_sequences(test_sentence)
# Without oov_token: [[4, 9, 2]]    — "phenomenal" is dropped
# With oov_token:    [[4, 9, 2, 1]] — "phenomenal" → ID 1 (<OOV>)
```

Dropped tokens change sequence lengths and can cause shape mismatches. Always set `oov_token`.

---

## Section 3 — TextVectorization (Modern API)

### Comparison: Tokenizer vs TextVectorization

| Feature | `Tokenizer` | `TextVectorization` |
|---|---|---|
| API generation | Legacy (Keras 1.x era) | Modern (TF 2.x) |
| Returns | Python object | Keras layer |
| Embedded in model | No | Yes |
| Runs on GPU | No | Yes |
| Exported with model | No (requires separate save) | Yes (part of model graph) |
| Exam relevance | High (still tested) | High (preferred pattern) |

### Using TextVectorization

```python
import tensorflow as tf

vectorize_layer = tf.keras.layers.TextVectorization(
    max_tokens=10000,            # vocabulary size
    output_mode='int',           # return integer IDs
    output_sequence_length=200   # pad/truncate to this length
)

# adapt() builds the vocabulary — call ONLY on training data
train_text_ds = tf.data.Dataset.from_tensor_slices(train_sentences)
vectorize_layer.adapt(train_text_ds)

# Check vocabulary
vocab = vectorize_layer.get_vocabulary()
print(f"Vocabulary size: {len(vocab)}")
print(f"First 10 tokens: {vocab[:10]}")
# ['', '[UNK]', 'the', 'was', ...]
# Index 0 = padding; Index 1 = [UNK] (out-of-vocabulary)
```

### output_mode Options

| Mode | Output | Use Case |
|---|---|---|
| `'int'` | Integer sequence | Embedding-based models |
| `'binary'` | Multi-hot vector | Bag-of-words logistic regression |
| `'count'` | Word count vector | Naive Bayes-style models |
| `'tf_idf'` | TF-IDF weighted vector | Classical NLP baselines |

---

## Section 4 — The Embedding Layer

### How Embedding Works

The `Embedding` layer is a trainable lookup table. Conceptually:

```text
Input integer 42 → Look up row 42 of weight matrix W → Return 64-dimensional vector
```

The weight matrix `W` has shape `(vocab_size, embedding_dim)` and is updated by backpropagation during training. Words that appear in similar contexts (surrounding words) are pushed toward similar vectors — this is the origin of semantic similarity in learned embeddings.

### Constructor Parameters

```python
embedding_layer = tf.keras.layers.Embedding(
    input_dim=10001,     # vocabulary size + 1 (index 0 reserved for padding)
    output_dim=64,       # dimensionality of each embedding vector
    input_length=200,    # sequence length (required for Sequential API)
    mask_zero=True       # propagate padding mask to downstream layers
)
```

The off-by-one rule: if your vocabulary contains 10,000 words, token IDs range from 1 to 10,000. Index 0 is used for padding. Therefore `input_dim` must be `10001` (= `vocab_size + 1`).

### Output Shape

```python
# Input: integer sequence of shape (batch_size, sequence_length)
# Example: (32, 200) — batch of 32 reviews, each 200 tokens

# After Embedding(10001, 64):
# Output shape: (32, 200, 64)
# Each of the 200 token positions now has a 64-dimensional vector
```

### What Follows the Embedding Layer

| Aggregation Layer | Output Shape | Notes |
|---|---|---|
| `GlobalAveragePooling1D()` | `(batch, 64)` | Average across all positions; simple, fast |
| `GlobalMaxPooling1D()` | `(batch, 64)` | Max across positions; captures strongest feature |
| `LSTM(64)` | `(batch, 64)` | Sequential processing; captures word order |
| `GRU(64)` | `(batch, 64)` | Faster than LSTM; comparable quality |
| `Flatten()` | `(batch, 200*64)` | Full concatenation; fixed input length required |

---

## Section 5 — Text Classification Architectures

### Architecture 1 — Bag-of-Embeddings (Fast Baseline)

```python
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(10001, 64, input_length=200),
    tf.keras.layers.GlobalAveragePooling1D(),     # average across positions
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
```

GlobalAveragePooling1D produces a single vector by averaging all token embeddings. This is effectively a bag-of-words model — word order is lost. It trains quickly and performs well for simple sentiment tasks.

### Architecture 2 — LSTM Classifier

```python
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(10001, 64, input_length=200, mask_zero=True),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

`Bidirectional` wraps the LSTM to process the sequence in both forward and backward directions, concatenating both hidden states. This captures context from both sides of each word and typically improves accuracy by 2–5% on sentiment tasks.

### Architecture 3 — TextVectorization Inside the Model

```python
# Build a model that accepts raw strings
string_input = tf.keras.Input(shape=(1,), dtype=tf.string)
x = vectorize_layer(string_input)
x = tf.keras.layers.Embedding(len(vectorize_layer.get_vocabulary()), 64)(x)
x = tf.keras.layers.GlobalAveragePooling1D()(x)
x = tf.keras.layers.Dense(64, activation='relu')(x)
x = tf.keras.layers.Dropout(0.3)(x)
output = tf.keras.layers.Dense(1, activation='sigmoid')(x)

export_model = tf.keras.Model(string_input, output)
export_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

This model accepts raw strings at prediction time:

```python
predictions = export_model.predict(["The film was outstanding!"])
```

---

## Section 6 — Complete IMDB Sentiment Workflow

### Loading and Preprocessing

```python
import tensorflow as tf
import numpy as np

# Load IMDB — already integer-encoded
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.imdb.load_data(
    num_words=10000
)

# Inspect a sample
print(f"Training samples: {len(x_train)}")
print(f"Sequence lengths (first 5): {[len(s) for s in x_train[:5]]}")

# Pad to fixed length
MAXLEN = 200
x_train = tf.keras.preprocessing.sequence.pad_sequences(
    x_train, maxlen=MAXLEN, padding='post', truncating='post'
)
x_test = tf.keras.preprocessing.sequence.pad_sequences(
    x_test, maxlen=MAXLEN, padding='post', truncating='post'
)
print(f"x_train shape: {x_train.shape}")   # (25000, 200)
```

### Training and Evaluation

```python
VOCAB_SIZE = 10001
EMBED_DIM  = 64

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(VOCAB_SIZE, EMBED_DIM, input_length=MAXLEN),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=3, restore_best_weights=True
    )
]

history = model.fit(
    x_train, y_train,
    epochs=20,
    batch_size=128,
    validation_split=0.2,
    callbacks=callbacks
)

loss, acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {acc:.4f}")
```

---

## Key Vocabulary

| Term | Definition |
|---|---|
| Tokenization | Splitting text into tokens and assigning each an integer ID |
| Vocabulary | The complete set of unique tokens known to the tokenizer |
| `oov_token` | Special token assigned to words not seen during vocabulary fitting |
| Padding | Adding zeros to short sequences to reach a target length |
| Truncation | Removing tokens from sequences that exceed the target length |
| `Embedding` | A trainable lookup table mapping integer IDs to dense vectors |
| `input_dim` | The vocabulary size; must equal `vocab_size + 1` |
| `output_dim` | The dimensionality of each embedding vector |
| `mask_zero` | Flag that propagates padding masks to downstream recurrent layers |
| `adapt()` | Method that fits `TextVectorization` vocabulary on training data |
| `GlobalAveragePooling1D` | Averages embedding vectors across all sequence positions |
| Sentiment analysis | Binary or multi-class classification of text emotional tone |

---

## Review Questions

1. Why must `input_dim` in the `Embedding` layer equal `vocab_size + 1`?
2. What is the output shape of `Embedding(10001, 64)` given input shape `(32, 200)`?
3. When should you use `GlobalAveragePooling1D` instead of `LSTM` after an `Embedding` layer?
4. What happens to unknown words if `oov_token` is not set in `Tokenizer`?
5. What is the difference between `padding='pre'` and `padding='post'`, and which is better for LSTM models?
6. Why must `adapt()` be called only on training data, never on test data?
7. What is the advantage of embedding `TextVectorization` inside the model vs. using it externally?
8. For multi-class text classification with 5 categories, what activation and loss function should you use?

---

Texas Wesleyan University — CIS-4345 Machine Learning and Deep Learning

Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.

---

## 9. Supplemental Resources

**1. [TensorFlow Text Classification with TF Hub](https://www.tensorflow.org/tutorials/keras/text_classification_with_hub)**
Official TensorFlow tutorial that walks through sentiment classification on the IMDB dataset using pre-trained text embeddings from TF Hub. Demonstrates how to use a pre-built embedding module as a Keras layer, complementing this module's coverage of custom `Embedding` and `TextVectorization` layers.

**2. [fast.ai NLP Course — Practical Deep Learning for Coders](https://course.fast.ai/Lessons/lesson8.html)**
Jeremy Howard's practical NLP lessons from fast.ai, covering tokenization, transfer learning with language models, and fine-tuning for classification. Provides a modern perspective on NLP that extends beyond the TF exam fundamentals covered in this module.

**3. [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)**
Stanford NLP's GloVe project page, offering pre-trained word vectors (50d, 100d, 200d, 300d) trained on Wikipedia and Common Crawl. Includes the original paper and download links. Directly applicable to the technique of loading pre-trained embeddings into a Keras `Embedding` layer with `trainable=False`.
