# themoviedb.org => film ve dizi arşivi
# themoviedb'nin sunduğu apiyi uygulamanızda kullanınız.
# Anahatar kelimeye göre arama
# En popüler film listesi
# Vizyondaki film listesi

import requests

class TheMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "016d6f1740096827e537c3fdd53bee4c"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()
movieApi = TheMovieDb()

while True:
    secim = input("1 - Popular Movies\n2 - Search Movies\n3 - Exit\n")

    if secim == '3':
        break
    else:
        if secim == '1':
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title']) # sadece film isimleri gelir
        
        elif secim == '2':
            keyword = input("keyword: ")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies['results']:
                print(movie['name'])