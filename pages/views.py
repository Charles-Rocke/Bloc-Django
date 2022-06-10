from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    model = "User"
    template_name = "pages/home.html"
    fields = ['name', 'email']