from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView
from django import forms

# Create your tests here.
class CustomUsetTests(TestCase):
    
    # confirms a new user can be created
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email = "test@email.com", password = "notrequired"
        )
        self.assertEqual(user.email, "test@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_user(
            email = "super@email.com", password = "notrequired"
        )
        self.assertEqual(user.email, "super@email.com")
        self.assertTrue(user.is_active) 
        self.assertFalse(user.is_staff) # set to false for tests
        self.assertFalse(user.is_superuser) # set to false for tests
        

# Sign up tests
class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)
        
    # test sign up template
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "pages/registration/signup.html")
        self.assertContains(self.response, "Sign up")
        self.assertNotContains(self.response, "Login")
        
    # test sign up form
    def test_signup_form(self):
        self.assertContains(self.response, "csrfmiddlewaretoken")
    
    # test sign up view
    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)