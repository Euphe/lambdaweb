# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 17:59
from __future__ import unicode_literals

import ckeditor_uploader.fields
import colorfield.fields
import django.db.models.deletion
import filebrowser.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('git_username', models.CharField(max_length=300, verbose_name='Git username')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='Группа')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('first_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Фамилия')),
                ('profile_image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True,
                                                                     verbose_name='Изображения профиля')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Участника',
                'verbose_name_plural': 'Участники'
            },
        ),

        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    choices=[('mdi-github-circle', 'GitHub'), ('mdi-twitter', 'Twitter'), ('mdi-gmail', 'Mail'),
                             ('mdi-vk', 'Vk'), ('mdi-facebook', 'Facebook')], max_length=300,
                    verbose_name='Название социальной сети')),
                ('link', models.CharField(max_length=300, verbose_name='Ссылка на профиль')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'социальных сетей',
                'verbose_name_plural': 'социальных сетей'
            }
        ),

        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Участники проекта')),
                ('git', models.URLField(blank=True, null=True, verbose_name='Cсылка на Git')),
                ('image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True,
                                                             verbose_name='Главное изображение')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты'
            }
        ),

        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название партнера')),
                ('type_partner', models.CharField(
                    choices=[('info', 'Информационный'), ('finance', 'Финансовый'), ('general', 'Генеральный')],
                    max_length=300, verbose_name='Тип партнера')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Адрес')),
                ('site', models.CharField(max_length=500, verbose_name='Сайт')),
                ('phone', models.CharField(blank=True, max_length=500, null=True, verbose_name='Телефон')),
                ('image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True,
                                                             verbose_name='Изображение')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),

        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_description', models.TextField(verbose_name='SEO Описание')),
                ('key_words', models.TextField(verbose_name='Ключ слова')),
            ],
            options={
                'verbose_name': 'SEO',
                'verbose_name_plural': 'SEO',
            },
        ),

        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=10)),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
    ]
