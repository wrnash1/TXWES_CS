# Video Script: Module 01 - ML Fundamentals

**Course:** CIS-4345 Machine Learning and Deep Learning

**Institution:** Texas Wesleyan University

**Instructor:** Professor Nash

**Estimated Duration:** 20-24 minutes

**TensorFlow Developer Certificate Alignment:** Foundation Concepts

---

## [00:00 - 01:30] Opening and Welcome

**[VISUAL: Title card — "Module 01: ML Fundamentals | CIS-4345 | Professor Nash"]**

Welcome to CIS-4345, Machine Learning and Deep Learning. I'm Professor Nash, and this is Module 01 — ML Fundamentals.

Over the next 16 modules, we are going to build every skill you need to earn the TensorFlow Developer Certificate. That certification is issued by Google and tests your ability to write real, working TensorFlow and Keras code under a timed exam environment. This is not a multiple-choice test about theory — you will be given a coding environment and asked to build, compile, train, and evaluate neural networks. Practical ability matters, and we start building that ability right here in Module 01.

Today's session covers three foundational areas. First, we examine what machine learning actually is and why it differs fundamentally from traditional rule-based programming. Second, we survey the three core learning paradigms: supervised, unsupervised, and reinforcement learning. Third, we walk through the complete ML pipeline — the sequence of steps every ML project follows from raw data to deployed model. Understanding this pipeline gives you a mental map for every subsequent module in this course.

Let's get started.

---

## [01:30 - 05:00] What Is Machine Learning?

**[VISUAL: Slide — "Traditional Programming vs. Machine Learning"]**

Before we talk about machine learning specifically, let's contrast it with the programming approach you have used throughout your CS coursework.

In traditional programming, you write explicit rules. A developer examines data, reasons about patterns, and codes those patterns as if-then logic. The program follows your rules precisely. This works well when the rules are knowable and stable — calculating a tax bill, sorting a list, validating a form field.

Machine learning inverts this relationship. Instead of writing rules, you provide examples: pairs of inputs and correct outputs. The algorithm examines those examples and infers the rules itself. The learned rules are encoded in numerical parameters called weights. When you present the model with a new input it has never seen, it applies those learned weights to generate a prediction.

**[VISUAL: Diagram — Two-column comparison: left column "Traditional Programming" with inputs plus rules producing output; right column "Machine Learning" with inputs plus outputs producing rules (the model)]**

This inversion is powerful because many real-world problems are far too complex to hand-code. Consider recognizing handwritten digits. A digit "7" can be written in thousands of different ways — slight rotations, variable thickness, different slants. Writing explicit rules to cover every variation would be nearly impossible. But if you show a machine learning algorithm tens of thousands of labeled examples of handwritten digits, it can learn the underlying pattern that makes a "7" distinguishable from a "1" or a "4".

The key insight is: machine learning is useful when the mapping from input to output is too complex or too dynamic to specify manually, but when you have enough labeled examples to learn from.

---

## [05:00 - 10:00] The Three Learning Paradigms

**[VISUAL: Slide — "Three Learning Paradigms"]**

Every machine learning problem falls into one of three paradigms. Understanding which paradigm your problem belongs to determines which algorithms you will use and how you will structure your data.

### Supervised Learning

**[VISUAL: Diagram — Input features X arrow to Model arrow to Label y, with example: "Image of cat → 'cat'"]**

In supervised learning, your training dataset consists of input-output pairs. Each training example has a feature vector X and a corresponding label y. The algorithm's job is to learn a function f such that f(X) approximates y as closely as possible.

Two major task types live under supervised learning. Classification predicts a discrete category — spam or not-spam, digit 0 through 9, disease present or absent. Regression predicts a continuous numerical value — house price, temperature tomorrow, predicted sales revenue.

The TensorFlow Developer Certificate exam focuses almost entirely on supervised learning. Image classification, text sentiment analysis, and time-series forecasting are all supervised tasks. You will use supervised learning in every module from Module 03 onward.

