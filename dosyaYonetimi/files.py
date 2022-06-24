# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.


# "w": (Wirte) yazma modu. Dosyayı konumda oluşturur.
#   Dosyayı konumda oluşturur
#   Dosya mevcutsa içeriğini siler ve yeniden ekleme yapar

# file = open("newfile.txt","w")
# file = open("C:/users/selim/desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding='utf-8') # encoding => kullanılan karakter türünü belirtir(utf-8 Türkçe karakter bilindiği üzere)
# file.write("Selim Tekin")
# file.close()
# file = open("newfile.txt","w",encoding='utf-8') # tekrardan burada çağırırsak içerik silinir


# "a":  (Append) sonuna ekleme. Dosya konumda yoksa oluşturur.
# file = open("newfile.txt","a",encoding='utf-8')
# file.write("Selim Tekin\n")
# file.close()


# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# file = open("newfile2.txt","x",encoding='utf-8')


# "r": (Read) okuma. varsayılan. Dosya konumda yoksa hata verir