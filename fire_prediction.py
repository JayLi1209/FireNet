"""
Building the regression model from the dataset
FW_Veg_Rem_Combined.csv is a dataset of US wildfires by location, weather, and other attributes
"""

import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
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
X = df.loc[:, feature_cols]
y = df.loc[:, 'fire_size']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# creating the ridge regression model
model = Ridge(alpha=100)

# fitting the model
model.fit(X_train, y_train)

# Save the trained model as a .sav file
filename = "fire_prediction_model_unscaled.sav"
pickle.dump(model, open(filename, 'wb'))


