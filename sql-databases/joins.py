from math import prod
from matplotlib.pyplot import getp
import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "node-app")
    cursor = connection.cursor()

    # sql = "select * from products"
    # sql = "select * from categories"
    # sql = "select * from products inner join categories on categories.cat_id=products.cat_id" # products ve categories tablosundaki bilgiler aynı tupleda gelir.(Satır satır birleştirilerek tabi)
    # sql = "select products.name, products.price, categories.cat_name from products inner join categories on categories.cat_id=products.cat_id where categories.cat_name='Telefon'"
    sql = "select p.name, p.price, c.cat_name from products as p inner join categories as c on c.cat_id=p.cat_id where p.name='Samsung S6'"
    
    cursor.execute(sql)

    try:
        result = cursor.fetchall()
        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")

getProducts()