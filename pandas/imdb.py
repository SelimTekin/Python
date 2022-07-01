import numbers
import pandas as pd

df = pd.read_csv("imdb.csv")

# 1- Dosya hakkındaki bilgiler.
result = df     # ilk ve son 5 satır gelir ortadakilerin yerine ... yazar
result = df.columns     # kolon adları
result = df.info # DataFrame infosu gelir (farkı yok anladığım kadarıyla yani satır ve sütunlar geliyor)

# 2- İlk 5 kaydı gösterin
result = df.head()

# 3- İlk 10 kaydı gösterin
result = df.head(10)

# 4- Son 5 kaydı gösterin
result = df.tail()

# 5- Son 10 kaydı gösterin
result = df.tail(10)

# 6- Sadece title kolonunu alın.
result = df["movie name\r\n"]

# 7- Sadece title kolonunu içeren ilk 5 kaydı alın.
result = df["movie name\r\n"].head()

# 8- Sadece title ve rating kolonunu içeren ilk 5 kaydı alın.
result = df[["movie name\r\n", "RATING"]].head()

# 9- Sadece title ve rating kolonunu içeren son 7 kaydı alın.
result = df[["movie name\r\n", "RATING"]].tail(7)

# 10- Sadece title ve rating kolonunu içeren ikinci 5 kaydı alın.
result = df[5:10][["movie name\r\n", "RATING"]].head()
result = df[5:10][["movie name\r\n", "RATING"]] # aynı

# 11- Sadece title ve rating kolonunu içeren ve imdb puanı 8.0 ve üstünde olan kayıtlardan ilk 50 tanesini alınız.
result = df[df["RATING"] >= 8.0][["movie name\r\n", "RATING"]].head(50)

# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getririniz.
i = 0
years = {"movies": []}
for i in range(len(df["Year"])):
    year = int(df["Year"][i])

    # print(type(year)) # int olduğundan emin olduk
    # if year < 0:     # yıllar negatif onu anladık
    #     print(year)

    if ((year <= -2010) & (year >= -2019)):
        years["movies"].append(df.loc[i]["movie name\r\n"])

    i += 1
result = pd.DataFrame(years)
# result = df[(df["Year"] >= 2014) &(df["Year"] <= 2015)][["movie name\r\n", "Year"]]
# result = type(df["Year"][0]) # str

# 13- Değerlendirme sayısı (votes) 100.000'den büyük ya da imdb puanı 8 ile 9 arasında olan filmleri listeleyiniz.
# i = 0
# votes = {"movies": [], "votes": []}
# for i in range(len(df["votes"])):
#     vote = df["votes"][i].replace(",", "")
#     rating = df["RATING"][i]
#     if ((int(vote) > 100000)) | ((rating >= 8) & (rating <= 9)):
#         votes["movies"].append(df.loc[i]["movie name\r\n"])
#         votes["votes"].append(df.loc[i]["votes"])

#     i += 1
# result = pd.DataFrame(votes)

# Hocanın yaptığı
# Bunda veriler string olduğu için sayısal karşılaştırma yapılamıyor. Üstte kendim sayısal verilere çevirip dictionary'e attım ve öyle yazdırdım.
# result = [(df["votes"] > 100000) | ((df["RATING"] >= 8) & (df["RATING"] <= 9))][["movie name\r\n", "votes"]]

# print(df.columns)
print(result)