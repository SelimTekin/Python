# with open("newfile.txt", "r+", encoding="utf-8") as file: # r+ hem okuma hem yazma
#     file.seek(20) # 20. konumdan itibaren deneme yazar
#     file.write("deneme") # 0. indexten itibaren deneme yazar

# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     print(file.read())

# *******Sayfa sonunda güncelleme***********
# with open("newfile.txt", "a", encoding="utf-8") as file:
#     file.write("\nEnes Dönmez")

# *******Sayfa başında güncelleme***********

# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Enes Dönmez\n" + content
#     # print(content) # şu an dosyaya yazılmadı
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())


# *******Sayfa ortasında güncelleme***********


with open("newfile.txt", "r+", encoding="utf-8") as file:
    list = file.readlines() # dosya satırlarını listeye atar
    list.insert(1, "Ali Korkmaz\n") #1. indexten önce yazar
    file.seek(0)
    # for i in list:
    #     file.write(i)
    file.writelines(list) # for yerine writelines() fonksiyonunu kullandık satır satır yazar

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())