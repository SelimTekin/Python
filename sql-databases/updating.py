import mysql.connector

def updateProduct(id, name, price):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "node-app")
    cursor = connection.cursor()

    # if name!='': # boşluğun karşılığı False'tur. Burada da name boş değilse diye sorduk veya şu şekilde olur (not name)
    sql = "update products set name=%s,price=%s where id=%s" # where olmazsa bütün satırlar etkilenir
    values = (name, price, id)
    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi.")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")

updateProduct(1, 'Iphone 8', 6000)