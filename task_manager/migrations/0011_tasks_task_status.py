# Generated by Django 4.2.6 on 2023-10-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0010_tasks_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='task_status',
            field=models.CharField(default='open', max_length=100, null=True),
        ),
    ]
