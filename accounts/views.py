from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.
class SignupPageView(CreateView):
    model = CustomUser
    fields = [
        'email',
        'first_name',
        'last_name',
        'company',
    ]
    success_url = reverse_lazy("home")
    template_name = "pages/registration/signup.html"
    
class SignupSuccessPageView(TemplateView):
    template_name = "pages/registration/signupsuccess.html"