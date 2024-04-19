import sqlite3

connection = sqlite3.connect('demo.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS demo(IDNO INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL,AGE INTEGER NOT NULL,SALARY FLOAT NOT NULL)")
INFO = [

    (1001,'ROHIT',38,2710000),
    (1002,'PRASHANTH',29,900000),
    (1004,"HARI",32,1090000),
    (1003,'VENKY',30,1290000)
]
cursor.executemany('INSERT INTO demo (IDNO,NAME,AGE,SALARY) VALUES (?,?,?,?)',INFO)
connection.commit()
connection.close()
print('connection closed.')