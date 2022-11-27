import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.write("""
# Loan Prediction App
This app predicts the **Palmer Penguin** species!
Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.
""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        sex = st.sidebar.selectbox('Sex',('male','female'))
        Marital Status= st.sidebar.selectbox('Marital Status',('Unmaried','maried'))
        Applicants monthly income = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
        Total loan amount = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
        Credit_History = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
        data = {'sex': sex,
                'Marital Status': Marital Status,
                'Applicants monthly income': Applicants monthly income,
                'Total loan amount': Total loan amount,
                'Credit_History': Credit_History}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

# Combines user input features with entire penguins dataset
# This will be useful for the encoding phase
penguins_raw = pd.read_csv('data.csv')
penguins = penguins_raw.drop(columns=['Credit_History'])
df = pd.concat([input_df,penguins],axis=0)
