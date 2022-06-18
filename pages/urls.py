from django.urls import path
from .views import HomePageView, SignupSuccessPageView

# url patterns
urlpatterns = [
    path("", HomePageView.as_view(), name = "home"),
    path("success/", SignupSuccessPageView.as_view(), name = "signupsuccess"),
]
