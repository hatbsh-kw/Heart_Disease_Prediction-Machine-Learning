from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles  # Corrected import
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Serve static files from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load the saved model and scaler
model = joblib.load('svm_heart_disease_model.joblib')
scaler = joblib.load('scaler.joblib')

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define the input data model using Pydantic
class HeartDiseaseInput(BaseModel):
    age: float
    sex: int
    chest_pain_type: int
    resting_blood_pressure: float
    serum_cholestoral: float
    fasting_blood_sugar: int
    resting_ecg: int
    max_heart_rate: float
    exercise_induced_angina: int
    oldpeak: float
    slope: int
    num_major_vessels: int
    thal: int

# Prediction endpoint
@app.post("/predict/")
async def predict(
    request: Request,
    age: float = Form(...),
    sex: int = Form(...),
    chest_pain_type: int = Form(...),
    resting_blood_pressure: float = Form(...),
    serum_cholestoral: float = Form(...),
    fasting_blood_sugar: int = Form(...),
    resting_ecg: int = Form(...),
    max_heart_rate: float = Form(...),
    exercise_induced_angina: int = Form(...),
    oldpeak: float = Form(...),
    slope: int = Form(...),
    num_major_vessels: int = Form(...),
    thal: int = Form(...),
):
    # Convert input data to a numpy array
    data = np.array([[ 
        age, sex, chest_pain_type, resting_blood_pressure,
        serum_cholestoral, fasting_blood_sugar, resting_ecg,
        max_heart_rate, exercise_induced_angina, oldpeak,
        slope, num_major_vessels, thal
    ]])

    # Scale the input data
    scaled_data = scaler.transform(data)

    # Make a prediction using the model
    prediction = model.predict(scaled_data)
    prediction_label = "Presence" if prediction[0] == 1 else "Absence"

    # Render the prediction result in the template
    return templates.TemplateResponse("result.html", {"request": request, "prediction": prediction_label})

# Root endpoint
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})
