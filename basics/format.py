name = 'Selim'
surname = 'Tekin'
age = 19

# print('My name is {} {}'.format(name,surname))
# print('My name is {1} {0}'.format(name,surname))
# print('My name is {s} {n}'.format(n=name,s=surname))
# print('My name is {} {}'.format(name,surname))
# print("My name is {} {} and I'm {} years old".format(name,surname,age))

#result = 200 / 700
# print("the result is {r:10.4}".format(r=result)) # 10, karakterler dahil kaç boşluk bırakalacağını belirtir 1 yazalım ki boşluk olmasın

print(f"My name is {name[-3:-1]} {surname} and I'm {age} years old")
print(f"My name is {name[::2]} {surname} and I'm {age} years old") # 2 karakterde bir yazıyor
print(f"My name is {name[::-1]} {surname} and I'm {age} years old") # Tersten yazıyor

s = '12345' * 5 # ifadeyi 5 kere yazar
print(s)