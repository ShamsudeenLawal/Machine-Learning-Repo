
# load packages
import numpy as np
import pandas as pd
import joblib
import streamlit as st
from streamlit_option_menu import option_menu

# load model(s)
diabetes_model = joblib.load("./logistic_regression_model.pkl")
model_features = joblib.load("./model_features.pkl")

# sidebar for navigation
with st.sidebar:
    selected = option_menu("Disease Prediction Systems",
                           ["Diabetes Prediction"],
                           icons=["activity"],
                           default_index=0)
    
# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    # page title
    st.title("Diabetes Prediction using ML")

    # getting input data
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure")
    with col1:
        SkinThickness = st.text_input("Skin Thickness")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age of the Person")


    # Prediction code
    diab_diagnosis = ""

    # Button for prediction
    if st.button("Diabetes Test Result"):
        # features = np.array([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age], dtype="float32")
        features = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        features = pd.DataFrame(features, columns=model_features)
        diab_prediction = diabetes_model.predict(features)
        
        if diab_prediction[0]==1:
            diab_diagnosis = "This person is diabetic"
        else:
            diab_diagnosis = "This person is not diabetic"
    
    st.success(diab_diagnosis)
