# Time Series Forecasting for Portfolio Management Optimization

This repository contains the end-to-end framework developed for **Guide Me in Finance (GMF) Investments**. The project integrates advanced statistical and deep learning time series forecasting models to predict market volatility, evaluate asset momentum, and optimize portfolio allocation strategies under Modern Portfolio Theory (MPT).

---

## 🏢 Business Context & Core Objective
Predicting exact asset movements systematically violates the pure application of the Efficient Market Hypothesis (EMH). Therefore, this framework treats model predictions as structural components of an institutional decision-making framework. 

As Financial Analysts at GMF Investments, our goal is to construct an allocation engine across three strategic asset classes covering the period from **January 1, 2015, to June 30, 2026**:
*   **Tesla (TSLA):** High-growth, high-volatility vehicle used for aggressive tactical alpha generation.
*   **Vanguard Total Bond Market ETF (BND):** Low-risk asset providing foundational portfolio stabilization and consistent income.
*   **S&P 500 ETF (SPY):** Broad market operational anchor providing core diversification.

---

## 📂 Project Directory Structure

```text
portfolio-optimization/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml          # Automated CI Preprocessing Tests
├── data/
│   └── processed/                 # Stored historical and calculated features
├── notebooks/
│   ├── 1_exploratory_data_analysis.ipynb
│   └── README.md
├── src/
│   ├── __init__.py
│   ├── data_loader.py             # Data fetching & handling engine
│   └── eda_utils.py               # Risk modeling & statistical testing APIs
├── tests/
│   ├── __init__.py
│   └── test_data.py               # Framework verification tests
├── scripts/
│   └── __init__.py
├── requirements.txt               # Library tracking manifest
└── README.md

```

---

## 🚀 Installation & Setup

### 1. Environment Setup

Clone this repository to your local engine and configure a python environment:

```bash
# Clone the workspace repository
git clone [https://github.com/your-username-or-org/portfolio-optimization.git](https://github.com/your-username-or-org/portfolio-optimization.git)
cd portfolio-optimization

# Build out isolated python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install locked production dependencies
pip install -r requirements.txt

```

### 2. Verify Data Pipeline via Unit Tests

Execute the testing suite via `pytest` to verify logic integrity before running computational sequences:

```bash
pytest tests/

```

---

## 📈 Current Milestone Progress (Interim Dashboard)

### Task 1: Exploratory Data Analysis & Risk Footprints

* **Pipeline Setup:** Successfully configured structural streaming from the `yfinance` API covering 2015–2026. Forward-fill strategies implemented to patch gaps across assets without adding prospective trend-bias.
* **Stationarity Verified:** Stationarity testing completed via the **Augmented Dickey-Fuller (ADF)** test. Raw assets prove heavily non-stationary ($p > 0.05$), while their corresponding daily returns pass validation checks ($p < 0.001$), validating first-difference implementations ($d=1$).
* **Baseline Assets Profiles (2015-2026):**
* *TSLA:* Annualized Volatility: **54.3%** | Sharpe Ratio: **0.78**
* *SPY:* Annualized Volatility: **16.1%** | Sharpe Ratio: **0.85**
* *BND:* Annualized Volatility: **5.8%**  | Sharpe Ratio: **0.22**



### Task 2: Advanced Forecasting Configurations

* **Data Validation Splits:** Preserved chronological indexing using a hard split line: Training Data window spans 2015–2024; testing and evaluation sequence spans 2025–2026.
* **Classical Statistics Implementation:** Completed initial fitting for an $\text{ARIMA}(1, 1, 2)$ matrix targeting TSLA price dynamics. Residual behavior shows complete mitigation of internal historical tracking dependence.
