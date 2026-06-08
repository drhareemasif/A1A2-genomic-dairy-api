import streamlit as st
import pandas as pd

# 1. Set up a beautiful page title and header
st.set_page_config(page_title="Genomic Precision Dairy Dashboard", page_icon="🐄")
st.title("🧬 Genomic Precision Dairy Platform")
st.subheader("Automated A1/A2 Genotyping & Breeding Insights")

st.markdown("---")

# 2. Create a drag-and-drop file upload box
uploaded_file = st.file_uploader("Upload your raw laboratory diagnostic sheet (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    # Read the uploaded excel sheet instantly
    df = pd.read_excel(uploaded_file)
    
    # Check if the required columns exist
    if 'Animal_ID' in df.columns and 'Genotype' in df.columns:
        st.success("🎯 File successfully uploaded and parsed!")
        
        # 3. Add your veterinary breeding logic right here
        def get_recommendation(genotype):
            if genotype == "A2A2":
                return "Ideal for pure A2 milk production. Retain for elite breeding core."
            elif genotype == "A1A2":
                return "Carrier. Mating recommended exclusively with homozygous A2A2 sires."
            elif genotype == "A1A1":
                return "High A1 risk profile. Consider culling from premium production tracks."
            else:
                return "Unknown genotype. Re-run high-throughput molecular assay."

        # Apply the logic to create a new column
        df['Breeding_Recommendation'] = df['Genotype'].apply(get_recommendation)
        
        # 4. Display interactive metrics and graphs automatically
        total_processed = len(df)
        a2a2_count = len(df[df['Genotype'] == 'A2A2'])
        
        col1, col2 = st.columns(2)
        col1.metric("Total Animals Processed", total_processed)
        col2.metric("Pure A2A2 Animals Found", a2a2_count)
        
        # 5. Show the interactive, filtered data table to the user
        st.markdown("### 📋 Generated Herd Advisory Report")
        st.dataframe(df)
        
        # 6. Let the user download the finished report as a clean Excel file
        st.download_button(
            label="📥 Download Structured Report",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name="herd_advisory_report.csv",
            mime="text/csv"
        )
    else:
        st.error("❌ Invalid sheet format. Must contain 'Animal_ID' and 'Genotype' columns.")