# SQLite server tabanlı bir veritabanı değil. json, excel gibi bir dosya
# sadece bir uygulama için kullanılacaksa uygulamalar arası bilgiler paylaşılmayacaksa sadece bir uygulamaya özel bilgiler olacaksa sqlite kullanılabilir.

import sqlite3
from tkinter import N # python ile birlikte gelir. PyPi ile bir paket yüklememize gerek yok

connection = sqlite3.connect("chinook.db") # aynı klasör içerisinde böyle bir veritabanı arar. Yoksa oluşturur

cursor = connection.cursor()

cursor.execute("select * from customers")
result = cursor.fetchall()
# print(result)

for i in result:
    print(i)

connection.close()