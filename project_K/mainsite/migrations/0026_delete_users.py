# Generated by Django 5.0.7 on 2024-08-12 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0025_alter_comments_comment_name_alter_tasks_implementer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]