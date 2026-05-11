import pymysql

dataBase = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    port = 3307,
)


#prepare a cursor object 
cursorObject = dataBase.cursor() 

cursorObject.execute("CREATE DATABASE IF NOT EXISTS emp")

print("Database connected and verified successfully!")

dataBase.close()