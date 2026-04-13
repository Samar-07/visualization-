Nepal Tourism Board — Visitor Arrivals Analysis
March 2026 | Top 10 Source Market Countries

Overview
This project analyzes international visitor arrivals to Nepal for March 2026 using data published by the Nepal Tourism Board (NTB), sourced from the Department of Immigration.
The analysis focuses on the top 10 source market countries and visualizes arrival trends, year-on-year growth, and post-pandemic recovery status.

Data Source

Publisher: Nepal Tourism Board (NTB)
Original Source: Department of Immigration, Government of Nepal
Period: March 2026 (Calendar Year)
Total Arrivals: 120,516 international visitors
Raw File: data/raw/march-2026-1.pdf


Project Structure
NTB/
├── data/
│   ├── raw/                          # Original NTB PDF reports
│   │   └── march-2026-1.pdf
│   └── processed/                    # Cleaned CSV files
│       ├── ntb_march_2026_nationality.csv   # All countries (51)
│       └── top10_march_2026.csv             # Top 10 countries only
├── scripts/
│   └── top10.py                      # Python script to extract top 10
└── README.md

Dataset Columns
ColumnDescriptionRankPosition 1–10 by March 2026 arrivalsRegionGeographic region (South Asia, Europe, Americas etc.)CountryNationality of visitorMarch_2026Arrivals in March 2026Share_Pct% share of total 120,516 arrivalsMarch_2025Arrivals in March 2025 (preceding year)YoY_Change_Pct% change vs March 2025March_2019Arrivals in March 2019 (pre-pandemic baseline)vs_2019_Change_Pct% change vs March 2019

Top 10 Countries — March 2026
RankCountryArrivalsShare1India25,72821.3%2China11,2209.3%3Sri Lanka10,7598.9%4United States7,9746.6%5Myanmar6,0205.0%6Australia4,8454.0%7United Kingdom4,8144.0%8Bangladesh4,6763.9%9Germany4,0863.4%10Thailand3,8973.2%

Key Insights

India dominates with 21.3% of all arrivals — 1 in 5 tourists in Nepal was Indian
Myanmar is the fastest growing market with +60.4% growth vs March 2025
USA saw the sharpest decline at -28.1% vs March 2025
South Asia (SAARC) accounts for 35.4% of all arrivals combined
China has not recovered from pre-pandemic levels, still -35.5% vs March 2019


How to Run
Make sure you have Python and pandas installed:
bashpip install pandas
Then run the extraction script:
bashcd NTB/scripts
python top10.py
This reads data/processed/ntb_march_2026_nationality.csv and outputs data/processed/top10_march_2026.csv

Dashboard
Built in Google Looker Studio using the processed CSV as data source.
Charts included:

World heatmap by Share_Pct
Bar chart — arrivals by country
YoY growth chart
COVID recovery status chart


Data based on preliminary monthly raw data provided by the Department of Immigration, Nepal.