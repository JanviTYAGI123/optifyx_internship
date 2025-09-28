
## LIVE DEMO: https://huggingface.co/spaces/janvityagi3/optifyx

---
title: Student Placement Prediction
emoji: 🎓
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
---

# Student Placement Prediction

A machine learning model that predicts whether a student will get placed based on their academic performance and skills.

## Features

- **Input Parameters:**
  - IQ Score
  - CGPA (Cumulative Grade Point Average)
  - 10th Grade Marks (%)
  - 12th Grade Marks (%)
  - Communication Skills (0-10 scale)

- **Model:** Random Forest Classifier with hyperparameter tuning
- **Output:** Placement prediction (Placed/Not Placed)

## How to Use

1. Enter the student's details in the input fields
2. Click "Submit" to get the placement prediction
3. The model will analyze the data and provide a prediction

## Model Details

- **Algorithm:** Random Forest Classifier
- **Training:** Grid Search CV with 5-fold cross-validation
- **Features:** 5 input features for prediction
- **Performance:** Optimized through hyperparameter tuning

## Dataset

The model was trained on student performance data including academic records and skill assessments.

