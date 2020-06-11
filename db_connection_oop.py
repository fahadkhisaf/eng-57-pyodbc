import pyodbc

class MSDBconnection():

    # shoul establish connection with any DB we have in MSsql
    def __init__(self, database='Northwind', server='databases2.spartaglobal.academy', username='SA', password='Passw0rd2018'):
        # 1) DB server connection variables
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        # making connection and cursors
        self.conn = self._establish_connection()
        self.cursor = self.conn.cursor()


    # 2) establishing the connection
    def _establish_connection(self):
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        return connection


    # 3) open to SQL injections
    def sql_query(self, sql_string):
        # call method to filter out DROP table and DELETE * and only allow certain SQL queries
        return self.cursor.execute(sql_string)


# nwind = MSDBconnection()
#
# print(nwind.sql_query('SELECT * FROM PRODUCTS'))
#
# results = nwind.sql_query('SELECT * FROM PRODUCTS')
#
# while True:
#     row = results.fetchone()
#
#     if row == None:
#         break
#     print(row.ProductName)