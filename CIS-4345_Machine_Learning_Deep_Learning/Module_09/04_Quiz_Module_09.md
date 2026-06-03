# Quiz: Module 09 — Natural Language Processing with TensorFlow

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

### Question 1

What is the purpose of calling `tokenizer.fit_on_texts(train_sentences)` before `tokenizer.texts_to_sequences(test_sentences)`?

- A) It trains the neural network weights on the training sentences so the model can classify the test sentences immediately.
- B) It builds the vocabulary index from the training text, assigning integer IDs to words, so the same mapping can be applied consistently to both training and test sentences.
- C) It automatically pads all sentences in the training set to the same length so they can be fed into the model as a uniform batch.
- D) It applies data augmentation to the training sentences by randomly shuffling word order to prevent the model from memorizing sentence structure.

**Correct Answer:** B) `fit_on_texts()` scans the training corpus and builds `tokenizer.word_index` — a dictionary mapping each word to a unique integer. This vocabulary is then fixed and applied to test sentences via `texts_to_sequences()`, ensuring consistent encoding. The tokenizer must never be re-fit on test data.

**Distractor Analysis:**

- *Why A is incorrect:* `fit_on_texts()` is a text preprocessing step — it builds a vocabulary mapping, not a trained neural network. Model training happens in `model.fit()`, which is called separately.
- *Why B is correct:* The vocabulary is built only from training data so that no test data information leaks into the preprocessing step. Words in test sentences that were not seen during `fit_on_texts()` receive the `<OOV>` token.
- *Why C is incorrect:* Padding is a separate step performed by `pad_sequences()`. `fit_on_texts()` does not modify sequence lengths.
- *Why D is incorrect:* `fit_on_texts()` performs no augmentation — it only counts word frequencies and assigns integer IDs.

---

### Question 2

Which of the following is the most accurate definition of a word embedding in NLP?

- A) A sparse binary vector of length equal to the vocabulary size, where only the index corresponding to the current word is set to 1 and all other indices are 0.
- B) A dense, continuous vector representation of a word that is learned during training, positioning semantically similar words near each other in the embedding space.
- C) A preprocessing function that removes punctuation, converts text to lowercase, and splits sentences into individual word tokens before integer encoding.
- D) A fixed mathematical transformation that converts each character in a word to its ASCII integer value and concatenates them into a vector.

**Correct Answer:** B) Unlike one-hot encoding (option A), embeddings are low-dimensional dense vectors (e.g., 64 or 128 dimensions) whose values are learned via backpropagation. Words that appear in similar contexts end up with similar vectors, capturing semantic relationships.

**Distractor Analysis:**

- *Why A is incorrect:* This describes one-hot encoding, which is sparse, high-dimensional, and captures no semantic relationships between words. Embeddings are the dense, learned alternative.
- *Why B is correct:* In Keras: `tf.keras.layers.Embedding(input_dim=vocab_size+1, output_dim=64, input_length=200)`. The layer is trainable by default — its weights are the embedding vectors, updated during `model.fit()`.
- *Why C is incorrect:* This describes text preprocessing/tokenization steps (cleaning and splitting), which happen before embedding. Preprocessing and embedding are distinct pipeline stages.
- *Why D is incorrect:* ASCII character encoding is not a word embedding. It encodes individual characters by code point, not word meanings, and captures no semantic information.

---

### Question 3

A developer builds a text classifier on movie reviews. Which code correctly implements the full tokenization and padding pipeline?

- A) `tok = Tokenizer(num_words=10000, oov_token='<OOV>'); tok.fit_on_texts(train_texts); seqs = tok.texts_to_sequences(train_texts); padded = pad_sequences(seqs, maxlen=200, padding='post')`
- B) `tok = Tokenizer(num_words=10000); tok.fit_on_texts(train_texts + test_texts); seqs = tok.texts_to_sequences(train_texts); padded = pad_sequences(seqs, maxlen=200)`
- C) `tok = Tokenizer(num_words=10000, oov_token='<OOV>'); seqs = tok.texts_to_sequences(train_texts); tok.fit_on_texts(train_texts); padded = pad_sequences(seqs, maxlen=200)`
- D) `padded = pad_sequences(train_texts, maxlen=200, padding='post')`

