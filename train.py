from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

import pandas as pd
import category_encoders as ce
import joblib

CAT_COLS = ["client_gender", "district_name", "district_region"]
NUM_COLS = ["loan_amount", "loan_duration", "acc_age", "client_age", "district_inhabitants", "district_avg_salary"]
TARGET = "bad_payer"

def load_data():
    df = pd.read_csv("data/dataset.csv")
    X = df[CAT_COLS + NUM_COLS]
    y = df[TARGET]
    return X, y

def get_model_pipeline():
    # Check: # https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html
    categorical_transformer = Pipeline([
        ("TargetEncoder", ce.TargetEncoder())
    ])
   
    numeric_transformer = Pipeline([
        ("Imputer", SimpleImputer(strategy="mean")),
        ("Scaler", StandardScaler())
    ])
    
    preprocessor = ColumnTransformer([
        ("categorical", categorical_transformer, CAT_COLS),
        ("numeric", numeric_transformer, NUM_COLS),
    ])

    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                          ('classifier', LogisticRegression())])
    return pipeline


def main():
    print("[INFO] Start train script...")
    
    print("[INFO] Loading the data...")
    X, y = load_data()
    
    print("[INFO] Training the model...")
    pipeline = get_model_pipeline()
    pipeline.fit(X, y)
    
    print("[INFO] Saving the model pipeline artifact...")
    joblib.dump(pipeline, 'models/model_v0.joblib') 
    
    print("[INFO] train script ended")

if __name__ == "__main__":
    main()