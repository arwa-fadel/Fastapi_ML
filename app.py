from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
import joblib
import numpy as np
from starlette.responses import RedirectResponse

# Load the pre-trained model
model = joblib.load("iris_model.pkl")

# Initialize FastAPI
app = FastAPI()

# HTML form for user input
@app.get("/", response_class=HTMLResponse)
async def form():
    return """
        <html>
            <head>
                <title>Iris Prediction</title>
            </head>
            <body>
                <h2>Enter Iris Flower Measurements</h2>
                <form action="/predict" method="get">
                    <label>Sepal Length: <input type="number" step="0.1" name="sepal_length" required></label><br><br>
                    <label>Sepal Width: <input type="number" step="0.1" name="sepal_width" required></label><br><br>
                    <label>Petal Length: <input type="number" step="0.1" name="petal_length" required></label><br><br>
                    <label>Petal Width: <input type="number" step="0.1" name="petal_width" required></label><br><br>
                    <button type="submit">Predict</button>
                </form>
            </body>
        </html>
    """

# Prediction endpoint to handle form data
@app.get("/predict")
async def predict_iris(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    try:
        # Prepare input data for prediction
        data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        
        # Make prediction
        prediction = model.predict(data)
        species = {0: "setosa", 1: "versicolor", 2: "virginica"}

        # Return the result as species name
        return {"prediction": species[prediction[0]]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
