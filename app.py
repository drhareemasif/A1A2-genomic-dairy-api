import streamlit as st
import pandas as pd

# The uploader widget
uploaded_file = st.file_uploader("Upload your raw laboratory diagnostic sheet (.xlsx)", type=["xlsx"])

# The guard condition to prevent the crash
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df)
else:
    st.warning("Please upload an Excel file to continue.")
