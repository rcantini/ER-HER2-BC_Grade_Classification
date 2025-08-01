# ER+/HER2- Breast Cancer Grade Classification Using Machine Learning
> Intepretable grade prediction pipeline for **ER+/HER2- Breast Cancer** using an **8-gene signature**. It includes classification, clustering, survival analysis, knowledge distillation, OCR-based grade extraction, and LLM-powered clinical reporting.

## 🧬 Overview

This repository implements an effective and interpretable pipeline for predicting histological tumor grade in ER+/HER2- breast cancer patients.  

Key components include:
- Feature selection and grade classification using METABRIC gene expression data.
- Clustering analysis on TCGA samples.
- Survival analysis and statistical validation.
- Integration of OCR-extracted clinical annotations from pathology reports.
- Model explainability using SHAP.
- Report generation using Large Language Models (LLMs) for both patients and clinicians.


## 📂 Repository Structure

```plaintext
.
├── LLM-generated-reports/
│   ├── Gemini_2.0-Flash (reports and prompts)
│   ├── GPT-4o (reports and prompts)
│   └── experts_evaluation.xlsx (full per-patient and per-dimension scores)
│
├── notebooks/
│   ├── METABRIC_classification.ipynb
│   ├── TCGA_clustering_ER+.ipynb
│   └── metrics.ipynb
│
├── scripts/
│   ├── METABRIC_analysis.R
│   ├── TCGA_analysis.R
│   ├── download_reports.py
│   └── reports_filtering.py
│
├── TCGA_OCR_grades.csv (OCR-extracted grade information for TCGA)
└── README.md
```

## 📝 OCR-Based Grade Extraction

To foster further research, grade information for TCGA patients – extracted via OCR from unstructured, multipage PDF pathology reports – is provided in the `TCGA_OCR_grades.csv` file. Used reports are publicly available online at this [link](https://github.com/inodb/datahub/tree/add-symlink-path-report/tcga/pathology_reports).

## 📊 Expert Evaluations of LLM-Generated Clinical Reports

Reports were manually evaluated by domain experts on a 0–5 Likert scale (0 = poor, 5 = excellent) across four criteria:
- *Clinical clarity* – Is the interpretation clear, understandable, and clinically meaningful?
- *Scientific accuracy* – Are the genetic contributors correctly explained in the context of breast cancer biology?
- *Clinical utility* – Does the report support clinical decision-making?
- *Structural readability* – Is the report logically organized and easy to read?

An *overall quality* score was also computed as the mean of these four. To reduce bias, LLMs were anonymized as *LLM A* and *LLM B* during evaluation. The actual model identities are disclosed in the file post-evaluation.

See [`experts_evaluation.xlsx`](./experts_evaluation.xlsx) for:
- Scores achieved per patient and criterion  
- Post-evaluation model mapping  


## ✉️ Contact

For questions, collaborations, or support, feel free to contact:
- *Riccardo Cantini* – [riccardo.cantini@unical.it](mailto:riccardo.cantini@unical.it)  
- *Marianna Talia* – [marianna.talia@unical.it](mailto:marianna.talia@unical.it)
