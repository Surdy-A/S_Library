from django.views.generic import TemplateView
from pages import forms
from django.views.generic.edit import FormView
from django.core.mail import send_mail



class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView): 
    template_name = 'about.html'



class ContactUsView(FormView):
    template_name = "contact_form.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)