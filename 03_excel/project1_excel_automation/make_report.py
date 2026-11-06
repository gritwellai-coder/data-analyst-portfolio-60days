import pandas as pd
df = pd.read_csv('superstore_real.csv')

with pd.ExcelWriter('client_report.xlsx') as writer:
    df.groupby('Category')[['Sales', 'Profit']].sum().to_excel(writer,sheet_name='By Category')
    df.groupby('Region')[['Sales', 'Profit']].sum().to_excel(writer,sheet_name='By Region')