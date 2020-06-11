import pyodbc

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
db_string ='DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password

py_connect2 = pyodbc.connect(db_string)


cursor = py_connect2.cursor()


print(cursor)


query_result = cursor.execute("SELECT COUNT (*) AS 'Order count' FROM Orders")
print(query_result.fetchone()[0])

query_result2 = cursor.execute("SELECT COUNT(*) AS 'RIO' FROM Orders WHERE Shipcity IN ('Rio de Janeiro') ")
print(query_result2.fetchone()[0])

query_result3 = cursor.execute("""
SELECT COUNT(OrderID) 
FROM Orders 
WHERE ShipCity IN ('Rio de Janeiro','Reims'))
print(query_result3.fetchone()[0])""" )

print(query_result3.fetchone()[0])