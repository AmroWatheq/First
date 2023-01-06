from django.shortcuts import render, redirect
from . import models

def index(request):
    context = {
        "all_books" : models.get_all_books,
        "all_authors" : models.get_all_authors
    }
    return render(request, "index.html", context)

def add_book(request):
    models.add_book_model(request.POST["title"], request.POST["desc"])
    return redirect("/")

def show(request, id_book):
    this_book = models.get_id(id_book)
    context = {
        "title_book" : this_book.title,
        "id_book" : this_book.id,
        "all_authors_book" : models.get_all_authors_book(id_book),
        "all_authors" : models.get_all_authors
    }
    return render(request, "books.html", context)

def add_author(request):
    models.add_authors_book(request.POST['id_book'], request.POST['author'])
    return redirect(f"/show_book/{request.POST['id_book']}")