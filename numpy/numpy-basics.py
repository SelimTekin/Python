import numpy as np

# python list
py_list = [1,2,3,4,5,6,7,8,9]

# numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9]) # tek boyutlu dizi

print(type(py_list)) # list
print(type(np_array)) # numpy ndarray

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)    # matris oluşturduk(2 boyutlu)

print(np_array.ndim) # 1 (boyut)
print(np_multi.ndim) # 2 (boyut)

print(np_array.shape) # Çıktı: (9,) (tek boyutlu oluyor yani)
print(np_multi.shape) # Çıktı: (3, 3) (3'e 3'lük matris 2 boyutlu yani)