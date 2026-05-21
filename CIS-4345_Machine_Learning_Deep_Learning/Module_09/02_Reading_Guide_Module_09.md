# Reading Guide: Module 09 - Natural Language Processing with TensorFlow
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 09 - Natural Language Processing with TensorFlow**! Natural Language Processing (NLP) is one of the four core task categories on the TensorFlow Developer Certificate exam. Unlike images or numeric tables, text data must be converted into numbers before it can be fed into a neural network. This module covers the complete text preprocessing pipeline — tokenization, padding, and embedding — and how to combine these steps with LSTM or Dense layers to build sentiment analysis and text classification models.

You will learn to use `tf.keras.preprocessing.text.Tokenizer`, `pad_sequences`, and `tf.keras.layers.Embedding` to transform raw text into fixed-length integer sequences that models can learn from.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Tokenizer**: A Keras utility that builds a vocabulary from a corpus of text and converts sentences into sequences of integer token IDs. Key parameters: `num_words` limits the vocabulary to the top N most frequent words; `oov_token='<OOV>'` assigns a special ID to words not seen during `fit_on_texts()`. Usage: `tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>'); tokenizer.fit_on_texts(train_sentences); sequences = tokenizer.texts_to_sequences(train_sentences)`.

*   **`pad_sequences`**: A function that converts a list of variable-length integer sequences into a 2D numpy array of uniform length by adding zeros (or truncating). `padding='post'` adds zeros at the end; `padding='pre'` (default) adds zeros at the beginning. `truncating='post'` removes tokens from the end of sequences that exceed `maxlen`. Usage: `padded = pad_sequences(sequences, maxlen=200, padding='post', truncating='post')`.

*   **Word embedding**: A dense vector representation of a word that captures semantic relationships — words with similar meanings have similar vectors. Unlike one-hot encoding (which is sparse and has no semantic structure), embeddings are learned during training. The `tf.keras.layers.Embedding(input_dim, output_dim, input_length)` layer learns these vectors automatically.

*   **`word_index`**: A dictionary attribute of the Keras Tokenizer that maps each word string to its integer token ID, e.g., `{'the': 1, 'cat': 2, ...}`. The `<OOV>` token is typically assigned ID 1 when `oov_token` is set. `len(tokenizer.word_index)` gives the full vocabulary size including all words seen during training.

*   **Sequence classification**: An NLP task where the model takes a fixed-length integer sequence (a padded tokenized sentence) as input and outputs a class label or probability. For binary sentiment analysis (positive/negative), the output layer is `Dense(1, activation='sigmoid')` with `loss='binary_crossentropy'`. For multi-class text classification, the output is `Dense(num_classes, activation='softmax')` with `loss='sparse_categorical_crossentropy'`.

*   **`TextVectorization` layer**: A Keras preprocessing layer (TF 2.x) that integrates tokenization and vocabulary building directly into the model graph. Unlike the standalone `Tokenizer`, `TextVectorization` can be included as the first model layer, enabling the full text-to-prediction pipeline to be exported and deployed as a single SavedModel artifact.

---

### 2. Certification Exam Tips
*   **Full NLP Pipeline:** The TF exam NLP pattern is: `Tokenizer.fit_on_texts(train)` → `texts_to_sequences()` → `pad_sequences(maxlen, padding='post')` → `Embedding(vocab_size, embed_dim, input_length) → LSTM/Dense → output`. Know each step and its role.
*   **vocab_size off-by-one:** When creating the Embedding layer, use `vocab_size = len(tokenizer.word_index) + 1` (not `len(word_index)`) because token IDs start at 1, not 0, so index 0 is reserved for padding.
*   **OOV token matters:** Always set `oov_token='<OOV>'` so that test sentences with unseen words receive a defined token ID rather than being silently dropped. Dropped tokens change sequence lengths and cause shape mismatches.
*   **Study Resource:** The [TensorFlow NLP with TensorFlow tutorial](https://www.tensorflow.org/tutorials/text/word_embeddings) at tensorflow.org covers word embeddings and sequence models with the exact Keras API used on the exam. The free [Natural Language Processing with TensorFlow course on Coursera](https://www.coursera.org/learn/natural-language-processing-tensorflow) by Laurence Moroney (a Google engineer who helped design the TF exam) is one of the most exam-aligned NLP resources available.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Work through the [TensorFlow word embeddings tutorial](https://www.tensorflow.org/tutorials/text/word_embeddings) and the [text classification tutorial](https://www.tensorflow.org/tutorials/keras/text_classification) at tensorflow.org. These free official tutorials cover Tokenizer, pad_sequences, Embedding layers, and sequence classification — all directly tested on the exam.
*   **Required Video:** Watch the NLP lecture in the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This covers tokenization, vocabulary building, padding, and building LSTM-based text classifiers with `tf.keras`.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Tokenize and pad a text dataset**: Create a `Tokenizer(num_words=10000, oov_token='<OOV>')`, call `fit_on_texts(train_sentences)`, convert to sequences with `texts_to_sequences()`, and pad with `pad_sequences(maxlen=200, padding='post')`.
*   **Build an NLP classification model**: Define `Sequential([Embedding(vocab_size+1, 64, input_length=200), LSTM(64), Dense(1, activation='sigmoid')])` and compile with `binary_crossentropy`.
*   **Visualize embeddings**: After training, extract the embedding weight matrix with `model.layers[0].get_weights()[0]` and use the [TensorFlow Embedding Projector](https://projector.tensorflow.org/) to visualize word clusters in 2D or 3D space.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and write the full NLP preprocessing pipeline from memory (Tokenizer → pad_sequences → Embedding).
*   [ ] Work through the [TensorFlow word embeddings tutorial](https://www.tensorflow.org/tutorials/text/word_embeddings) and [text classification tutorial](https://www.tensorflow.org/tutorials/keras/text_classification).
*   [ ] Watch the NLP lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 09 lab: tokenize, pad, embed, and classify text with an LSTM.
*   [ ] Proceed to the Module 09 quiz.
