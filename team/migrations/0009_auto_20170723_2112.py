# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-23 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_auto_20170723_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='contact_link',
            field=models.CharField(blank=True, default='', help_text='Выводится на странице "участники"', max_length=300, verbose_name='Ссылка для связи'),
        ),
        migrations.AlterField(
            model_name='member',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Используется в описании на странице "участники"', max_length=300, verbose_name='Описание'),
        ),
    ]