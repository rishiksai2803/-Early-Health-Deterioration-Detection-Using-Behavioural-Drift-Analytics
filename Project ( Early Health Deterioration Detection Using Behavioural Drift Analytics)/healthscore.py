def evaluate_health(drift_score):
    weight = 10
    health_score = 100 - (drift_score * weight)

    if health_score >= 80:
        risk = "Normal"
    elif health_score >= 60:
        risk = "Moderate Risk"
    else:
        risk = "High Risk"

    return round(health_score,2), risk