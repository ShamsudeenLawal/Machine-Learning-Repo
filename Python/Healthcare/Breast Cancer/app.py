# Load packages
import sys
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import joblib

# Load model
bc_classifier = joblib.load("knn_pipeline.pkl")
model_features = joblib.load("model_features.pkl")

# model_features = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
#  'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean',
#  'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se',
#  'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se',
#  'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst',
#  'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst',
#  'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

model_feature_caps = [" ".join(col.strip().split("_")).upper() for col in model_features]

with st.sidebar:
    selected = option_menu("Disease Prediction using ML",
                           ["Breast Cancer Prediction"],
                           icons=["breast"],
                           default_index=0,)
    
if selected == "Breast Cancer Prediction":
    # Page details
    st.title("Breast Cancer Prediction using ML")

    # Get input data
    col1, col2, col3, col4= st.columns(4)

    with col1:
        radius_mean = st.text_input(model_feature_caps[0])
    with col2:
        texture_mean = st.text_input(model_feature_caps[1])
    with col3:
        perimeter_mean = st.text_input(model_feature_caps[2])
    with col4:
        area_mean = st.text_input(model_feature_caps[3])
    

    with col1:
        smoothness_mean = st.text_input(model_feature_caps[4])
    with col2:
        compactness_mean = st.text_input(model_feature_caps[5])
    with col3:
        concavity_mean = st.text_input(model_feature_caps[6])
    with col4:
        concave_points_mean = st.text_input(model_feature_caps[7])

    with col1:
        symmetry_mean = st.text_input(model_feature_caps[8])
    with col2:
        fractal_dimension_mean = st.text_input(model_feature_caps[9])
    with col3:
        radius_se = st.text_input(model_feature_caps[10])
    with col4:
        texture_se = st.text_input(model_feature_caps[11])

    with col1:
        perimeter_se = st.text_input(model_feature_caps[12])
    with col2:
        area_se = st.text_input(model_feature_caps[13])
    with col3:
        smoothness_se = st.text_input(model_feature_caps[14])
    with col4:
        compactness_se = st.text_input(model_feature_caps[15])

    with col1:
        concavity_se = st.text_input(model_feature_caps[16])
    with col2:
        concave_points_se = st.text_input(model_feature_caps[17])
    with col3:
        symmetry_se = st.text_input(model_feature_caps[18])
    with col4:
        fractal_dimension_se = st.text_input(model_feature_caps[19])

    with col1:
        radius_worst = st.text_input(model_feature_caps[20])
    with col2:
        texture_worst = st.text_input(model_feature_caps[21])
    with col3:
        perimeter_worst = st.text_input(model_feature_caps[22])
    with col4:
        area_worst = st.text_input(model_feature_caps[23])


    with col1:
        smoothness_worst = st.text_input(model_feature_caps[24])
    with col2:
        compactness_worst = st.text_input(model_feature_caps[25])
    with col3:
        concavity_worst = st.text_input(model_feature_caps[26])
    with col4:
        concave_points_worst = st.text_input(model_feature_caps[27])

    with col1:
        symmetry_worst = st.text_input(model_feature_caps[28])
    with col2:
        fractal_dimension_worst = st.text_input(model_feature_caps[29])


    # Prediction code
    breast_cancer_diagnosis = ""

    # Prediction Button
    if st.button("Breast Cancer Result"):
        features = [[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean,
                    symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se,
                    concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
                    compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]]

        features = pd.DataFrame(features, columns=model_features)

        bc_prediction = bc_classifier.predict(features)
        
        if bc_prediction[0]=="YES":
            breast_cancer_diagnosis = "This person has breasst cancer."
        else:
            breast_cancer_diagnosis = "This person does not have breast cancer."
    
    st.success(breast_cancer_diagnosis)

