# Quiz: Module 08 - Recurrent Neural Networks (RNNs) and LSTMs
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
In a Keras LSTM layer, what is the effect of setting `return_sequences=True`?
*   A) It causes the LSTM to run the sequence in reverse order, from the last time step to the first.
*   B) It outputs the hidden state at every time step, producing a 3D tensor of shape `(batch, timesteps, units)` — required when stacking a second recurrent layer on top.
*   C) It doubles the number of LSTM units by running two parallel LSTM cells on the same input sequence.
*   D) It causes the LSTM to repeat the input sequence multiple times during training to improve sequence memorization.
*   **Correct Answer:** B) By default (`return_sequences=False`), a Keras LSTM outputs only the final hidden state as a 2D tensor `(batch, units)`. Setting `return_sequences=True` outputs every hidden state, which is required as input to a subsequent LSTM or GRU layer.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Running a sequence in reverse is controlled by the `go_backwards=True` argument. `return_sequences` only affects which time steps are included in the output, not the direction of processing.
    *   *Why B is correct:* Stacking pattern: `LSTM(64, return_sequences=True) → LSTM(32) → Dense(output)`. The first LSTM must pass all time steps to the second; the second uses the default `return_sequences=False` before the Dense layer.
    *   *Why C is incorrect:* The number of units is set by the first positional argument to `LSTM(units)`. `return_sequences` does not add units or parallel cells.
    *   *Why D is incorrect:* `return_sequences` has no effect on how many times the sequence is processed. It only determines the shape of the output tensor.

---

**Question 2**
Which of the following is the most accurate definition of **LSTM (Long Short-Term Memory)**?
*   A) A type of convolutional layer that applies filters along the time axis of a 1D sequence, capturing local temporal patterns without using a recurrent hidden state.
*   B) A recurrent architecture that adds forget, input, and output gates along with a separate cell state to control information flow across time steps, solving the vanishing gradient problem that limits simple RNNs on long sequences.
*   C) A regularization technique that randomly zeroes out entire recurrent time steps during training to prevent the model from relying too heavily on any single position in the sequence.
*   D) A preprocessing layer that converts integer token IDs into dense continuous vectors before they are fed into a recurrent model.
*   **Correct Answer:** B) The LSTM cell state acts as a long-term memory highway; the gating mechanisms decide what to forget, what new information to write in, and what to output — allowing gradients to flow through hundreds of time steps without vanishing.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a 1D Convolutional layer (`Conv1D`), which applies learned filters along the time axis but has no hidden state or recurrence. `Conv1D` can complement RNNs but is architecturally distinct.
    *   *Why B is correct:* In Keras: `tf.keras.layers.LSTM(units=64)`. The three gates are implemented as learned weight matrices. LSTMs are the standard choice for text classification, sentiment analysis, and time series on the TF exam.
    *   *Why C is incorrect:* This loosely describes recurrent dropout, which is applied to the hidden state connections — but it is a regularization option within an LSTM, not the definition of LSTM itself.
    *   *Why D is incorrect:* This describes an Embedding layer (`tf.keras.layers.Embedding`), which is a preprocessing component that outputs dense vectors. It is used before an LSTM but is a separate layer type.

---

**Question 3**
A developer builds a text sentiment classifier. Which Keras code correctly implements an `Embedding → LSTM → Dense` architecture for binary classification?
*   A) `model = tf.keras.Sequential([tf.keras.layers.Embedding(10000, 64, input_length=200), tf.keras.layers.LSTM(64), tf.keras.layers.Dense(1, activation='sigmoid')])`
*   B) `model = tf.keras.Sequential([tf.keras.layers.LSTM(64, input_shape=(200, 1)), tf.keras.layers.Dense(1, activation='sigmoid')])`
*   C) `model = tf.keras.Sequential([tf.keras.layers.Embedding(10000, 64, input_length=200), tf.keras.layers.Flatten(), tf.keras.layers.Dense(1, activation='sigmoid')])`
*   D) `model = tf.keras.Sequential([tf.keras.layers.Embedding(10000, 64, input_length=200), tf.keras.layers.LSTM(64, return_sequences=True), tf.keras.layers.Dense(1, activation='sigmoid')])`
*   **Correct Answer:** A) `Embedding(vocab_size, embed_dim, input_length)` converts integer token sequences to dense vectors, `LSTM(64)` processes the sequence and outputs the final hidden state, and `Dense(1, sigmoid)` produces a binary probability.
*   **Distractor Analysis:**
    *   *Why A is correct:* This is the canonical TF exam text classification pattern. Compile with `loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']`. The Embedding layer handles `input_length=200` padded sequences.
    *   *Why B is incorrect:* Skipping the Embedding layer means raw integer token IDs are fed directly into the LSTM as numeric values. This would treat token IDs as ordinal numbers rather than learning distributed representations.
    *   *Why C is incorrect:* Inserting `Flatten()` between the Embedding and output layers destroys the temporal structure of the sequence — Flatten collapses all positions into one vector, so no recurrent processing occurs. This turns the model into a bag-of-embeddings classifier, not an LSTM.
    *   *Why D is incorrect:* When the final layer is `Dense(1)`, the LSTM must output a single vector, not a sequence. Using `return_sequences=True` outputs a 3D tensor `(batch, 200, 64)`, which is incompatible with `Dense(1)` without an additional pooling or flattening step.

