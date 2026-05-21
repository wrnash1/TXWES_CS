# Quiz: Module 09 - Natural Language Processing with TensorFlow
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What is the purpose of calling `tokenizer.fit_on_texts(train_sentences)` before `tokenizer.texts_to_sequences(test_sentences)`?
*   A) It trains the neural network weights on the training sentences so the model can classify the test sentences immediately.
*   B) It builds the vocabulary index from the training text, assigning integer IDs to words, so the same mapping can be applied consistently when converting both training and test sentences to sequences.
*   C) It automatically pads all sentences in the training set to the same length so they can be fed into the model as a uniform batch.
*   D) It applies data augmentation to the training sentences by randomly shuffling word order to prevent the model from memorizing sentence structure.
*   **Correct Answer:** B) `fit_on_texts()` scans the training corpus and builds `tokenizer.word_index` — a dictionary mapping each word to a unique integer. This vocabulary is then fixed and applied to test sentences via `texts_to_sequences()`, ensuring consistent encoding. The tokenizer must never be re-fit on test data.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `fit_on_texts()` is a text preprocessing step — it builds a vocabulary mapping, not a trained neural network. Model training happens in `model.fit()`, which is called separately.
    *   *Why B is correct:* The vocabulary is built only from training data so that no test data information leaks into the preprocessing step. Words in test sentences that were not seen during `fit_on_texts()` receive the `<OOV>` (out-of-vocabulary) token.
    *   *Why C is incorrect:* Padding is a separate step performed by `pad_sequences()`. `fit_on_texts()` does not modify sequence lengths.
    *   *Why D is incorrect:* `fit_on_texts()` performs no augmentation — it only counts word frequencies and assigns integer IDs.

---

**Question 2**
Which of the following is the most accurate definition of a **word embedding** in NLP?
*   A) A sparse binary vector of length equal to the vocabulary size, where only the index corresponding to the current word is set to 1 and all other indices are 0.
*   B) A dense, continuous vector representation of a word that is learned during training, positioning semantically similar words near each other in the embedding space.
*   C) A preprocessing function that removes punctuation, converts text to lowercase, and splits sentences into individual word tokens before integer encoding.
*   D) A fixed mathematical transformation that converts each character in a word to its ASCII integer value and concatenates them into a vector.
*   **Correct Answer:** B) Unlike one-hot encoding (option A), embeddings are low-dimensional dense vectors (e.g., 64 or 128 dimensions) whose values are learned via backpropagation. Words that appear in similar contexts end up with similar vectors, capturing semantic relationships like "king" - "man" + "woman" ≈ "queen".
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes one-hot encoding, which is sparse, high-dimensional, and captures no semantic relationships between words. Embeddings are the dense, learned alternative to one-hot encoding.
    *   *Why B is correct:* In Keras: `tf.keras.layers.Embedding(input_dim=vocab_size+1, output_dim=64, input_length=200)`. The layer is trainable by default — its weights are the embedding vectors, updated during `model.fit()`.
    *   *Why C is incorrect:* This describes text preprocessing / tokenization steps (cleaning and splitting), which happen before embedding. Preprocessing and embedding are distinct pipeline stages.
    *   *Why D is incorrect:* ASCII character encoding is not a word embedding — it encodes individual characters by code point, not word meanings. It captures no semantic or contextual information about words.

---

**Question 3**
A developer builds a text classifier on movie reviews. Which code correctly implements the full tokenization and padding pipeline before model training?
*   A) `tok = Tokenizer(num_words=10000, oov_token='<OOV>'); tok.fit_on_texts(train_texts); seqs = tok.texts_to_sequences(train_texts); padded = pad_sequences(seqs, maxlen=200, padding='post')`
*   B) `tok = Tokenizer(num_words=10000); tok.fit_on_texts(train_texts + test_texts); seqs = tok.texts_to_sequences(train_texts); padded = pad_sequences(seqs, maxlen=200)`
*   C) `tok = Tokenizer(num_words=10000, oov_token='<OOV>'); seqs = tok.texts_to_sequences(train_texts); tok.fit_on_texts(train_texts); padded = pad_sequences(seqs, maxlen=200)`
*   D) `padded = pad_sequences(train_texts, maxlen=200, padding='post')`
*   **Correct Answer:** A) This correctly follows the required order: create Tokenizer with OOV token, fit vocabulary only on training data, convert to sequences, then pad. Setting `oov_token='<OOV>'` ensures unseen test words receive a defined token rather than being silently dropped.
*   **Distractor Analysis:**
    *   *Why A is correct:* This is the canonical TF exam preprocessing pipeline. The same tokenizer is then applied to test data: `test_seqs = tok.texts_to_sequences(test_texts); test_padded = pad_sequences(test_seqs, maxlen=200, padding='post')`.
    *   *Why B is incorrect:* Calling `fit_on_texts(train_texts + test_texts)` is data leakage — the vocabulary is built using test data, which would not be available at inference time. The tokenizer should only be fit on training data.
    *   *Why C is incorrect:* `texts_to_sequences()` is called before `fit_on_texts()`, so the vocabulary does not exist yet. Calling `texts_to_sequences` on an unfitted tokenizer returns empty sequences.
    *   *Why D is incorrect:* `pad_sequences` expects integer sequences, not raw text strings. Raw text strings must first be converted to integer token IDs via `fit_on_texts()` and `texts_to_sequences()`.

