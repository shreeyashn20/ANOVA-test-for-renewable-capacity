# Import necessary libraries

import pandas as pd
from scipy import stats

# Define data
data = {
  "Sector": ["Wind Power", "Solar Power", "Small Hydro Power", "Biomass (Bagasse) Cogeneration", "Biomass(Non-bagasse) Cogeneration", "Waste to Power", "Waste to Energy (Off-grid)", "Total"],
  "2014-15": [2311.77, 1171.62, 251.68, 295.67, 60.05, 0.02, 9.71, 4100.57],
  "2015-16": [3423.05, 3130.36, 218.11, 304.85, 59.24, 0.23, 5.69, 7441.31],
  "2016-17": [5502.37, 5658.63, 106.38, 161.95, 2.29, 0.94, 11.77, 11466.81],
  "2017-18": [1865.23, 9563.69, 105.95, 519.14, 0.51, 21.54, 5.55, 12093.24],
  "2018-19": [1480.97, 6750.65, 107.34, 02.79, 20.97, 54.52, 6.58, 8759.59],
  "2019-20": [2117.79, 10065.06, 90.01, 7173.37, 42.48, 249.74, 19.11, 8843.31],
  "2020-21": [1503.31, 5628.81, 103.65, 59.69, 28.25, 524.97, 20.75, 7548.11],
  "2021-22": [110.53, 2760.51, 62.09, 09433.56, 0.0, 34.66, 52.28, 14081.97],
  "2022-23": [2275.55, 2783.87, 95.44, 33.56, 0.0, 0.0, 0.0, 15274.43],
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Perform ANOVA
f_statistic, p_value = stats.f_oneway(df['2014-15'], df['2015-16'], df['2016-17'], df['2017-18'], df['2018-19'], df['2019-20'], df['2020-21'], df['2021-22'], df['2022-23'])

# Print results
print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpretation
if p_value < 0.05:
  print("There is a statistically significant difference in the mean renewable energy capacity across different sectors.")
else:
  print("There is no statistically significant difference in the mean renewable energy capacity across different sectors.")