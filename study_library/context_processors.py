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


def get_context(request):
    return context
