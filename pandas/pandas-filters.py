import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 75).reshape(15, 5)
df = pd.DataFrame(data, index =range(1, 16), columns = ["Column1", "Column2", "Column3", "Column4", "Column5"])

result = df
result = df.columns # DataFrame'deki kolon adları gelir
result = df.head() # DataFrame'deki ilk 5 satır gelir
result = df.head(10) # DataFrame'deki ilk 10 satır gelir
result = df.tail() # DataFrame'deki son 5 satır gelir
result = df.tail(10) # DataFrame'deki son 10 satır gelir
result = df["Column1"].head() # DataFrame'deki ilk 5 satırın Column1'ini getirir
result = df.Column1.head() # aynı
result = df[["Column1", "Column2"]].head() # DataFrame'deki ilk 5 satırın Column1 ve Column2'sini getirir
result = df[["Column1", "Column2"]].tail() # DataFrame'deki son 5 satırın Column1 ve Column2'sini getirir
result = df[5:15][["Column1", "Column2"]].head() # 5'ten 15'e kadar ilk 5 satırın Column1 ve Column2'sini getirir
result = df[5:15][["Column1", "Column2"]].tail() # 5'ten 15'e kadar son 5 satırın Column1 ve Column2'sini getirir

result = df > 50 # 50'den büyükler için True küçükler iççin False yazar DataFramede
result = df[df > 50] # 50'den büyükleri(True değil değerlerini) yazar küçüklerin yerine NaN(Not a Number) yazar
result = df % 2 == 0
result = df[df["Column1"] > 50] # Column1'de 50'den büyük olan bütün satır ve sütunları yazar(diğer kolonlarda 50'den küçükler de yazar)
result = df[df["Column1"] > 50][["Column1", "Column2"]] # Column1'de 50'den büyük olan Colun1 ve Column2'yi yazar(2'de 5'den küüçük olsa dahi)
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
result = df[(df["Column1"] > 50) | (df["Column2"] <= 70)][["Column1", "Column2"]]
result = df.query("Column1 >= 50 & Column1 % 2 == 0") # 50'den büyük çift sayılar gelir
result = df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1", "Column2"]] # Column1 ve Column2'deki 50'den büyük çift sayılar gelir
result = df.query("Column1 >= 50 | Column1 % 2 == 0")[["Column1", "Column2"]] 

print(result)