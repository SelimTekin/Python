import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", # örneğin bir oyun yaptığında sunucu hostu satın alman lazım (192.23.45.56)
    user = "root",
    password = "",
    database = "denemepython"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW DATABASES")
# # mycursor.execute("CREATE DATABASE denemepython")

# for x in mycursor:
#     print(x)