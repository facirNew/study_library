from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# TODO slug unique=True
class StatusManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='AW')


class Author(models.Model):
    name = models.CharField(max_length=250, verbose_name='Автор')
    biography = models.TextField(null=True, verbose_name='Биография')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Жанры')
    slug = models.SlugField(verbose_name='URL', db_index=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = ('AW', 'available')
        NOT_AVAILABLE = ('NA', 'not available')

    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='URL')
    cover = models.CharField(max_length=250, verbose_name='Обложка', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author', verbose_name='Автор')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры')
    description = models.TextField(null=True, verbose_name='Краткое описание')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.AVAILABLE, verbose_name='Статус')
    comment = models.ManyToManyField(User, through='Comment', verbose_name='Комментарии')

    available = StatusManager()
    objects = models.Manager()

    class Meta:
        ordering = ['title', 'author']
        indexes = [
            models.Index(fields=['slug'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_info', kwargs={'book_name': self.slug})


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    book_1d = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment_book')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    text = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.create
