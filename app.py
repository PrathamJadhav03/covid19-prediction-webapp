# app.py
from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('knn_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()
        features = [int(data[key]) for key in data]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        
        result_text = ""
        if prediction[0] == 1:
            result_text = 'You may be affected with COVID-19 virus! Please get RTPCR test ASAP and stay in Quarantine for 14 days!'
        else:
            result_text = 'You do not have any symptoms of COVID-19. Stay home! Stay safe!'
        
        return jsonify({'prediction_text': result_text})

if __name__ == "__main__":
    app.run(debug=True)
