Multiple Disease Prediction System using Machine Learning

User intreface - https://private-user-images.githubusercontent.com/98437584/290889831-fdabe788-d49c-4996-8ee4-b1e0e37f09dc.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTQ1NjYzNzIsIm5iZiI6MTcxNDU2NjA3MiwicGF0aCI6Ii85ODQzNzU4NC8yOTA4ODk4MzEtZmRhYmU3ODgtZDQ5Yy00OTk2LThlZTQtYjFlMGUzN2YwOWRjLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTAxVDEyMjExMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTYzYzIzZDc3MDk5N2IwZGFmMWRjMzdjNmVmZTcwNGM5MDc1MWVjZDc1MzNmMWE0ODAyZDc5NzBlMDM2ZmM4MTkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.v_rahIkCgDACpMuzX0bMm9GtVHR00Lveuxmg3oayYe8

This project provides a streamlit web application for predicting multiple diseases, including diabetes, Parkinson's disease, and heart disease, using machine learning algorithms. The prediction models are deployed using Streamlit, a Python library for building interactive web applications.
Table of Contents

    Introduction
    Features
    Setup
    Usage
    Contributing
    License

Introduction

The Multiple Disease Prediction project aims to create a user-friendly web application that allows users to input relevant medical information and receive predictions for different diseases. The machine learning models trained on disease-specific datasets enable accurate predictions for diabetes, Parkinson's disease, and heart disease.
Features

The Multiple Disease Prediction web application offers the following features:

    User Input: Users can input their medical information, including age, gender, blood pressure, cholesterol levels, and other relevant factors.
    Disease Prediction: The application utilizes machine learning models to predict the likelihood of having diabetes, Parkinson's disease, and heart disease based on the inputted medical data.
    Prediction Results: The predicted disease outcomes are displayed to the user, providing an indication of the probability of each disease.
    Visualization: Visualizations are generated to highlight important features and provide insights into the prediction process.
    User-Friendly Interface: The web application offers an intuitive and user-friendly interface, making it easy for individuals without technical knowledge to use the prediction tool.

Setup

To use this project locally, follow these steps:

    Clone the repository:

git clone https://github.com/shaadclt/Multiple-Disease-Prediction-System.git

    Install the required dependencies by running:

pip install -r requirements.txt

    Download the pre-trained machine learning models for diabetes, Parkinson's disease, and heart disease. Make sure to place them in the appropriate directories within the project structure.

    Update the necessary configurations and file paths in the project files.

Usage

To run the Multiple Disease Prediction web application, follow these steps:

    Open a terminal or command prompt and navigate to the project directory.

    Run the following command to start the Streamlit application:

streamlit run multiplediseaseprediction.py

    Access the web application by opening the provided URL in your web browser.

    Input the relevant medical information as requested by the application.

    Click the "Predict" button to generate predictions for diabetes, Parkinson's disease, and heart disease based on the provided data.

    View the prediction results and any accompanying visualizations or insights.

Feel free to customize the web application's appearance, add more disease prediction models, or integrate additional features based on your specific requirements.
Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the project's GitHub repository.
License
This project is licensed under the MIT License. You are free to modify and use the code for both personal and commercial purposes.
