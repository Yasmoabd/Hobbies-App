# Generated by Django 3.2.8 on 2021-12-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobbyapp', '0014_alter_user_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profileImage',
            field=models.ImageField(default='media/defaultpic.png', upload_to='images/'),
        ),
    ]
