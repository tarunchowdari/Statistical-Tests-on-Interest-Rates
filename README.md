# Federal Reserve Interest Rate Statistical Analysis

This project performs statistical hypothesis testing on historical Federal Reserve interest rate data. It specifically compares the Effective Federal Funds Rate between the years 2000 and 2005 to determine if there are significant differences in central bank policy during these periods.

## Project Overview

The script loads interest rate data and performs the following statistical tests:

* **Z-Test**: Determines if there is a significant difference between the means of the two groups (assuming a normal distribution).
* **T-Test**: Compares the means of the two groups (useful if sample sizes were smaller, though often converges with Z-test on larger datasets).
* **F-Test**: Compares the variances (volatility) of the interest rates between the two years.

## Prerequisites

You need Python installed along with the following libraries:

* pandas
* numpy
* scipy

## Installation

1.  **Clone or download** this repository.
2.  **Install the required packages** using pip:

    ```bash
    pip install pandas numpy scipy
    ```

## Dataset Setup

1.  Download the dataset from Kaggle: [Federal Reserve Interest Rates](https://www.kaggle.com/datasets/federalreserve/interest-rates).
2.  Extract the files and locate `index.csv`.
3.  Place `index.csv` in the same directory as your Python script.

## Usage

1.  Create a file named `main.py` (or your preferred filename).
2.  Paste the following code into the file (this version uses `scipy` only and does not require `statsmodels`):

    ```python
    import pandas as pd
    import numpy as np
    from scipy import stats

    df = pd.read_csv('index.csv')

    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

    data = df.dropna(subset=['Effective Federal Funds Rate'])

    group1 = data[data['Year'] == 2000]['Effective Federal Funds Rate']
    group2 = data[data['Year'] == 2005]['Effective Federal Funds Rate']

    t_stat_calc, _ = stats.ttest_ind(group1, group2, equal_var=True)
    z_stat = t_stat_calc
    z_p_val = 2 * (1 - stats.norm.cdf(abs(z_stat)))

    t_stat, t_p_val = stats.ttest_ind(group1, group2)

    var1 = group1.var()
    var2 = group2.var()

    if var1 > var2:
        f_stat = var1 / var2
        df1 = len(group1) - 1
        df2 = len(group2) - 1
    else:
        f_stat = var2 / var1
        df1 = len(group2) - 1
        df2 = len(group1) - 1

    f_p_val = 2 * (1 - stats.f.cdf(f_stat, df1, df2))

    print("Statistical Test Results (Year 2000 vs 2005)")
    print("-" * 45)
    print(f"Z-Test  : Statistic = {z_stat:.4f}, P-Value = {z_p_val:.4f}")
    print(f"T-Test  : Statistic = {t_stat:.4f}, P-Value = {t_p_val:.4f}")
    print(f"F-Test  : Statistic = {f_stat:.4f}, P-Value = {f_p_val:.4f}")
    ```

3.  Run the script:

    ```bash
    python main.py
    ```

## Interpreting Results

* **P-Value < 0.05**: Reject the null hypothesis. There is a statistically significant difference between the two years.
* **P-Value >= 0.05**: Fail to reject the null hypothesis. The difference is likely due to random chance.
