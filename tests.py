import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.weightstats import ztest

df = pd.read_csv('index.csv')

df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

data = df.dropna(subset=['Effective Federal Funds Rate'])

group1 = data[data['Year'] == 2000]['Effective Federal Funds Rate']
group2 = data[data['Year'] == 2005]['Effective Federal Funds Rate']

z_stat, z_p_val = ztest(group1, group2)

t_stat, t_p_val = stats.ttest_ind(group1, group2)

var1 = np.var(group1, ddof=1)
var2 = np.var(group2, ddof=1)

if var1 > var2:
    f_stat = var1 / var2
    df1 = len(group1) - 1
    df2 = len(group2) - 1
else:
    f_stat = var2 / var1
    df1 = len(group2) - 1
    df2 = len(group1) - 1

f_p_val = 2 * (1 - stats.f.cdf(f_stat, df1, df2))

print(f"Z-Test Statistic: {z_stat:.4f}, P-Value: {z_p_val:.4f}")
print(f"T-Test Statistic: {t_stat:.4f}, P-Value: {t_p_val:.4f}")
print(f"F-Test Statistic: {f_stat:.4f}, P-Value: {f_p_val:.4f}")
