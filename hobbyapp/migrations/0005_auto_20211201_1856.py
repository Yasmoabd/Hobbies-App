# Generated by Django 3.2.8 on 2021-12-01 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hobbyapp', '0004_remove_user_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dateOfBirth',
        ),
    ]