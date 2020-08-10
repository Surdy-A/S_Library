import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.text import slugify



class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    ebook = models.FileField(upload_to='books', default='')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='shows', default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    images = models.ImageField(upload_to='images/', blank=False)
    isbn = models.CharField(max_length=200, default='')
    year = models.PositiveIntegerField(default='')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='shows', default='')
    description = models.CharField(max_length=1000, default='')
    image_thumbnail = ImageSpecField(source='images',
                                     processors=[ResizeToFill(700, 400)],
                                     format='JPEG',
                                     options={'quality': 95})
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='shows', default='')
    

    class Meta: 
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', kwargs={'pk': str(self.pk)})

class Category(models.Model):
    category = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('books:book_category', args=[self.slug])


#Author 
class Author(models.Model):
    author = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.author

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('books:book_author', args=[self.slug])

#Publisher
class Publisher(models.Model):
    publisher = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.publisher

    def save(self, *args, **kwargs):
        self.slug = slugify(self.publisher)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('books:book_publisher', args=[self.slug])




class Carousel(models.Model):
    carousel = models.CharField(max_length=200, default='')
    images = models.ImageField(upload_to='images/', blank=False)
    image_thumbnail = ImageSpecField(source='images',
                                     processors=[ResizeToFill(900, 350)],
                                     format='JPEG',
                                     options={'quality': 95})

    def __str__(self):
        return self.carousel


class Review(models.Model): 
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review