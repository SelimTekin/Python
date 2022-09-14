from django.shortcuts import render
from .models import Movie

# Create your views here.

# render edeceğimiz sayfa template klasörü altındaki (template yazılmıyor) movies klasörü altındaki list.html sayfası
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/list.html', context)

def detail(request):
    return render(request, 'movies/detail.html')

def search(request):
    return render(request, 'movies/search.html')