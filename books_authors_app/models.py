from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def add_book_model(title_a, desc_b):
    return Book.objects.create(title = title_a, desc = desc_b)


def get_all_books():
    return Book.objects.all()

def get_all_authors():
    return Author.objects.all()

def get_id(id_book):
    return Book.objects.get(id = id_book)

def get_all_authors_book(id_book):
    this_book = Book.objects.get(id = id_book)
    return this_book.authors.all()

def add_authors_book(id_book, name_author):
    this_book = get_id(id_book)
    this_author = Author.objects.get(first_name = name_author)
    return this_book.authors.add(this_author)