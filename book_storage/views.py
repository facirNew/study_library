from django.core.paginator import Paginator
from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import *

login_menu = [{'title': 'Вход', 'url_name': 'signin'},
              {'title': 'Регистрация', 'url_name': 'signup'},
              ]
menu = [
    {'url': 'home', 'name': 'На главную'},
    {'url': 'authors', 'name': 'Авторы'},
    {'url': 'genres', 'name': 'Жанры'},
]
context = {'menu': menu, 'login_menu': login_menu}


def index(request):
    book_list = Book.objects.all().order_by('?')[:10]
    context['books'] = book_list
    return TemplateResponse(request, 'book_storage/index.html', context=context)


def genres(request):
    page_number = request.GET.get('page')
    genres_list = Genre.objects.all().order_by('name')
    paginator = Paginator(genres_list, 10)
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return TemplateResponse(request, 'book_storage/genres.html', context=context)


def authors(request):
    author_set = set()
    for book in book_list:
        author_set.add(book['author'])
    context['authors'] = author_set
    return render(request, 'book_storage/authors.html', context=context)


def books(request):
    context['books'] = book_list
    return render(request, 'book_storage/books.html', context=context)


def book_info(request, book_name):
    current_book = Book.objects.get(slug=book_name)
    context['book'] = current_book
    return render(request, 'book_storage/book_info.html', context=context)


def genre_books(request, genre_name):
    page_number = request.GET.get('page')
    current_books = Book.objects.filter(genre__slug=genre_name)
    paginator = Paginator(current_books, 10)
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'book_storage/genre_books.html', context=context)


def author_books(request, author_name):
    current_books = []
    for book in book_list:
        if book['author'] == author_name:
            current_books.append(book['name'])
    context['books'] = current_books
    context['author'] = author_name
    return render(request, 'book_storage/author_book.html', context=context)


def signup(request):
    return render(request, 'book_storage/auth.html', context=context)


def signin(request):
    return render(request, 'book_storage/signin.html', context=context)


def add_book(request):
    return render(request, 'book_storage/add_book.html', context=context)

