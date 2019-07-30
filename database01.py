#!/usr/bin/env python3

import sqlite3

db.execSQL("create table if not exists test.db(ID, INT, PRIMARY KEY);"
    
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    conn.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT     NOT NULL,
        AGE            INT      NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);''')

print("Table created successfully")

conn.close()

