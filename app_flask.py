import streamlit as st
import numpy as np
import pandas as pd
import joblib
import base64
from flask import request
from flask import Flask

app = Flask(__name__)

CAT_COLS = ["client_gender", "district_name", "district_region"]
NUM_COLS = ["loan_amount", "loan_duration", "acc_age", "client_age", "district_inhabitants", "district_avg_salary"]

def load_model_pipeline():
    return joblib.load("models/model_v0.joblib")

def get_default_prediction(pipeline, features):
    X = pd.DataFrame([features])
    y = pipeline.predict_proba(X[CAT_COLS + NUM_COLS])
    y = y[0]
    probability = y[1] # classe positiva
    return X, probability

@app.route('/')
def hello_world():
    print('hello_world route')
    return 'Welcome to the Tera simple Machine Learning  API'

# Ex: http://localhost:5000/predict?loan_amount=50000&loan_duration=30
# Ex: http://localhost:5000/predict?loan_amount=25000&loan_duration=30
@app.route('/predict', methods=['GET'])
def predict():
    pipeline = load_model_pipeline();
    
    features = {}
    features["loan_amount"] = request.args.get('loan_amount')
    features["loan_duration"] = request.args.get('loan_duration')
    
    # These features is fixed to simplify the example
    features["client_gender"] = "M"
    features["client_age"] = "35"
    features["acc_age"] = "15"
    features["district_name"] = "Hl.m. Praha"
    features["district_region"] = "Prague"
    features["district_inhabitants"] = 1204953
    features["district_avg_salary"] = 12541
    
    X, y_pred = get_default_prediction(pipeline, features)
    
    result = {
        'prediction': round(y_pred, 4)
    }
    
    return result
    

if __name__ == "__main__":
    # command to run the flask app: export FLASK_APP=app_flask.py && flask run --host=0.0.0.0
    # command to run the flask app windows: set FLASK_APP=app_flask.py && flask run --host=0.0.0.0
    app.run(debug=True)