---

**Question 4**
When creating a Keras `Embedding` layer for a tokenizer with `len(tokenizer.word_index) == 10000`, what should `input_dim` be set to?
*   A) `10000` — matching exactly the number of unique words in the vocabulary.
*   B) `10001` — because token IDs start at 1 (not 0), so index 0 is reserved for padding and must be included in the embedding matrix dimensions.
*   C) `200` — matching the `maxlen` parameter used in `pad_sequences` to align the embedding with the sequence length.
*   D) `64` — matching the `output_dim` (embedding vector size) to keep the embedding matrix square.
*   **Correct Answer:** B) Keras token IDs are 1-indexed: the most frequent word gets ID 1, the second most frequent gets ID 2, etc. Index 0 is used for padding. Therefore, `input_dim` must be `vocab_size + 1 = 10001` to have a row for every possible index including 0.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Using `input_dim=10000` when tokens range from 0 to 10000 causes an index-out-of-bounds error at runtime, because there is no embedding vector for index 10000.
    *   *Why B is correct:* The correct usage is `Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=64, input_length=200)`. This is a common exam trap — forgetting the `+1` causes training failures with lookup errors.
    *   *Why C is incorrect:* `input_dim` is the vocabulary size (number of unique token IDs). `maxlen` / sequence length is passed to `input_length`, a separate parameter.
    *   *Why D is incorrect:* `input_dim` and `output_dim` serve completely different purposes and are independent. `input_dim` is the vocabulary size; `output_dim` is the dimensionality of each embedding vector.

---

**Question 5**
A text classification model achieves 95% training accuracy but only 60% validation accuracy after 20 epochs. The training set has 5,000 reviews and the vocabulary size is 50,000 words. What is the most effective corrective action?
*   A) Increase `maxlen` in `pad_sequences` from 200 to 500 so the model can read more context from each review.
*   B) Reduce overfitting by lowering the vocabulary size (`num_words`), reducing embedding dimensions, adding Dropout layers, or gathering more training data.
*   C) Switch from `padding='post'` to `padding='pre'` in `pad_sequences` to ensure the model sees word endings rather than zero-padded tails.
*   D) Replace `binary_crossentropy` with `mean_squared_error` as the loss function to produce smoother gradients on text data.
*   **Correct Answer:** B) The large gap between training and validation accuracy is classic overfitting. With a 50,000-word vocabulary and only 5,000 training examples, the embedding layer has far more parameters than the training data can constrain. Reducing `num_words` to 10,000, lowering `output_dim`, adding `Dropout(0.5)` after the LSTM, or collecting more labeled reviews all help close the generalization gap.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Increasing `maxlen` adds more input dimensions, which increases model capacity and would likely worsen overfitting, not reduce it. The problem is too much model capacity relative to training data size.
    *   *Why B is correct:* A vocabulary of 50,000 words with a 64-dimensional embedding produces a 3.2 million parameter embedding matrix. With only 5,000 examples, the model memorizes training sequences. Constraining the vocabulary to the top 10,000 words and adding `Dropout(0.3)` are the most effective quick fixes.
    *   *Why C is incorrect:* Padding direction (`pre` vs `post`) affects where zeros appear in sequences and has no meaningful impact on the overfitting problem. Either padding direction can be used correctly.
    *   *Why D is incorrect:* `mean_squared_error` is a regression loss — it is not appropriate for binary classification. `binary_crossentropy` is correct for this task. Changing the loss function does not address overfitting.
