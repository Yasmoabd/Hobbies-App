
from .models import User,Hobby

def testusers():
    u = User(username="test1")
    u.set_password('test1')
    u.save()
    u.city="london"
    u.email="test1@gmail.com"
    u.hobbies.add(Hobby(name="football"))
    u.save()

    u = User(username="test2")
    u.set_password('test2')
    u.save()
    u.city="london"
    u.email="test2@gmail.com"
    u.hobbies.add(Hobby(name="hockey"))
    u.save()

    u = User(username="test3")
    u.set_password('test3')
    u.save()
    u.city="london"
    u.email="test3@gmail.com"
    u.hobbies.add(Hobby(name="art"))
    u.save()

    u = User(username="test4")
    u.set_password('test4')
    u.save()
    u.city="london"
    u.email="test4@gmail.com"
    u.hobbies.add(Hobby(name="eating"))
    u.save()

    u = User(username="test5")
    u.set_password('test5')
    u.save()
    u.city="london"
    u.email="test5@gmail.com"
    u.hobbies.add(Hobby(name="climbing"))
    u.save()