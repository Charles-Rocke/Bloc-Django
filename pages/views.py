from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.models import CustomUser
# from webauthn import registration
from accounts.forms import CustomUserCreationForm

# Create your views here.
class HomePageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "pages/home.html"