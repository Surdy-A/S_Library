from django.urls import path

from .views import (
    BookListView, BookDetailView, 
    SearchResultsListView, 
    category, author,
     publisher, 
     ReviewViewForm
     ) 

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('<slug:category_slug>', category, name='book_category'),
    path('author/<slug:author_slug>', author, name='book_author'),
    path('publisher/<slug:publisher_slug>', publisher, name='book_publisher'),
    path('review', ReviewViewForm.as_view(), name='review'),
     
]
