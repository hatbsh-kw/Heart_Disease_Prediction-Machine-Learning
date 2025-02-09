Name= Habtamu kebede ID= 1401334

Deployed Website URL= https://heart-disease-prediction-machine-learning.onrender.com/

# Heart Disease Prediction FastAPI

This repository contains a FastAPI application that uses a Support Vector Machine (SVM) model for heart disease prediction. The model predicts whether an individual is likely to have heart disease ("Presence") or not ("Absence") based on various input features.

# Features

- A trained SVM model for heart disease prediction.
- A FastAPI application to serve the model as a web service.
- Provides a simple form to input data and get predictions.
- Includes deployment instructions for hosting on Render.

---

# Installation Instructions

1. Clone this repository to your local machine:

```bash
git clone [https://github.com/yourusername/heart-disease-prediction-api.git](https://github.com/hatbsh-kw/Heart_Disease_Prediction-Machine-Learning.git)
```

2. Navigate into the project directory:

```bash
cd heart-disease-prediction-api
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

4. Load the model and scaler files into your project directory.

---

# Running the Application Locally

1. Start the FastAPI application using Uvicorn:

```bash
uvicorn app:app --reload
```

2. The app will be available at `http://127.0.0.1:8000`.

3. Open your browser and go to `http://127.0.0.1:8000` to access the prediction form.

---

# POST /predict/

This endpoint predicts whether an individual has heart disease or not. It expects form data with the following fields:

- `age`: Age of the individual (float)
- `sex`: Gender (1 = male, 0 = female)
- `chest_pain_type`: Chest pain type (integer)
- `resting_blood_pressure`: Resting blood pressure (float)
- `serum_cholestoral`: Serum cholesterol (float)
- `fasting_blood_sugar`: Fasting blood sugar (binary, 1 = True, 0 = False)
- `resting_ecg`: Resting electrocardiographic results (integer)
- `max_heart_rate`: Maximum heart rate achieved (float)
- `exercise_induced_angina`: Exercise-induced angina (binary, 1 = Yes, 0 = No)
- `oldpeak`: Depression induced by exercise (float)
- `slope`: Slope of the peak exercise ST segment (integer)
- `num_major_vessels`: Number of major vessels colored by fluoroscopy (integer)
- `thal`: Thalassemia (integer)

---

#Test Cases for API

Here are some test cases you can use to test the FastAPI application, which will return the prediction result ("Presence" or "Absence"):

1. Test Case 1 - Presence of heart disease

   - Input:
     - `age`: 63
     - `sex`: 1 (Male)
     - `chest_pain_type`: 3
     - `resting_blood_pressure`: 145
     - `serum_cholestoral`: 233
     - `fasting_blood_sugar`: 1 (True)
     - `resting_ecg`: 0
     - `max_heart_rate`: 150
     - `exercise_induced_angina`: 0
     - `oldpeak`: 2.3
     - `slope`: 3
     - `num_major_vessels`: 0
     - `thal`: 2
   - Expected Output: **Presence**

2. Test Case 2 - Absence of heart disease
   - Input:
     - `age`: 52
     - `sex`: 0 (Female)
     - `chest_pain_type`: 2
     - `resting_blood_pressure`: 130
     - `serum_cholestoral`: 250
     - `fasting_blood_sugar`: 0 (False)
     - `resting_ecg`: 1
     - `max_heart_rate`: 175
     - `exercise_induced_angina`: 0
     - `oldpeak`: 1.2
     - `slope`: 2
     - `num_major_vessels`: 0
     - `thal`: 2
   - Expected Output: **Absence**

---

# Test the API with cURL

You can test the prediction endpoint using cURL. Here are examples for both Presence and Absence predictions:

# Test Case 1 - Presence of Heart Disease (Expected Output: "Presence")

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'age=63&sex=1&chest_pain_type=3&resting_blood_pressure=145&serum_cholestoral=233&fasting_blood_sugar=1&resting_ecg=0&max_heart_rate=150&exercise_induced_angina=0&oldpeak=2.3&slope=3&num_major_vessels=0&thal=2'
```

Expected Response:

```json
{
  "prediction": "Presence"
}
```

# Test Case 2 - Absence of Heart Disease (Expected Output: "Absence")

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'age=52&sex=0&chest_pain_type=2&resting_blood_pressure=130&serum_cholestoral=250&fasting_blood_sugar=0&resting_ecg=1&max_heart_rate=175&exercise_induced_angina=0&oldpeak=1.2&slope=2&num_major_vessels=0&thal=2'
```

Expected Response:

```json
{
  "prediction": "Absence"
}
```
