import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

def split_and_scale(df):
    X = df[['mass (g)', 'reclat', 'reclong', 'year']]
    y = df['classification_type']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test, scaler


def train_gradient_boosting(X_train, y_train):
    model = GradientBoostingClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, "models/gradient_boosting_model.pkl")
    return model


def train_svm(X_train, y_train):
    model = SVC(probability=True)
    model.fit(X_train, y_train)
    joblib.dump(model, "models/svc_model.pkl")
    return model
