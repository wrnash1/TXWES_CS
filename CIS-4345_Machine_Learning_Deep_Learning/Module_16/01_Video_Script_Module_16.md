# Video Script: Module 16 — TensorFlow Developer Certificate Exam Preparation

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Production Notes

- **Runtime target:** 22–26 minutes
- **Format:** Screencast with live code; whiteboard-style review slides for each exam category
- **Visual aids:** Exam structure diagram; category breakdown table; common mistake checklist
- **Code environment:** Google Colab — simulate PyCharm exam conditions as closely as possible

---

## SEGMENT 1 — Welcome to the Final Module (0:00–2:30)

Welcome to Module 16 — the final module of CIS-4345. This is our capstone and exam preparation session. If you have worked through every module in this course, you have covered every topic tested on the TensorFlow Developer Certificate exam. Today we pull it all together.

The TensorFlow Developer Certificate is a professional credential issued by Google. It tests your ability to build, train, and evaluate neural networks using TensorFlow 2.x and the Keras API. The exam is five hours long, conducted in a special PyCharm IDE environment with internet access. You are given five problems and graded by how well your models perform on held-out test data, not by whether your code style is perfect.

Here is a critical framing: the exam is practical, not theoretical. You will never be asked "what is the gradient of the sigmoid function." You will be asked to build a model that achieves a target accuracy on a provided dataset. This means your preparation must be hands-on. You need to be able to write working Keras code quickly and correctly from memory.

By the end of this lecture you will have reviewed all four exam categories, seen the most common mistakes and how to avoid them, and built a personal study checklist.

---

## SEGMENT 2 — Exam Structure Overview (2:30–5:00)

[SLIDE: Exam category breakdown table]

The TensorFlow Developer Certificate exam has five problems drawn from four categories:

**Category 1: TensorFlow Fundamentals**

This covers tensors, basic operations, the Keras Sequential and Functional API, training with `model.fit()`, callbacks, and evaluation. Every exam problem involves these fundamentals. You cannot succeed in any category without mastering them.

**Category 2: Image Classification**

You will build and evaluate a CNN for image classification. Topics include Conv2D, MaxPooling2D, Flatten, Dense layers, binary and multi-class classification, data augmentation, and transfer learning with a pretrained base model like MobileNetV2 or VGG16.

**Category 3: Natural Language Processing**

You will build a model for text classification or sentiment analysis. Topics include the Tokenizer API, text-to-sequences, padding, Embedding layers, GlobalAveragePooling1D, and possibly LSTM or bidirectional LSTM.

**Category 4: Time Series Forecasting**

You will build a model to forecast a time series. Topics include windowed datasets, 1D CNNs for sequences, LSTM forecasting, normalization, and computing MAE on the validation set.

Problems are not labeled by category in the exam. You read the problem description, recognize the task type, and write the appropriate model. This is why fluency across all four categories is essential.

---

## SEGMENT 3 — Category 1 Deep Dive: TF Fundamentals (5:00–8:30)

[SLIDE: Sequential API checklist]

Let me review the most frequently tested patterns from Category 1.

First, **model compilation**. You must know which loss function to pair with which problem:

```python
# Binary classification
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Multi-class with integer labels
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Multi-class with one-hot labels
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Regression
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
```

Memorize this table. Wrong loss function is the single most common mistake on the exam.

Second, **callbacks**. The exam often specifies a target accuracy. You need an `EarlyStopping` callback that stops training when the target is hit:

```python
class TargetAccuracyCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if logs.get('accuracy') >= 0.99:
            print("\nReached 99% accuracy — stopping training.")
            self.model.stop_training = True
```

Know how to write a custom callback. It will appear on the exam.

Third, the **Functional API** for multi-input or multi-output models:

```python
inp = tf.keras.Input(shape=(128,))
x = tf.keras.layers.Dense(64, activation='relu')(inp)
out = tf.keras.layers.Dense(1, activation='sigmoid')(x)
model = tf.keras.Model(inputs=inp, outputs=out)
```

Sequential vs Functional: use Sequential for single-input, single-output linear stacks. Use Functional for everything else.

