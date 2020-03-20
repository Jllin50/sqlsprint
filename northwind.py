import sqlite3
import pandas as pd

DB_FILEPATH = 'northwind_small_plural.sqlite3'
connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

#Top 10 highest priced products

query = '''SELECT ProductName, UnitPrice FROM Products
  ORDER BY UnitPrice DESC
  LIMIT 10'''
result = cursor.execute(query).fetchall()
print(f'The top 10 highest priced products and their price: \n {result}\n')

# Average age at hire date

query = '''SELECT avg(HireDate - BirthDate) FROM Employees'''
result = cursor.execute(query).fetchall()
print(f'Average Age at Hire Date: \n {result[0][0]}\n')

# Stretch - How does the average age of employee at hire vary by city?

query = '''SELECT City, avg(HireDate - BirthDate)
FROM Employees
GROUP BY City'''
result = cursor.execute(query).fetchall()
print(f'Average age of employee at hire date by city:')
for s in result:
  print(f'{s[0]}: {s[1]}')
print()
  

# - What are the ten most expensive items (per unit price) in the database *and* their suppliers

query = '''SELECT ProductName, CompanyName FROM Products, Suppliers
WHERE Products.SupplierID = Suppliers.SupplierID
ORDER BY Products.UnitPrice DESC
LIMIT 10'''
result = cursor.execute(query).fetchall()
print(f'Most expensive items and their suppliers: {result}\n')

# - What is the largest category (by number of unique products in it)?

query = '''SELECT CategoryName FROM Categories, Products
GROUP BY Categories.CategoryID
ORDER BY COUNT(DISTINCT Products.ProductID) DESC
LIMIT 1'''
result = cursor.execute(query).fetchall()
print(f'Largest product category: {result[0][0]}')

