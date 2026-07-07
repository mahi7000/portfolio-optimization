import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller

def perform_adf_test(series):
    """Executes Augmented Dickey-Fuller test to evaluate stationarity properties."""
    result = adfuller(series.dropna())
    return {
        'ADF Statistic': result[0],
        'p-value': result[1],
        'Critical Values': result[4],
        'Stationary': result[1] < 0.05
    }

def calculate_risk_metrics(returns_series, confidence_level=0.05):
    """Computes historical Value at Risk (VaR) and the annualized Sharpe Ratio."""
    var_threshold = np.percentile(returns_series, confidence_level * 100)
    
    mean_ret = returns_series.mean()
    std_ret = returns_series.std()
    
    # Annualized Sharpe ratio assuming risk-free rate = 0
    sharpe_ratio = (mean_ret / std_ret) * np.sqrt(252) if std_ret != 0 else 0
    
    return {
        'VaR_95': var_threshold,
        'Sharpe_Ratio': sharpe_ratio
    }