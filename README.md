<p align="center">
  <img src="assets/logo.png" alt="Meteorite Landings Classification Logo" width="140">
</p>

<h1 align="center">Meteorite Landings Classification 🪐</h1>

<p align="center">
  <a href="https://github.com/Vishnu-K-Menon/Meteorite-Landings-Classification/actions/workflows/ci.yml">
    <img src="https://github.com/Vishnu-K-Menon/Meteorite-Landings-Classification/actions/workflows/ci.yml/badge.svg" alt="Build Status">
  </a>
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+">
  <a href="https://github.com/Vishnu-K-Menon/Meteorite-Landings-Classification/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Vishnu-K-Menon/Meteorite-Landings-Classification" alt="License: MIT">
  </a>
  <img src="https://img.shields.io/github/stars/Vishnu-K-Menon/Meteorite-Landings-Classification?style=social" alt="GitHub stars">
</p>

<p align="center">
  <img src="assets/demo.gif" alt="Meteorite Landings Classification Demo" width="700">
</p>



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
