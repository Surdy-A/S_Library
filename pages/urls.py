from django.urls import path

from .views import HomePageView, AboutPageView , ContactUsView



urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), 
    path('', HomePageView.as_view(), name='home'),
    path(
        "contact-us/",
        ContactUsView.as_view(),
        name="contact_us",
    )
]