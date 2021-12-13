import datetime
import json
from datetime import datetime
from typing import Reversible
import unittest
from django.http import response
from django.test import Client
from django.test import TestCase
from django.urls import reverse
from hobbyapp.models import Hobby, User

class test1(unittest.TestCase):
    def setUp(self) -> None:
        testUser = User.objects.create(username="TEST_USERNAME")
        testUser.set_password("TEST_PASSWORD")
        # need to save after setting password
        testUser.save()
 
    def test_signup_form(self):
        client = Client()
        initialCount = users = User.objects.all().count()
        response = client.post(reverse('signup'), data={
            'username': 'foo',
            'password': 'foo',
        })
        self.assertEqual(response.status_code, 200)
        users = User.objects.all()
        self.assertEqual(users.count(), initialCount+1)


    def test_login(self):
        client = Client()
        response = client.post(reverse('login'),data={
            'username': 'TEST_USERNAME',
            'password':'TEST_PASSWORD',
        })

        self.assertEqual(response.status_code, 200)

    def test_Change_dob(self):
        client = Client()
        client.login(username='TEST_USERNAME',password='TEST_PASSWORD')
        response = client.put(reverse('user dob api'),data={
            'dob':datetime.today().strftime('%Y-%m-%d')
        },content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
 

    def test_change_hobbies(self):
        client = Client()
        data = []
        h = Hobby(name='testHobby')
        h.save()
        data.append(h.id)
        client.login(username='TEST_USERNAME',password='TEST_PASSWORD')
        response = client.put(reverse('user hobbies api'),data={
            'hobbies':data
        },content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
 

    def tearDown(self):
        for userObject in User.objects.all():
            if userObject.username=='foo':
                userObject.delete()
            if userObject.username=='TEST_USERNAME':
                userObject.delete()

       

# Create your tests here.
