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

---

### Question 11 (5 points)

What does the `oov_token='<OOV>'` parameter in `tf.keras.preprocessing.text.Tokenizer` do?

- A) It removes out-of-vocabulary words from the training sentences entirely so they do not corrupt the model.
- B) It reserves a special integer token for words encountered at test time that were not in the training vocabulary.
- C) It limits the vocabulary to only words that appear at least twice, treating all rare words as out-of-vocabulary.
- D) It tells the tokenizer to skip punctuation and special characters that do not belong in the vocabulary.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* When a word in a test sentence was not seen during `fit_on_texts()`, Keras assigns it the `<OOV>` token's integer ID (typically 1, since the OOV token is added first). Without this setting, unknown words are silently dropped, which can cause significant information loss for long or technical documents where many words are out-of-vocabulary.
  - *Why A is incorrect:* The OOV token does not remove words — it replaces them with a fixed integer ID. Removing unknown words entirely is the behavior when `oov_token` is NOT set.
  - *Why C is incorrect:* Minimum frequency filtering is controlled by a separate mechanism (not a built-in `Tokenizer` argument). The `oov_token` setting is purely about how to handle words absent from the trained vocabulary.
  - *Why D is incorrect:* Punctuation filtering is handled separately (e.g., using `filters=` in the Tokenizer constructor). The OOV token is specifically for handling vocabulary mismatches between training and test sets.

---

### Question 12 (5 points)

A developer uses `pad_sequences(sequences, maxlen=200, padding='pre', truncating='pre')`. What do `padding='pre'` and `truncating='pre'` do?

- A) `padding='pre'` adds zeros at the end; `truncating='pre'` removes tokens from the end of long sequences.
- B) `padding='pre'` adds zeros at the beginning; `truncating='pre'` removes tokens from the beginning of sequences that exceed `maxlen`.
- C) `padding='pre'` adds zeros at the beginning; `truncating='pre'` removes the entire sequence if it exceeds `maxlen`.
- D) Both settings are equivalent to `padding='post'` and `truncating='post'` — the prefix is only applied during validation.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `padding='pre'` places the zero tokens before the actual word tokens, so the words appear at the end of the padded sequence. `truncating='pre'` removes tokens from the start of sequences longer than `maxlen`, preserving the end of the sequence (where the "punchline" or conclusion often appears in reviews). This is preferred for LSTM models because the most recent tokens (at the sequence end) feed directly into the final hidden state.
  - *Why A is incorrect:* This describes `padding='post'` and `truncating='post'`. The `pre` prefix specifically places zeros/truncation at the beginning, not the end.
  - *Why C is incorrect:* `truncating='pre'` removes individual tokens from the beginning, not the entire sequence. Sequences longer than `maxlen` are trimmed to exactly `maxlen` tokens.
  - *Why D is incorrect:* `pre` and `post` are distinct settings with opposite behavior. They are applied identically during both training and validation — there is no mode distinction.

---

### Question 13 (5 points)

What does `Bidirectional(LSTM(64))` do compared to a standard `LSTM(64)` layer?

- A) It doubles the LSTM's memory by stacking two LSTM layers with 64 units each in sequence.
- B) It processes the sequence in both forward and backward directions and concatenates the two hidden states, producing a 128-dimensional output.
- C) It applies the LSTM twice to the same sequence (forward only) and averages the two outputs for more stable training.
- D) It is an alias for `LSTM(64, return_sequences=True)` that returns the full sequence for use in the next layer.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A `Bidirectional` wrapper creates two LSTM instances: one processes the sequence left-to-right, the other right-to-left. Their final hidden states are concatenated by default (merge mode `'concat'`), producing a `2 * 64 = 128`-dimensional output vector. This allows the model to capture context from both directions — useful for sentiment, where a word's meaning can depend on what follows it.
  - *Why A is incorrect:* Stacking two sequential LSTM layers uses `return_sequences=True` on the first layer. A `Bidirectional` wrapper does not stack layers in sequence — it runs two LSTMs in parallel on the same input.
  - *Why C is incorrect:* The forward and backward LSTMs receive the sequence in opposite orders (reversed), not the same order twice. The merge mode (default: concatenate) combines their outputs, not by averaging.
  - *Why D is incorrect:* `return_sequences=True` is a separate parameter. `Bidirectional(LSTM(64))` with the default `return_sequences=False` still produces a single vector, not a sequence. The output dimension is doubled (128), not the temporal dimension.

---

### Question 14 (5 points)

A developer trains a sentiment classifier on 25,000 IMDB reviews. The model uses an `Embedding(10001, 64)` layer followed by `GlobalAveragePooling1D()` and `Dense(1, activation='sigmoid')`. How many trainable parameters does the embedding layer contribute?

