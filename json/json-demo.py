
# En altta notlar var

import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user) # bir objeye dönüştürdük(bu olmadan alttaki şekilde username çağıramayız)
                    newUser = User(username=user['username'], password=user['password'], email=user['email'])
                    self.users.append(newUser)
                print(self.users)

    def register(self, user: User): # User tipinde user paramtresi
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu.\n")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Login yapıldı.")
                break
        
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Çıkış yapıldı.')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('Giriş yapılmadı.')

    def savetoFile(self): # Bu bilgileri alıp JSON bilgisi olarak database'e kaydedecek
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__)) # user bir class ve onu dictionary'e çeviriyoruz listeye append etmek için
        with open('users.json', 'w') as file:
            json.dump(list, file) # users'ı file olarak kaydediyoruz

repository = UserRepository()
while True:
    print("Menü".center(50,"*"))
    secim = input('1-Register\n2-Login\n3-Logout\n4-identity\n5-Exit\n\n')

    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username=username, password=password, email=email)
            repository.register(user)

        elif secim == '2':
            if repository.isLoggedIn:
                print('Zaten giriş yaptınız.')
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)
        elif secim == '3':
            repository.logout()
        elif secim == '4':
            repository.identity()





# dumps: kayıt edilebilir json bilgiye çeviriyoruz(dosyaya kaydederken değil)
# dump: json dosyasına kaydederken kullanıyoruz

# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None