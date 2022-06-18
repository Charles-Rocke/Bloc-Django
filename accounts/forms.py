from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

# forms here
# Custom user form
class CustomUserCreationForm(SignupForm):
    
    first_name = forms.CharField(max_length = 25, widget=forms.TextInput(attrs={'placeholder': 'First name','class':'form-control'}))
    last_name = forms.CharField(max_length = 25, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    company = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Company name'}))
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password1')
    
    def save(self, request):
        user = super(CustomUserCreationForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.company = self.cleaned_data['company']
        user.save()
        return user
    
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
