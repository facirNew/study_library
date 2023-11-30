from django.contrib import admin

from book_storage.models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'get_genres', 'status']
    list_filter = ['title', 'author', 'genre']
    search_fields = ['title', 'author', 'genre']

    @staticmethod
    def get_genres(obj):
        return [genre.name for genre in obj.genre.all()]

