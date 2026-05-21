# Reading Guide: Module 08 - Recurrent Neural Networks (RNNs) and LSTMs
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 08 - Recurrent Neural Networks (RNNs) and LSTMs**! While CNNs excel at spatial data like images, Recurrent Neural Networks are designed for sequential data — text, time series, speech, and any domain where the order of inputs matters. RNNs maintain a hidden state that carries information from previous time steps, allowing the network to learn temporal dependencies. The Long Short-Term Memory (LSTM) architecture solves the vanishing gradient problem that limits simple RNNs, making it the standard choice for sequences with long-range dependencies.

RNNs and LSTMs are one of the four core task categories on the TensorFlow Developer Certificate exam. You will learn how to build sequence models using `tf.keras.layers.SimpleRNN`, `LSTM`, and `GRU`, and how to handle variable-length input sequences.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Recurrent Neural Network (RNN)**: A neural network architecture designed for sequential data. At each time step t, the layer receives both the current input x_t and the hidden state h_{t-1} from the previous time step, and produces a new hidden state h_t. This shared state allows the network to maintain memory across the sequence. In Keras: `tf.keras.layers.SimpleRNN(units=64, return_sequences=True)`.

*   **LSTM (Long Short-Term Memory)**: An advanced RNN variant that introduces three gating mechanisms — the forget gate, input gate, and output gate — along with a separate cell state that carries long-range information through the sequence. These gates control what information is stored, discarded, or output at each time step, solving the vanishing gradient problem that prevents simple RNNs from learning dependencies across many time steps. In Keras: `tf.keras.layers.LSTM(units=64)`.

*   **GRU (Gated Recurrent Unit)**: A simplified LSTM variant with only two gates (reset gate and update gate) and no separate cell state. GRUs have fewer parameters than LSTMs and often achieve comparable performance on shorter sequences while training faster. In Keras: `tf.keras.layers.GRU(units=64)`.

*   **`return_sequences`**: A Keras LSTM/RNN parameter that controls the output shape. `return_sequences=True` outputs the hidden state at every time step (shape: `(batch, timesteps, units)`) — required when stacking multiple recurrent layers. `return_sequences=False` (default) outputs only the final hidden state (shape: `(batch, units)`) — used before a Dense output layer.

*   **Vanishing gradient problem**: A training instability in deep networks where gradients shrink exponentially as they propagate backwards through many time steps during backpropagation through time (BPTT). This prevents early time steps from receiving useful gradient signal, making it impossible for simple RNNs to learn dependencies spanning dozens or hundreds of time steps. LSTMs and GRUs address this through their gating mechanisms.

*   **Embedding layer**: A trainable lookup table that maps discrete token indices (integers) to dense continuous vectors. Used as the first layer in text processing models: `tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=64, input_length=max_len)`. The `output_dim` is the size of each embedding vector; larger values capture more semantic information but require more memory.

---

### 2. Certification Exam Tips
*   **Stack Two LSTMs Correctly:** To stack two LSTM layers, the first must have `return_sequences=True` to pass the full sequence to the second layer. The second LSTM uses `return_sequences=False` (default). Pattern: `LSTM(64, return_sequences=True) → LSTM(32) → Dense(output)`.
*   **Embedding + LSTM Pattern:** The standard TF exam NLP/text sequence model pattern is: `Embedding(vocab_size, embed_dim, input_length) → LSTM(units) → Dense(output)`. The Embedding layer must come first and converts integer token IDs to vectors.
*   **Input Shape for Sequences:** For numeric sequences (no Embedding), the input shape is `(timesteps, features)`. For a univariate time series: `input_shape=(window_size, 1)`. For text after padding: use the Embedding layer and `input_length=max_len` instead of specifying `input_shape` manually.
*   **Study Resource:** The [TensorFlow text classification with RNNs tutorial](https://www.tensorflow.org/text/tutorials/text_classification_rnn) at tensorflow.org walks through building an LSTM text classifier end-to-end including the Embedding layer and is directly representative of exam tasks. The [Keras RNN guide](https://www.tensorflow.org/guide/keras/working_with_rnns) covers all recurrent layer options, `return_sequences`, and stacking patterns.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Work through the [TensorFlow RNN tutorial](https://www.tensorflow.org/text/tutorials/text_classification_rnn) and the [Keras RNN guide](https://www.tensorflow.org/guide/keras/working_with_rnns) at tensorflow.org. These free official resources cover LSTM, GRU, `return_sequences`, and stacking recurrent layers — all directly tested on the exam.
*   **Required Video:** Watch the RNN and LSTM lecture in the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This covers the hidden state mechanism, the vanishing gradient problem, LSTM gates, and how to build sequence models with `tf.keras`.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Build a stacked LSTM model**: Define a Sequential model with `Embedding → LSTM(64, return_sequences=True) → LSTM(32) → Dense(1, activation='sigmoid')` for binary sequence classification.
*   **Prepare padded sequences**: Use `tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=200, padding='post')` to convert variable-length integer token lists to fixed-length arrays.
*   **Train and inspect history**: Call `model.fit()` with validation data and plot `history.history['accuracy']` vs `history.history['val_accuracy']` to diagnose overfitting in the sequence model.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and draw a diagram showing how the LSTM cell state and hidden state flow between time steps.
*   [ ] Work through the [TensorFlow RNN tutorial](https://www.tensorflow.org/text/tutorials/text_classification_rnn) and the [Keras RNN guide](https://www.tensorflow.org/guide/keras/working_with_rnns).
*   [ ] Watch the RNN/LSTM lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 08 lab: stacked LSTM with Embedding layer for text classification.
*   [ ] Proceed to the Module 08 quiz.
