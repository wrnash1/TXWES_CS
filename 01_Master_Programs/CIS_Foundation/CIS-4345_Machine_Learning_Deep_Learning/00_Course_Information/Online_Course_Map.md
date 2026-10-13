# Online Course Map

## CIS-4345 – Machine Learning & Deep Learning

**16-Week Course | Target Certification: TensorFlow Developer Certificate**

---

## Course Theme Overview

This course is organized into six thematic blocks that build progressively from classical ML foundations through neural networks, computer vision, NLP, advanced architectures, and production deployment — culminating in the Google TensorFlow Developer Certificate exam.

- Block 1 | Weeks 1–2 | ML Foundations
- Block 2 | Weeks 3–5 | Core Algorithms and Neural Networks
- Block 3 | Weeks 6–8 | Computer Vision
- Block 4 | Weeks 9–11 | NLP and Model Evaluation
- Block 5 | Weeks 12–14 | Advanced Topics
- Block 6 | Weeks 15–16 | Deployment and Certification Prep

---

## Week-by-Week Breakdown

---

### Block 1 — ML Foundations (Weeks 1–2)

**Week 1 | Module 01: Machine Learning Fundamentals**

* Topics: Supervised vs. unsupervised vs. reinforcement learning, the ML workflow (data → model → evaluate → deploy), bias-variance tradeoff, overfitting and underfitting, train/validation/test splits, loss functions, gradient descent
* Tools introduced: Google Colab, NumPy, Pandas, Matplotlib
* What students build: A Colab notebook exploring a tabular dataset (e.g., Kaggle Titanic) — data loading, exploratory analysis, and a baseline sklearn model
* Cert alignment: Foundational ML concepts underpin all four TF Developer exam task categories
* Assessment: Quiz 01, Discussion 01

**Week 2 | Module 02: Python for Machine Learning**

* Topics: NumPy array operations and broadcasting, Pandas DataFrames for ML pipelines, Matplotlib/Seaborn visualization, feature scaling (StandardScaler, MinMaxScaler), train/test split with sklearn, loading CSV and image datasets
* Tools introduced: NumPy, Pandas, Matplotlib, Seaborn, scikit-learn
* What students build: A data preprocessing pipeline notebook — raw CSV → cleaned features → scaled inputs → split datasets, ready for model training
* Cert alignment: Data preparation is a prerequisite skill for every TF Developer exam scenario
* Assessment: Quiz 02, Lab 02 (preprocessing pipeline), Discussion 02

---

### Block 2 — Core Algorithms and Neural Networks (Weeks 3–5)

**Week 3 | Module 03: Regression with Neural Networks**

* Topics: Linear regression review, mean squared error loss, gradient descent step-by-step, feature engineering for regression, evaluating regression models (MAE, RMSE, R²), first TensorFlow regression model
* Tools introduced: TensorFlow 2.x, Keras Sequential API
* What students build: A TF regression model predicting a continuous target (e.g., housing prices or fuel efficiency) using `tf.keras.Sequential` with Dense layers
* Cert alignment: Direct match — TF Developer exam Category 1 covers building and training regression models
* Assessment: Quiz 03, Lab 03 (TF regression notebook), Discussion 03

**Week 4 | Module 04: Neural Networks and Classification**

* Topics: Multi-layer perceptrons, activation functions (ReLU, sigmoid, softmax), binary and multi-class classification, categorical cross-entropy loss, one-hot encoding, model accuracy metrics, confusion matrices
* Tools introduced: TensorFlow/Keras, sklearn metrics
* What students build: A multi-class classification network (e.g., Fashion MNIST) — architecture design, training loop, accuracy evaluation, and prediction visualization
* Cert alignment: Classification networks are tested across all four TF Developer exam categories
* Assessment: Quiz 04, Lab 04 (classification network), Discussion 04

**Week 5 | Module 05: TensorFlow and Keras In Depth**

