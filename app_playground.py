import streamlit as st
import numpy as np
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
import pandas.util.testing as testing
np.random.seed(1)

 # Setting the rows and columns of the desired data

def get_fake_timseries():
    testing.N, testing.K = 300, 4 # Setting the rows and columns of the desired data
    df = testing.makeTimeDataFrame(freq='D')
    df.columns = ['Brazil', 'Argentina', 'USA', 'Japan']
    df.index.name = 'dt'
    df = df.reset_index()
    return df
    
def app():
    # Sidebar
    st.sidebar.title("Example App")
    country = st.sidebar.selectbox('Select country', ['Brazil', 'Argentina','USA', 'Japan'])
    
    # Main content
    st.title("Dashboard")
    st.subheader("Dataset:")
    df = get_fake_timseries();
    st.write(df.head(5))
    
    # Plotting a chart
    st.subheader(f"{country} - daily death ratio:")
    fig, ax = plt.subplots()
    sns.lineplot(x='dt', y=country, data=df)
    st.pyplot(fig)

if __name__ == "__main__":
    # command to run the app: streamlit run app.py
    app()