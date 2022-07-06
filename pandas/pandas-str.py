import pandas as pd

data = pd.read_csv("datasets/nba.csv")

# count = data.isnull().sum().sum() # hiç nan yok ama yine de nan olanları silelim
data.dropna(inplace = True) # seriyi günceller

# data["player_name"] = data["player_name"].str.upper()
# data["player_name"] = data["player_name"].str.lower()
# data["index"] = data["player_name"].str.find('a') # a'nın kaçıncı indexte olduğunu bulan fonksiyon
# data = data.player_name.str.contains("Jordan") # İçinde Jordan olanlara True yazdı (diğerleri False)
# data = data[data.player_name.str.contains("Jordan")] # İçinde Jordan olanları getirdi
# data = data.player_name.str.replace(' ', '-').str.repalce('*', '')
data[["FirstName", "LastName"]] = data['player_name'].loc[data['player_name'].str.split().str.len()==2].str.split(expand=True) # ad soyad olarak ayırdık isimleri (tek adlı olanları)

# print(data.columns) # kolonların ne olduğuna baktık
print(data.head(10))