# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0002_auto_20160112_0640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('profile_image', models.FilePathField()),
                ('human_image', models.FilePathField()),
                ('best_image', models.FilePathField()),
                ('interest_image', models.FilePathField()),
                ('location', models.CharField(max_length=60)),
                ('industry', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('active', models.BooleanField()),
                ('reports', models.IntegerField()),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='dating',
            name='user_profile',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hobbyperson',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_from',
            field=models.ForeignKey(related_name='user_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_to',
            field=models.ForeignKey(related_name='user_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
