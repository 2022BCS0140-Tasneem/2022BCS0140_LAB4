from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Create FastAPI app
app = FastAPI(title="Wine Quality Prediction API")

# Load trained model
model = joblib.load("model.pkl")

# Input schema
class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

# Root endpoint
@app.get("/")
def home():
    return {"message": "Wine Quality Inference API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(features: WineFeatures):
    data = np.array([[
        features.fixed_acidity,
        features.volatile_acidity,
        features.citric_acid,
        features.residual_sugar,
        features.chlorides,
        features.free_sulfur_dioxide,
        features.total_sulfur_dioxide,
        features.density,
        features.pH,
        features.sulphates,
        features.alcohol
    ]])

    prediction = model.predict(data)

    return {
        "name": "Tasneem Kousar",
        "roll_no": "2022BCS0140",
        "wine_quality": int(round(prediction[0]))
    }
