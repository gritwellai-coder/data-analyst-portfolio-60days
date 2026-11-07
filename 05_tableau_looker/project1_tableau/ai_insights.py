import pandas as pd
df = pd.read_csv('05_tableau_looker/project1_tableau/superstore_for_powerbi.csv')
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
worst_category = df.groupby('Category')['Profit'].sum().idxmin()
print(f"Total Sales: ${total_sales:,.0f}")
print(f"Worst Category: {worst_category} - needs attention")
print(f"Total Profit: ${total_profit:,.0f}")
