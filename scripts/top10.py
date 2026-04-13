import pandas as pd

# Load the data
df = pd.read_csv('../data/processed/ntb_march_2026_nationality.csv')

# Remove subtotals and others
exclude = ['Others']
df_countries = df[~df['Country'].isin(exclude)]

# Also remove any row where Region is in the Country column (subtotal rows)
regions = ['SOUTH ASIA (SAARC)', 'ASIA (OTHER)', 'EUROPE', 'OCEANIA', 'AMERICAS', 'MIDDLE EAST', 'AFRICA', 'OTHERS']
df_countries = df_countries[~df_countries['Country'].isin(regions)]

# Sort by March 2026 arrivals descending and take top 10
top10 = df_countries.sort_values('March_2026', ascending=False).head(10)

# Reset index
top10 = top10.reset_index(drop=True)
top10.index += 1  # Start ranking from 1

# Add rank column
top10.insert(0, 'Rank', top10.index)

# Save to processed folder
top10.to_csv('../data/processed/top10_march_2026.csv', index=False)

print("Top 10 Countries - International Visitor Arrivals to Nepal (March 2026)")
print("=" * 70)
print(top10[['Rank', 'Country', 'Region', 'March_2026', 'Share_Pct', 'YoY_Change_Pct']].to_string(index=False))
print("\nFile saved to data/processed/top10_march_2026.csv")