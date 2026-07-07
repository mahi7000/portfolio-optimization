import pytest
import pandas as pd
import numpy as np
from src.data_loader import calculate_returns
from src.eda_utils import calculate_risk_metrics

def test_calculate_returns():
    mock_data = pd.DataFrame({'TSLA': [100.0, 105.0, 110.25]})
    returns = calculate_returns(mock_data)
    assert len(returns) == 2
    assert np.isclose(returns['TSLA'].iloc[0], 0.05)

def test_calculate_risk_metrics():
    mock_returns = pd.Series([0.01, -0.02, 0.015, -0.01, 0.005, 0.02, -0.03])
    metrics = calculate_risk_metrics(mock_returns)
    assert 'VaR_95' in metrics
    assert 'Sharpe_Ratio' in metrics