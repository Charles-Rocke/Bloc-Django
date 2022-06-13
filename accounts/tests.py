from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class CustomUsetTests(TestCase):
    
    # confirms a new user can be created
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = "testuser", email = "test@email.com", password = "testpass1"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = "superuser", email = "super@email.com", password = "superpass1"
        )
        self.assertEqual(user.username, "superuser")
        self.assertEqual(user.email, "super@email.com")
        self.assertTrue(user.is_active) 
        self.assertFalse(user.is_staff) # set to false for tests
        self.assertFalse(user.is_superuser) # set to false for tests