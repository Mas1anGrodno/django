# Generated by Django 5.0.7 on 2024-08-06 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_alter_tasks_priority_alter_tasks_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Имя Пользователя')),
                ('email', models.EmailField(max_length=255, verbose_name='Электронная почта')),
                ('password', models.CharField(max_length=255, verbose_name='Пароль')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователь',
                'ordering': ['-date_joined'],
            },
        ),
        migrations.AddField(
            model_name='tasks',
            name='task_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='implementer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='mainsite.auth_user', to_field='username', verbose_name='Пользователь'),
        ),
    ]