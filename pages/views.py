
from django.views.generic import TemplateView
from django.http import HttpResponse
from webauth.mixins import WebAuthRequiredMixin

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
    
    
    
# signup success page
class SignupSuccessPageView(TemplateView):
    template_name = "signupsuccess.html"
    

# customer portal page
class PortalPageView(WebAuthRequiredMixin, TemplateView):
    template_name = "portal_home.html"

# pricing page view
class PricingPageView(TemplateView):
    template_name = "pricing.html"