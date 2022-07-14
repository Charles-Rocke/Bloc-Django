from django.urls import path
from pages import views

# url patterns
urlpatterns = [
    path("", views.HomePageView.as_view(), name = "home"),
    path("pricing", views.PricingPageView.as_view(), name = "pricing"),
    path("success/", views.SignupSuccessPageView.as_view(), name = "signupsuccess"),
    path("portal/home", views.PortalPageView.as_view(), name = "portal_home"),
]
