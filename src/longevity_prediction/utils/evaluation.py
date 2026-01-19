import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score

def evaluate_regression_metrics_df(y_true, y_pred, warn=True):
    y_true = np.array(y_true).flatten()
    y_pred = np.array(y_pred).flatten()

    # Safety check for percentage metrics
    epsilon = 1e-8
    near_zero = np.abs(y_true) < 1e-6
    if warn and np.any(near_zero):
        print("Warning: `y_true` contains near-zero values - MAPE and RMSPE may be unstable.")

    # Calculations
    mse = mean_squared_error(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    
    # Percentage errors
    pct_diffs = np.abs(y_true - y_pred) / np.maximum(np.abs(y_true), epsilon)
    mape = np.mean(pct_diffs) * 100
    rmspe = np.sqrt(np.mean(pct_diffs**2)) * 100

    # Correlation (Handling zero-variance edge cases)
    try:
        pearson = np.corrcoef(y_true, y_pred)[0, 1]
    except:
        pearson = np.nan

    metrics = {
        "MSE": mse,
        "RMSE": rmse,
        "MAE": mae,
        "MAPE [%]": mape,
        "RMSPE [%]": rmspe,
        "R²": r2_score(y_true, y_pred),
        "Pearson correlation": pearson
    }

    return pd.DataFrame(list(metrics.items()), columns=["Metric", "Value"]).round(4)