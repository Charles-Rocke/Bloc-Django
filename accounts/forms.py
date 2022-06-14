from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

# forms here

# Custom user form
class CustomUserCreationForm(forms.Form):
    class Media:
        css = {
            'all': ('css/main.css',),
        }
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'Enter email'}))
    first_name = forms.CharField(max_length = 25)
    last_name = forms.CharField(max_length = 25)
    company = forms.CharField(max_length = 100)
    
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "first_name",
            "last_name",
            "company",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "email",
            "company",
        )
