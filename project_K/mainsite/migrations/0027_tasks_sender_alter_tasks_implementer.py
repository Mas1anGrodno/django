# Generated by Django 5.0.7 on 2024-08-12 19:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0026_delete_users'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='sender',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_sender', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='implementer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_user', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
    ]