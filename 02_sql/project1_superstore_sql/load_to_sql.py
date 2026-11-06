import pandas as pd
import sqlite3

df = pd.read_csv('superstore_real.csv')
# Clean column names for SQL
df.columns = [c.lower().replace(' ','_').replace('-','_') for c in df.columns]

conn = sqlite3.connect('superstore.db')
df.to_sql('orders', conn, if_exists='replace', index=False)

print(f"Loaded {len(df)} rows into superstore.db -> table 'orders'")
print("Columns:", list(df.columns)[:5])

# Test query
q = conn.execute("SELECT category, SUM(sales) as total_sales FROM orders GROUP BY category").fetchall()
print("\nSales by Category (SQL):")
for row in q:
    print(row)

conn.close()
