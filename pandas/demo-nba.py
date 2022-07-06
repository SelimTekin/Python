import pandas as pd

df = pd.read_csv("datasets/nba.csv")

# 1- İlk 10 kaydı getiriniz
result = df.head(10)

# 2- Toplma kaç kayıt vardır ?
result = len(df.index) # 11700

# 3- Tüm oyuncuların toplam yaş ortalaması nedir ?
result = df["age"].mean()

# 4- En yaşlı oyuncunun yaşı kaçtır ?
result = df["age"].max() # 44

# 5- En yaşlı oyuncunun adı nedir ?
result = df[df["age"] == df["age"].max()]["player_name"] # 4840    Kevin Willis
result = df[df["age"] == df["age"].max()]["player_name"].iloc[0] # Kevin Willis

# 6- Yaşı 20-35 arasında olan oyuncuların isim ve oyandıkları takımları azalan şekilde sıralı getiriniz.
result = df[(df["age"] >= 20) & (df["age"] < 25)][["player_name", "team_abbreviation", "age"]].sort_values("age", ascending = False)

# 7- "John Holland" isimli oyuncunun oynadığı takımın ismi nedir ?
result = df[df["player_name"] == "John Holland"]["team_abbreviation"].iloc[0]

# 8- Takımlara göre oyuncuların ortalama yaş bilgisi nedir ?
result = df.groupby("team_abbreviation").mean() # Her kolondaki bilgilerin ortalamasını yazar
result = df.groupby("team_abbreviation").mean()["age"] # Sadece takımların yaş ortalaması yazar

# 9- Kaç farklı takım mevcuttur ?
result = len(df.groupby("team_abbreviation"))
result = len(df["team_abbreviation"].unique())
result = df["team_abbreviation"].nunique() # bu da sayısını verir yani aynı

# 10- Her takımda kaç oyuncu oynamaktadır ?
result = df["team_abbreviation"].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
df.dropna(inplace = True) # NaN olanları temizler. inplace = True ile orijinal listeyi güncelledi. (bizim tablomuzda yok ama yazalım yine de)
result = df[df["player_name"].str.contains("and")]

# İkinci yöntem
def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["player_name"].apply(str_find)]

print(result)