**Correct Answer:** A) This correctly follows the required order: create Tokenizer with OOV token, fit vocabulary only on training data, convert to sequences, then pad. Setting `oov_token='<OOV>'` ensures unseen test words receive a defined token rather than being silently dropped.

**Distractor Analysis:**

- *Why A is correct:* This is the canonical TF exam preprocessing pipeline. The same tokenizer is then applied to test data: `test_seqs = tok.texts_to_sequences(test_texts); test_padded = pad_sequences(test_seqs, maxlen=200, padding='post')`.
- *Why B is incorrect:* Calling `fit_on_texts(train_texts + test_texts)` is data leakage — the vocabulary is built using test data, which would not be available at inference time.
- *Why C is incorrect:* `texts_to_sequences()` is called before `fit_on_texts()`, so the vocabulary does not exist yet. This returns empty sequences.
- *Why D is incorrect:* `pad_sequences` expects integer sequences, not raw text strings. Text must first be converted to integer token IDs.

---

### Question 4

When creating a Keras `Embedding` layer for a tokenizer with `len(tokenizer.word_index) == 10000`, what should `input_dim` be set to?

- A) `10000` — matching exactly the number of unique words in the vocabulary.
- B) `10001` — because token IDs start at 1 (not 0), so index 0 is reserved for padding and must be included in the embedding matrix.
- C) `200` — matching the `maxlen` parameter used in `pad_sequences` to align the embedding with the sequence length.
- D) `64` — matching the `output_dim` (embedding vector size) to keep the embedding matrix square.

**Correct Answer:** B) Keras token IDs are 1-indexed: the most frequent word gets ID 1, the second most frequent gets ID 2, etc. Index 0 is used for padding. Therefore `input_dim` must be `vocab_size + 1 = 10001` to have a row for every possible index including 0.

**Distractor Analysis:**

- *Why A is incorrect:* Using `input_dim=10000` when tokens range from 0 to 10000 causes an index-out-of-bounds error at runtime, because there is no embedding vector for index 10000.
- *Why B is correct:* The correct usage is `Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=64, input_length=200)`. Forgetting the `+1` is a very common exam mistake.
- *Why C is incorrect:* `input_dim` is the vocabulary size. `maxlen` / sequence length is passed to `input_length`, a separate parameter.
- *Why D is incorrect:* `input_dim` and `output_dim` are independent. `input_dim` is the vocabulary size; `output_dim` is the dimensionality of each embedding vector.

---

### Question 5

A text classification model achieves 95% training accuracy but only 60% validation accuracy after 20 epochs. The training set has 5,000 reviews and the vocabulary size is 50,000 words. What is the most effective corrective action?

- A) Increase `maxlen` in `pad_sequences` from 200 to 500 so the model can read more context from each review.
- B) Reduce overfitting by lowering the vocabulary size (`num_words`), reducing embedding dimensions, adding Dropout layers, or gathering more training data.
- C) Switch from `padding='post'` to `padding='pre'` in `pad_sequences` to ensure the model sees word endings rather than zero-padded tails.
- D) Replace `binary_crossentropy` with `mean_squared_error` as the loss function to produce smoother gradients on text data.

**Correct Answer:** B) The large gap between training and validation accuracy is classic overfitting. With a 50,000-word vocabulary and only 5,000 training examples, the embedding layer has far more parameters than the training data can constrain. Reducing `num_words` to 10,000, adding `Dropout(0.5)`, or collecting more labeled reviews all help.

**Distractor Analysis:**

- *Why A is incorrect:* Increasing `maxlen` adds more input dimensions, which increases model capacity and would likely worsen overfitting.
- *Why B is correct:* A vocabulary of 50,000 words with a 64-dimensional embedding produces a 3.2 million parameter embedding matrix. With only 5,000 examples, the model memorizes training sequences. Constraining the vocabulary and adding `Dropout(0.3)` are the most effective quick fixes.
- *Why C is incorrect:* Padding direction has no meaningful impact on the overfitting problem.
- *Why D is incorrect:* `mean_squared_error` is a regression loss and is not appropriate for binary classification. Changing the loss function does not address overfitting.

