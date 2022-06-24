list = [1,2,3]
tuple = 1,'iki',3

# print(type(list))
# print(type(tuple))

# print(len(list))
# print(len(tuple))

list = ['Selim', 'Tekin']
tuple = ('Selim', 'Tekin')
names = tuple + ('İcabi','Yunus Emre','Yavuz')  # tuple'ın üzerine ekleme yaptık

list[0] = 'Yavuz' # listenin 0. elemanını değiştirebilirsin
# tuple[0] = 'Yavuz' # Ancak tuple'da değişiklik yapamazsın hata verir

print(names)