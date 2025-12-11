import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

def myf(y, yhat):
    """
    Basic regression metrics:
    ME, MPE, MAE, MSE, MAPE
    """
    err  = y - yhat
    ME   = np.round(err.mean(), 3)
    MPE  = np.round((err / y).mean(), 3)
    MAE  = np.round(mean_absolute_error(y, yhat), 3)
    MSE  = np.round(mean_squared_error(y, yhat), 3)
    MAPE = np.round(np.mean(np.abs(err / y)), 3)

    print("\nResults:")
    print("ME:   ", ME)
    print("MPE:  ", MPE)
    print("MAE:  ", MAE)
    print("MSE:  ", MSE)
    print("MAPE: ", MAPE)


def myf2(y, yhat):
    """
    Extended metrics including RMSE.
    Mirrors the logic used in the notebook with safe handling
    of division by zero for percentage-based metrics.
    """
    err = y - yhat

    ME  = np.round(err.mean(), 3)
    MAE = np.round(mean_absolute_error(y, yhat), 3)
    MSE = np.round(mean_squared_error(y, yhat), 3)
    RMSE = np.round(np.sqrt(MSE), 3)

    with np.errstate(divide="ignore", invalid="ignore"):
        mpe_vals  = err / y
        mape_vals = np.abs(err / y)
        mpe_vals  = np.where(np.isfinite(mpe_vals), mpe_vals, np.nan)
        mape_vals = np.where(np.isfinite(mape_vals), mape_vals, np.nan)

    MPE  = np.round(np.nanmean(mpe_vals), 3)
    MAPE = np.round(np.nanmean(mape_vals), 3)

    print("\nResults:")
    print("ME:    ", ME)
    print("MPE:   ", MPE)
    print("MAE:   ", MAE)
    print("MSE:   ", MSE)
    print("RMSE:  ", RMSE)
    print("MAPE:  ", MAPE)
