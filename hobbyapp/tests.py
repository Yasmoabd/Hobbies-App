import datetime
import json
from datetime import datetime
from typing import Reversible
from django.http import response
from django.test import TestCase
from django.urls import reverse
from hobbyapp.models import Hobby, User
class test1(TestCase):
    def setUp(self):
        testUser = User.objects.create(username='TEST_USERNAME')
        testUser.set_password('TEST_PASSWORD')
        # need to save after setting password
        testUser.save()

    def test_signup_form(self):
        response = self.client.post(reverse('signup'), data={
            'username': 'foo',
            'password': 'foo',
        })
        self.assertEqual(response.status_code, 200)
        users = User.objects.all()
        self.assertEqual(users.count(), 2)

    def test_login(self):
        response = self.client.post(reverse('login'),data={
            'username': 'TEST_USERNAME',
            'password':'TEST_PASSWORD',
        })
        self.assertEqual(response.status_code, 200)

    def test_Change_dob(self):
        self.client.login(username='TEST_USERNAME',password='TEST_PASSWORD')
        response = self.client.put(reverse('user dob api'),data={
            'dob':datetime.today().strftime('%Y-%m-%d')
        },content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_change_hobbies(self):
        data = []
        h = Hobby(name='testHobby')
        h.save()
        data.append(h.id)
        self.client.login(username='TEST_USERNAME',password='TEST_PASSWORD')
        response = self.client.put(reverse('user hobbies api'),data={
            'hobbies':data
        },content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
# Create your tests here.
