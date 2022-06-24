from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

simdi = datetime.now()
# simdi = datetime.today() # aynı


# result = datetime.now()
# result = simdi.year
# result = simdi.month
# result = simdi.day
# result = simdi.hour
# result = simdi.minute
# result = simdi.second

# result = datetime.ctime(simdi) # Çıkıt: Tue Jun 21 14:57:32 2022 (biraz daha detay gün ve ay adı)
# result = datetime.strftime(simdi,'%Y') # Çıktı: '&Y' -> 20022 / '%y' -> 22
# result = datetime.strftime(simdi,'%X') # Çıktı: 15:00:57 (saat)
# result = datetime.strftime(simdi,'%x') # Çıktı: 06/21/22 (tarih)
# result = datetime.strftime(simdi,'%d') # Çıktı: 21 (gün)
# result = datetime.strftime(simdi,'%A') # Çıktı: Tuesday (string olarak gün)
# result = datetime.strftime(simdi,'%B') # Çıktı: June (string olarak ay)
# result = datetime.strftime(simdi,'%Y %B %A') # Çıktı: 2022 June Tuesday

# print(result)


t = '21 June 2022 hour 15:10:30'
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
dt = dt.year
print(dt)

birthday = datetime(2002,11,6,2,0,0) # son 3 parametre olan saat dakika ve saniye bilgilerini vermezsek 00:00:00 olur
print(birthday)

result = datetime.timestamp(birthday) # Çıktı: 1036537200.0 (saniye)
result = datetime.fromtimestamp(result) # Çıktı: 2002-11-06 02:00:00 (saniyeden datetime'a)
result = datetime.fromtimestamp(0) # Çıktı: 1970-01-01 03:00:00 (bilgisayarlar için milat olan tarihe dönüştürür 0. saniye)
result = simdi - birthday # Çıktı: 7167 days, 13:18:38.310405 (tiemdelta)
# result = result.days # Çıktı: 7167
# result = result.seconds # Çıktı: 48075 
# result = result.microseconds # Çıktı: 95310

print(simdi)

result = simdi + timedelta(days=730, minutes=10) # Çıktı: 2024-06-20 15:35:18.627669
result = simdi - timedelta(days=10) # Çıktı: 2022-06-11 15:26:14.965481
print(result)


# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)




# python.org / w3Schools