# Generated by Django 3.1.2 on 2021-01-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ufirstname', models.CharField(max_length=50)),
                ('ulastname', models.CharField(max_length=50)),
                ('upassword', models.CharField(max_length=10)),
                ('uconfirmpassword', models.CharField(max_length=10)),
                ('ugender', models.CharField(max_length=10)),
                ('umail', models.EmailField(max_length=15)),
                ('uphone', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
