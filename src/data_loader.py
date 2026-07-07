import yfinance as yf
import pandas as pd
import numpy as np

def fetch_financial_data(tickers=["TSLA", "BND", "SPY"], start_date="2015-01-01", end_date="2026-06-30"):
    """Fetches and merges adjusted closing prices from yfinance API."""
    data_dict = {}
    for ticker in tickers:
        df = yf.download(ticker, start=start_date, end=end_date)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.droplevel(1)
        data_dict[ticker] = df['Adj Close']
        
    combined_df = pd.DataFrame(data_dict)
    combined_df = combined_df.ffill().bfill()
    return combined_df

def calculate_returns(df):
    """Calculates regular daily percentage returns and volatility metrics."""
    returns = df.pct_change().dropna()
    return returns