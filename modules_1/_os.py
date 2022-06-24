import os
import datetime

# result = dir(os)
# result = os.name # Çıktı: nt (Yani windows işletim sistemi)

# Dizin değiştirme
# os.chdir("C:\\") # C dizinine gitti
# os.chdir("../..") # 2 üst dizine gitti


# Klsaör oluşturma
# os.mkdir("newdirectory") # C dizininde(yukardıa gittik C dizinine) newdirectory adında klasör oluşturdu
# os.makedirs("C:/Users/selim/Desktop/python_temelleri7modules_1/newdirectory/yeniklasör")
# os.makedirs("newdirectory/yeniklasör") # aynı
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory") # bulunduğu dizindeki klasörü siler
# os.removedirs("yeniklaör/yeniklaör") # herhangi bi dizindeki klasörü silmek için

# Etkin dizin öğrenme (Bulunduğumuz dizin)
# result = os.getcwd() # Çıktı: C:\Users\selim\Desktop\python_temelleri\modules_1 (bu dosyanın path'ini gösterdi)


# Listeleme
# result = os.listdir() # Çıktı: ['date.py', 'newdirectory', 'os.py'] (bu dizindeki)
# result = os.listdir('C:\\') # (C dizinindekileri listeler)
# for dosya in os.listdir():
#     if dosya.endswith('.py'): # sonu .py ile biten (yani py uzantılı) dosyaları listeler
#         print(dosya)

# result = os.stat("date.py")
# result = result.st_size/1024 # 1024'e bölerek byte'tan kb'ye çevirdik
# result = datetime.datetime.fromtimestamp(result.st_ctime) # Çıktı: 2022-06-21 14:49:40.710941 (dosyanın oluşturulma zamanı)
# result = datetime.datetime.fromtimestamp(result.st_atime) # a -> access (son erişilme tarihi)
# result = datetime.datetime.fromtimestamp(result.st_mtime) # m -> modified (değiştirilme tarihi)

# os.system("notepad.exe") # notepad programını açtı


# path (dosya ismi vs değiştirme)
# result = os.path.abspath("os.py") # os.py dosyasının tam yolunu verir
# result = os.path.dirname("C:/Users/selim/Desktop/python_temelleri/modules_1/os.py") # taqm konumu verilen dosyanın dizin ismini alıyoruz
# result = os.path.dirname(os.path.abspath("os.py")) # tam yolunu bilmediğimiz dosyanın dizinini bulmak için
# result = os.path.exists("os.py") # aradığımız konumda dosya var mı (True döner)
# result = os.path.exists("C:/Users/selim/Desktop/python_temelleri/modules_1/os.py") # aynı (True döner)
# result = os.path.exists("C:/Users/selim/Desktop/python_temelleri/modules_1/os2.py") # aynı (False döner)
# result = os.path.exists("C:/Users/selim/Desktop/python_temelleri/modules_1") # klasör sorguladık var mı diye (True döner)
# result = os.path.exists("C:/Users/selim/Desktop/python_temelleri/modules_12") # aynı (False döner)
# result = os.path.isdir("C:/Users/selim/Desktop/python_temelleri/modules_1") # klasör mü diye sorduk (True döner)
# result = os.path.isdir("C:/Users/selim/Desktop/python_temelleri/modules_12") # aynı (False döner olmadığı için)
# result = os.path.isdir("C:/Users/selim/Desktop/python_temelleri/modules_12") # aynı (False döner dosya olduğu için)
# result = os.path.isfile("C:/Users/selim/Desktop/python_temelleri/modules_1/os.py") # dosya mı diye sorduk (True döner)
# result = os.path.isfile("C:/Users/selim/Desktop/python_temelleri/modules_1") # aynı (False döner)
# result = os.path.join("C:\\","deneme","deneme1") # Çıktı: C:\deneme/deneme1 dizinleri birleştirdi (isdir diye sorarsak False döner olmadığı için)
# result = os.path.split("C:\\deneme") # Çıktı: ('C:\\', 'deneme') dizinleri ayırdı
# result = os.path.splitext("os.py") # Çıktı: ('os', '.py') dosyanın ismini ve uzantısını ayırır
# result = result[0] # Çıktı: os (dolayısıyla dosya ismini değiştirmek için uzantısından ayırıp değiştirmeliyiz)
# result = result[1] # Çıktı: .py

# Dosya adını değiştirme
result = os.path.abspath("os.py")
# oldbase = os.path.splitext("os") # bu olursa dosyanın değiştirdiğimiz isimli kopyası olur
newname = result.replace('os', '_os')
result = os.rename(result,newname)

print(result)
