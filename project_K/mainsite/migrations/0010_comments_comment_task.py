# Generated by Django 5.0.7 on 2024-08-06 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_alter_tasks_options_alter_project_proj_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='task_coment', to='mainsite.tasks', verbose_name='Коментарий задачи'),
            preserve_default=False,
        ),
    ]
