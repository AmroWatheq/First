from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('show_book/<int:id_book>', views.show, name="show"),
    path('show_book/add_author', views.add_author)
]
