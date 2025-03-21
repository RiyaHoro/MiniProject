from django.shortcuts import render
from django.conf import settings
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# ✅ Load dataset ONCE at startup (prevents reloading on every request)
csv_path = os.path.join(settings.BASE_DIR, 'Diabetes_prediction', 'diabetes.csv')
data = pd.read_csv(csv_path)

# ✅ Prepare dataset
X = data.drop("Outcome", axis=1)
Y = data["Outcome"]

# ✅ Train the model ONCE at startup
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, Y_train)

# ✅ Define feature names to avoid `UserWarning`
FEATURE_NAMES = X.columns.tolist()


def home(request):
    return render(request, 'home.html')


def predict(request):
    return render(request, 'predict.html')


def result(request):
    try:
        # ✅ Safely get input values (avoids KeyError)
        val1 = float(request.GET.get('n1', 0))
        val2 = float(request.GET.get('n2', 0))
        val3 = float(request.GET.get('n3', 0))
        val4 = float(request.GET.get('n4', 0))
        val5 = float(request.GET.get('n5', 0))
        val6 = float(request.GET.get('n6', 0))
        val7 = float(request.GET.get('n7', 0))
        val8 = float(request.GET.get('n8', 0))

        # ✅ Convert input to DataFrame with correct column names
        input_data = pd.DataFrame([[val1, val2, val3, val4, val5, val6, val7, val8]], columns=FEATURE_NAMES)

        # ✅ Make prediction
        pred = model.predict(input_data)
        result2 = "Positive" if pred[0] == 1 else "Negative"

    except Exception as e:
        result2 = f"Error: {str(e)}"

    return render(request, 'predict.html', {"result2": result2})
