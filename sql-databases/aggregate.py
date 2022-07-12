import mysql.connector

def getProductInfo():
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "node-app")
    cursor = connection.cursor()

    sql = "select count(*) from products" # Satır sayısını getirir
    sql = "select avg(Price) from products" # ortalama (bu arada büyük küçük harf duyarlılığı yok :) Price ile price aynı oluyor)
    sql = "select sum(Price) from products" # toplam
    sql = "select min(Price) from products" # minimum fiyat
    sql = "select max(Price) from products" # maksimum fiyat
    sql = "select name, price from products where price = (select max(price) from products)" # maksimum fiyata sahip isim ve fiyat
    
    cursor.execute(sql)

    result = cursor.fetchone() # fetchone liste şeklinde getirmez

    print(f"result: {result[0]} {result[1]}")

getProductInfo()