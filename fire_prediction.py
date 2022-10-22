import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt
import sqlite3

# con = sqlite3.connect("FPA_FOD_20170508.sqlite")
# df = pd.read_sql_query("SELECT * from Fires", con)
#
# df[['FIPS_NAME', 'STATE', 'FIRE_YEAR']].to_csv('fire.csv')

# first gather the data we want to train our model on
df = pd.read_csv('FW_Veg_Rem_Combined.csv')
feature_cols = ['latitude', 'longitude', 'Temp_pre_7', 'Wind_pre_7', 'Hum_pre_7', 'Prec_pre_7']
X = df.loc[:, feature_cols]
y = df.loc[:, 'fire_size']

# normalize data

def normalize_df(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

def normalize_series(s):
    values = s.values

    values = values.reshape((len(values), 1))

    scaler = MinMaxScaler()
    scaler = scaler.fit(values)
    normalized = scaler.transform(values)
    return normalized

X = normalize_df(X)
y = normalize_series(y)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101)

# creating a regression model
model = KNeighborsRegressor()

# fitting the model
model.fit(X_train, y_train)

# making predictions
predictions = model.predict(X_test)

test_loc = np.array([[33.884106, -112.781170, 12, 7, 50, 2]])
test_loc.reshape(-1, 6)

# model evaluation
print('mean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print('test location : ', model.predict(test_loc))
