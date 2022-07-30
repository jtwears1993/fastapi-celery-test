import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from app.db.crud import get_volumes, save_predictions
from sqlalchemy.orm import Session

def _get_data(db, tank_id):
    data = get_volumes(db, tank_id)
    return pd.DataFrame.from_records(data)

def _create_features(df: pd.DataFrame):
    time = np.arange(len(df.index))
    df['time'] = time
    df = df[['reporting_day', 'total_volume', 'time']]
    return df

def _split_data(data: pd.DataFrame):
    X = np.array(data.time.values)
    y = np.array(data.toal_volume.values).reshape(-1,1)
    test_size = int(len(X)*0.7)
    X = X.sort_index(ascending=False)
    y = y.sort_index(ascending=False)
    X_train = X[test_size:]
    y_train = y[test_size:]
    X_test = X[:test_size]
    y_test = y[:test_size]
    df_results = data[:test_size]
    return X_train, X_test, y_train, y_test, df_results

def _train(X_train, y_train):
    regressor = LinearRegression()
    return regressor.fit(X_train, y_train)

def _predict(model: LinearRegression, X_test: np.array) -> pd.Series:
    return pd.Series(model.predict(X_test), X_test)

def volume_forecaster(db: Session, tank_id: int, reporting_day: str):
    # get data
    data = _get_data(db, tank_id, reporting_day)
    df = _create_features(data)
    X_train, X_test, y_train, y_test, df_results = _split_data(df)
    regressor: LinearRegression = _train(X_train, y_train)
    predictions = _predict(regressor, X_test)
    predictions_and_actuals_df = pd.concat(predictions, df_results)
    save_predictions(db, tank_id, reporting_day, predictions_and_actuals_df)
    return 200