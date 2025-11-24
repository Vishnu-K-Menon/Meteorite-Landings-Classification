<p align="center">
  <img src="assets/logo.png" alt="Meteorite Landings Classification Logo" width="160"/>
</p>

<h1 align="center">Meteorite Landings Classification 🪐</h1>

<p align="center">
  <img src="https://github.com/Vishnu-K-Menon/Meteorite-Landings-Classification/actions/workflows/ci.yml/badge.svg" alt="CI Status">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python">
  <img src="https://img.shields.io/github/license/Vishnu-K-Menon/Meteorite-Landings-Classification" alt="MIT License">
  <img src="https://img.shields.io/github/stars/Vishnu-K-Menon/Meteorite-Landings-Classification?style=social" alt="Stars">
</p>


## Contents

- [Project overview](#project-overview)
- [Dataset](#dataset)
- [Repository structure](#repository-structure)
- [Installation](#installation)
- [How to run](#how-to-run)
  - [1. Using Python scripts (recommended)](#1-using-python-scripts-recommended)
  - [2. Using Jupyter notebooks](#2-using-jupyter-notebooks)
- [Models](#models)
- [Pipeline architecture](#pipeline-architecture)
- [Demo](#demo)
- [Future improvements](#future-improvements)
- [License](#license)

---

## Project overview

This project explores supervised learning on meteorite landings to predict **coarse meteorite types** from physical and geospatial features.

Key steps:

- **Data preprocessing**
  - Clean missing / invalid values (mass, year, coordinates, etc.)
  - Filter out impossible years and obviously corrupted entries
- **Feature engineering**
  - One-hot encode categorical columns
  - Scale numeric features
  - Map detailed `recclass` values to 6 macro classes:
    - Chondrites  
    - Achondrites  
    - Iron meteorites  
    - Stony-iron meteorites  
    - Lunar meteorites  
    - Martian meteorites
- **Modeling**
  - Classical ML: Random Forest, Gradient Boosting, SVM (RBF)
  - A fully-connected PyTorch neural network
- **Export**
  - Persist trained models for reuse in `models/`
  - Provide a simple `predict.py` script for inference

---

## Dataset

The project uses the publicly available **NASA Meteorite Landings** dataset.

Expected layout:

```text
Data/
├─ raw/
│  └─ Meteorite_Landings.csv        # original dataset
└─ processed/
   └─ Preprocessed_Meteorite_Landings.csv  # created by preprocessing step
You can download the CSV from NASA’s open data portal and place it in Data/raw/ as Meteorite_Landings.csv.

Repository structure
text
Copy code
.
├─ Data/
│  ├─ raw/
│  │  └─ Meteorite_Landings.csv
│  └─ processed/
│     └─ Preprocessed_Meteorite_Landings.csv
├─ models/
│  ├─ gradient_boosting_model.pkl
│  ├─ svc_model.pkl
│  └─ meteorite_land_nn_weights.pth
├─ notebook/
│  ├─ 01_meteorite_preprocessing.ipynb
│  └─ 02_meteorite_classification.ipynb
├─ src/
│  ├─ data_preprocessing.py      # load raw CSV, clean & save processed data
│  ├─ feature_engineering.py     # feature transforms & encoders
│  ├─ neural_net.py              # PyTorch model definition
│  ├─ train_models.py            # train/evaluate RF, GBM, SVM, NN
│  ├─ predict.py                 # load saved model(s) and run inference
│  └─ utils.py                   # shared helpers
├─ assets/
│  ├─ logo.png                   # project logo (optional)
│  ├─ pipeline_diagram.png       # architecture diagram (optional)
│  └─ demo.gif                   # short demo gif (optional)
├─ README.md
├─ requirements.txt
├─ .gitignore
└─ LICENSE
The scripts in src/ mirror what’s in the notebooks, making it easier to reuse this project as a library or component in other work.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Vishnu-K-Menon/Meteorite-Landings-Classification.git
cd Meteorite-Landings-Classification
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
# or
.\.venv\Scripts\activate       # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
How to run
1. Using Python scripts (recommended)
1.1 Preprocess the raw data
Make sure the raw CSV is at:

text
Copy code
Data/raw/Meteorite_Landings.csv
Then run:

bash
Copy code
python src/data_preprocessing.py
This will create the cleaned dataset:

text
Copy code
Data/processed/Preprocessed_Meteorite_Landings.csv
(If the script exposes command-line arguments, see the top of data_preprocessing.py for details.)

1.2 Train and evaluate models
bash
Copy code
python src/train_models.py
This script:

Loads the processed CSV

Performs train/test split and scaling

Trains:

Random Forest

Gradient Boosting

SVM (RBF kernel)

PyTorch neural network

Prints metrics (accuracy, classification reports, confusion matrices)

Saves trained artifacts to models/:

gradient_boosting_model.pkl

svc_model.pkl

meteorite_land_nn_weights.pth

1.3 Run predictions
Once models are trained, you can run quick predictions using:

bash
Copy code
python src/predict.py
predict.py loads the appropriate model and runs inference on example samples (or on a file, depending on how you configure it in the script).

2. Using Jupyter notebooks
If you prefer a more exploratory workflow:

Start Jupyter:

bash
Copy code
jupyter notebook
Open and run:

notebook/01_meteorite_preprocessing.ipynb

Cleans the raw data and writes Preprocessed_Meteorite_Landings.csv.

notebook/02_meteorite_classification.ipynb

Trains all the models, reports metrics, and saves trained weights.

Models
The repository currently trains and compares:

Random Forest

Gradient Boosting

Support Vector Machine (RBF kernel)

Fully-connected neural network (PyTorch)

Typical evaluation includes:

Train/test split using train_test_split

Feature scaling with StandardScaler

Metrics:

Overall accuracy

Per-class precision/recall/F1 (classification_report)

Confusion matrices (via seaborn heatmaps)

You can adapt train_models.py to log additional metrics or to run cross-validation/hyperparameter search.

Pipeline architecture
Add an architecture diagram in assets/pipeline_diagram.png and it will be rendered here:

markdown
Copy code
![Pipeline overview](assets/pipeline_diagram.png)
Suggested blocks for the diagram:

Raw data ingestion (NASA CSV)

Data preprocessing (cleaning, filtering, type conversion)

Feature engineering (encoding, scaling, target mapping)

Model training (RF / GBM / SVM / NN)

Model selection & evaluation

Saved artifacts + predict.py inference

Demo
You can capture a short terminal or notebook run as a GIF and place it at assets/demo.gif.
It will show up here:

markdown
Copy code
![Demo of training + prediction](assets/demo.gif)
Future improvements
Add a proper CI pipeline (GitHub Actions) so the build badge reflects real test status

Hyperparameter tuning with cross-validation

Model comparison report and visualization

Simple FastAPI/Streamlit app wrapping predict.py

Geospatial visualizations of meteorite landings on a map

License
This project is licensed under the MIT License – see LICENSE for details.

arduino
Copy code










