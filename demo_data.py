import sqlite3
import pandas as pd

DB_FILEPATH = 'demo_data.sqlite3'
connection = sqlite3.connect(DB_FILEPATH)

cursor = connection.cursor()
query = '''CREATE TABLE demo (
    s text PRIMARY KEY,
    x INT,
    y INT
)'''
result = cursor.execute(query)

query = '''INSERT INTO demo (s,x,y)
VALUES 
   ('g',3 ,9),
   ('v',5 ,7),
   ('f',8 ,7);'''

result = cursor.execute(query)

connection.commit()

query = '''SELECT COUNT(*) FROM DEMO'''
result = cursor.execute(query).fetchall()
print(f'Total number of rows: {result[0][0]} \n')\

query = '''SELECT COUNT(*) FROM DEMO
            WHERE x > 5 AND y > 5'''
result = cursor.execute(query).fetchall()
print(f'Number of rows with x and y > 5: {result[0][0]} \n')

query = '''SELECT COUNT(DISTINCT y) FROM DEMO'''
result = cursor.execute(query).fetchall()
print(f'Number of unique y values: {result[0][0]}')


