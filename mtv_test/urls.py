from django.urls import path
from .views import authors, authors_add, authors_of_books

urlpatterns = [
    path('authors/', authors),
    path('authors/add/', authors_add),
    path('authors_of_books/', authors_of_books)
]
