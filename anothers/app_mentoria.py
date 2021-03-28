import streamlit as st
import numpy as np
import pandas as pd
import joblib
import base64

#CSV -> uiashdouashudash1892389jsndijashd88h21893iojiojsiodaj891231893onaosndsaod1023901092312093

def load_model_pipeline():
    return joblib.load("models/model_v0.joblib")

def get_default_prediction(pipeline, features):
    X = pd.DataFrame([features])
    y = pipeline.predict_proba(X)
    y = y[0]
    probability = y[1] # classe positiva
    return X, probability

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    print(b64)
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

def app():
    pg_engine = return_db_con()
    pipeline = load_model_pipeline();
    
    st.sidebar.title("Loan default 2")
    
    # input features dictionary
    features = {}
    
    # Check here for the streamlit sheet cheat: https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
    st.sidebar.subheader("Client info teste:")
    features["client_gender"] = st.sidebar.radio('Gender:', ["M", "F", "I"])
    features["client_age"] = st.sidebar.slider('Client age(years):', 21, 100, 50)
    features["acc_age"] = st.sidebar.slider('Account age(years):', 10, 50, 25)
    
    st.sidebar.subheader("Loan info:")
    features["loan_amount"] = st.sidebar.slider('Loan amount($):', 1000, 1000000, 100000, step=1000)
    features["loan_duration"] = st.sidebar.slider('Loan duration(days):', 12, 60, 30)
    
    # District name, Region name, District population, District avg. income
    district_options = [
        ("Hl.m. Praha", "Prague", "1204953", "12541"),
        ("Karvina", "north Moravia", "285387", "10177"),
        ("Brno - mesto", "south Moravia", "387570", "9897"),
        ("Ostrava - mesto", "north Moravia", "323870", "10673"),
        ("Zlin", "south Moravia", "197099", "9624")
    ]
    
    district = st.sidebar.selectbox("District:", district_options, format_func=lambda x: x[0])
    
    features["district_name"] = district[0]
    features["district_region"] = district[1]
    features["district_inhabitants"] = district[2]
    features["district_avg_salary"] = district[3]

    X, y_pred = get_default_prediction(pipeline, features)
    
    st.subheader('Features: ')
    st.write(X)
    
    st.subheader(f"Probability of default: {round(y_pred,2)}")
    
    X.to_csv('data/out.csv')
    
    '''
    # X is our input dataframe
    #st.markdown(get_table_download_link(X), unsafe_allow_html=True)
    if st.button('Send email'):
        send_email(X)
        print('email sent')
        # insert(X, pg_engine)
        # add db insert function inser(X)
    '''

if __name__ == "__main__":
    # command to run the app: streamlit run app.py
    app()