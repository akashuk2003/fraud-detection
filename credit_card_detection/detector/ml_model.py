import joblib
import numpy as np

model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

def predict_fraud(amount, hour, tx_type, merchant, location, freq):
    # Build realistic feature vector (30 features)
    features = [
        hour,            # Time
        tx_type * 2,     # Online risk
        merchant * 3,    # Merchant risk
        location * 2,    # Location anomaly
        freq * 1.5       # Frequency spike
    ]

    # Fill remaining PCA-like features safely
    while len(features) < 29:
        features.append(0)

    features.append(amount)

    features = np.array(features).reshape(1, -1)
    features = scaler.transform(features)

    prob = model.predict_proba(features)[0][1]

    result = "FRAUD" if prob > 0.6 else "NOT FRAUD"
    return result, round(prob, 2)