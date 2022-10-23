from flask import Flask
from flask import Flask, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('fire_prediction_model.sav', 'rb'))

@app.route("/", methods=['POST'])
def predictor():
    data = request.get_json()
    print(data)
    predictions = model.predict(data['x'])
    return {"Risk": predictions.tolist(), "Location": "asdf", "data3": 1}


