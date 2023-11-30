from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=250)
    biography = models.TextField(null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = ('AW', 'available')
        NOT_AVAILABLE = ('NA', 'not available')

    title = models.CharField(max_length=100)
    cover = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author')
    genre = models.ManyToManyField(Genre)
    description = models.TextField(null=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.AVAILABLE)
    comment = models.ManyToManyField(User, through='Comment')

    class Meta:
        ordering = ['title', 'author']
        indexes = [
            models.Index(fields=['title'])
        ]

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    book_1d = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment_book')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.create
