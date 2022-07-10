# dosya adı select olursa çalıştırdğımızda hata alırız. (select mysql modülü içerisinde olan bir komut)

from math import prod
import mysql.connector

def insertProduct(name, price, imgUrl, description):
    connection  = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name, price, imgUrl, description) VALUES(%s, %s, %s, %s)"
    values = (name, price, imgUrl, description)

    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'Son eklenen kaydın id {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")

def insertProducts(list):
    connection  = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name, price, imgUrl, description) VALUES(%s, %s, %s, %s)"
    values = list

    cursor.executemany(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'Son eklenen kaydın id {cursor.lastrowid + 1}')
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")


def getProducts():
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "node-app")
    cursor = connection.cursor()

    # cursor.execute("select * from products")
    cursor.execute("select name, price from products")

    # result = cursor.fetchall() # hepsini getirir
    result = cursor.fetchone() # ilk kaydı getirir
    print(f"name: {result[0]} price: {result[1]}")

    # for product in result:
    #     # print(f"name: {product[1]} price: {product[2]}")
    #     print(f"name: {product[0]} price: {product[1]}")

    # print(result)

getProducts()