# trader-behavior-insights
Exploratory data analysis of trader performance based on market sentiment (Fear vs. Greed) using Python, Pandas, and Seaborn.
# Trader Behavior Insights

This project explores the relationship between trader performance (Closed PnL) and market sentiment (Fear vs. Greed). The goal is to uncover behavioral patterns that could inform smarter trading strategies.

Due to non-overlapping dates between the provided sentiment and trading data, synthetic sentiment labels were generated to enable full exploratory analysis.

## Objectives

- Merge sentiment and trading data
- Clean and prepare time-series trade records
- Generate insights through visualizations
- Analyze how performance varies under different sentiment conditions

## Tools Used

- Python (Pandas, NumPy)
- Data visualization (Matplotlib, Seaborn)
- Data cleaning and transformation

## Key Files

- `trader_eda.py`: Full code for cleaning, merging, generating fake sentiment, and running EDA
- `boxplot_fake_sentiment.png`: Distribution of Closed PnL under Fear/Greed
- `avg_pnl_fake_sentiment.png`: Average PnL comparison between Fear and Greed days

## Note

The original sentiment dataset did not align date-wise with the trading data. Therefore, randomized sentiment labels were applied per date to simulate market sentiment. This approach enables full analysis while demonstrating EDA skills.



