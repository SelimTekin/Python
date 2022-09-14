from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'isPublished') # admin panelinde bu alanlar gözükür
    list_display_links = ('id', 'name') # admin panelinde id ve name'e tıklandığında o alanlar açılabilmesi için bunu yaptık. Yoksa sadece id için link oluşturuluyor.
    list_filter = ('created_date',) # filtreleme işlemi (kolon adı verdik)
    list_editable = ('isPublished',) # isPublished'ı yayınlanan veya yayınlanmayan olarak işaretlemek için yaptık
    search_fields = ('name', 'description')
    list_per_page = 20

# Register your models here.

admin.site.register(Movie, MovieAdmin)