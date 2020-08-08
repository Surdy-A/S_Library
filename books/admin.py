from django.contrib import admin
from .models import Book, Review, Category, Carousel, Author, Publisher

class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "price",)

admin.site.register(Book, BookAdmin)

admin.site.register(Category)
admin.site.register(Carousel)
admin.site.register(Author)
admin.site.register(Publisher)
