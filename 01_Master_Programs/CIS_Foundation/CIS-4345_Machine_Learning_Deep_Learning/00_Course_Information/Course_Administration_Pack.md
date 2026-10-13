# Course Administration Pack
## CIS-4345: Machine Learning and Deep Learning
### Texas Wesleyan University — Department of Computer Science & Information Technology
**Semester:** Fall 2026 | **Format:** 100% Online Asynchronous | **LMS:** Canvas

---

## 1. Course Description

CIS-4345 Machine Learning and Deep Learning prepares students for professional-level applied machine learning using TensorFlow 2.x and the Keras API. The course builds progressively from ML fundamentals and supervised learning through deep neural network architectures (CNNs, RNNs/LSTMs), natural language processing, time series forecasting, and generative models. The course culminates in the **TensorFlow Developer Certificate** exam — a Google-administered professional certification that demonstrates the ability to build, train, and deploy deep learning models in industry settings.

All readings, videos, and lab materials are **Zero Textbook Cost (ZTC)** — every required resource is freely available online. No textbook purchase is required at any point during the course.

---

## 2. Zero Textbook Cost (ZTC) Required Materials

All required course materials are free to access. Students should bookmark these resources on the first day of class.

### Primary Learning Resources

| Resource | URL | Used For |
|---|---|---|
| TensorFlow Documentation | https://www.tensorflow.org/api_docs | API reference for all TF/Keras code |
| Keras API Documentation | https://keras.io/api/ | Layer-by-layer Keras reference |
| TF DCGAN Tutorial | https://www.tensorflow.org/tutorials/generative/dcgan | Module 14 (Generative Models) |
| TF VAE Tutorial | https://www.tensorflow.org/tutorials/generative/cvae | Module 14 (Generative Models) |
| TF Time Series Tutorial | https://www.tensorflow.org/tutorials/structured_data/time_series | Module 13 (Time Series) |
| TF Transfer Learning Guide | https://www.tensorflow.org/tutorials/images/transfer_learning | Module 07 (Transfer Learning) |
| TF Lite Conversion Guide | https://www.tensorflow.org/lite/models/convert/convert_models | Module 15 (Deployment) |
| TF Developer Certificate Program | https://www.tensorflow.org/certificate | Module 16 (Final Exam Prep) |

### Supplementary Free Resources (Highly Recommended)

| Resource | URL | Notes |
|---|---|---|
| Machine Learning with Python & TensorFlow Course | https://www.youtube.com/watch?v=cKzgMFG5HpU | Primary video lecture series — used in all modules |
| TF Developer Certificate on Coursera (free audit) | https://www.coursera.org/professional-certificates/tensorflow-in-practice | Most exam-representative free resource; Laurence Moroney |
| fast.ai Practical Deep Learning | https://course.fast.ai/ | Strongly recommended supplemental; free; covers CNNs and transfer learning |
| Kaggle Learn: Intro to Deep Learning | https://www.kaggle.com/learn/intro-to-deep-learning | Free hands-on notebooks; no setup required |

---

## 3. Required Software and Tools

All software listed below is free. Students must have these installed and working before the first lab in Module 01.

### Core Tools

*   **Python 3.9–3.11** — Download from [python.org](https://www.python.org/downloads/). Do not use Python 3.12+ as TensorFlow 2.x compatibility is not guaranteed.
*   **TensorFlow 2.x** — Install via pip: `pip install tensorflow`. Verify with `python -c "import tensorflow as tf; print(tf.__version__)"`.
*   **Jupyter Notebook or JupyterLab** — Install via pip: `pip install notebook`. Launch with `jupyter notebook` from the terminal. All labs are provided as `.ipynb` notebooks.
*   **PyCharm Community Edition** — Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/). Required for the Module 16 mock exam (the TF Developer Certificate exam runs in PyCharm).

### Recommended Additional Libraries

Install all at once with: `pip install numpy pandas matplotlib scikit-learn keras-tuner pillow`

*   **NumPy** — Array operations used in every module
*   **Pandas** — Data loading and manipulation
*   **Matplotlib** — Training curve plots, confusion matrices, time series visualization
*   **scikit-learn** — Metrics (confusion matrix, precision/recall/F1, ROC/AUC), preprocessing utilities
*   **keras-tuner** — Required for Module 12 (Hyperparameter Tuning)
*   **Pillow** — Image loading for CNN labs (Modules 06–07)

