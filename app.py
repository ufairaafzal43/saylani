# app.py
import streamlit as st
import pandas as pd
import joblib

# Load your single trained model using joblib
model = joblib.load("early_warning_dropout_model.pkl")

st.title("🎓 Student Risk Prediction")
st.write("Enter student details to predict their academic risk level (Low, Medium, High).")

# Input form
with st.form("student_form"):
    raisedhands = st.number_input("Raised Hands", min_value=0, max_value=100, value=10)
    visited_resources = st.number_input("Visited Resources", min_value=0, max_value=100, value=10)
    announcements_view = st.number_input("Announcements Viewed", min_value=0, max_value=50, value=5)
    discussion = st.number_input("Discussion Participation", min_value=0, max_value=50, value=5)
    absence_days = st.number_input("Student Absence Days", min_value=0, max_value=50, value=0)

    submitted = st.form_submit_button("Predict Risk")

if submitted:
    # Create dataframe
    student_input = pd.DataFrame([{
        "raisedhands": raisedhands,
        "VisITedResources": visited_resources,
        "AnnouncementsView": announcements_view,
        "Discussion": discussion,
        "StudentAbsenceDays": absence_days
    }])

    # Predict
    risk = model.predict(student_input)[0]  # assuming model outputs labels directly

    st.success(f"Predicted Student Risk: **{risk}**")
