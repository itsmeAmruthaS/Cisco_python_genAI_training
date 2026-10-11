

import sqlite3
try:
    conn = sqlite3.connect('example.db')
except Exception as eobj:
    print(f"Error occurred: {eobj}")

sth = conn.cursor
sth.execute("select * from example")

for var in sth:
    print(var)
conn.close()




