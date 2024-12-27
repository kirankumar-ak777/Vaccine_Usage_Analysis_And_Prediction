
# H1N1 Vaccine Prediction Project

## Overview
This project focuses on predicting whether individuals are likely to get the H1N1 vaccine, based on various demographic, health, and behavioral features. By leveraging logistic regression and feature selection techniques, the model aims to achieve high accuracy and reliability.

## Technologies Used
- **Python**: Main programming language for data processing and building the dashboards.
- **Pandas**: For data manipulation and preprocessing.
- **Pylab**: Supports visualization by combining matplotlib and NumPy for plotting and data manipulation.
- **Seaborn & Matplotlib**: For additional data visualizations during EDA.
- **Scikit-learn**: Used for implementing machine learning algorithms, including model training, evaluation, and feature selection.
- **Plotly & Dash**: For creating interactive visualizations and web-based dashboards.
- **Streamlit**: For deploying the interactive dashboards online.


## Project Structure and Concepts

### 1.Data Preparation
   **Target Variable:**h1n1_vaccine, which indicates if an individual received the H1N1 vaccine.

   **Predictor Variables:**Features related to demographics, health status, and vaccine awareness, which are pre-processed as needed.

## 2.Feature Selection:
   **Recursive Feature Elimination (RFE):**A feature selection method used to select the most relevant features for the model, reducing complexity and improving interpretability.

   **Optimal Features:**Using RFE, we identify and retain features that best contribute to predicting the target variable, aiming for a balance between model accuracy and simplicity.

## 3.Data Balancing:
   **Class Imbalance Issue:**Since the dataset may contain a class imbalance (more people either receiving or not receiving the     vaccine), balancing is necessary to prevent bias in the model.

   **Over-Sampling (SMOTE):**The Synthetic Minority Over-sampling Technique (SMOTE) generates synthetic samples for the minority class to achieve a balanced dataset.

   **Under-Sampling:**Randomly reduces the size of the majority class to match the minority class, another method to address class imbalance.

## 4.Model Training
   **Logistic Regression:**A statistical model used for binary classification, selected here to predict the binary outcome (vaccine uptake) with interpretability and efficiency.

   **Training and Testing Split:**To ensure generalization, the data is split into training and test sets, with 70% for training and 30% for testing.

## 5.Model Evaluation and Threshold Tuning
   #### Performance Metrics:
   **Precision:** Measures the accuracy of positive predictions.
   **Recall:**Indicates the proportion of actual positives that are correctly identified.
   **F1 Score:**Harmonic mean of precision and recall, providing a single score for evaluation.
   **Accuracy:**Overall correctness of the model's predictions

   #### Threshold Tuning:
   - Using different probability thresholds to maximize the metrics and balance them for the best possible prediction.
   - Evaluates thresholds from 0 to 1.0 in increments, selecting the one with the highest balanced metric average for optimal performance.

## 6.ROC Curve and AUC (Area Under Curve):
   **ROC Curve:** Graphs True Positive Rate (sensitivity) against False Positive Rate (1-specificity), providing insight into model performance across thresholds.

   **AUC:**Area under the ROC curve, indicating the model's overall ability to distinguish between classes.
   

## Key Findings
- The model demonstrated robust performance, with an optimal threshold maximizing precision, recall, accuracy, and F1 scores. The AUC   score confirms the model's reliability in distinguishing individuals who are likely to take the H1N1 vaccine.

## You can access the deployed Streamlit app on Render here: [Streamlit App][(https://vaccine-usage-analysis-and-prediction-6xp9.onrender.com/)].

