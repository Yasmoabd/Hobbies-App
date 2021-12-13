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

        paulo = User.objects.create(username="TEST_USERNAME")

        paulo.set_password("TEST_PASSWORD")

        # need to save after setting password

        paulo.save()

 

        response = client.post(reverse('login'),data={

            'username': 'TEST_USERNAME',

            'password':'TEST_PASSWORD',

        })

        self.assertEqual(response.status_code, 200)

 

    def test_Change_dob(self):

        client = Client()

        client.login(username='foo',password='foo')

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

        client.login(username='foo',password='foo')

        response = client.put(reverse('user hobbies api'),data={

            'hobbies':data

        },content_type='application/json'

        )

        self.assertEqual(response.status_code, 200)

 

    def test_clean(self):

        print(User.objects.count())

        for userObject in User.objects.all():

            if userObject.username=='foo':

                userObject.delete()

            if userObject.username=='TEST_USERNAME':

                userObject.delete()

        print(User.objects.count())

 

       

# Create your tests here.
