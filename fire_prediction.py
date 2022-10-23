"""
Building the regression model from the dataset
FW_Veg_Rem_Combined.csv is a dataset of US wildfires by location, weather, and other attributes
"""


import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
import pickle

"""
Normalizes the input data, which is in several columns of a dataframe
"""
def normalize_df(df):
    result = df.copy()
    ss = StandardScaler()
    return pd.DataFrame(ss.fit_transform(result), columns=result.columns)

"""
Normalizes the single series that includes all output values
"""
def normalize_series(s):
    values = s.values

    values = values.reshape((len(values), 1))

    scaler = StandardScaler()
    scaler = scaler.fit(values)
    return scaler.transform(values)




# df = pd.read_csv('uscountiesProcessed.csv')
# df['latlong'] = list(zip(df.lat, df.lng))
# df = df.drop(['lat', 'lng'], axis = 1)
# counties_and_latlong = dict(zip(df.county, df.latlong))

# first gather the data we want to train our model on
df = pd.read_csv('FW_Veg_Rem_Combined.csv')
feature_cols = ['latitude', 'longitude', 'Temp_pre_7', 'Wind_pre_7', 'Hum_pre_7']
X = df.loc[:, feature_cols]
y = df.loc[:, 'fire_size']
X_train = normalize_df(X)
y_train = normalize_series(y)

# creating the ridge regression model
model = Ridge(alpha=3)

# fitting the model
model.fit(X_train, y_train)

# Save the trained model as a .sav file
filename = "fire_prediction_model.sav"
pickle.dump(model, open(filename, 'wb'))