### Cloud Alternative (No Local Install Required)
Students who cannot install software locally may use **Google Colab** ([colab.research.google.com](https://colab.research.google.com)) — a free browser-based Jupyter environment with TensorFlow pre-installed and free GPU access. All labs are compatible with Colab.

---

## 4. Grading Policy

### Grade Breakdown

| Category | Weight | Details |
|---|---|---|
| Weekly Quizzes (Modules 01–15) | 20% | 15 quizzes × 5 questions each; auto-graded in Canvas |
| Weekly Discussion Boards (Modules 01–15) | 20% | 15 discussions; initial post + 2 peer replies each |
| Hands-on Lab Assignments (Modules 01–15) | 30% | 15 labs; submitted as Jupyter notebooks or PyCharm `.py` files |
| Final Certification Exam (Module 16) | 30% | Mock exam or TF Developer Certificate attempt; scored on model accuracy thresholds |

### Grading Scale

| Grade | Range | Description |
|---|---|---|
| A | 90–100% | Excellent |
| B | 80–89% | Good |
| C | 70–79% | Satisfactory |
| D | 60–69% | Passing |
| F | Below 60% | Failure |

### Late Work Policy
All weekly assignments are due **Sunday at 11:59 PM CST**. Late submissions are accepted up to 72 hours after the deadline with a **10% penalty per day**. Submissions more than 3 days late receive a zero unless documented extenuating circumstances are provided to the instructor in advance.

### Quiz Retake Policy
Canvas quizzes may be attempted **once**. Each quiz contains 5 multiple-choice questions worth 20 points total (4 points each). Quizzes are open-note and open-resource — the goal is reinforcing understanding, not testing memorization under pressure.

---

## 5. Assignment Submission Instructions

### Quizzes
Quizzes are completed directly in Canvas and auto-graded. Open the module, navigate to the Quiz item, and submit before the Sunday deadline. Quizzes are available from Monday through Sunday of each module week.

### Discussion Boards
Post your initial response by **Thursday at 11:59 PM CST**. Reply to at least two peers by **Sunday at 11:59 PM CST**. Initial posts must be substantive (minimum 150 words). Replies must engage with the peer's argument, not just affirm it.

### Lab Assignments
Submit either:
*   A **.ipynb notebook file** with all cells executed and output visible (File → Download → Download .ipynb in Colab, or File → Save As in JupyterLab), OR
*   A **.py Python script file** if working in PyCharm

Upload through the Canvas Lab Assignment submission portal for the respective module. Include your name, student ID, and module number in a comment at the top of your file.

### Module 16 Final Exam
Students have two options for the Module 16 final:
1.  **Mock Exam (Required minimum):** Complete the four-problem mock exam provided in the Module 16 lab. Submit all four `.h5` model files plus a brief writeup (300+ words) describing your approach for each task category.
2.  **TF Developer Certificate Attempt (Bonus):** Students who register for and attempt the official TensorFlow Developer Certificate exam ([tensorflow.org/certificate](https://www.tensorflow.org/certificate)) during the semester receive full credit for the final exam component regardless of pass/fail outcome, plus a 5% bonus applied to the final grade upon submitting their score report.

---

## 6. Academic Integrity and AI Use Policy

Texas Wesleyan University requires all submitted work to represent the student's own understanding and effort.

*   **Permitted AI use:** Using AI tools (ChatGPT, Copilot, Gemini) to explain error messages, clarify concepts, and debug code is permitted and encouraged. AI is a professional tool in ML engineering.
*   **Not permitted:** Submitting AI-generated text as your own discussion posts, having AI write your lab analysis sections, or using AI to answer quiz questions without reading the material.
*   **Code:** Using AI to suggest code patterns is permitted. However, you must be able to explain every line you submit. Lab grading may include follow-up questions during office hours.

Violations are subject to Texas Wesleyan University academic dishonesty policies, which may result in a zero on the assignment or course failure.

---

## 7. Instructor Contact and Support

*   **Instructor:** Professor Nash
*   **Email:** nash@txwes.edu (response within 24–48 hours on weekdays)
*   **Office Hours:** Online by appointment via Zoom or Microsoft Teams
*   **Canvas Inbox:** Preferred for course-specific questions — all Canvas messages are monitored daily
*   **Announcements:** Check Canvas Announcements at the start of each week for updates, reminders, and any schedule changes

### University Support Resources
*   **Tutoring & Learning Center (TLC):** Free peer tutoring for CS and math — [txwes.edu/academics/tlc](https://txwes.edu/academics/tlc)
*   **University Library:** Research databases, citation guides — [txwes.edu/library](https://txwes.edu/library)
*   **Writing Center:** Discussion post and documentation writing support
*   **Disability Services:** Contact the Office of Disability Services in the West Library building for accommodation requests
