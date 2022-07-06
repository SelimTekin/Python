from concurrent.futures import thread
import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 15).reshape(5, 3)
df = pd.DataFrame(data, index = ['a', 'c', 'e', 'f', 'h'], columns = ["column1", "column2", "column3"])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# Çıktı:     column1  column2  column3
        # a     94.0     89.0     79.0
        # b      NaN      NaN      NaN
        # c     73.0     46.0     93.0
        # d      NaN      NaN      NaN
        # e     35.0     48.0     29.0
        # f     65.0     91.0     34.0
        # g      NaN      NaN      NaN
        # h     72.0     61.0     23.0

newColumn = [np.nan, 30, np.nan, 51, np.nan, 30, np.nan, 10]
df["column4"] = newColumn

result = df
result = df.drop("column1", axis=1) # column1 silindi. axis=0 -> satır, axis=1 -> sütun
result = df.drop(["column1", "column2"], axis=1) # column1 ve column2 silindi.
result = df.drop("a", axis=0) # a satırı silindi.
result = df.drop(["a", "b", "h"], axis=0) # a, b, h satırları silindi.

result = df.isnull() # null mü ? evet null veya hayır null değil
result = df.notnull() # null değil mi ? evet null değil veya hayır null
# result = df.isnull().sum()
# Çıktı:  column1    3 # toplam 3 tane true var column1'de
        # column2    3
        # column3    3
        # dtype: int64
    
result = df["column1"].isnull().sum() # 3
result = df["column1"].isnull()
result = df[df["column1"].isnull()]
result = df[df["column1"].isnull()]["column1"]
result = df[df["column1"].notnull()]["column1"]

result = df.dropna() # herhangi bir satırda nan varsa o satır silinir. varsayılan axis = 0 -> satıra göre
result = df.dropna(axis=1) # herhangi bir sütunda nan varsa o sütun silinir.
result = df.dropna(how = "any") # bir satırdaki herhangi bir kolonda nan varsa satır komple silinir
result = df.dropna(how = "all") # bir satırdaki tüm kolonlar nan ise satır komple silinir
result = df.dropna(subset = ["column1", "column2"], how = "any") # column1 ve 2'nin herhangi birinde nan var ise satır komple silinir
result = df.dropna(subset = ["column1", "column2"], how = "all") # column1 ve 2'nin hepsinde nan var ise satır komple silinir
result = df.dropna(thresh = 2) # en az 2 tane kolonda normal veri olanlar (yani nan olmayanlar)
result = df.dropna(thresh = 4)

result = df.fillna(value = 'no input') # nan olanların yerine no input yazar
result = df.fillna(value = 1) # nan olanların yerine 1 yazar (çarpma işlemi yapacaksak mesela)

result = df.sum() # her satırdaki kolonların toplam değerleri
result = df.sum().sum() # her satırdaki kolonların toplam değerlerinin toplamı (yani her şeyin toplamı)
result = df.size # nan olanlar dahil toplam eleman sayısı gelir
result = df.isnull().sum() # her kolondaki nan sayısı
result = df.isnull().sum().sum() # toplam nan sayısı

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet


result = df.fillna(value = ortalama(df)) # nan olan yerlere ortalamayı yazar

print(df)
print(result)