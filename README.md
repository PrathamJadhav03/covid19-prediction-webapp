# COVID-19 Prediction Web Application

## Overview

This project is a web application that predicts the likelihood of a user being affected by COVID-19 based on their symptoms and exposure history. The prediction is performed using machine learning algorithms including Logistic Regression, K-Nearest Neighbors (KNN), and Random Forest. The application is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend.

## Features

- Predict COVID-19 infection based on user inputs
- Utilizes Logistic Regression, KNN, and Random Forest for predictions
- Dynamic and interactive user interface
- Visualization of model performance
- Responsive design with attractive CSS and images

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Virtualenv (recommended)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/PrathamJadhav03/covid19-prediction-webapp.git
    cd covid19-prediction-webapp
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn plotly colorama flask
    ```

4. **Run the application:**

    ```bash
    flask run
    ```

    The application will be accessible at `http://127.0.0.1:5000`.

## Usage

1. Open the web application in your browser.
2. Fill out the form with the symptoms and exposure history.
3. Click the "Predict" button.
4. The prediction result will be displayed on the page.

## Data Description

The dataset contains information about various symptoms and contact history of individuals. The features include:
- Breathing Problem
- Fever
- Dry Cough
- Sore throat
- Running Nose
- Asthma
- Chronic Lung Disease
- Headache
- Heart Disease
- Diabetes
- Hyper Tension
- Fatigue
- Gastrointestinal issues
- Abroad travel
- Contact with COVID Patient
- Attended Large Gathering
- Visited Public Exposed Places
- Family working in Public Exposed Places

## Code Structure

- **app.py**: Main Flask application.
- **static/**: Static files (CSS, JavaScript, images).
- **templates/**: HTML templates.
- **model_training.ipynb**: Jupyter notebook for training the machine learning models.
- **model.py**: Python script for saving and loading the trained machine learning models.

## Model Training

The machine learning models are trained using a dataset containing various symptoms and exposure history of patients. The `model_training.ipynb` notebook contains the code for training and evaluating these models. The trained models are saved and used by the Flask application to make predictions.

## Web Application

The Flask web application provides an interactive interface where users can input their symptoms and contact history to get a COVID-19 prediction. The application uses the trained K-Nearest Neighbors model for making predictions.

## Acknowledgements

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly](https://plotly.com/)
- [scikit-learn](https://scikit-learn.org/)
- [Flask](https://flask.palletsprojects.com/)