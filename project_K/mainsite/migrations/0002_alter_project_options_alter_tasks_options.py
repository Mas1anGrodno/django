# Generated by Django 5.0.7 on 2024-07-26 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['proj_create'], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проект'},
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['priority'], 'verbose_name': 'Задачи', 'verbose_name_plural': 'Задачи'},
        ),
    ]