* Topics: Keras functional API vs. Sequential API, model compilation (`optimizer`, `loss`, `metrics`), callbacks (`EarlyStopping`, `ModelCheckpoint`, `ReduceLROnPlateau`), training history plots, saving and loading models (`model.save`, `tf.saved_model`)
* Tools introduced: TensorFlow/Keras callbacks, TensorBoard (optional), Google Colab GPU runtime
* What students build: A fully configured training pipeline with callbacks — early stopping, checkpoint saving, and loss/accuracy curves plotted from training history
* Cert alignment: Model saving/loading and callback usage are explicitly tested in the TF Developer exam
* Assessment: Quiz 05, Lab 05 (callbacks and model persistence), Discussion 05

---

### Block 3 — Computer Vision (Weeks 6–8)

**Week 6 | Module 06: Convolutional Neural Networks (CNNs)**

* Topics: Convolution operation intuition, filters and feature maps, pooling layers (MaxPooling, GlobalAveragePooling), CNN architecture patterns (Conv→Pool→Flatten→Dense), image preprocessing with `ImageDataGenerator`, data normalization
* Tools introduced: TensorFlow/Keras CNN layers, `tf.keras.preprocessing.image`
* What students build: A CNN image classifier trained on CIFAR-10 or a custom dataset — convolutional base, pooling, flattening, and dense output with softmax
* Cert alignment: Direct match — TF Developer exam Category 2 focuses entirely on image classification with CNNs
* Assessment: Quiz 06, Lab 06 (CNN image classifier), Discussion 06

**Week 7 | Module 07: Transfer Learning**

* Topics: Pre-trained model concepts (ImageNet weights), feature extraction vs. fine-tuning, freezing layers (`layer.trainable = False`), adding custom classification heads, `tf.keras.applications` (MobileNetV2, InceptionV3, ResNet50), data augmentation layers
* Tools introduced: `tf.keras.applications`, TensorFlow Hub
* What students build: A transfer learning pipeline using MobileNetV2 — load pre-trained base, freeze weights, add custom Dense head, fine-tune top layers on a small custom image dataset
* Cert alignment: Transfer learning is a core topic in TF Developer exam Category 2
* Assessment: Quiz 07, Lab 07 (MobileNetV2 transfer learning), Discussion 07

**Week 8 | Module 08: Recurrent Neural Networks and LSTMs**

* Topics: Sequence modeling concepts, vanishing gradient problem, RNN architecture, LSTM cell mechanics (input/forget/output gates), GRU as a lighter alternative, sequence padding and masking, stateful vs. stateless RNNs
* Tools introduced: `tf.keras.layers.LSTM`, `tf.keras.layers.GRU`, `tf.keras.layers.SimpleRNN`
* What students build: A sequence model for a simple time-series or character-level prediction task — padded input sequences, LSTM layers, and Dense output
* Cert alignment: RNN/LSTM architectures are tested in TF Developer exam Categories 3 and 4
* Assessment: Quiz 08, Lab 08 (LSTM sequence model), Discussion 08

---

### Block 4 — NLP and Model Evaluation (Weeks 9–11)

**Week 9 | Module 09: Natural Language Processing with TensorFlow**

* Topics: Text tokenization (`tf.keras.preprocessing.text.Tokenizer`), word embeddings (embedding layer, Word2Vec concepts), sequence padding (`pad_sequences`), sentiment classification with LSTM/Conv1D, text preprocessing pipeline
* Tools introduced: TensorFlow text preprocessing, `tf.keras.layers.Embedding`, TensorFlow Datasets
* What students build: A text sentiment classifier (e.g., IMDB reviews) — tokenization pipeline, embedding layer, LSTM or Conv1D layers, binary classification output
* Cert alignment: Direct match — TF Developer exam Category 3 covers NLP with TensorFlow
* Assessment: Quiz 09, Lab 09 (sentiment classifier), Discussion 09

**Week 10 | Module 10: Data Augmentation and Regularization**

