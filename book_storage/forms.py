from django import forms
from book_storage import models


class AddBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'cover', 'author', 'genre', 'description', 'status']
