# Generated by Django 5.0.7 on 2024-08-12 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0021_rename_users_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment_name',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='implementer',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
