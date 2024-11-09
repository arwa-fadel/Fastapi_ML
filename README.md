# Fastapi_ML
This is an implementation for tasks in a course project with Qafza.

for now it has:
Task 2 (deploy an ml moddel using fastapi) 
and 
Task 3 (contain it in docker)
________________________________________________________________________________________________

# Iris Flower Classification API

This is a simple machine learning application using FastAPI to classify iris flowers based on user-provided measurements. The application is trained on the classic Iris dataset using a Random Forest classifier. Users can input measurements for an iris flower’s sepal and petal dimensions through a browser form, and the application will predict the flower species.

## Features

- **Simple HTML Form Interface**: Allows users to input iris flower measurements directly in the browser.
- **Prediction Endpoint**: Processes the measurements and predicts the iris flower species (Setosa, Versicolor, or Virginica) based on the input.

## Technology Stack

- **FastAPI**: For creating a web API.
- **Scikit-Learn**: For training the machine learning model.
- **Uvicorn**: ASGI server for running the FastAPI app.
- **Docker**: For containerizing the application.

## Setup and Usage

### 1. Prerequisites

- Ensure you have [Docker](https://www.docker.com/) installed on your machine.

### 2. Training the Model (Optional)

If you want to retrain the model (optional), run the following script:

```bash
python train_model.py 
```

This will generate a iris_model.pkl file, which is a pre-trained model saved for use in the application.

#### 3. Building and Running the Docker Container

1. Build the Docker Image:

`docker build -t iris-fastapi-app .`

2. Run the Docker Container:

`docker run -p 8000:8000 iris-fastapi-app`

The application will be accessible at http://localhost:8000

##### 4. The Application

Using the HTML Form
- Open your browser and navigate to http://localhost:8000/.
- You will see a form where you can enter the following measurements for the iris flower:
    Sepal Length
    Sepal Width
    Petal Length
    Petal Width
- After entering the values, click the Predict button to submit the form.
- The app will display a prediction, showing one of the three species: Setosa, Versicolor, or Virginica.

Or uou can Use the API Endpoint Directly
by entering the following URL in your browser and replace the query parameter values as needed.:
http://localhost:8000/predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2

You should see a JSON response like:
`{"prediction": "setosa"}`

##### 5. File Structure
==app.py==: The FastAPI application file.
==train_model.py==: Script to train and save the Random Forest model.
==iris_model.pkl==: The pre-trained model file.
==Dockerfile==: Configuration file for Docker to containerize the application.

*Tip: don't forget to activate your environments & keep the files in the same directory <3*




**done by: arwa fadel**