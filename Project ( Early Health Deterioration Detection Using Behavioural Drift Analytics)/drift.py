def calculate_baseline(df):
    baseline = df.iloc[:7].mean()
    return baseline

def calculate_drift(df, baseline):
    current = df.iloc[-1]

    drift = abs(current - baseline)

    drift_score = drift.mean()

    return drift, drift_score, current