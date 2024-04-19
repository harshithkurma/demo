import sqlite3 as sql
conn = sql.connect("test.db")
cursor = conn.cursor()
cursor.execute('select * from test')
result = cursor.fetchall()
print(result)
for row in result: print(result)# To print individual tuples