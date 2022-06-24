# key - value 34 => İstanbul 57 => Sinop

# sehirler = ['İstanbul','Sinop']
# plakalar = [34,57]

# print(plakalar[sehirler.index('İstanbul')]) # Dictionary olmadan bu şekilde kullanılır. sehirler dizisinde İstanbul'un indexi 0 olduğu için plakalar dizisindeki 0. indexi yazdıracak.

# plakalar = {'İstanbul' : 34, 'Sinop' : 57}

# plakalar['Ankara'] = 6 # Olmayan key eklemesi yapar
# plakalar['Sinop'] = 'new value' # var olan key'in value'sunu değiştirir

# print(plakalar['İstanbul'])
# print(plakalar['Sinop'])

# users = {
#     'selimtekin':{
#         'age' : 19,
#         'roles' : ['admin','user'],
#         'email' : 'selim@gmail.com',
#         'address' : 'İstanbul',
#         'phone' : '123456'
#     },
#     'enesdönmez':{
#         'age' : 19,
#         'roles' : ['user'],
#         'email' : 'enes@gmail.com',
#         'address' : 'İstanbul',
#         'phone' : '123456789'
#     }
# }
# print(users['selimtekin']['roles'][0])

# ----------------- Dictionary Demo -----------------

ogrenciler = {}

number = input('Öğrenci no: ')
name = input('Öğrenci ad: ')
surname = input('Öğrenci soyad: ')
phone = input('Öğrenci telefon: ')

# ogrenciler[number] = {
#     'name' : name,
#     'surname' : surname,
#     'phone' : phone
# }                        # tek bir veri için

ogrenciler.update({
    number : {
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone
    }
})                         # birden fazla veri için

print(ogrenciler)

print('*'*50)



ogrNo = input('Öğrenci no: ')
ogrenci = ogrenciler[ogrNo]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")