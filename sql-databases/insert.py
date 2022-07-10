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

list = []
while True:
    name = input("Ürün adı giriniz: ")
    price = input("Ürün fiyatı giriniz: ")
    imgUrl = input("Ürün resim adı giriniz: ")
    description = input("Ürün açıklaması giriniz: ")

    list.append((name, price, imgUrl, description))

    result = input("Devam etmek istiyor musunuz ? (e/h)")

    if result == 'h':
        print("Kayıtlarınız veritabanına aktarılıyor...")
        print(list)
        insertProducts(list)
        break

# insertProduct(name, price, imgUrl, description)