* Topics: Image augmentation (`RandomFlip`, `RandomRotation`, `RandomZoom`), text augmentation strategies, Dropout layers, L1/L2 weight regularization, Batch Normalization, learning rate schedules, comparing regularized vs. unregularized training curves
* Tools introduced: `tf.keras.layers.RandomFlip`, `tf.keras.layers.Dropout`, `tf.keras.layers.BatchNormalization`
* What students build: An augmented CNN pipeline — preprocessing layers for augmentation baked into the model graph, Dropout applied to Dense layers, training/validation curves compared with and without regularization
* Cert alignment: Augmentation and regularization techniques are tested across all TF Developer exam categories
* Assessment: Quiz 10, Lab 10 (augmented and regularized model), Discussion 10

**Week 11 | Module 11: Model Evaluation and Performance Tuning**

* Topics: Precision, recall, F1-score, ROC-AUC, confusion matrix interpretation, class imbalance strategies (class weights, oversampling), learning curve analysis, diagnosing underfitting vs. overfitting, cross-validation with Keras
* Tools introduced: sklearn metrics, TensorFlow/Keras training history, Matplotlib
* What students build: A model evaluation report notebook — training a classifier, computing full sklearn metrics, plotting ROC curve and confusion matrix, diagnosing and addressing a performance issue
* Cert alignment: Evaluation and iteration are implicit in all TF Developer exam task categories
* Assessment: Quiz 11, Lab 11 (evaluation and diagnostics notebook), Discussion 11

---

### Block 5 — Advanced Topics (Weeks 12–14)

**Week 12 | Module 12: Hyperparameter Tuning**

* Topics: Manual tuning strategies, Keras Tuner (Random Search, Bayesian Optimization, Hyperband), tunable parameters (learning rate, units, dropout rate, batch size), automated search setup, reading tuner results and selecting best model
* Tools introduced: Keras Tuner (`keras_tuner`), Google Colab
* What students build: A Keras Tuner experiment on a classification or regression problem — define hypermodel, run Random Search, retrieve best hyperparameters, retrain final model
* Cert alignment: Understanding model optimization supports TF Developer exam scenario problem-solving
* Assessment: Quiz 12, Lab 12 (Keras Tuner experiment), Discussion 12

**Week 13 | Module 13: Time Series Forecasting**

* Topics: Time series characteristics (trend, seasonality, stationarity), windowing datasets with `tf.data`, univariate and multivariate forecasting, Conv1D for time series, LSTM forecasting models, MAE evaluation for forecasting, comparing statistical baselines vs. DL models
* Tools introduced: `tf.data.Dataset`, `tf.keras.layers.Conv1D`, `tf.keras.layers.LSTM`
* What students build: A time series forecasting model on a public dataset (e.g., sunspot activity or weather data) — windowed `tf.data` pipeline, LSTM or Conv1D architecture, forecasting plot with actual vs. predicted values
* Cert alignment: Direct match — TF Developer exam Category 4 covers sequences and time series
* Assessment: Quiz 13, Lab 13 (time series forecasting notebook), Discussion 13

**Week 14 | Module 14: Generative Models — GANs and VAEs**

* Topics: Generative vs. discriminative models, GAN architecture (generator + discriminator adversarial training), mode collapse and training instability, Variational Autoencoders (encoder-decoder, latent space, reparameterization trick), applications (image synthesis, data augmentation, anomaly detection)
* Tools introduced: TensorFlow/Keras custom training loops, `tf.GradientTape`
* What students build: A simple GAN or VAE trained on MNIST — custom training loop with `tf.GradientTape`, generator/decoder output visualization, latent space interpolation
* Cert alignment: Advanced architecture knowledge reinforces all TF Developer exam task categories
* Assessment: Quiz 14, Lab 14 (GAN or VAE notebook), Discussion 14

---

### Block 6 — Deployment and Certification (Weeks 15–16)

**Week 15 | Module 15: TF Serving, TFLite, and Model Deployment**

* Topics: Saving models in SavedModel format, TensorFlow Serving overview, TFLite model conversion (`tf.lite.TFLiteConverter`), post-training quantization (dynamic range, float16, full integer), TFLite interpreter usage, deploying models to edge devices and mobile, TensorFlow.js basics
* Tools introduced: `tf.lite.TFLiteConverter`, TensorFlow Serving (Docker), TensorFlow.js
* What students build: A complete export pipeline — train a classification model, convert to TFLite with quantization, run inference with the TFLite interpreter, compare pre- and post-quantization accuracy and model size
* Cert alignment: Model saving and conversion are explicitly covered in the TF Developer exam
* Assessment: Quiz 15, Lab 15 (TFLite export and inference), Discussion 15

