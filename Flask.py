from flask import Flask, request
import pickle

app = Flask(__name__)
model = pickle.load(open('fire_prediction_model.sav', 'rb'))
scaler = pickle.load(open('input_scaler_model.sav', 'rb'))

@app.route("/", methods=['POST'])
def predictor():
    data = request.get_json()
    scaled_input = scaler.predict(data['x'])
    prediction = model.predict(scaled_input)
    if (prediction < 100):
        size = 'small'
    elif (prediction < 1000):
        size = 'medium'
    else:
        size = 'large'
    return {"Risk": size, "Location": "asdf", "data3": 1}


