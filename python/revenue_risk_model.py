def assign_risk(score):
    if score >= 8000:
        return "Low Risk"
    elif score >= 3000:
        return "Medium Risk"
    else:
        return "High Risk"