**Week 16 | Module 16: Final Exam Prep and TensorFlow Developer Certification**

* Topics: Full TF Developer exam objective review (four categories: regression/classification, CNNs, NLP, time series), timed Colab problem practice, common exam pitfalls (incorrect save format, missing `pad_sequences`, wrong loss function), exam logistics and registration, portfolio project polish
* Tools: Review all tools from Modules 01–15; Google Colab, TensorFlow Docs
* What students build: A timed mock exam session — one problem per TF Developer exam category completed under simulated exam conditions, plus a final portfolio notebook
* Cert alignment: This module is entirely exam-preparation focused — every objective in the TF Developer Certificate is reviewed
* Assessment: Quiz 16, Lab 16 (mock exam portfolio), **Final Exam**

---

## TensorFlow Developer Certificate Exam Alignment

The Google TensorFlow Developer Certificate exam consists of five timed Colab problems across four task categories:

- **Category 1 — Basic/Regression:** Covered in Modules 03–05
- **Category 2 — Image Classification / CNNs:** Covered in Modules 06–07
- **Category 3 — NLP / Text Classification:** Covered in Modules 08–09
- **Category 4 — Sequences / Time Series:** Covered in Modules 08, 13
- **Cross-cutting skills (all categories):** Callbacks, model saving, data pipelines, augmentation — Modules 05, 10, 11, 15

* Exam format: Colab-based, take-home, 5-hour window, 5 problems
* Students submit a `.h5` or SavedModel file for each problem; models are auto-graded on accuracy thresholds
* Exam registration: [https://developers.google.com/certification/tensorflow-developer](https://developers.google.com/certification/tensorflow-developer)
* Exam fee: Not included in course — students register independently

---

## Canvas Weekly Rhythm (Monday–Sunday)

Each module follows a consistent 7-day structure:

- **Monday:** Module opens — lecture notes and reading materials available in Canvas
- **Tuesday:** Lecture video(s) released — conceptual walkthrough of core topic
- **Wednesday:** Lab notebook released in Google Colab — students work through guided exercises
- **Thursday:** Discussion prompt opens — post initial response (150+ words) by Saturday
- **Friday–Saturday:** Lab submission window — submit Colab notebook link or exported `.ipynb` to Canvas
- **Saturday:** Reply to at least two classmates' Discussion posts
- **Sunday 11:59 PM CT:** All assignments due — Quiz, Lab, and Discussion

---

## ZTC (Zero Textbook Cost) Resources

This course uses exclusively free, publicly available tools and resources. No paid software or textbook is required.

- **Google Colab:** [https://colab.research.google.com](https://colab.research.google.com) — free cloud Jupyter notebooks with GPU/TPU runtime; all labs run here
- **TensorFlow Documentation:** [https://www.tensorflow.org/learn](https://www.tensorflow.org/learn) — official tutorials, API reference, and the TF Developer Certificate study guide
- **Kaggle:** [https://www.kaggle.com](https://www.kaggle.com) — free datasets, free Kaggle notebooks (GPU-enabled), and introductory ML courses
- **TensorFlow Hub:** [https://tfhub.dev](https://tfhub.dev) — pre-trained models for transfer learning (used in Module 07)
- **Keras Documentation:** [https://keras.io](https://keras.io) — layer reference, model API docs, and code examples
- **TensorFlow Datasets (TFDS):** [https://www.tensorflow.org/datasets](https://www.tensorflow.org/datasets) — curated datasets ready for TF pipelines (MNIST, IMDB, CIFAR-10, etc.)
- **Google ML Crash Course:** [https://developers.google.com/machine-learning/crash-course](https://developers.google.com/machine-learning/crash-course) — supplemental reading for Modules 01–02
