import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'sakib123'
)

curserObject = database.cursor()

curserObject.execute("CREATE DATABASE tushanco")

print("All Done!")