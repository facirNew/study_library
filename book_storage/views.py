from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse

from .models import *

context = {}


def index(request):
    book_list = Book.available.all().order_by('?')[:10]
    context['books'] = book_list
    return TemplateResponse(request, 'book_storage/index.html', context=context)


def genres(request):
    page_number = request.GET.get('page')
    genres_list = Genre.objects.all().order_by('name')
    paginator = Paginator(genres_list, 20)
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return TemplateResponse(request, 'book_storage/genres.html', context=context)


def authors(request):
    page_number = request.GET.get('page')
    authors_list = Author.objects.all().order_by('name')
    paginator = Paginator(authors_list, 20)
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'book_storage/authors.html', context=context)


def books(request):
    page_number = request.GET.get('page')
    book_list = Book.available.all()
    paginator = Paginator(book_list, 20)
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'book_storage/books.html', context=context)


def book_info(request, book_name):
    current_book = get_object_or_404(Book, slug=book_name)
    context['book'] = current_book
    return render(request, 'book_storage/book_info.html', context=context)


def genre_books(request, genre_name):
    page_number = request.GET.get('page')
    current_books = Book.available.filter(genre__slug=genre_name)
    paginator = Paginator(current_books, 10)
    page_obj = paginator.get_page(page_number)
    genre = Genre.objects.get(slug=genre_name)
    context['page_obj'] = page_obj
    context['genre'] = genre.name
    return render(request, 'book_storage/genre_books.html', context=context)


def author_books(request, author_name):
    page_number = request.GET.get('page')
    current_book = Book.available.filter(author__slug=author_name)
    paginator = Paginator(current_book, 10)
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    author = Author.objects.get(slug=author_name)
    context['author'] = author.name
    return render(request, 'book_storage/author_book.html', context=context)


def add_book(request):
    return render(request, 'book_storage/add_book.html', context=context)


def search(request):
    find = request.GET.get('search')
    context['find_book'] = Book.available.filter(Q(title__contains=find.lower())
                                                 | Q(title__contains=find.title())
                                                 | Q(title__contains=find.upper()))
    context['find_author'] = Author.objects.filter(Q(name__contains=find.lower())
                                                   | Q(name__contains=find.title())
                                                   | Q(name__contains=find.upper()))
    context['find_genres'] = Genre.objects.filter(Q(name__contains=find.lower())
                                                  | Q(name__contains=find.title())
                                                  | Q(name__contains=find.upper()))
    return render(request, 'book_storage/search.html', context=context)
