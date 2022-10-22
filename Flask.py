from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello_world():
    data = request.get_json()
    # model = main(...)
    # predictions = model.predict(X_test)
    # return
    return {"data": [1,2,3], "data2": "asdf", "data3": 1}

# google cloud
# tunnel

