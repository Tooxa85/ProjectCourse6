# Generated by Django 5.2.3 on 2025-06-19 09:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='юзер'),
        ),
        migrations.AddField(
            model_name='letter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='юзер'),
        ),
        migrations.AddField(
            model_name='mail',
            name='clients',
            field=models.ManyToManyField(blank=True, related_name='clients', to='main.client', verbose_name='клиенты'),
        ),
        migrations.AddField(
            model_name='mail',
            name='message',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.letter'),
        ),
        migrations.AddField(
            model_name='mail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AddField(
            model_name='mailinglog',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client', verbose_name='клиенты'),
        ),
        migrations.AddField(
            model_name='mailinglog',
            name='mail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.mail', verbose_name='рассылка'),
        ),
    ]
