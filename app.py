import streamlit as st
import pandas as pd
from model import train_model

st.title("🚀 AI Test Failure Prediction Dashboard")

uploaded_file = st.file_uploader("Upload Test Results CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Data")
    st.dataframe(df)

    model, encoder = train_model(df)

    st.write("### Failure Risk Prediction")

    df_copy = df.copy()
    df_copy["module"] = encoder.transform(df_copy["module"])
    X = df_copy[["module", "execution_time", "previous_failures", "build_number"]]

    predictions = model.predict(X)
    df["Predicted_Failure"] = predictions

    st.dataframe(df)

    high_risk = df[df["Predicted_Failure"] == 1]

    st.write("### 🔴 High Risk Test Cases")
    st.dataframe(high_risk)

    st.success("Model trained and predictions generated!")
