import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "schooldb"
)

mycursor = connection.cursor()

# mycursor.execute("Show Database")

mycursor.execute("Show Tables")

for i in mycursor:
    print(i)