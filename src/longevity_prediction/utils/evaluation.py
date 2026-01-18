import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score


def evaluate_regression_metrics_df(y_true, y_pred, warn=True):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    diffs = y_true - y_pred
    abs_diffs = np.abs(diffs)
    pct_diffs = abs_diffs / np.maximum(np.abs(y_true), 1e-8)
    pct_diff_squared = ((diffs / np.maximum(np.abs(y_true), 1e-8)) ** 2)

    if warn and np.any(np.abs(y_true) < 1e-6):
        print("Warning: `y_true` contains near-zero values - MAPE and RMSPE may be unstable.")

    mse = root_mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mse)

    metrics = {
        "MSE": mse,
        "RMSE": rmse,
        "RMSPE [%]": np.sqrt(np.mean(pct_diff_squared)) * 100,
        "MAE": mae,
        "MAPE [%]": np.mean(pct_diffs) * 100, 
        "R²": r2_score(y_true, y_pred),
        "Korelacja Pearsona": np.corrcoef(y_true, y_pred)[0, 1]
    }

    df = pd.DataFrame(list(metrics.items()), columns=["Metric", "Value"])
    return df.round(4)