---

### Question 6

What is the output shape of `tf.keras.layers.Embedding(10001, 64)` given an input of shape `(32, 200)`?

- A) `(32, 64)` — one embedding vector per sample in the batch.
- B) `(32, 200, 64)` — one 64-dimensional embedding vector per token position per sample.
- C) `(200, 64)` — one embedding vector per sequence position, independent of batch size.
- D) `(32, 200)` — the same shape as the input but cast to float32.

**Correct Answer:** B) The `Embedding` layer maps each integer ID to a vector, so for each of the `32` samples and each of the `200` sequence positions, it outputs a 64-dimensional vector. The result is a 3D tensor of shape `(batch_size, sequence_length, embedding_dim)`.

**Distractor Analysis:**

- *Why A is incorrect:* A shape of `(32, 64)` would mean one vector per sample, collapsing the sequence dimension. That would require a `GlobalAveragePooling1D` or similar aggregation step after the embedding.
- *Why B is correct:* The output is always 3D: `(batch, timesteps, features)`. This is why layers after `Embedding` must be able to accept 3D input — either `LSTM`, `GRU`, `GlobalAveragePooling1D`, or `Flatten`.
- *Why C is incorrect:* The batch dimension is always preserved. TensorFlow always processes inputs in batches, so the output includes the batch dimension as the first axis.
- *Why D is incorrect:* The `Embedding` layer transforms integer IDs into dense float vectors — it does not preserve the integer values or the original shape.

---

### Question 7

What is the key difference between `GlobalAveragePooling1D` and an `LSTM` layer when used after an `Embedding` layer?

- A) `GlobalAveragePooling1D` has trainable weights; `LSTM` does not. The pooling layer learns which positions are most important.
- B) `GlobalAveragePooling1D` averages all position embeddings into one vector, discarding word order; `LSTM` processes the sequence step-by-step and captures word order and dependencies.
- C) `GlobalAveragePooling1D` produces a 3D output tensor that can feed into another sequence layer; `LSTM` always produces a 2D output.
- D) `LSTM` is faster to train than `GlobalAveragePooling1D` because it uses matrix operations instead of sequential recurrence.

**Correct Answer:** B) `GlobalAveragePooling1D` computes the mean embedding vector across all 200 positions — producing a single 64-dimensional vector that captures word frequency but not order. `LSTM` processes the sequence token-by-token, maintaining a hidden state that encodes context and word order.

**Distractor Analysis:**

- *Why A is incorrect:* `GlobalAveragePooling1D` has no trainable weights — it performs a fixed average operation. The `LSTM` is the layer with trainable weights (input, forget, output, and cell gate weight matrices).
- *Why B is correct:* For tasks where word order matters (negation, sarcasm, complex syntax), LSTM outperforms bag-of-embeddings models. For simple topic classification or keyword-based sentiment, GAP1D is often competitive and much faster.
- *Why C is incorrect:* It is the opposite: `LSTM` (with `return_sequences=False`, the default) produces 2D output `(batch, units)`. `GlobalAveragePooling1D` also produces 2D output `(batch, embed_dim)`. Neither outputs 3D by default.
- *Why D is incorrect:* `GlobalAveragePooling1D` is far faster than `LSTM` because it is a simple mean operation with no recurrence or learnable parameters. LSTM training is significantly slower due to sequential computation.

---

### Question 8

A developer wants to build a model that accepts raw text strings and produces predictions without any external preprocessing. Which Keras approach enables this?

- A) Use `Tokenizer.fit_on_texts()` on the training data and save the tokenizer as a JSON file alongside the saved model.
- B) Embed a `TextVectorization` layer as the first layer inside the Keras model, call `adapt()` on training data, and save the model with `model.save()`.
- C) Convert all text to ASCII byte arrays before training and pass raw byte values to the `Embedding` layer directly.
- D) Use `tf.strings.split()` inside a `tf.py_function` wrapper in the `tf.data` pipeline and apply it at inference time.

**Correct Answer:** B) When `TextVectorization` is embedded as the first model layer, it becomes part of the computation graph that is saved with the model. The saved model accepts raw string tensors and applies tokenization, vocabulary lookup, and padding internally.

