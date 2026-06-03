# Lab Activity: Module 14 — Machine Learning for IoT

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

**Estimated Time:** 120–150 minutes

---

## Objective

In this lab you will work through two TinyML exercises. Part 1 runs a pre-trained keyword spotting model on the ESP32 using TensorFlow Lite Micro and measures inference latency and memory usage. Part 2 uses Python on your development machine to train a small regression model, apply post-training int8 quantization, and compare model size and accuracy before and after quantization.

---

## Prerequisites

- ESP32 development board with a microphone module (INMP441 I2S microphone or equivalent), or use simulated audio input from a pre-recorded array
- Arduino IDE with ESP32 board support and the `EloquentTinyML` or `TensorFlowLite_ESP32` library installed
- Python 3.10+ with TensorFlow 2.x: `pip install tensorflow numpy matplotlib`
- 4 GB RAM minimum on the development machine for TensorFlow

---

## Part 1 — Keyword Spotting on ESP32

### Step 1.1 — Install the TensorFlow Lite library

In Arduino IDE: Sketch → Include Library → Manage Libraries. Search for "TensorFlowLite_ESP32" and install the latest version.

Alternatively, install the Arduino_TensorFlowLite library from the Arduino Library Manager.

### Step 1.2 — Load the hello_world_speech example

Navigate to: File → Examples → TensorFlowLite_ESP32 → micro_speech

This example includes:

- A pre-trained model for "yes" / "no" keyword detection
- Audio provider for I2S microphone input
- MFCC feature generation
- Inference and result output over serial

### Step 1.3 — Examine the model header

Open `micro_speech_model_data.cc` (or `model.h` depending on library version). You will see the model stored as:

```cpp
const unsigned char g_model[] = {
  0x1c, 0x00, 0x00, 0x00, 0x54, 0x46, 0x4c, 0x33, ...
};
const int g_model_len = 18712;
```

Record the value of `g_model_len`. This is the model size in bytes. Note that 18,712 bytes = approximately 18 KB — a complete speech classifier.

### Step 1.4 — Measure arena size requirements

In the `micro_speech.ino` main file, locate the tensor arena declaration:

```cpp
constexpr int kTensorArenaSize = 10 * 1024;  // 10 KB
uint8_t tensor_arena[kTensorArenaSize];
```

Try reducing `kTensorArenaSize` to `8*1024`, then `6*1024`. Rebuild each time. Record the smallest value that allows `AllocateTensors()` to succeed (the serial monitor will report the error if the arena is too small). This gives you the actual minimum arena requirement for this model.

### Step 1.5 — Flash and test

Rebuild with the correct arena size. Flash to the ESP32. Open serial monitor at 115200 baud. Speak "yes" or "no" clearly toward the microphone. Observe the serial output:

```text
Heard yes (score: 211)
Heard no (score: 198)
Heard unknown
```

### Step 1.6 — Measure inference latency

Add timing code around the inference call in `main_functions.cc`:

```cpp
int64_t start = esp_timer_get_time();   // microseconds
TfLiteStatus invoke_status = interpreter->Invoke();
int64_t end = esp_timer_get_time();
MicroPrintf("Inference time: %lld us\n", end - start);
```

Flash and observe. Record the inference time in microseconds. Expected range: 5,000–20,000 µs (5–20 ms) depending on clock speed and arena configuration.

---

## Part 2 — Post-Training Quantization with TensorFlow

This part runs entirely on your development machine. You will train a small neural network for a regression task (predicting temperature from simulated sensor features), then apply full integer quantization and compare the results.

### Step 2.1 — Generate synthetic training data

```python
# file: quantization_lab.py
import numpy as np
import tensorflow as tf
import os

np.random.seed(42)
tf.random.set_seed(42)

# Simulate 3 sensor features: humidity, pressure, raw_ADC
# that correlate with temperature via a nonlinear relationship
N = 5000
humidity    = np.random.uniform(20, 90, N).astype(np.float32)
pressure    = np.random.uniform(980, 1040, N).astype(np.float32)
raw_adc     = np.random.uniform(100, 900, N).astype(np.float32)

# Nonlinear target temperature
temperature = (
    0.15 * humidity
    + 0.02 * (pressure - 1013)
    - 0.001 * (raw_adc - 500) ** 2
    + 18.0
    + np.random.normal(0, 0.5, N)
).astype(np.float32)

X = np.stack([humidity, pressure, raw_adc], axis=1)
y = temperature

# Train/validation split
split = int(0.8 * N)
X_train, X_val = X[:split], X[split:]
y_train, y_val = y[:split], y[split:]

print(f"Training samples: {len(X_train)}")
print(f"Temperature range: {y.min():.1f} – {y.max():.1f} C")
```

### Step 2.2 — Build and train the model

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(3,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1)   # regression output
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.summary()

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    batch_size=64,
    verbose=1
)

# Evaluate float32 model
val_mae = model.evaluate(X_val, y_val, verbose=0)[1]
print(f"\nFloat32 validation MAE: {val_mae:.4f} C")

# Save the float32 model
model.save("temp_model_f32.keras")
```

### Step 2.3 — Convert to TFLite float32 baseline

```python
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model_f32 = converter.convert()

with open("temp_model_f32.tflite", "wb") as f:
    f.write(tflite_model_f32)

