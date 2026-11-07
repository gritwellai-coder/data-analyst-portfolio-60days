import pandas as pd
df = pd.read_csv('01_python/project1_ecommerce/superstore_real.csv')
df = df.dropna(subset=['Order ID'])
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df['Profit Margin'] = df['Profit']/df['Sales']
df.to_csv('04_powerbi/project1_superstore_dashboard/superstore_for_powerbi.csv', index=False)
