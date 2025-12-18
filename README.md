# 📏 Son Height Prediction using Simple Linear Regression

This project implements a **Simple Linear Regression model** to predict a **son’s height based on the father’s height**. It demonstrates the complete workflow of a machine learning project, from model training to **web-based deployment** using Flask.

The application provides an **interactive web interface** where users can input the father’s height and get a predicted son’s height instantly.

---

## 📌 Project Overview

Height prediction based on parental attributes is a classic example used to explain **linear regression concepts** in Machine Learning.

This project focuses on:

* Understanding the relationship between two variables
* Building a simple yet effective regression model
* Deploying the trained model as a web application

---

## 🧠 ML Workflow

```
Dataset Loading
      ↓
Data Preprocessing
      ↓
Simple Linear Regression Model
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Saving (Pickle)
      ↓
Flask Web Application
      ↓
Cloud Deployment (Render)
```

---

## ⚙️ Technologies Used

* **Programming Language:** Python
* **Machine Learning:** Scikit-learn
* **Web Framework:** Flask
* **Frontend:** HTML, CSS
* **Model Storage:** Pickle (.pkl)
* **Deployment Platform:** Render

---

## 🧪 Dataset Description

The dataset consists of two numerical variables:

* **Father’s Height** (independent variable)
* **Son’s Height** (dependent variable / target)

This makes it a **simple linear regression** problem with a single input feature.

---

## 📐 Model Used – Simple Linear Regression

The model learns a linear relationship of the form:

```
Son_Height = m × Father_Height + c
```

Where:

* `m` is the slope
* `c` is the intercept

---

## 📊 Model Evaluation

The model performance is evaluated using:

* R² Score
* Mean Squared Error (MSE)

These metrics help assess how well the regression line fits the data.

---

## 💾 Model Saving

The trained model is saved using Pickle for reuse during deployment.

```python
import pickle

with open('linear_model.pkl', 'wb') as f:
    pickle.dump(model, f)
```

---

## 🌐 Web Application

* Built using **Flask**
* User inputs father’s height via a form
* Model predicts son’s height in real-time
* Clean and simple UI using HTML & CSS

---

## 🚀 Deployment

The application is deployed on **Render**, allowing users to access the prediction model online through a web browser.

---

## 📌 Use Cases

* Learning Simple Linear Regression
* ML model deployment demonstration
* Educational ML projects
* Beginner-friendly regression example

---

## 🔮 Future Enhancements

* Add mother’s height as an additional feature
* Convert to Multiple Linear Regression
* Improve UI design
* Add data visualization

---


## ⭐ Acknowledgment

This project is a beginner-friendly demonstration of **Simple Linear Regression and Flask-based deployment**.

If you like this project, don’t forget to ⭐ star the repository!

