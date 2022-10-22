import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sqlite3

# con = sqlite3.connect("FPA_FOD_20170508.sqlite")
# df = pd.read_sql_query("SELECT * from Fires", con)
#
# df[['FIPS_NAME', 'STATE', 'FIRE_YEAR']].to_csv('fire.csv')

df = pd.read_csv('FW_Veg_Rem_Combined.csv')

relevant_data = df[['latitude', 'longitude', 'Temp_pre_7', 'Wind_pre_7', 'Hum_pre_7']]


print(relevant_data)