# Generated by Django 4.2.6 on 2023-10-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0006_remove_tasks_assignee'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