- A) 64
- B) 640,000
- C) 640,064
- D) 200 × 64 = 12,800

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* The `Embedding(10001, 64)` layer creates a matrix of shape `(10001, 64)` — one 64-dimensional vector for each of the 10,001 vocabulary entries (10,000 words + 1 padding index). Total parameters: `10001 * 64 = 640,064`. These are all trainable by default and updated via backpropagation during `model.fit()`.
  - *Why A is incorrect:* 64 is the embedding dimension per word, not the total number of parameters. The full embedding matrix multiplies this by the vocabulary size.
  - *Why B is incorrect:* 640,000 ignores the `+1` for the padding/OOV index. The correct `input_dim` is 10,001 (not 10,000), so the matrix has 10,001 rows, giving `10001 * 64 = 640,064`.
  - *Why D is incorrect:* `200` is the sequence length (`maxlen`), not the vocabulary size. The embedding matrix's row count equals the vocabulary size, not the sequence length. Sequence length determines how many times the embedding matrix is accessed per sample, not its size.

---

### Question 15 (5 points)

Which of the following correctly defines the `TextVectorization` layer and calls `adapt()` properly?

- A) `tv = TextVectorization(max_tokens=10000, output_sequence_length=200); tv.adapt(train_texts + test_texts)`
- B) `tv = TextVectorization(max_tokens=10000, output_sequence_length=200); tv.adapt(train_texts)`
- C) `tv = TextVectorization(max_tokens=10000); tv.fit(train_texts, epochs=5)`
- D) `tv = TextVectorization(output_sequence_length=200); tv.adapt(x_train, y_train)`

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `TextVectorization` is created with the vocabulary limit and output length, then `adapt()` is called on training text only. `adapt()` scans the training corpus to build the vocabulary, equivalent to `Tokenizer.fit_on_texts()`. Passing test data to `adapt()` constitutes data leakage.
  - *Why A is incorrect:* Calling `adapt(train_texts + test_texts)` leaks test vocabulary into the model's preprocessing step. If the model is later deployed to production, this means production vocabulary will have inflated the training-time vocabulary in a way that cannot be replicated.
  - *Why C is incorrect:* `TextVectorization` does not have a `fit()` method. The correct method is `adapt()`. Also, `adapt()` is called once on the full training set, not for multiple epochs.
  - *Why D is incorrect:* `adapt()` accepts only text data (not labels). Passing `y_train` as a second argument would raise a TypeError or be silently ignored depending on the TensorFlow version.

---

### Question 16 (5 points)

After training an NLP model, a developer runs `model.predict(["This film was absolutely fantastic!"])`. What must be true for this to work without any external preprocessing?

- A) The developer must manually call `tokenizer.texts_to_sequences()` on the input string before calling `model.predict()`.
- B) A `TextVectorization` layer must be the first layer inside the model, having been previously `adapt()`-ed on the training vocabulary.
- C) The model must use `output_mode='binary'` in its `TextVectorization` layer so raw strings can be accepted.
- D) The raw string must be wrapped in a `tf.constant()` call to convert it to a TensorFlow string tensor before prediction.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* When `TextVectorization` is embedded as the first model layer, the model's input signature accepts raw Python strings or `tf.string` tensors. Keras automatically converts the Python string list to the appropriate tensor type. The vectorization layer handles tokenization and padding internally, making the model fully self-contained.
  - *Why A is incorrect:* External tokenization is needed only when using the legacy `Tokenizer` API with a separate preprocessing step. When `TextVectorization` is inside the model, no external preprocessing is required — that is the entire point of the pattern.
  - *Why C is incorrect:* `output_mode='binary'` produces a multi-hot vocabulary bag representation, not an integer sequence. It does not affect whether the model accepts raw strings. The string-acceptance behavior comes from having `TextVectorization` as the first layer, regardless of output mode.
  - *Why D is incorrect:* Keras's `model.predict()` automatically converts Python lists and strings to tensors internally. Manually wrapping in `tf.constant()` is not required and does not change the behavior.

---

### Question 17 (5 points)

What is the effect of setting `return_sequences=True` in an LSTM layer that is NOT the last LSTM in a stacked architecture?

- A) It makes the LSTM output the hidden state for every time step, producing a 3D output of shape `(batch, timesteps, units)` that the next LSTM layer can process.
- B) It repeats the final hidden state across all time steps, producing a 3D output of shape `(batch, timesteps, units)` for visualization purposes.
- C) It forces the LSTM to process the sequence in reverse order, returning the sequence from last token to first.
- D) It has no effect on output shape — `return_sequences` only affects which loss function is used during training.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* By default, `LSTM` returns only the final hidden state — shape `(batch, units)`. With `return_sequences=True`, it returns the hidden state at every time step — shape `(batch, timesteps, units)`. This 3D output is required as input to a subsequent LSTM layer, which expects a sequence, not a single vector. Forgetting `return_sequences=True` on all but the last stacked LSTM is a common error.
  - *Why B is incorrect:* The output is the actual computed hidden state at each time step, not a repetition of the final state. Each time step produces a different hidden state that reflects the sequence processed so far up to that point.
  - *Why C is incorrect:* Reversing the sequence is the function of the `go_backwards=True` parameter, not `return_sequences`. `return_sequences` only controls whether the full sequence of hidden states or just the last one is returned.
  - *Why D is incorrect:* `return_sequences=True` directly changes the output tensor's shape from 2D to 3D. This has significant architectural consequences — the next layer must accept 3D input. It has no effect on the loss function.

