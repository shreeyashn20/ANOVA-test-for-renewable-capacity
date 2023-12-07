# ANOVA-test-for-renewable-capacity
## Renewable Energy Capacity Analysis in India

This repository contains Python code for analyzing the cumulative renewable energy capacity across various sectors in India from 2014 to 2023. The code includes:

* Importing and processing the data.
* Performing an Analysis of Variance (ANOVA) to compare the mean renewable energy capacity across different sectors.
* Interpreting the results of the ANOVA test.

### Installation

1. Clone this repository to your local machine.
2. Open a terminal and navigate to the repository directory.
3. Install the required libraries:

```
pip install pandas scipy
```

### Data

The data for this analysis is stored in the `data.csv` file. It contains the following columns:

| Column | Description |
|---|---|
| **Sector** | Name of the renewable energy sector. |
| **Year** | Year (format: YYYY-YY). |
| **Cumulative Achievements** | Cumulative renewable energy capacity (MW) for each sector and year. |

**Note:** Replace `data.csv` with the actual path to your data file.

### Running the Code

1. Open a terminal in the repository directory.
2. Run the following command:

```
python renewable_energy_analysis.py
```

### Results

The F-statistic and p-value from the ANOVA test will be printed to the console. Interpret the results based on:

* **Significant difference:** P-value < 0.05 indicates a statistically significant difference in mean renewable energy capacity across sectors.
* **No significant difference:** P-value > 0.05 suggests no statistically significant difference in mean renewable energy capacity across sectors.

### Further Analysis

This code provides a foundation for exploring the data further:

* **Visualizations:** Create charts and graphs to visualize trends.
* **Post-hoc tests:** Identify specific sectors with significant differences.
* **Growth trends:** Analyze the growth of individual sectors.
* **Influencing factors:** Investigate factors affecting sector growth.

### Contributions

This repository is open-source and welcomes contributions. Please fork the repository, make enhancements, and submit pull requests.

### License

This project is licensed under the MIT License.

