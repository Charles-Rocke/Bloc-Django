from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    """User model."""
    email = models.EmailField(('Email'), unique=True)
    first_name = models.CharField(('First Name'), max_length=50, blank=True)
    last_name = models.CharField(('Last Name'), max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []