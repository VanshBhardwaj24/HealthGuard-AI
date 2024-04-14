import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np



diabetes_model = pickle.load(open('C:/Users/Raghav/Desktop/drive-download-20231114T064631Z-001/saved models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Raghav/Desktop/drive-download-20231114T064631Z-001/saved models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('C:/Users/Raghav/Desktop/drive-download-20231114T064631Z-001/saved models/parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction")

    # Getting the input data from the user
    pregnancies = st.text_input("Number of Pregnancies")
    glucose = st.text_input("Glucose Level")
    blood_pressure = st.text_input("Blood Pressure value")
    skin_thickness = st.text_input("Skin Thickness value")
    insulin = st.text_input("Insulin Level")
    bmi = st.text_input("BMI value")
    diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function value")
    age = st.text_input("Age of the Person")

    # Code for Prediction
    diab_diagnosis = ""

    # Creating a button for Prediction
    if st.button("Diabetes Test Result"):
        # Convert input values to numeric
        input_data = np.array([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age], dtype=float).reshape(1, -1)

        diab_prediction = diabetes_model.predict(input_data)

        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The person is not diabetic"

    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")

    # Getting the input data from the user
    age = st.text_input("Age")
    sex = st.text_input("Sex")
    cp = st.text_input("Chest Pain types")
    trestbps = st.text_input("Resting Blood Pressure")
    chol = st.text_input("Serum Cholestoral in mg/dl")
    fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")
    restecg = st.text_input("Resting Electrocardiographic results")
    thalach = st.text_input("Maximum Heart Rate achieved")
    exang = st.text_input("Exercise Induced Angina")
    oldpeak = st.text_input("ST depression induced by exercise")
    slope = st.text_input("Slope of the peak exercise ST segment")
    ca = st.text_input("Major vessels colored by fluoroscopy")
    thal = st.text_input("Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect")

    # Code for Prediction
    heart_diagnosis = ""

    # Creating a button for Prediction
    if st.button("Heart Disease Test Result"):
        # Convert input values to numeric
        input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal], dtype=float).reshape(1, -1)

        heart_prediction = heart_disease_model.predict(input_data)

        if heart_prediction[0] == 1:
            heart_diagnosis = "The person is having heart disease"
        else:
            heart_diagnosis = "The person does not have any heart disease"

    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction")

    # Getting the input data from the user
    fo = st.text_input("MDVP:Fo(Hz)")
    fhi = st.text_input("MDVP:Fhi(Hz)")
    flo = st.text_input("MDVP:Flo(Hz)")
    jitter_percent = st.text_input("MDVP:Jitter(%)")
    jitter_abs = st.text_input("MDVP:Jitter(Abs)")
    rap = st.text_input("MDVP:RAP")
    ppq = st.text_input("MDVP:PPQ")
    ddp = st.text_input("Jitter:DDP")
    shimmer = st.text_input("MDVP:Shimmer")
    shimmer_db = st.text_input("MDVP:Shimmer(dB)")
    apq3 = st.text_input("Shimmer:APQ3")
    apq5 = st.text_input("Shimmer:APQ5")
    apq = st.text_input("MDVP:APQ")
    dda = st.text_input("Shimmer:DDA")
    nhr = st.text_input("NHR")
    hnr = st.text_input("HNR")
    rpde = st.text_input("RPDE")
    dfa = st.text_input("DFA")
    spread1 = st.text_input("spread1")
    spread2 = st.text_input("spread2")
    d2 = st.text_input("D2")
    ppe = st.text_input("PPE")

    # Code for Prediction
    parkinsons_diagnosis = ""

    # Creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        # Convert input values to numeric
        input_data = np.array([fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe], dtype=float).reshape(1, -1)

        parkinsons_prediction = parkinsons_model.predict(input_data)

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
