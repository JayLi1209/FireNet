<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, request
import numpy as np
>>>>>>> 8c1a19f0efea8fdb0381368d84ef1bb3cf7c8732
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


# normalize data
def normalize_df(df):
    result = df.copy()
    ss = StandardScaler()
    return pd.DataFrame(ss.fit_transform(result), columns=result.columns)


def normalize_series(s):
    values = s.values

    values = values.reshape((len(values), 1))

    scaler = StandardScaler()
    scaler = scaler.fit(values)
    normalized = scaler.transform(values)
    return normalized



# first gather the data we want to train our model on
df = pd.read_csv('uscountiesProcessed.csv')
df['latlong'] = list(zip(df.lat, df.lng))
df = df.drop(['lat', 'lng'], axis=1)
counties_and_latlong = dict(zip(df.county, df.latlong))

# first gather the data we want to train our model on
df = pd.read_csv('FW_Veg_Rem_Combined.csv')
feature_cols = ['latitude', 'longitude', 'Temp_pre_7', 'Wind_pre_7', 'Hum_pre_7', 'Prec_pre_7']
X = df.loc[:, feature_cols]
y = df.loc[:, 'fire_size']
X_train = normalize_df(X)
y_train = normalize_series(y)

# creating a regression model
model = Ridge(alpha=3)

# fitting the model
model.fit(X_train, y_train)


@app.route("/", methods=['POST'])
def predictor():
    # print("hiii")
    data = request.get_json()
    print(data)
    predictions = model.predict(data['x'])
    return {"Risk": predictions.tolist(), "Location": "asdf", "data3": 1}


