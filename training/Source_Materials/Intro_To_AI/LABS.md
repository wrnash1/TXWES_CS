# Intro to AI Labs (Python & ML Basics)

## Lab 1: Python Environment for Data Science
**Objective**: Setting up the tools for AI development.

1.  **Verification**: Check your Python version: `python3 --version`.
2.  **PIP**: Use `pip` to install `numpy`, `pandas`, and `scikit-learn`.
3.  **Calculations**: Write a simple Python script `test_math.py` that creates a 3x3 Numpy matrix and calculates its transpose.

## Lab 2: Data Exploration with Pandas
**Objective**: Loading and inspecting datasets.

1.  **CSV**: Download a small sample CSV (e.g., Iris dataset) or create one.
2.  **Loading**: Write a script to load the CSV using `pandas.read_csv()`.
3.  **Inspection**: Print the first 5 rows and the summary statistics (`df.describe()`).
4.  **Filtering**: Filter the data to show only rows where a specific column value is greater than a certain threshold.

## Lab 3: Your First Machine Learning Model
**Objective**: Train a simple Linear Regression model.

1.  **Model Selection**: Import `LinearRegression` from `sklearn.linear_model`.
2.  **Training**: Create a small X and y array (e.g., predicting house prices based on square footage).
3.  **Prediction**: Train the model using `.fit()` and predict a new value.
4.  **Evaluation**: Calculate the Mean Squared Error (MSE) of your predictions.

---
**Submission**: Run `../txwes-submit.sh` after completing each lab.
