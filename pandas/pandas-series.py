import pandas as pd         # pandas heterojen bir kütüphanedir. Farklı tipte veriler alabilir.
import numpy as np          # numpy homojen bir kütüphanedir. Farklı tipte veriler alamaz.


# data
# numbers = [20, 30, 40, 50]
# letters = ['a', 'b', 'c', 'd']
# scalar = 5
# dict = {'a':10, 'b':20, 'c':30, 'd':40}
# random_numbers = np.random.randint(10, 100, 6)

# pandas_series = pd.Series()
# pandas_series = pd.Series(numbers)
# Çıktı:  0    20
        # 1    30
        # 2    40
        # 3    50
        # dtype: int64

# pandas_series = pd.Series(letters)
# Çıktı:  0    a
        # 1    b
        # 2    c
        # 3    d
        # dtype: object

# pandas_series = pd.Series(scalar, [0, 1, 2, 3])
# Çıktı:  0    5
        # 1    5
        # 2    5
        # 3    5
        # dtype: int64

# pandas_series = pd.Series(numbers, ['a', 'b', 'c', 'd'])
# Çıktı:  a    20
        # b    30
        # c    40
        # d    50
        # dtype: int64

# pandas_series = pd.Series(dict)
# Çıktı:  a    10
        # b    20
        # c    30
        # d    40
        # dtype: int64

# pandas_series = pd.Series(random_numbers)
# Çıktı:  0    27
        # 1    96
        # 2    11
        # 3    38
        # 4    16
        # 5    16
        # dtype: int32
    
# pandas_series = pd.Series([20, 30, 40, 50], ['a', 'b', 'c', 'd'])
# result = pandas_series[0] # 20
# result = pandas_series[-1] # 50
# result = pandas_series[:2]  # a    20       # İlk 2 eleman
#                             # b    30
#                             # dtype: int64

# result = pandas_series[-2:] # Son 2 eleman
# result = pandas_series['a'] # 20
# result = pandas_series['d'] # 50
# result = pandas_series[['a', 'c']]  # a    20
                                    # c    40
                                    # dtype: int64

# result = pandas_series[['a', 'c', 'e']]  # a    20
                                    # c    40
                                    # e    NaN (videoda böyle fakat ben çalıştırdığımda hata veriyor)(NaN -> Not a Number)
                                    # dtype: int64

# result = pandas_series.ndim # 1 (boyut)
# result = pandas_series.dtype # int64
# result = pandas_series.shape # (4,) tek boyutlu olduğu için(4 eleman var)
# result = pandas_series.sum() # 140 (toplam)
# result = pandas_series.max() # 50
# result = pandas_series.min() # 20
# result = pandas_series + pandas_series
# Çıktı:  a     40
        # b     60
        # c     80
        # d    100
        # dtype: int64

# result = pandas_series + 50
# Çıktı:  a     70         # Her elemana 50 eklendi
        # b     80
        # c     90
        # d    100
        # dtype: int64

# result = np.sqrt(pandas_series) # Her elemanın karekökü (Çıktılar yukarıdaki gibi görünür)

# result = pandas_series >= 50
# Çıktı:  a    False
        # b    False
        # c    False
        # d     True
        # dtype: bool

# result = pandas_series % 2 == 0

# print(pandas_series[pandas_series % 2 == 0]) # Çift olanlar yazılır
# print(pandas_series)
# print(result)


opel_2018 = pd.Series([20, 30, 40, 50], ['astra', 'corsa', 'mokka', 'insignia'])
opel_2019 = pd.Series([40, 30, 20, 10], ['astra', 'corsa', 'Grandland', 'insignia'])

total = opel_2018 + opel_2019
# Çıktı:  Grandland     NaN
        # astra        60.0
        # corsa        60.0
        # insignia     60.0
        # mokka         NaN
        # dtype: float64

print(total)
print(total['astra']) #  60.0
print(total['combo']) #  hata verir
