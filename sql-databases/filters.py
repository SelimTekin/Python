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

    # cursor.execute("select * from products where name='Samsung S6' or price>=1000")
    # cursor.execute("select * from products where name like '%Samsung%' and price=3000")
    # içinde Samsung olan kayıtları getirir.(başında Samsung olanlar Samsung%, sonunda olanlar %Samsung ile sorgulanır)
    cursor.execute("select * from products where id=1")

    # result = cursor.fetchall() # tek bir kayıt olsa bile liste şeklinde getirir ancak fetchone liste şeklinde getirmez
    result = cursor.fetchone() # fetchone liste şeklinde getirmez

    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")

def getProductById(id):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "node-app")
    cursor = connection.cursor()

    sql = "select * from products where id=%s"
    params = (id,) # id %s'nin yerine gelecek parametreler oluyor. (virgül olmazsa hata veriyor)
    
    cursor.execute(sql, params)

    result = cursor.fetchone() # fetchone liste şeklinde getirmez

    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")


getProductById(1)