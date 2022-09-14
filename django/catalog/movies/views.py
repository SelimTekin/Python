from django.shortcuts import render

# Create your views here.

# render edeceğimiz sayfa template klasörü altındaki (template yazılmıyor) movies klasörü altındaki list.html sayfası
def index(request):
    return render(request, 'movies/list.html')

def detail(request):
    return render(request, 'movies/detail.html')

def search(request):
    return render(request, 'movies/search.html')