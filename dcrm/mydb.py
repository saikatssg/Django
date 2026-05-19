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

#add repository as project under git

# git config --global user.name "saikatssg"
# git config --global user.email "rccsaikat@gmail.com"
#  git config --global push.default matching
# git config --global alias.co checkout
# git init