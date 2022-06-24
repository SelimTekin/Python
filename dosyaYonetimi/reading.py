# try:
#     file = open("newfile2.txt","r") # "r" olmasa da zaten varsayılan olarak çalışır.
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası.")
# finally:
#     print("Dosya kapandı.")
#     file.close()


file = open("newfile.txt","r", encoding = "utf-8")

# for döngüsü

# for i in file:       # dosyayı satır satır okur
#     print(i, end="") # end="" print'ten sonra bir satır boşluk bırakmasını engeller


# **************read() fonksiyonu

# content1 = file.read()

# print("içerik 1")
# print(content1)

# file = open("newfile.txt","r", encoding = "utf-8")

# content2 = file.read()
# print("içerik 2")
# print(content2) # cursor sona içeriğin sonuna geldi. okuyacak içerik kalmadığı için bi şey yazmaz. (Eğer bi üstteki file değişkeni olmazsa tabi)


# content = file.read(5) # 5 byte yani her karakter 1 byte # Çıktı: Selim
# content = file.read(3) # cursor 5. karakterin sonunda olduğu için oradan itibaren okumaya başlar. # Çıktı: (boşluk karakteri)Te
# content = file.read(3) # Çıktı: kin

# print(content)


# **************readline() fonksiyonu

# print(file.readline(),end="") # satır olarak okur
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline()) # boşluk olur satırda
# print(file.readline()) # boşluk olur satırda


# **************readlines() fonksiyonu
liste = file.readlines()

print(liste) # liste olarak yazar. Her satır sonunda \n ifadesi bulunur

print(liste[0],end="")
print(liste[1])
print(liste[2])

file.close()