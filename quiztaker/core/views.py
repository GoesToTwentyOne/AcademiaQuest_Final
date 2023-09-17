from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import date

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'date': date.today().year}
        return context
class AboutView(TemplateView):
    template_name='about.html'
    
    

class ContactView(TemplateView):
    template_name='contact.html'