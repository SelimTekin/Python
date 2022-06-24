# a, b, c, d = 5, 5, 10, 4
# username = 'selimtekin'

# result = a==b # True döndürür (a b'ye eşit mi diye sorar)
# result = a != b # False
# result = a >= b # True
# result = (True == 1) # True
# result = (False == 0) # True
# result = False + True + 40 # 41
# result = ('slmtkn' == username) # False

email = 'selim@gmail.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower())

print(f'Email bilgisi doğru mu: {isEmail} ve Parola doğru mu: {isPassword}')