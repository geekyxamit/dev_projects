# Generated by Django 4.2.6 on 2023-10-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='abcd@gmail.com', max_length=200, unique=True),
        ),
    ]
