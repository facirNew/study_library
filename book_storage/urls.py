from django.urls import path, re_path
from book_storage import views


urlpatterns = [
    path('author/<slug:author_name>/', views.author_books, name='author_books'),
    path('genres/<slug:genre_name>/', views.genre_books, name='genre_books'),
    path('books/<slug:book_name>/', views.book_info, name='book_info'),
    path('add_book/', views.add_book, name='add_book'),
    path('search/', views.search, name='search'),
    re_path(r'^author', views.authors, name='authors'),
    re_path(r'^genres', views.genres, name='genres'),
    re_path(r'^books', views.books, name='books'),
    path('', views.index, name='home'),
]
