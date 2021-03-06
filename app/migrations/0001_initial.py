# Generated by Django 3.1.2 on 2021-05-25 20:11

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'admin_user',
            },
            managers=[
                ('adminobject', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ContactusDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('csubject', models.CharField(max_length=100)),
                ('cphonenumber', models.CharField(max_length=15)),
                ('cemail', models.EmailField(max_length=50)),
                ('cmsg', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'ContactUStable',
            },
            managers=[
                ('contactdbobject', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='user_response',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_Email', models.EmailField(max_length=30)),
                ('image_path', models.CharField(max_length=50)),
                ('prediction_made', models.CharField(max_length=100)),
                ('user_response', models.CharField(max_length=10)),
                ('date', models.DateField(max_length=20)),
            ],
            options={
                'db_table': 'user_result_response',
            },
            managers=[
                ('userresponse_model_obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('upassword', models.CharField(max_length=50)),
                ('umail', models.EmailField(max_length=50)),
                ('uphone', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('person', django.db.models.manager.Manager()),
            ],
        ),
    ]
