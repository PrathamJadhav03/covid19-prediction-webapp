# model.py
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import joblib

def train_models():
    covid_data = pd.read_csv("Covid Dataset.csv")
    
    # Encode categorical features
    label_encoder = LabelEncoder()
    for col in covid_data.columns:
        covid_data[col] = label_encoder.fit_transform(covid_data[col])
    
    # Drop less relevant features
    covid_data = covid_data.drop(['Wearing Masks', 'Sanitization from Market'], axis=1)
    
    # Split data
    X = covid_data.drop('COVID-19', axis=1)
    y = covid_data['COVID-19']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101)
    
    # Train KNN
    knn = KNeighborsClassifier()
    param_grid = {'n_neighbors': np.arange(1, 50)}
    knn_cv = GridSearchCV(knn, param_grid, cv=5)
    knn_cv.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(knn_cv, 'knn_model.pkl')

if __name__ == "__main__":
    train_models()