### Unsupervised Learning

**[VISUAL: Diagram — Input features X arrow to Model with no labels shown; output shows clusters or reduced dimensions]**

In unsupervised learning, your data has no labels. The algorithm finds structure in the data on its own. The two most common unsupervised tasks are clustering and dimensionality reduction.

Clustering groups similar data points together. K-means clustering, for example, assigns each point to one of k groups based on distance to cluster centroids. A marketing team might cluster customers by purchase behavior without knowing in advance what customer segments exist.

Dimensionality reduction compresses high-dimensional data into fewer dimensions while preserving as much information as possible. Principal Component Analysis, or PCA, is the classic example. Autoencoders — a type of neural network we will discuss later in the course — perform learned dimensionality reduction.

### Reinforcement Learning

**[VISUAL: Diagram — Agent, Environment, State, Action, Reward cycle]**

Reinforcement learning is the third paradigm. Unlike supervised and unsupervised learning, reinforcement learning does not use a fixed dataset at all. Instead, an agent interacts with an environment, takes actions, and receives reward or penalty signals based on those actions. Over time, the agent learns a policy — a mapping from states to actions — that maximizes cumulative reward.

Reinforcement learning drives breakthroughs in game playing, robotics control, and recommendation systems. However, it is outside the scope of the TensorFlow Developer Certificate exam, so we will not spend significant time on it this semester. You should understand the concept and be able to distinguish it from supervised and unsupervised learning.

---

## [10:00 - 16:00] The ML Pipeline

**[VISUAL: Slide — "The ML Pipeline: 7 Stages"]**

Regardless of which learning paradigm you use, every machine learning project follows a common sequence of stages. Professionals call this the ML pipeline. Understanding these stages deeply will make you a far more effective practitioner — and it will make the rest of this course make sense.

### Stage 1: Problem Definition

Before writing a single line of code, you must define the problem precisely. What are you predicting? What counts as a correct prediction? What data do you have available, and is there enough of it? Is this a classification problem or a regression problem? Answering these questions shapes every subsequent decision.

### Stage 2: Data Collection

You need labeled examples to train a supervised model. Data may come from databases, APIs, web scraping, sensors, user logs, or third-party datasets. The quantity and quality of your data is often the single largest factor in your model's final performance. Garbage in, garbage out.

### Stage 3: Data Preprocessing

**[VISUAL: Code snippet showing pandas read_csv, dropna, and train_test_split]**

Raw data is almost never ready for a model. Preprocessing steps include handling missing values, removing duplicates, encoding categorical variables, scaling numerical features, and splitting data into train, validation, and test sets. This stage typically consumes 60-80% of a data scientist's project time.

### Stage 4: Feature Engineering

Feature engineering transforms raw variables into representations that help the model learn. For tabular data, this might mean creating interaction terms, binning continuous variables, or extracting date components. For images, you might normalize pixel values to the range 0 to 1. For text, you might convert words to integer indices or dense vector embeddings. Good features can make a simple model outperform a complex model on bad features.

### Stage 5: Model Selection and Training

You select an algorithm and architecture, instantiate the model, and call the training procedure. In TensorFlow and Keras, this means defining a model with `tf.keras.Sequential` or the functional API, compiling it with an optimizer and loss function, then calling `model.fit()` on your training data.

**[VISUAL: Slide — "The Keras Three-Step Pattern"]**

I want you to memorize what I call the Keras three-step pattern right now, because you will type it hundreds of times this semester:

Step one — define the model architecture.

Step two — compile with optimizer, loss, and metrics.

Step three — fit on training data.

That pattern is the heartbeat of every lab, every exam task, and every real-world TensorFlow project.

### Stage 6: Model Evaluation

After training, you evaluate the model's performance on the held-out test set using appropriate metrics. For classification tasks: accuracy, precision, recall, F1-score. For regression: mean absolute error, mean squared error, R-squared. The test set is used only once — at the very end — to produce an honest performance estimate.

