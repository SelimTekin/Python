# username = 'Selim'
# password = '12345'

# if (username == 'Selim'):
#     if(password == '1234'):
#         print('Hoşgeldiniz')
#     elif(password != '1234'):
#         print('Parola yanlış')
# else:
#     print('username yanlış')

import datetime

tarih = input("aracınız hangi tarihte trafiğe çıktı (2022/6/13): ")
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days <= 365:
    print("1. servis aralığı")
elif days > 365 and days <= 365*2:
    print("2. servis aralığı")
elif days > 365*2 and days <= 365*3:
    print("3. servis aralığı")
else:
    print('hatalı bilgi girdiniz')