---

## SEGMENT 4 — Category 2 Deep Dive: Image Classification (8:30–12:30)

[SLIDE: CNN architecture checklist]

For image classification, you must be able to build a complete CNN pipeline in about 15 minutes under exam conditions.

**Canonical CNN architecture for exam problems:**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu',
                           input_shape=(height, width, channels)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
```

For binary classification, the last layer is `Dense(1, activation='sigmoid')` and you use `binary_crossentropy`.

**Data augmentation** — the exam frequently tests this:

```python
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip('horizontal'),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.1)
])
```

Add augmentation as the first layers of your model or in a preprocessing model.

**Transfer learning** — know how to freeze and fine-tune:

```python
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3), include_top=False, weights='imagenet'
)
base_model.trainable = False  # Freeze

x = base_model.output
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dense(128, activation='relu')(x)
output = tf.keras.layers.Dense(num_classes, activation='softmax')(x)
model = tf.keras.Model(base_model.input, output)
```

After initial training, unfreeze the base model and fine-tune at a very low learning rate (`1e-5` or `2e-5`).

**Common image mistakes:**

- Forgetting to normalize pixel values to [0, 1]
- Wrong `input_shape` — must match your data dimensions exactly
- Using `softmax` output with `binary_crossentropy` — do not do this

---

## SEGMENT 5 — Category 3 Deep Dive: NLP (12:30–16:30)

[SLIDE: NLP pipeline — tokenize → pad → embed → classify]

The NLP exam problem typically provides a CSV with text and labels. Your pipeline has five steps.

**Step 1: Tokenize**

```python
tokenizer = tf.keras.preprocessing.text.Tokenizer(
    num_words=10000, oov_token='<OOV>'
)
tokenizer.fit_on_texts(train_sentences)
train_seqs = tokenizer.texts_to_sequences(train_sentences)
val_seqs = tokenizer.texts_to_sequences(val_sentences)
```

Always fit the tokenizer on training data only.

**Step 2: Pad**

```python
from tensorflow.keras.preprocessing.sequence import pad_sequences

MAX_LEN = 120
train_padded = pad_sequences(train_seqs, maxlen=MAX_LEN,
                              padding='post', truncating='post')
val_padded = pad_sequences(val_seqs, maxlen=MAX_LEN,
                            padding='post', truncating='post')
```

**Step 3: Build the model**

```python
VOCAB_SIZE = 10000
EMBED_DIM = 16

