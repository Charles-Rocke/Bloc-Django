from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


# forms here
# pricing plan choices


# Custom user form
class CustomUserCreationForm(SignupForm):
    
    first_name = forms.CharField(max_length = 25, widget=forms.TextInput(attrs={'placeholder': 'First name','class':'form-control'}))
    last_name = forms.CharField(max_length = 25, widget=forms.TextInput(attrs={'placeholder': 'Last name','class':'form-control'}))
    company = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Company name','class':'form-control'}))
    # creating a select field 
    pricing_plan=forms.ChoiceField(
                    widget=forms.Select,
                    label="Pricing plan",
                    choices= (('',''),('startup','startup '),('enterprise','enterprise'),),
                    )
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password1')
    
    def save(self, request):
        user = super(CustomUserCreationForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.company = self.cleaned_data['company']
        user.pricing_plan = self.cleaned_data['pricing_plan']
        user.save()
        return user
    
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "first_name",
            "last_name",
            "company",
            "pricing_plan",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "email",
            "company",
            "pricing_plan",
        )
