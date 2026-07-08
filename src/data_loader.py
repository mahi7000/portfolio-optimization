import yfinance as yf
import pandas as pd
import numpy as np

def fetch_financial_data(tickers=["TSLA", "BND", "SPY"], start_date="2015-01-01", end_date="2026-06-30"):
    """
    Fetches financial data and extracts the adjusted close price.
    Handles any variant of MultiIndex or auto-adjusted columns seamlessly.
    """
    data_dict = {}
    
    # Download all tickers at once to let yfinance handle formatting uniformly
    print(f"Downloading data for {tickers}...")
    df = yf.download(tickers, start=start_date, end=end_date, auto_adjust=False)
    
    # Case 1: MultiIndex columns (e.g., standard yfinance batch output)
    if isinstance(df.columns, pd.MultiIndex):
        # Find out which level contains the price metrics ('Adj Close', 'Close', etc.)
        # Usually it's level 0. We find where 'Adj Close' or 'Close' lives.
        for level in range(df.columns.nlevels):
            unique_labels = df.columns.get_level_values(level).unique()
            if 'Adj Close' in unique_labels:
                # Extract 'Adj Close' cross-section safely
                combined_df = df.xs('Adj Close', axis=1, level=level)
                break
            elif 'Close' in unique_labels:
                combined_df = df.xs('Close', axis=1, level=level)
                break
    else:
        # Case 2: Flat columns (single ticker scenario or modified output)
        df.columns = df.columns.str.strip()
        if 'Adj Close' in df.columns:
            combined_df = df[['Adj Close']]
        elif 'Close' in df.columns:
            combined_df = df[['Close']]
        else:
            raise KeyError(f"Could not find closing columns. Headers available: {list(df.columns)}")
            
    # Ensure all columns match the requested tickers precisely and handle edge case sorting
    combined_df = combined_df[tickers]
    
    # Clean the index and handle missing trading day values safely via forward-fill
    combined_df = combined_df.ffill().bfill()
    
    return combined_df
def calculate_returns(df):
    """Calculates regular daily percentage returns and volatility metrics."""
    returns = df.pct_change().dropna()
    return returns