model_nlp = tf.keras.Sequential([
    tf.keras.layers.Embedding(VOCAB_SIZE, EMBED_DIM, input_length=MAX_LEN),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

Or use `GlobalAveragePooling1D` instead of LSTM for a simpler, faster model:

```python
model_nlp_simple = tf.keras.Sequential([
    tf.keras.layers.Embedding(VOCAB_SIZE, EMBED_DIM, input_length=MAX_LEN),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

For multi-class text classification, change the final layer to `Dense(num_classes, activation='softmax')` and use `sparse_categorical_crossentropy`.

**Common NLP mistakes:**

- Fitting the tokenizer on validation or test data
- Wrong `input_length` in the Embedding layer
- Not using `oov_token` — out-of-vocabulary words in validation will cause silent shape issues

---

## SEGMENT 6 — Category 4 Deep Dive: Time Series (16:30–19:30)

[SLIDE: Windowed dataset flow diagram]

For time series, the exam typically gives you a CSV with one or more numeric columns and asks you to forecast the next value. Your pipeline has four steps.

**Step 1: Create the windowed dataset**

```python
def windowed_dataset(series, window_size, batch_size, shuffle_buffer):
    ds = tf.data.Dataset.from_tensor_slices(series)
    ds = ds.window(window_size + 1, shift=1, drop_remainder=True)
    ds = ds.flat_map(lambda w: w.batch(window_size + 1))
    ds = ds.shuffle(shuffle_buffer)
    ds = ds.map(lambda w: (w[:-1], w[-1]))
    return ds.batch(batch_size).prefetch(1)
```

Memorize this function. It will appear on every time series problem.

**Step 2: Normalize**

```python
mean = train_series.mean()
std = train_series.std()
train_norm = (train_series - mean) / std
```

Always normalize before building the dataset. Denormalize predictions afterward.

**Step 3: Build the model**

```python
# CNN approach
model_ts = tf.keras.Sequential([
    tf.keras.layers.Conv1D(64, kernel_size=3, activation='relu',
                           input_shape=[WINDOW_SIZE, 1]),
    tf.keras.layers.MaxPooling1D(pool_size=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])
```

Or LSTM:

```python
model_ts_lstm = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, return_sequences=True,
                         input_shape=[WINDOW_SIZE, 1]),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(1)
])
```

**Step 4: Evaluate with MAE**

The exam specifies a target MAE. After prediction, denormalize and compute:

```python
mae = tf.keras.metrics.mean_absolute_error(actual, predicted).numpy()
print(f"MAE: {mae:.4f}")
```

**Common time series mistakes:**

- Random train/validation split (must be temporal)
- Forgetting to add the channel dimension `tf.expand_dims(w, axis=-1)` for Conv1D
- Evaluating MAE on normalized predictions instead of denormalized ones

---

## SEGMENT 7 — Exam Strategy and Practice Problems (19:30–22:30)

[SLIDE: Exam day checklist]

Here is your five-point exam strategy.

**Point 1: Read all five problems first.** Some problems are easier than others. Tackle the ones you are most confident about first to secure points quickly.

**Point 2: Start with a working skeleton.** Do not try to build the perfect model on the first attempt. Get code that runs and reaches a reasonable baseline, then iterate.

**Point 3: Know your loss functions cold.** Binary → `binary_crossentropy`. Multi-class with integers → `sparse_categorical_crossentropy`. Multi-class with one-hot → `categorical_crossentropy`. Regression → `mse`. Wrong loss often means near-zero accuracy.

**Point 4: Memorize the windowed dataset function.** You cannot Google the implementation during the exam. Write it from memory three times this week until it is automatic.

**Point 5: Know how to use callbacks to hit target metrics.** Custom `Callback` subclass with `on_epoch_end` checking `logs.get('accuracy')` or `logs.get('val_accuracy')` is the standard pattern. Write it once cleanly and reuse.

Let me run through two rapid-fire practice problems verbally:

**Practice Problem A:** "Build a model to classify 10,000 customer reviews as positive or negative. Reviews are provided as raw text strings."

Your mental checklist: binary classification → `binary_crossentropy` → tokenize train only → pad to fixed length → `Embedding` → LSTM or GlobalAveragePooling1D → `Dense(1, sigmoid)`.

**Practice Problem B:** "Given a CSV of hourly temperature readings for one year, forecast the next temperature. Achieve MAE below 2.5."

Your mental checklist: time series → temporal split → normalize → `windowed_dataset` → Conv1D or LSTM → evaluate denormalized MAE → iterate window size or model depth if MAE is too high.

---

## SEGMENT 8 — Career Paths and Closing (22:30–24:00)

The TensorFlow Developer Certificate is a strong credential for entry-level and mid-level ML engineering roles. After earning it, the natural progression is:

- **ML Engineer**: Building and deploying models in production (Modules 14 content is directly relevant)
- **Data Scientist**: End-to-end analysis and model building (all modules)
- **Research Engineer**: Contributing to new model architectures (Module 15 background)
- **MLOps Engineer**: Infrastructure, monitoring, and pipeline automation (Module 14 TFX content)

Regardless of path, the certificate signals that you can write working TensorFlow code to solve real problems — which is exactly what employers want to see.

You have come a long way since Module 1. You now know how to build neural networks from scratch, train CNNs for computer vision, apply NLP techniques to text data, forecast time series, deploy models to production, and understand the frontier architectures powering modern AI.

Prepare well, sleep before the exam, and trust your preparation. Good luck. It has been a privilege to teach this course.

---

## End of Script

**Total estimated runtime:** 24 minutes

**Key code files referenced:** Review code from all prior labs

**TF Developer Certificate alignment:** All four categories — comprehensive exam review
