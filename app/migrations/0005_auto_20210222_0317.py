# Generated by Django 3.1.2 on 2021-02-21 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210222_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='uconfirmpassword',
        ),
        migrations.RemoveField(
            model_name='users',
            name='ugender',
        ),
    ]
