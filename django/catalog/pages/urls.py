from django.urls import path
from . import views # dosya aynı klasörde olduğu için . (nokta) yazdık

# http://127.0.0.1:8000/
urlpatterns = [
    path('', views.index, name='index'), # http://127.0.0.1:8000/index -> kullanıcı bu şekilde index diye belirtmezse tırnak işareti boş olmalı
    path('about', views.about, name='about')
]