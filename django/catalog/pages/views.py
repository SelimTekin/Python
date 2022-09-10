from django.shortcuts import render
from django.http import HttpResponse # yanıt almak için

# Create your views here.


# http://127.0.0.1:8000/ # bu porta gittiğinde sayfa görünür
def index(request):
    # return HttpResponse('<h1>Hello from pages app</h1>')
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')