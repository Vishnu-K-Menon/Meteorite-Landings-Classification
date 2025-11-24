<p align="center">
  <img src="assets/logo.png" alt="Meteorite Landings Classification Logo" width="160"/>
</p>

<h1 align="center">Meteorite Landings Classification 🪐</h1>

<p align="center">
  <img src="https://github.com/Vishnu-K-Menon/Meteorite-Landings-Classification/actions/workflows/ci.yml/badge.svg" alt="CI Status">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+">
  <img src="https://img.shields.io/github/license/Vishnu-K-Menon/Meteorite-Landings-Classification" alt="License MIT">
  <img src="https://img.shields.io/github/stars/Vishnu-K-Menon/Meteorite-Landings-Classification?style=social" alt="Stars">
</p>

---

This project implements an end-to-end machine learning pipeline to classify meteorites into broad categories using the **NASA Meteorite Landings** dataset.

The system includes:

- Data cleaning & validation  
- Feature engineering  
- Mapping NASA `recclass` labels to **6 macro meteorite types**  
- Training multiple ML models (Random Forest, Gradient Boosting, SVM)  
- Training a PyTorch fully-connected neural network  
- Saving trained models for reuse via a `predict.py` script  

The codebase is fully modular with a clean `/src` directory.

---

## 🚀 Features

- **End-to-end ML workflow** from raw CSV → trained models  
- **Robust preprocessing** (type fixing, missing value imputation, year filtering)  
- **Feature scaling & transformation**  
- **Model comparison** across classical ML and neural networks  
- **Reusable model weights** stored in `/models`  
- **Notebook + script versions** for maximum reproducibility  

---

## 📁 Repository Structure

```text
.
├─ assets/
│  └─ logo.png                     # Project logo
│
├─ Data/
│  ├─ raw/
│  │  └─ Meteorite_Landings.csv    # Raw NASA dataset
│  └─ processed/
│     └─ Preprocessed_Meteorite_Landings.csv
│
├─ models/
│  ├─ gradient_boosting_model.pkl
│  ├─ svc_model.pkl
│  └─ meteorite_land_nn_weights.pth
│
├─ notebook/
│  ├─ 01_meteorite_preprocessing.ipynb
│  └─ 02_meteorite_classification.ipynb
│
├─ src/
│  ├─ data_preprocessing.py        # Data cleaning & processing
│  ├─ feature_engineering.py       # Feature engineering utilities
│  ├─ neural_net.py                # PyTorch NN model
│  ├─ train_models.py              # Train/evaluate all models
│  ├─ predict.py                   # Load model + run inference
│  └─ utils.py                     # Shared helpers
│
├─ requirements.txt
├─ LICENSE
├─ .gitignore
└─ README.md
```
📊 Dataset

The dataset used is:

NASA — Meteorite Landings Dataset

Expected file location:
Data/raw/Meteorite_Landings.csv

Preprocessing produces:
Data/processed/Preprocessed_Meteorite_Landings.csv

🧠 Models Included

Random Forest

Gradient Boosting

Support Vector Machine (RBF)

PyTorch fully-connected neural network

Evaluation includes:

Accuracy score

Classification report

Confusion matrices

Comparison across models

📜 License

This project is licensed under the MIT License.
See LICENSE for details.

---

# 🚀 You're All Set  
Just paste the above into your README and push — it will render beautifully.

If you want:

✅ an architecture diagram  
✅ a demo GIF  
✅ multiple logo styles  
✅ a “Model Performance” table  
— I can generate them for you.
