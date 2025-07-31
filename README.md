# ER-HER2-BC_Grade_Classification
Intepretable grade prediction pipeline for ER+/HER2- breast cancer using an 8-gene signature. Includes classification, clustering, survival analysis, OCR-based grade extraction, and LLM-powered clinical reporting.

## 🧬 Overview

This repository implements a complete and interpretable pipeline for predicting histological tumor grade in ER+/HER2- breast cancer patients.  
Key components include:

- Feature selection and grade classification using METABRIC gene expression data.
- Unsupervised clustering and validation on TCGA samples.
- Integration of OCR-extracted clinical annotations from pathology reports.
- Survival analysis.
- Model explainability using SHAP.
- Report generation using Large Language Models (LLMs) for both patients and clinicians.


## 📂 Repository Structure

```plaintext
.
├── scripts/
│   ├── METABRIC_analysis.R
│   ├── TCGA_analysis.R
│   ├── download_reports.py
│   └── reports_filtering.py
│
├── notebooks/
│   ├── METABRIC_classification.ipynb
│   ├── TCGA_clustering_ER+.ipynb
│   └── metrics.ipynb
│
├── LLM-generated-reports/
│   ├── Gemini_2.0-Flash (reports and prompts)
│   ├── GPT-4o (reports and prompts)
|
└── `TCGA_OCR_grades.csv` – Contains OCR-extracted grade information for TCGA.
└── README.md
```

## 📝 OCR-Based Grade Extraction

Grade information for TCGA patients was extracted via OCR from unstructured, multipage PDF pathology reports is provided in the `TCGA_OCR_grades.csv` file. Used reports are publicly available online at this [link](https://github.com/inodb/datahub/tree/add-symlink-path-report/tcga/pathology_reports).
