# ER-HER2-BC_Grade_Classification
Intepretable grade prediction pipeline for ER+/HER2- breast cancer using an 8-gene signature. Includes classification, clustering, survival analysis, OCR-based grade extraction, and LLM-powered clinical reporting.

## 🧬 Overview

This repository implements a complete and interpretable pipeline for predicting histological tumor grade in ER+/HER2- breast cancer patients.  
Key components include:

- Feature selection and grade classification using METABRIC gene expression data.
- Unsupervised clustering and validation on TCGA samples.
- Integration of OCR-derived clinical annotations from pathology reports.
- Survival analysis (OS, RFS, DFI, PFI).
- Model explainability using SHAP.
- Report generation using Large Language Models (LLMs) for both patients and clinicians.

---

## 📂 Repository Structure

```plaintext
.
├── data/
│   ├── METABRIC_expression_clinical.csv
│   ├── TCGA_expression_clinical_clusters.csv
│   └── TCGA_OCR_grades.csv
│
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
├── models/
│   ├── distilled_model.pkl
│   └── tree_ensemble_summary.json
│
├── reports/
│   ├── patient_report_example.txt
│   ├── clinician_report_example.txt
│   ├── SHAP_summary_patient_62.png
│   └── Radar_plot_patient_62.png
│
├── llm_prompts/
│   ├── doctor_prompt.md
│   └── patient_prompt.md
│
└── README.md
