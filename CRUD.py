import pyodbc

class DB:
    def __init__(self, server='databases2.spartaglobal.academy', database='Northwind', username='SA', password='Passw0rd2018'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.connection.cursor()
    # Method to read data from the Products table
    def read(self, what):
        query = self.cursor.execute(f'SELECT {what} FROM Products')
        return query.fetchone()
    # Method to create a new table, which is a clone of the Products table
    def create(self, new_table_name ):
        return self.cursor.execute(f"CREATE TABLE {new_table_name} AS SELECT * FROM Products")
    # Method to update data in the Products table
    def update(self, column_to_change, new_value, condition_column, condition_value):
        return self.cursor.execute(f"UPDATE Products SET {column_to_change} = {new_value} WHERE {condition_column} = {condition_value}")
SpartaDB = DB()
print(SpartaDB.connection)
print(SpartaDB.cursor)
