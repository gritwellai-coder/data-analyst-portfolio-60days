
import sqlite3
conn = sqlite3.connect('superstore.db')
queries = open('upwork_queries.sql').read().split(';')
for i, q in enumerate(queries, 1):
    q=q.strip()
    if not q or q.startswith('--'): continue
    if len(q) < 20: continue
    print(f"\n--- Q{i} ---")
    try:
        cur = conn.execute(q)
        rows = cur.fetchall()
        for r in rows[:5]:
            print(r)
        if len(rows)>5:
            print(f"... and {len(rows)-5} more")
    except Exception as e:
        print("Error:", e)
conn.close()
