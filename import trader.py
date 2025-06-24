import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Step 1: Load the trader data
trader_data = pd.read_csv('historical_data.csv')

# Step 2: Clean column names
trader_data.columns = trader_data.columns.str.strip().str.lower()

# Step 3: Convert timestamps and extract date
trader_data['timestamp'] = pd.to_datetime(trader_data['timestamp'])
trader_data['date'] = trader_data['timestamp'].dt.date

# Step 4: Assign random fake sentiment (Fear/Greed) per unique date
unique_dates = trader_data['date'].unique()
fake_sentiment = pd.DataFrame({
    'date': unique_dates,
    'classification': [random.choice(['Fear', 'Greed']) for _ in unique_dates]
})

# Step 5: Merge fake sentiment with trader data
merged_data = pd.merge(trader_data, fake_sentiment, on='date', how='left')

# Step 6: Normalize column names
merged_data.columns = merged_data.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 7: Create EDA DataFrame
eda_df = merged_data.dropna(subset=['classification', 'closed_pnl'])

# Clean up classification + ensure closed_pnl is numeric
eda_df['classification'] = eda_df['classification'].str.title()
eda_df['closed_pnl'] = pd.to_numeric(eda_df['closed_pnl'], errors='coerce')
eda_df = eda_df.dropna(subset=['closed_pnl'])

# Step 8: Confirm data shape
print("\nEDA DataFrame shape:", eda_df.shape)
print("Sample rows:")
print(eda_df[['account', 'date', 'classification', 'closed_pnl']].head())

# Step 9: Boxplot – PnL distribution by sentiment
plt.figure(figsize=(8, 6))
sns.boxplot(x='classification', y='closed_pnl', data=eda_df, palette='Set2')
plt.title('Closed PnL Distribution on Fear vs. Greed Days (Fake Sentiment)')
plt.xlabel('Market Sentiment')
plt.ylabel('Closed PnL')
plt.grid(True)
plt.tight_layout()
plt.savefig('boxplot_fake_sentiment.png')
plt.show()

# Step 10: Barplot – Average PnL per sentiment
avg_pnl = eda_df.groupby('classification')['closed_pnl'].mean().reset_index()

plt.figure(figsize=(6, 4))
sns.barplot(x='classification', y='closed_pnl', data=avg_pnl, palette='Set2')
plt.title('Average Closed PnL by Market Sentiment (Fake Sentiment)')
plt.xlabel('Market Sentiment')
plt.ylabel('Average Closed PnL')
plt.tight_layout()
plt.savefig('avg_pnl_fake_sentiment.png')
plt.show()
