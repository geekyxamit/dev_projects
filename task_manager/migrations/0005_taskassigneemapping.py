# Generated by Django 4.2.6 on 2023-10-07 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0004_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskAssigneeMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to='task_manager.user')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_task', to='task_manager.tasks')),
            ],
        ),
    ]