size_f32 = os.path.getsize("temp_model_f32.tflite")
print(f"Float32 TFLite model size: {size_f32} bytes ({size_f32/1024:.1f} KB)")
```

### Step 2.4 — Apply full integer (int8) quantization

```python
def representative_dataset():
    """Provide 200 representative samples for quantization calibration."""
    for i in range(200):
        sample = X_train[i:i+1].astype(np.float32)
        yield [sample]

converter_q = tf.lite.TFLiteConverter.from_keras_model(model)
converter_q.optimizations = [tf.lite.Optimize.DEFAULT]
converter_q.representative_dataset = representative_dataset
converter_q.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter_q.inference_input_type  = tf.int8
converter_q.inference_output_type = tf.int8

tflite_model_int8 = converter_q.convert()

with open("temp_model_int8.tflite", "wb") as f:
    f.write(tflite_model_int8)

size_int8 = os.path.getsize("temp_model_int8.tflite")
print(f"Int8 TFLite model size: {size_int8} bytes ({size_int8/1024:.1f} KB)")
print(f"Size reduction: {size_f32/size_int8:.2f}x")
```

### Step 2.5 — Evaluate the int8 model accuracy

```python
def run_tflite_inference(model_path, X_data):
    """Run inference on a TFLite model and return predictions."""
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    input_details  = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_scale     = input_details[0]['quantization'][0]
    input_zero_pt   = input_details[0]['quantization'][1]
    output_scale    = output_details[0]['quantization'][0]
    output_zero_pt  = output_details[0]['quantization'][1]

    preds = []
    for sample in X_data:
        # Quantize input to int8
        quantized = np.round(sample / input_scale + input_zero_pt).astype(np.int8)
        interpreter.set_tensor(input_details[0]['index'], quantized.reshape(1, 3))
        interpreter.invoke()
        raw_output = interpreter.get_tensor(output_details[0]['index'])[0][0]
        # Dequantize output
        preds.append((raw_output - output_zero_pt) * output_scale)
    return np.array(preds)

preds_int8 = run_tflite_inference("temp_model_int8.tflite", X_val)
mae_int8   = np.mean(np.abs(preds_int8 - y_val))
print(f"Int8 quantized validation MAE: {mae_int8:.4f} C")
print(f"Accuracy delta vs float32: {abs(mae_int8 - val_mae):.4f} C")
```

### Step 2.6 — Print comparison summary

```python
print("\n===== Quantization Results =====")
print(f"{'Metric':<30} {'Float32':>10} {'Int8':>10}")
print("-" * 52)
print(f"{'Model size (bytes)':<30} {size_f32:>10} {size_int8:>10}")
print(f"{'Validation MAE (C)':<30} {val_mae:>10.4f} {mae_int8:>10.4f}")
print(f"{'Size reduction':<30} {'1.00x':>10} {size_f32/size_int8:>9.2f}x")
print(f"{'MAE increase':<30} {'0.0000':>10} {abs(mae_int8-val_mae):>10.4f}")
```

Expected results: approximately 4x size reduction with under 0.1 degree C MAE increase.

---

## Part 3 — Generate the C Header for ESP32 Deployment

Convert the quantized model to a C array for embedding in firmware:

```bash
# On Linux/macOS/WSL
xxd -i temp_model_int8.tflite > temp_model_int8.h
head -5 temp_model_int8.h
```

The resulting `.h` file contains:

```cpp
unsigned char temp_model_int8_tflite[] = {
  0x1c, 0x00, 0x00, 0x00, ...
};
unsigned int temp_model_int8_tflite_len = 1248;
```

Record `temp_model_int8_tflite_len`. This is the number of bytes that must fit in ESP32 flash for your model.

---

## Troubleshooting Guide

- **Error: AllocateTensors() failed** — The tensor arena is too small. Increase `kTensorArenaSize` by 2 KB increments until it succeeds.
- **Error: TfLiteStatus TFLITE_ERROR at Invoke()** — An operation in the model is not registered in the resolver. Check the resolver and add the missing operation.
- **Python: TypeError during representative_dataset** — Ensure the generator yields `[sample]` as a list of a single numpy array with `dtype=float32` and shape `(1, n_features)`.
- **Int8 MAE much higher than float32 MAE (>0.5 C)** — The representative dataset may not cover the full input value range. Ensure it uses training data that spans the full humidity, pressure, and raw_ADC ranges.
- **`xxd` not found on Windows** — Use WSL or install Git for Windows which includes xxd in its bin directory.

---

## Deliverables

Submit the following to the Canvas LMS assignment portal:

1. Screenshot of the ESP32 serial monitor from Part 1 showing at least three keyword detections with scores and the measured inference time in microseconds.
2. Record of the minimum tensor arena size found in Step 1.4 and the model size in bytes from Step 1.3.
3. The printed comparison table from Step 2.6 showing float32 vs. int8 size and MAE.
4. The first 5 lines of the generated `temp_model_int8.h` C array header from Part 3.
5. Written analysis (150–200 words): Explain why the representative dataset is required for full integer quantization but not for dynamic range quantization. In your answer, define what "scale" and "zero_point" represent in the quantization formula, and explain how the representative dataset is used to compute them.

---
