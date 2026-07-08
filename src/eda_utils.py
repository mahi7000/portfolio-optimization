import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller

def perform_adf_test(series):
    """
    Executes an Augmented Dickey-Fuller test to evaluate stationarity properties.
    """
    result = adfuller(series.dropna())
    return {
        'ADF Statistic': result[0],
        'p-value': result[1],
        'Critical Values': result[4],
        'Stationary': result[1] < 0.05
    }

def detect_outliers_zscore(returns_series, threshold=3.0):
    """
    Identifies statistical anomalies using a standard deviation Z-score boundary.
    """
    mean = returns_series.mean()
    std = returns_series.std()
    z_scores = (returns_series - mean) / std
    outliers = returns_series[abs(z_scores) > threshold]
    return outliers

def calculate_risk_metrics(returns_series, confidence_level=0.05):
    """
    Computes historical Value at Risk (VaR 95%) and the annualized Sharpe Ratio.
    """
    # 95% Historical VaR calculation
    var_95 = np.percentile(returns_series.dropna(), confidence_level * 100)
    
    # Annualized Sharpe ratio assuming risk-free rate = 0
    mean_ret = returns_series.mean()
    std_ret = returns_series.std()
    sharpe_ratio = (mean_ret / std_ret) * np.sqrt(252) if std_ret != 0 else 0
    
    return {
        'VaR_95': var_95,
        'Sharpe_Ratio': sharpe_ratio
    }