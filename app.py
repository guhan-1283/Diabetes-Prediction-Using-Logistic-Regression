import streamlit as st
import numpy as np
import pandas as pd
import joblib
import time


model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config("Diabetes Prediction Model",layout="centered")
st.title("Diabetes Prediction")

st.divider()

st.write("Using this model, You can able to predict whether the person has diabetes or not")

gender_dict = {'Male':1,'Female':0,"Other":2}

gender_label = st.selectbox("Enter the Gender",["Gender"]+list(gender_dict.keys()))


if gender_label == "Gender":
    gender = None

else:
    gender = gender_dict[gender_label]

age = st.number_input("Enter the Age",placeholder="Age")

hypertension_dict = {'Yes':1,'No':0}

hypertension_label = st.selectbox("Do you have High Pressure",["High Pressure"]+list(hypertension_dict.keys()))

if hypertension_label == "High Pressure":
    hypertension = None

else:
    hypertension = hypertension_dict[hypertension_label]


heart_disease_dict = {"Yes":1,"No":0}

heart_disease_label = st.selectbox("Do you have Heart Disease",["Heart Disease"]+list(heart_disease_dict.keys()))

if heart_disease_label == "Heart Disease":
    heart_disease = None

else:
    heart_disease = heart_disease_dict[heart_disease_label]


smoke_dict = {
    "No info":0,"Current":1,"Ever":2,"Former":3,"Never":4,'Not Current':5
}


smoke_label = st.selectbox("Enter Smoke History",["Smoke History"]+list(smoke_dict.keys()))

if smoke_label == "Smoke History":
    smoke = None

else:
    smoke = smoke_dict[smoke_label]


bmi = st.number_input("Enter the BMI",placeholder="Body Mass Index")

sugar_level = st.number_input("Enter average Sugar Level in last 2-3 months",placeholder="Sugar level")

blood_glucose_level = st.number_input("Enter the Blood Glucose Level",placeholder="Blood Glucose")

X = [gender,age,hypertension,heart_disease,smoke,bmi,sugar_level,blood_glucose_level]

st.divider()

predict = st.button("Press this Button to predict")

if predict:
        with st.spinner("Wait for model to predict"):
            time.sleep(2.0)
            X1 = np.array([X])

            scaled_data = scaler.transform(X1)
            prediction = model.predict(scaled_data)

            if prediction == 1:
                st.error("**Diabetes Detected**\n\nThis person is likely to have diabetes. Please consult a medical professional.")
            else:
                st.success("**No Diabetes Detected**\n\nThis person is unlikely to have diabetes.")




else:
    "Please press the Predict Button for Prediction"

