# Generated by Django 4.2.6 on 2023-10-07 18:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0009_alter_taskassigneemapping_assignee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
