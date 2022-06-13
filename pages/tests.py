from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

# Create your tests here.
class HomePageTests(SimpleTestCase):
    # Dont repeat yourself setup
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)
        
    # test that url exists at correct location
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)
        
    # test if correct template is used
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "pages/base.html")
        self.assertTemplateUsed(self.response, "pages/home.html")
        
    # test template has correct html code
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Passwordless.")
        self.assertContains(self.response, "Period.")
        
    # test home page does not have incorrect code
    def test_homepage_contains_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page")
        
    # test that HomePageView 'resolves' a given URL path
    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)