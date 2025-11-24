# Meteorite Landings Classification 🪐

This project builds a full machine learning pipeline to classify meteorites into broad types using the **NASA Meteorite Landings** dataset. It covers:

- Data cleaning, imputation, and feature engineering
- Grouping detailed `recclass` labels into 6 macro meteorite types
- Training classical ML models (Random Forest, Gradient Boosting, SVM)
- Training a simple feed-forward neural network in PyTorch
- Exporting trained models for reuse

> All the logic currently lives in Jupyter notebooks so it’s easy to follow step-by-step.

---

## Project structure

```text
meteorite-landings-classification/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ LICENSE
├─ data/
│  ├─ raw/
│  │  └─ Meteorite_Landings.csv
│  └─ processed/
│     └─ Preprocessed_Meteorite_Landings.csv
├─ notebooks/
│  ├─ 01_meteorite_preprocessing.ipynb
│  └─ 02_meteorite_classification.ipynb
├─ models/
│  ├─ gradient_boosting_model.pkl
│  ├─ svc_model.pkl
│  └─ meteorite_land_nn_weights.pth
└─ src/   # (optional if you later refactor notebooks into scripts)
