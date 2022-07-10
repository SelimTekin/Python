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

    # cursor.execute("select * from products order by price desc") # tersten yani en yüksek fiyatlıdan sıralar
    cursor.execute("select * from products order by name, price") # önce name'e göre sıralar sonra aynı name'e sahip olanların fiyatına göre sıralar
    
    try:
        result = cursor.fetchall()
        for product in result:
            print(f"id: {product[0]} name: {product[1]} price: {product[2]}")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")
    

def getProductById(id):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "node-app")
    cursor = connection.cursor()

    sql = "select * from products where id=%s"
    params = (id,) # id %s'nin yerine gelecek parametreler oluyor. (virgül olmazsa hata veriyor)
    
    cursor.execute(sql, params)

    result = cursor.fetchone() # fetchone liste şeklinde getirmez

    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")


getProducts()