**Distractor Analysis:**

- *Why A is incorrect:* Saving the tokenizer as a separate JSON file means the consumer of the model must still implement and apply the tokenizer externally. This is error-prone, as mismatches between saved tokenizer and model version are common deployment bugs.
- *Why B is correct:* After `model.save('my_model')`, the inference caller only needs `loaded_model.predict(["raw string here"])` — no preprocessing knowledge required. This is the production-grade pattern.
- *Why C is incorrect:* Raw byte values have no semantic relationship to word meaning. This approach would produce meaningless embeddings because the vocabulary is character codes, not words.
- *Why D is incorrect:* `tf.py_function` wrappers run in Python eager mode and cannot be serialized into the TensorFlow SavedModel graph. They also add complexity and are not a deployable pattern for production models.

---

### Question 9

Which output activation and loss function should be used for multi-class text classification with 5 categories (mutually exclusive)?

- A) `activation='sigmoid'`, `loss='binary_crossentropy'`
- B) `activation='softmax'`, `loss='sparse_categorical_crossentropy'` (when labels are integers)
- C) `activation='relu'`, `loss='mean_squared_error'`
- D) `activation='tanh'`, `loss='categorical_hinge'`

**Correct Answer:** B) For mutually exclusive multi-class classification, `softmax` normalizes the output to a probability distribution over 5 classes. `sparse_categorical_crossentropy` expects integer labels (0–4) directly. If labels are one-hot encoded, use `categorical_crossentropy` instead.

**Distractor Analysis:**

- *Why A is incorrect:* `sigmoid` and `binary_crossentropy` are for binary classification (2 classes). For 5 mutually exclusive classes, `softmax` must be used so the outputs sum to 1 and represent a proper probability distribution.
- *Why B is correct:* The output layer would be `Dense(5, activation='softmax')`. If labels are integers 0–4, compile with `loss='sparse_categorical_crossentropy'`. If labels are one-hot vectors, use `loss='categorical_crossentropy'`.
- *Why C is incorrect:* `relu` can produce values outside [0, 1] and does not normalize across classes. `mean_squared_error` is a regression loss and is inappropriate for classification tasks.
- *Why D is incorrect:* `tanh` maps to [-1, 1] and does not produce class probabilities. `categorical_hinge` is a margin-based loss used in specific SVM-style multi-class settings, not standard text classification.

---

### Question 10

When should `mask_zero=True` be set in the `Embedding` layer?

- A) When using `TextVectorization` instead of `Tokenizer`, because `TextVectorization` uses index 0 differently.
- B) When the sequences contain padding (zeros) and downstream layers such as `LSTM` or `GRU` should ignore those padded positions.
- C) When the vocabulary size exceeds 10,000 words and the embedding matrix would otherwise be too large.
- D) When `output_mode='binary'` is used in `TextVectorization` to ensure binary outputs are masked correctly.

**Correct Answer:** B) When sequences are padded with zeros, the embedding layer receives index 0 for padding positions. Setting `mask_zero=True` generates a boolean mask that marks index 0 positions as "do not compute" — `LSTM` and `GRU` layers automatically skip these positions, preventing padding tokens from contaminating the hidden state.

**Distractor Analysis:**

- *Why A is incorrect:* `mask_zero=True` behavior is identical regardless of whether `Tokenizer` or `TextVectorization` was used. The key condition is whether zeros in the sequence represent padding — not which preprocessing API was used.
- *Why B is correct:* Without `mask_zero=True`, an LSTM processes all 200 positions including zero-padded ones, treating the zeros as vocabulary index 0. This introduces noise from padding into the sequence representation, particularly for short reviews padded extensively.
- *Why C is incorrect:* `mask_zero=True` has no effect on vocabulary size or embedding matrix dimensions. Those are controlled by `input_dim` and `output_dim`.
- *Why D is incorrect:* `output_mode='binary'` in `TextVectorization` produces a multi-hot vector, not integer sequences. `mask_zero=True` is irrelevant in that output mode since an `Embedding` layer would not be used.

---

Texas Wesleyan University — CIS-4345 Machine Learning and Deep Learning

Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.
