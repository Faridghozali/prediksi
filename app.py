import streamlit as st
import pandas as pd
import numpy as np
import pickle

def main():
    st.title("kategori")
    
    menu=["Gender","Married","ApplicantIncome","LoanAmount","Credit_History"]
    Choice= st.sidebar.selectbox("Menu",menu)
     if Choice == "Gender":
        st.subheader = ("Gender")
    else choice == "married":
        st.subheader =("Unmarried")
