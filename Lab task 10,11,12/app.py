from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load Model
with open(r'C:\Ai Project\AI_Lab_Project\model_files.pkl', 'rb') as f:
    data = pickle.load(f)
    model = data["model"]
    encoders = data["encoders"]

@app.route('/')
def home():
    options = {
        'gender': sorted(encoders['gender'].classes_),
        'race': sorted(encoders['race/ethnicity'].classes_),
        'education': sorted(encoders['parental level of education'].classes_),
        'lunch': sorted(encoders['lunch'].classes_),
        'prep': sorted(encoders['test preparation course'].classes_)
    }
    return render_template('index.html', options=options)

@app.route('/predict', methods=['POST'])
def predict():
    inputs = [
        encoders['gender'].transform([request.form['gender']])[0],
        encoders['race/ethnicity'].transform([request.form['race']])[0],
        encoders['parental level of education'].transform([request.form['education']])[0],
        encoders['lunch'].transform([request.form['lunch']])[0],
        encoders['test preparation course'].transform([request.form['prep']])[0]
    ]

    features = np.array([inputs])
    prediction = model.predict(features)[0]

    colors = {'A': 'success', 'B': 'info', 'C': 'warning', 'F': 'danger'}
    color = colors.get(prediction, 'secondary')

    return render_template('result.html', grade=prediction, color=color)

if __name__ == '__main__':
    app.run(debug=True)