---

### Question 18 (5 points)

A developer evaluates three NLP architectures on the IMDB dataset: (1) Embedding + GlobalAveragePooling1D, (2) Embedding + LSTM(64), (3) Embedding + Bidirectional(LSTM(64)). Listed from fastest to slowest training time, what is the expected order?

- A) Bidirectional LSTM → LSTM → GlobalAveragePooling1D
- B) GlobalAveragePooling1D → LSTM → Bidirectional LSTM
- C) LSTM → GlobalAveragePooling1D → Bidirectional LSTM
- D) All three train at approximately the same speed because the bottleneck is always the Embedding layer.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `GlobalAveragePooling1D` has no trainable parameters and performs a simple mean — it is nearly instant. A single `LSTM(64)` processes the sequence recurrently with 64 hidden units, which is computationally significant but manageable. `Bidirectional(LSTM(64))` runs two LSTM instances (forward + backward), roughly doubling the LSTM computation. Training time scales as: GAP1D << LSTM << BiLSTM.
  - *Why A is incorrect:* This is the reverse of the correct order. Bidirectional LSTM is the slowest because it has twice the recurrent computation of a single LSTM.
  - *Why C is incorrect:* LSTM is slower than GlobalAveragePooling1D, not faster. GAP1D is a parameter-free mean operation while LSTM involves sequential matrix multiplications through gated recurrent cells.
  - *Why D is incorrect:* The Embedding layer's forward pass is a simple lookup operation — very fast. The computational bottleneck for recurrent models is the sequential LSTM computation, which cannot be parallelized over the time dimension.

---

### Question 19 (5 points)

In a text classification model, the embedding layer is initialized with `trainable=False` and pre-trained GloVe vectors. What does `trainable=False` mean in this context?

- A) The embedding layer is excluded from the model graph and does not participate in the forward pass.
- B) The GloVe weight matrix is frozen — the embedding vectors are used as fixed features and are not updated by backpropagation.
- C) The embedding layer outputs zeros during training to prevent the pre-trained weights from interfering with the new model layers.
- D) The embedding layer is only updated every 10 epochs to slow down the fine-tuning of the pre-trained weights.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Setting `trainable=False` on a Keras layer freezes its weights — they are excluded from the gradient computation and not updated during `model.fit()`. For pre-trained embeddings (GloVe, Word2Vec, FastText), this is commonly done when the pre-trained vectors are high quality and the task dataset is small. The embeddings still participate in the forward pass but their values remain constant.
  - *Why A is incorrect:* `trainable=False` does not remove the layer from the computation graph. The forward pass still flows through the embedding layer — it produces outputs normally. Only the backward pass (weight update) is blocked.
  - *Why C is incorrect:* A frozen layer still computes its normal output — it does not produce zeros. Zeroing outputs would destroy all semantic information encoded in the embeddings.
  - *Why D is incorrect:* There is no built-in mechanism that updates frozen layers on a schedule. A layer is either trainable or not throughout training, unless `layer.trainable` is explicitly toggled between calls to `model.compile()`.

---

### Question 20 (5 points)

A text classification model achieves 88% test accuracy on IMDB sentiment analysis. To squeeze out additional accuracy without retraining, a developer applies test-time averaging over 5 slightly different padded versions of each review. Why might this help for NLP models?

- A) Averaging predictions across multiple tokenizations reduces vocabulary mismatch errors caused by `<OOV>` tokens.
- B) Different `padding='pre'` and `padding='post'` configurations, or slight random dropout during inference, produce diverse prediction distributions whose average is more reliable than any single prediction.
- C) Averaging five predictions forces the model to produce a probability of exactly 0.5, providing a conservative baseline.
- D) Padding configuration has no effect on LSTM predictions because LSTMs always produce the same output for the same sequence of non-padding tokens.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* This is test-time augmentation (TTA) applied to NLP. Different padding placements change which hidden states the LSTM computes at each step (padding position affects when meaningful tokens are presented). Enabling `Dropout` during inference (via `model(x, training=True)`) creates stochastic predictions that, when averaged, reduce prediction variance. Both strategies are valid TTA approaches for sequence models.
  - *Why A is incorrect:* Different padding configurations do not change which words map to `<OOV>` — that is entirely determined by the tokenizer's vocabulary. TTA via padding variation does not address vocabulary coverage.
  - *Why C is incorrect:* Averaging diverse predictions does not force a result of 0.5. If all 5 predictions for a clearly positive review are above 0.8, their average is also above 0.8. Averaging reduces variance; it does not collapse predictions to a central value.
  - *Why D is incorrect:* LSTM output does depend on padding position. With `padding='pre'`, the LSTM processes zeros first and then meaningful tokens, with the final hidden state seeing the most recent tokens. With `padding='post'`, it processes meaningful tokens first and then zeros. These produce different final hidden states and different predictions.
