from django.urls import path
from .views import HomePageView, AboutPageView , ContactUsView
from books.views import BookListView

app_name = 'pages'
urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), 
    path('', BookListView.as_view(), name='home'),
    path("contact-us/", ContactUsView.as_view(),  name="contact_us"),
]