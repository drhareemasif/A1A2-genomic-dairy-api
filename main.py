from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io

app = FastAPI(title="Genomic Precision Dairy API")

def generate_recommendation(genotype: str) -> str:
    genotype = str(genotype).strip().upper()
    if genotype == "A2A2":
        return "Ideal for pure A2 milk production. Retain for elite breeding core."
    elif genotype == "A1A2":
        return "Carrier. Mating recommended exclusively with homozygous A2A2 sires."
    elif genotype == "A1A1":
        return "High A1 risk profile. Consider culling from premium production tracks."
    else:
        return "Unknown genotype. Re-run high-throughput molecular assay."

@app.post("/upload-diagnostics/")
async def process_diagnostic_sheet(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        if file.filename.endswith('.csv'):
            df = pd.read_csv(io.BytesIO(contents))
        else:
            df = pd.read_excel(io.BytesIO(contents))
        
        if 'Animal_ID' not in df.columns or 'Genotype' not in df.columns:
            return {"error": "Invalid sheet format. Must contain 'Animal_ID' and 'Genotype' columns."}
        
        df['Breeding_Recommendation'] = df['Genotype'].apply(generate_recommendation)
        result_json = df.to_dict(orient="records")
        
        return {
            "status": "Success",
            "filename": file.filename,
            "total_animals_processed": len(df),
            "data": result_json
        }
    except Exception as e:
        return {"error": f"Failed to process file: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)