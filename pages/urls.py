from django.urls import path
from .views import HomePageView

# url patterns
urlpatterns = [
    path("", HomePageView.as_view(), name = "home"),
]
