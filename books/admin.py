from django.contrib import admin
from .models import *

# Register your models here.
class BookCheck(admin.ModelAdmin):
    list_display = ('id_book', 'tieu_de', 'the_loai', 'image' )
    search_fields = ['tieu_de']
    list_filter = ('id_book', 'tieu_de', 'the_loai' )

admin.site.register(Book, BookCheck)
admin.site.register(Category)