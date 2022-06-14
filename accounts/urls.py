from django.urls import path
from pages import views

# urls here
urlpatterns = [
    path("", views.HomePageView.as_view(), name = "home")
]
