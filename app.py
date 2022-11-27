import streamlit as st
import pandas as pd
import numpy as np
import pickle

def main():
    st.title("kategori")
    
    menu=["Gender","Married","ApplicantIncome","LoanAmount","Credit_History"]
    Choice= st.sidebar.selectbox("Menu",menu)
     if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
 
    LoanAmount = LoanAmount / 1000
