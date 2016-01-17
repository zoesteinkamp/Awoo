# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('smoking', models.CharField(max_length=30)),
                ('height', models.CharField(max_length=20)),
                ('body_type', models.CharField(max_length=40)),
                ('ethnicity', models.CharField(max_length=30)),
                ('sexual_orientation', models.CharField(max_length=20)),
                ('future_plans', models.TextField(max_length=200)),
                ('education', models.CharField(max_length=20)),
                ('income', models.CharField(max_length=30)),
                ('religion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hobby_name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HobbyPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hobby_id', models.ForeignKey(to='dating.Hobby')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bulk_message', models.TextField()),
                ('date', models.DateTimeField()),
                ('title_message', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('profile_image', models.FilePathField()),
                ('human_image', models.FilePathField()),
                ('best_image', models.FilePathField()),
                ('interest_image', models.FilePathField()),
                ('location', models.CharField(max_length=60)),
                ('industry', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('active', models.BooleanField()),
                ('reports', models.IntegerField()),
                ('last_login', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='messages',
            name='user_from',
            field=models.ForeignKey(related_name='user_from', to='dating.User'),
        ),
        migrations.AddField(
            model_name='messages',
            name='user_to',
            field=models.ForeignKey(related_name='user_to', to='dating.User'),
        ),
        migrations.AddField(
            model_name='hobbyperson',
            name='user_id',
            field=models.ForeignKey(to='dating.User'),
        ),
        migrations.AddField(
            model_name='dating',
            name='user_profile',
            field=models.OneToOneField(to='dating.User'),
        ),
    ]
