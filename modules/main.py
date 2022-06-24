import mod # Kendi oluşturduğumuz mod modülünü python klasörünün(lib klasörü yani modüllerin olduğu klasör) içine koyduk yine çalıştı. Aynı dizinde bulamazsa gidip o klasöre bakar yine çalışır.

# C:\Users\selim\AppData\Local\Programs\Python\Python310\Lib (mod bu pathte)

# math modülü gibi bazı modülleri yukarıdaki pathte bulamauyabiliriz çünkü 
# bunlar c ile yazılıp dll(kütüphane) haline çevirilmiştir. (Hız açısından)


# help(mod)
# help(mod.func)
result = mod.number # Çıktı: 10
result = mod.numbers # Çıktı: [1, 2, 3]
result = mod.person['name'] # Çıktı: Selim
result = mod.person['age'] # Çıktı: 19
result = mod.func(10)

p = mod.Person()
p.speak()
print(result)

# import sys
# sys.path # aşağıdaki terminale bunları yazarsak modülün bulunduğu konumu gösterir
# sys.builtin_module_names yazarsak builtin modüllerini görürüz. Bunlar dll şeklinde bilgisayarımızda yer alıyor. -math modülü burada-