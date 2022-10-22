import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import MinMaxScaler


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


def main():

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

    # making prediction

    test_loc.reshape(-1, 6)



if __name__ == "__main__":
    main()
