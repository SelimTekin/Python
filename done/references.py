# value type => string, number  (verinin kendisiyle ilgileniyoruz)
x = 5
y = 25

x = y

y = 10

print(x,y) # Çıktı: 25 10

#reference => list, class  (adresle ilgileniyoruz)

a = ['apple','banana']
b = ['apple','banana']

a = b

b[0] = 'grape'

print(a,b) # Çıktı: ['grape','banana'] ['grape','banana'] çünkü aynı adresi tutuyorlar