---

**Question 4**
Why do simple RNNs fail to learn long-range dependencies in sequences, and how do LSTMs address this?
*   A) Simple RNNs use softmax activation in hidden layers, which saturates and blocks gradient flow. LSTMs replace softmax with ReLU to keep gradients active.
*   B) Simple RNNs process sequences in fixed-length windows and cannot handle sequences longer than their window size. LSTMs have no maximum sequence length.
*   C) Simple RNNs suffer from vanishing gradients during backpropagation through time — gradients shrink exponentially over many steps, preventing early time steps from learning. LSTMs use gating mechanisms and a cell state that allow gradients to flow more directly across long sequences.
*   D) Simple RNNs require fixed-size inputs and cannot handle variable-length sequences. LSTMs use padding to equalize sequence lengths before processing.
*   **Correct Answer:** C) In backpropagation through time, the gradient of the loss with respect to early hidden states is the product of many Jacobian matrices — when these are small, the product shrinks to near zero (vanishing). The LSTM cell state provides an additive gradient path that avoids the multiplicative shrinkage.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Simple RNNs typically use tanh activation in hidden layers, not softmax. The vanishing gradient problem stems from repeated multiplication of small gradients across time steps, not from the activation function choice alone.
    *   *Why B is incorrect:* Simple RNNs can theoretically process sequences of any length — the hidden state is updated at each time step regardless of sequence length. The issue is that the gradient signal becomes negligibly small for early time steps, not that there is a hard length limit.
    *   *Why C is correct:* The LSTM forget gate controls how much of the cell state to preserve. Because the cell state update is additive (not just multiplicative), gradients can flow back through many time steps without the exponential decay that affects simple RNNs.
    *   *Why D is incorrect:* Variable-length sequence handling via padding is a preprocessing concern that applies to both simple RNNs and LSTMs equally. It is not a distinguishing capability of LSTMs.

---

**Question 5**
A developer trains an LSTM model on movie review sequences. Training accuracy reaches 96% but validation accuracy plateaus at 68%. What is the most likely problem and the best corrective action?
*   A) Underfitting — increase the number of LSTM units and add more layers to capture the complex sequential patterns in the reviews.
*   B) Overfitting — add `Dropout` between layers, reduce LSTM units, or apply recurrent dropout within the LSTM layer using the `recurrent_dropout` parameter.
*   C) Vanishing gradients — switch from LSTM to SimpleRNN, which has fewer parameters and is less prone to gradient issues.
*   D) Data leakage — the training and validation sequences overlap; re-split the dataset with a different random seed to create truly independent sets.
*   **Correct Answer:** B) A large gap between training accuracy (96%) and validation accuracy (68%) is the classic overfitting signature. For LSTMs, effective regularization options include `Dropout(0.3)` between layers and `LSTM(64, recurrent_dropout=0.2)` to drop connections within the recurrent computation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Underfitting produces high loss and low accuracy on both training and validation sets. The high training accuracy (96%) rules out underfitting — the model has sufficient capacity to learn the training data.
    *   *Why B is correct:* Standard LSTM regularization: `model.add(LSTM(64, recurrent_dropout=0.2))` and `model.add(Dropout(0.3))` between layers. `EarlyStopping(monitor='val_accuracy', patience=3)` also prevents wasting additional epochs once the gap appears.
    *   *Why C is incorrect:* Switching to SimpleRNN would make the vanishing gradient problem worse, not better. SimpleRNN struggles with long sequences precisely because it lacks the gating mechanisms that help LSTM learn stable representations.
    *   *Why D is incorrect:* Data leakage would inflate validation accuracy (make it appear artificially high), not cause it to plateau low. The symptom here — high training, low validation — points to overfitting, not leakage.
