# Genomic Precision Dairy Management Platform API

An open-source diagnostic-to-digital pipeline designed to bridge the gap between raw molecular biology laboratory results and automated herd management systems. 

This functional Python prototype utilizes the **FastAPI** framework to automatically parse high-throughput laboratory sheets (Excel/CSV) for bovine A1/A2 $\beta$-casein variants, instantly executing a programmatic veterinary rule-set to yield actionable breeding strategies.

## 🧬 Diagnostic Logic Matrix
* **A2A2 (Homozygous):** Ideal for pure A2 milk production. Retained for elite breeding core.
* **A1A2 (Heterozygous):** Carrier status. Automated mating recommendation restricted exclusively to homozygous A2A2 sires to transition herd profiles.
* **A1A1 (Homozygous Risk):** High A1 risk profile. Flagged for potential separation or culling tracks from premium production channels.

## 💻 Local Deployment Instructions

### Prerequisites
Ensure you have Python installed on your machine. Install the required dependencies using the command prompt:
```bash
pip install fastapi uvicorn pandas openpyxl pillow python-multipart
python main.py
http://127.0.0.1:8000/docs
