# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bulk_message', models.TextField()),
                ('date', models.DateTimeField()),
                ('title_message', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='messages',
            name='user_from',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='user_to',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 12, 6, 39, 45, 676756, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 12, 6, 40, 0, 866183, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.AddField(
            model_name='message',
            name='user_from',
            field=models.ForeignKey(related_name='user_from', to='dating.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='user_to',
            field=models.ForeignKey(related_name='user_to', to='dating.User'),
        ),
    ]
