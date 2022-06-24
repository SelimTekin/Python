
# message = 'Hello there. My name is Selim'

# message = message.upper() # Hepsi büyük
# message = message.lower() # Hepsi küçük
# message = message.title() # Her kelimenin baş harfleri büyük
# message = message.capitalize() # Sadece ilk harf büyük
# message = message.strip() # baştaki ve sondaki boşluk karakterleri silinir
# message = message.lstrip() # soldaki boşluk karakterleri silinir
# message = message.rstrip() # sağdaki boşluk karakterleri silinir
# message = message.lstrip('leH') # parametredeki karakterler baştan silinir Çıktı: o there. My name is Selim.
# message = message.split() # Her kelime boşluk karakterlerinden ayrılıp bir diziye atanır
# message = message[2] # Ayrılan dizinin 2 indexinde bulunan kelimeyi döndürür
# #message = message.split('.') # Her kelime nokta karakterlerinden ayrılıp bir diziye atanır
# message = '*'.join(message) # diziye ayrılan kelimeleri birleştirip arasına yıldız koyar

# index = message.find('Selim') # Parametredeki kelimenin kaçıncı indexten başladığını yazar eğer yoksa -1 döndürür

# isFound = message.startswith('H') # String parametredeki karakter ile mi başlıyor
# isFound = message.endswith('n') # String parametredeki karakter ile mi bitiyor


# message = message.replace('Selim','Yavuz') # Birinci parametreyi ikincisiyle değiştirir
# message = message.replace(' ', '*',5) # 5 karakter değiştirir.
# message = message.replace(' ', '') # boşluk karakterleri silinir
# message = message.replace(' ', '*').replace('e','a')
# message = message.replace('ç', 'c').replace('ö','o') # Mesela url yazarken Türkçe karakterleri İngilizce karakterlerle değiştirmek içiin kullanılır

# message = message.center(100) # 100 karakterlik bir konteynır oluşturup stringi ortalar
# message = message.center(100,'*') # 100 karakterlik bir konteynır oluşturup eşit sayıda yıldızın arasına alır
# message = message.ljust(100,'*') # İfadeyi sola yaslar sağına yıldız ekler
# message = message.ljust(100,'*') # İfadeyi sağa yaslar soluna yıldız ekler

message = 'www.selimtekin.com'
course = 'Selim Tekin Python kursu (40 saat)'
# message = message.strip('w.ocm')
# message = message.count('a')
# message = message.count('www')
# message = message.count('www',0,10) # 0 ile 10 arasında kaç adet www var

# course = course.isalpha() # String alfabetik mi diye bakar. Course stringi alfabetik değildir çünkü sayı barındırıyor(4)
course = course.isdigit() # course nümerik mi diye bakar. Nümerik değil çünkü harf var
print(course)
