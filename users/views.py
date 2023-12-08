from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginUserForm

login_menu = [{'title': 'Вход', 'url_name': 'users:signin'},
              {'title': 'Регистрация', 'url_name': 'users:signup'},
              ]
menu = [
    {'url': 'home', 'name': 'На главную'},
    {'url': 'authors', 'name': 'Авторы'},
    {'url': 'genres', 'name': 'Жанры'},
    {'url': 'books', 'name': 'Книги'},
]
context = {'menu': menu, 'login_menu': login_menu}


def signin(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
    context['form'] = form
    return render(request, 'users/signin.html', context=context)


def signup(request):
    return HttpResponse('signup')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:signin'))
