import joblib
import torch
import numpy as np
from neural_net import MeteoriteNet

def predict_with_gb(df_row):
    model = joblib.load("models/gradient_boosting_model.pkl")
    return model.predict([df_row])[0]

def predict_with_svm(df_row):
    model = joblib.load("models/svc_model.pkl")
    return model.predict([df_row])[0]

def predict_with_nn(df_row):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = MeteoriteNet()
    model.load_state_dict(torch.load("models/meteorite_land_nn_weights.pth", map_location=device))
    model.eval()

    with torch.no_grad():
        x = torch.tensor(df_row, dtype=torch.float32).unsqueeze(0)
        preds = model(x)
        return preds.argmax().item()
