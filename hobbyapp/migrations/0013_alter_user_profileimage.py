# Generated by Django 3.2.8 on 2021-12-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobbyapp', '0012_user_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profileImage',
            field=models.ImageField(upload_to='images'),
        ),
    ]