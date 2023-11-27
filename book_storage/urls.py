from django.urls import path, re_path
from book_storage import views


urlpatterns = [
    path('author/<slug:author_name>/', views.author_books, name='author_books'),
    path('genres/<slug:genre_name>/', views.genre_books, name='genre_books'),
    path('books/<str:book_name>/', views.book_info, name='book_info'),
    re_path(r'^authors', views.authors, name='authors'),
    re_path(r'^genres', views.genres, name='genres'),
    re_path(r'^books', views.books, name='books'),
    re_path(r'^', views.index, name='home'),
]
