from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime 

from django.db.models.deletion import CASCADE
from django.utils import timezone
import datetime
# Create your models here

class Hobby(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }



class User(AbstractUser):
    profileImage = models.ImageField(upload_to='images/', default="media/defaultpic.png")
    email = models.EmailField()
    city = models.CharField(max_length=200)
    dateOfBirth = models.DateField(default=timezone.now)
    hobbies = models.ManyToManyField(Hobby)
    friends = models.ManyToManyField("User", blank=True)

    def to_dict(self):
        return {
            'id': self.id
        }

    


class Friend_Request(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)

    def to_dict(self):
        return {
            'id': self.id
        }
