# app_streamlit.py
import streamlit as st
from joblib import load

# Load the pre-trained RandomForest model
model_path = "models/model.joblib"
model = load(model_path)

def predict(features):
    # Make predictions using the loaded model
    prediction = model.predict_proba([features])
    return prediction

def main():
    st.title("Machine Learning Model Prediction")

    # User input form
    Time = st.slider("Time", min_value=0.0, max_value=10.0, value=5.0)
    V1 = st.slider("V1", min_value=-10.0, max_value=10.0, value=5.0)
    V2 = st.slider("V2", min_value=-50.0, max_value=10.0, value=5.0)
    V3 = st.slider("V3", min_value=-20.0, max_value=10.0, value=5.0)
    V4 = st.slider("V4", min_value=0.0, max_value=10.0, value=5.0)
    V5 = st.slider("V5", min_value=0.0, max_value=10.0, value=5.0)
    V6 = st.slider("V6", min_value=0.0, max_value=10.0, value=5.0)
    V7 = st.slider("V7", min_value=0.0, max_value=10.0, value=5.0)
    V8 = st.slider("V8", min_value=0.0, max_value=10.0, value=5.0)
    V9 = st.slider("V9", min_value=0.0, max_value=10.0, value=5.0)
    V10 = st.slider("V10", min_value=0.0, max_value=10.0, value=5.0)
    V11 = st.slider("V11", min_value=0.0, max_value=10.0, value=5.0)
    V12 = st.slider("V12", min_value=0.0, max_value=10.0, value=5.0)
    V13 = st.slider("V13", min_value=0.0, max_value=10.0, value=5.0)
    V14 = st.slider("V14", min_value=0.0, max_value=10.0, value=5.0)
    V15 = st.slider("V15", min_value=0.0, max_value=10.0, value=5.0)
    V16 = st.slider("V16", min_value=0.0, max_value=10.0, value=5.0)
    V17 = st.slider("V17", min_value=0.0, max_value=10.0, value=5.0)
    V18 = st.slider("V18", min_value=0.0, max_value=10.0, value=5.0)
    V19 = st.slider("V19", min_value=0.0, max_value=10.0, value=5.0)
    V20 = st.slider("V20", min_value=0.0, max_value=10.0, value=5.0)
    V21 = st.slider("V21", min_value=0.0, max_value=10.0, value=5.0)
    V22 = st.slider("V22", min_value=0.0, max_value=10.0, value=5.0)
    V23 = st.slider("V23", min_value=0.0, max_value=10.0, value=5.0)
    V24 = st.slider("V24", min_value=0.0, max_value=10.0, value=5.0)
    V25 = st.slider("V25", min_value=0.0, max_value=10.0, value=5.0)
    V26 = st.slider("V26", min_value=0.0, max_value=10.0, value=5.0)
    V27 = st.slider("V27", min_value=0.0, max_value=10.0, value=5.0)
    V28 = st.slider("V28", min_value=0.0, max_value=10.0, value=5.0)
    Amount = st.slider("Amount", min_value=0.0, max_value=1000.0, value=5.0)

    if st.button("Predict"):
        features = [Time,
                V1,
                V2,
                V3,
                V4,
                V5,
                V6,
                V7,
                V8,
                V9,
                V10,
                V11,
                V12,
                V13,
                V14,
                V15,
                V16,
                V17,
                V18,
                V19,
                V20,
                V21,
                V22,
                V23,
                V24,
                V25,
                V26,
                V27,
                V28,
                Amount
                ]
        result = predict(features)
        st.success(f"The prediction is: {result}")

if __name__ == "__main__":
    main()

# streamlit run app_streamlit.py