### Stage 7: Deployment

A model that lives only in a notebook delivers no business value. Deployment means packaging the trained model and making it accessible to applications. TensorFlow offers several deployment paths: TensorFlow Serving for production server-side inference, TensorFlow Lite for mobile and edge devices, and TensorFlow.js for browser-based inference. We will cover deployment in Module 15.

---

## [16:00 - 19:30] Bias-Variance Tradeoff and Generalization

**[VISUAL: Slide — "Bias-Variance Tradeoff"]**

One of the most important conceptual frameworks in all of machine learning is the bias-variance tradeoff. Understanding this framework will help you diagnose model problems throughout the entire course.

Bias refers to systematic error — the gap between a model's average predictions and the true values. A high-bias model is too simple. It makes strong assumptions and fails to capture the true complexity of the data. We call this underfitting. A linear model trying to fit a clearly non-linear dataset is underfitting.

Variance refers to sensitivity to fluctuations in training data. A high-variance model learns the training data so precisely — including its noise — that it fails to generalize to new examples. We call this overfitting. A deep neural network with millions of parameters trained on a small dataset will likely overfit.

**[VISUAL: Three-curve diagram — underfitting model (straight line through curved data), ideal model (smooth fit), overfitting model (wiggly line through every training point)]**

The goal of every ML project is to find the sweet spot: low bias and low variance. In practice, reducing bias often increases variance and vice versa. You manage this tradeoff using techniques we will study throughout the course: regularization, dropout, data augmentation, early stopping, and cross-validation.

A critical diagnostic habit: always compare training accuracy to validation accuracy. If training accuracy is high and validation accuracy is low, your model is overfitting. If both are low, your model is underfitting. We will return to this diagnostic repeatedly.

---

## [19:30 - 22:00] TensorFlow Developer Certificate Connection

**[VISUAL: Slide — "TensorFlow Developer Certificate — What It Tests"]**

Let me connect everything we discussed today directly to the TensorFlow Developer Certificate exam.

The exam is a five-hour, open-book coding test. You work in a Python IDE — typically PyCharm with the TensorFlow plugin — and are given a series of coding problems. You must build Keras models that achieve specified accuracy thresholds to receive credit for each problem. There are typically five problems covering: a basic dense network, image classification with a CNN, image classification with transfer learning, text classification, and time-series forecasting.

Every one of those problem categories is a supervised learning task. Every one uses the Keras three-step pattern. Every one requires you to understand train-test splits, overfitting, and evaluation metrics — all concepts we introduced today.

The official certification page is at tensorflow.org/certificate. I encourage you to read the candidate handbook this week so you know exactly what you are working toward.

---

## [22:00 - 24:00] Module Summary and Lab Preview

**[VISUAL: Slide — "Module 01 Summary"]**

Let's wrap up. Here is what you must take away from Module 01.

Machine learning differs from traditional programming by learning rules from data rather than following hand-coded rules. The three paradigms are supervised learning — learning from labeled examples — unsupervised learning — finding structure without labels — and reinforcement learning — learning from reward signals. The ML pipeline has seven stages: problem definition, data collection, preprocessing, feature engineering, model selection and training, evaluation, and deployment. The bias-variance tradeoff defines the core challenge of building models that generalize. And the Keras three-step pattern — define, compile, fit — is the coding foundation for every task on the TensorFlow Developer Certificate exam.

For this week's lab, you will set up your Python environment, install TensorFlow and scikit-learn, load a dataset, perform a train-test split, and inspect your data. The lab walks you through each step with complete code examples. Completing it will prepare you for the increasingly complex labs starting in Module 03.

Complete the lab, take the quiz, and post to the discussion board by the posted deadlines. I will see you in Module 02, where we dive into Python tools for machine learning: NumPy, pandas, and Matplotlib.

---

*[END OF MODULE 01 VIDEO SCRIPT]*
