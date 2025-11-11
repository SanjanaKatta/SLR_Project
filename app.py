from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model
model = pickle.load(open('SLR_Project.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        father_height = float(request.form['father_height'])
        prediction = model.predict(np.array([[father_height]]))
        predicted_height = round(prediction[0], 2)
        return render_template('result.html', prediction=predicted_height)
    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

