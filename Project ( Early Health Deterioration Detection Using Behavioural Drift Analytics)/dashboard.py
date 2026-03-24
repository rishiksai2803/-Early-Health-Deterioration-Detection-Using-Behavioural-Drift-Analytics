import streamlit as st
import pandas as pd
from preprocessing import preprocess_data
from drift_analysis import calculate_baseline, calculate_drift
from health_evaluation import evaluate_health

st.title("🧠 Behavioural Drift Health Monitoring System")

# Load data
df = preprocess_data()

st.subheader("📊 Dataset")
st.dataframe(df)

# Calculate
baseline = calculate_baseline(df)
drift, drift_score, current = calculate_drift(df, baseline)
health_score, risk = evaluate_health(drift_score)

# Show results
st.subheader("📈 Results")

st.write("### Drift Score:", round(drift_score,2))
st.write("### Health Score:", health_score)
st.write("### Risk Level:", risk)

# Bar chart
st.subheader("📊 Behaviour Comparison")

comparison = pd.DataFrame({
    "Baseline": baseline,
    "Current": current
})

st.bar_chart(comparison)