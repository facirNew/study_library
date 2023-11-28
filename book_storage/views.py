from django.shortcuts import render
from django.template.response import TemplateResponse

book_list = [
    {'name': 'some_book_0', 'genre': 'some_genre_1', 'author': 'some_author_1'},
    {'name': 'some_book_1', 'genre': 'some_genre_2', 'author': 'some_author_2'},
    {'name': 'some_book_2', 'genre': 'some_genre_3', 'author': 'some_author_3'},
    {'name': 'some_book_3', 'genre': 'some_genre_2', 'author': 'some_author_4'},
    {'name': 'some_book_4', 'genre': 'some_genre_1', 'author': 'some_author_5'},
    {'name': 'some_book_5', 'genre': 'some_genre_2', 'author': 'some_author_1'},
    {'name': 'some_book_6', 'genre': 'some_genre_3', 'author': 'some_author_2'},
    {'name': 'some_book_7', 'genre': 'some_genre_2', 'author': 'some_author_3'},
    {'name': 'some_book_8', 'genre': 'some_genre_1', 'author': 'some_author_4'},
    {'name': 'some_book_9', 'genre': 'some_genre_2', 'author': 'some_author_5'},
]
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
    book_name = request.GET.get('name', '')
    book_genre = request.GET.get('genre', '')
    book_author = request.GET.get('author', '')
    if book_author and book_name and book_genre:
        book = {'name': book_name, 'genre': book_genre, 'author': book_author}
        if not any(book['name'] == b['name'] for b in book_list):
            book_list.append(book)
    return TemplateResponse(request, 'book_storage/index.html', context=context)


def genres(request):
    genre_set = set()
    for book in book_list:
        genre_set.add(book['genre'])
    context['genres'] = genre_set
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
    current_book = {}
    for book in book_list:
        if book['name'] == book_name:
            current_book = book

    context['name'] = current_book['name']
    context['author'] = current_book['author']
    context['genre'] = current_book['genre']
    return render(request, 'book_storage/book_info.html', context=context)


def genre_books(request, genre_name):
    current_books = []
    for book in book_list:
        if book['genre'] == genre_name:
            current_books.append(book['name'])
    context['books'] = current_books
    context['genre'] = genre_name
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

