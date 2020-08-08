from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Book, Category, Carousel, Author, Publisher
from .forms import ReviewForm 
from django import forms
from books import forms


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'
    paginate_by = 2
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['authors'] = Author.objects.all()
        context['publisher'] = Publisher.objects.all()
        return context




def category(request, category_slug='None'):
    category = 'None'
    books = Book.objects.all()
    categories = Category.objects.all()
    
    #Pagination
    paginator = Paginator(books, 1)
    page = request.GET.get('page')
    books_page = paginator.get_page(page)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)

    return render(request, "books/book_category.html", {
        'category': category,
        'categories': categories,
        'books': books,
        'books_page':books_page})


def author(request, author_slug='None'):
    author = 'None'
    books = Book.objects.all()
    
    #Pagination
    paginator = Paginator(books, 1)
    page = request.GET.get('page')
    books_page = paginator.get_page(page)
    
    if author_slug:
        author = get_object_or_404(Author, slug=author_slug)
        books = books.filter(author=author)

    return render(request, "books/book_author.html", {
        'author': author,
        'authors': authors,
        'books': books,
        'books_page':books_page})


def publisher(request, publisher_slug='None'):
    publisher = 'None'
    books = Book.objects.all()
    publishers = Publisher.objects.all()
    
    #Pagination
    paginator = Paginator(books, 1)
    page = request.GET.get('page')
    books_page = paginator.get_page(page)
    
    if publisher_slug:
        publisher = get_object_or_404(Publisher, slug=publisher_slug)
        books = books.filter(publisher=publisher)

    return render(request, "books/book_publisher.html", {
        'publisher': publisher,
        'publishers': publishers,
        'books': books,
        'books_page':books_page})
        


class BookDetailView(
    LoginRequiredMixin,
    DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'




class SearchResultsListView(ListView): 
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))


class ReviewViewForm(FormView):
    template_name = "books/book_detail.html"
    form_class = ReviewForm
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form)

def CommentView(request, book):
    book = get_object_or_404(Book, slug=book)
    review=book.review.all()
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = ReviewForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = ReviewForm()

    return render(request, 'books/book_detail.html', {'comments_form': comments_form, 'review':review})

