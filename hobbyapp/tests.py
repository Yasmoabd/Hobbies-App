
from django.test import TestCase

from hobbyapp.models import User
class test1(TestCase):
    def setUp(self):
        paulo = User.objects.create(username='TEST_USERNAME')
        paulo.set_password('TEST_PASSWORD')
        # need to save after setting password
        paulo.save()

    def test_users_count(self):
        """Check that we have 1 user in test DB"""
        n_users = User.objects.all().count()
        self.assertEqual(n_users, 1)
        
# Create your tests here.
