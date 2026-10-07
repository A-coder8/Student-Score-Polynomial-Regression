# Student Score Prediction 🎓🤖

[🇮🇷 فارسی](README.fa.md)

A Machine Learning regression project for predicting a student's final score based on academic and personal features.

## 📌 Features

The model uses the following features:

- Age
- Study Hours
- Attendance
- Previous Score
- Sleep Hours
- Homework Hours
- Extracurricular Activities
- Parent Education
- Internet Access

Target variable:

- Final Score

## 🧠 Technologies

This project uses:

- `Python`
- `Pandas`
- `Scikit-learn`
- `Linear Regression`
- `PolynomialFeatures`
- `pd.get_dummies()`

## 📊 Dataset

The dataset contains **1000 synthetic student records**.

Columns:

id
age
study_hours
attendance
previous_score
sleep_hours
homework_hours
extracurricular
parent_education
internet_access
final_score

## Results for Different Degrees

- with degree 1
- R2Score =  0.5847473050789392
-----------------------------------------------
- with degree 2
- R2Score =  0.7474677115016702
-----------------------------------------------
- with degree 3
- R2Score =  0.7113879479591073
