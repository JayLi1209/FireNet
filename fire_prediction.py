"""
Building the regression model from the dataset
FW_Veg_Rem_Combined.csv is a dataset of US wildfires by location, weather, and other attributes
"""

import pandas as pd
from sklearn.linear_model import Ridge
import pickle

# first gather the data we want to train our model on
df = pd.read_csv('FW_Veg_Rem_Combined.csv')

# remove missing data
df = df[df.Temp_pre_7 != -1.0]
df = df[df.Temp_pre_7 != 0.0]
df = df[df.Wind_pre_7 != -1.0]
df = df[df.Wind_pre_7 != 0.0]
df = df[df.Hum_pre_7 != -1.0]
df = df[df.Hum_pre_7 != 0.0]

feature_cols = ['latitude', 'longitude', 'Temp_pre_7', 'Wind_pre_7', 'Hum_pre_7']
X_train = df.loc[:, feature_cols]
y_train = df.loc[:, 'fire_size']

# creating the ridge regression model
model = Ridge(alpha = 3.0)

# fitting the model
model.fit(X_train, y_train)

# Save the trained model as a .sav file
filename = "fire_prediction_model_unscaled.sav"
pickle.dump(model, open(filename, 'wb'))


