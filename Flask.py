from flask import Flask, request
import pickle

app = Flask(__name__)
model = pickle.load(open('fire_prediction_model_unscaled.sav', 'rb'))

@app.route("/", methods=['POST'])
def predictor():
    data = request.get_json()
    prediction = model.predict(data['x'])
    if (prediction < 500):
        size = 'small'
    elif (prediction < 1500):
        size = 'medium'
    else:
        size = 'large'
    return {"Risk": size, "Location": "asdf", "data3": 1}


