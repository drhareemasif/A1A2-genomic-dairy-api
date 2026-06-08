import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Genomic Precision Dairy Dashboard", page_icon="🐄")
st.title("🐄 Genomic Precision Dairy Platform")
st.subheader("Automated A1/A2 Genotyping & Breeding Insights")

st.markdown("---")

# The upload widget
uploaded_file = st.file_uploader("Upload your raw laboratory diagnostic sheet (.xlsx)", type=["xlsx"])

# THE GUARD: Only process the file if it has been uploaded
if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.write(df)
    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload your .xlsx file to view the dashboard.")
