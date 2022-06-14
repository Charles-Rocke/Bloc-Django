from django.urls import path
from .views import SignupPageView, SignupSuccessPageView

# urls here
urlpatterns = [
    path("signup/", SignupPageView.as_view(), name = "signup"),
    path("signup/success/", SignupSuccessPageView.as_view(), name = "signupsuccess"),
]
