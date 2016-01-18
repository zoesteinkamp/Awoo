# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0004_auto_20160118_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='active',
            field=models.BooleanField(default=b'false'),
        ),
        migrations.AlterField(
            model_name='account',
            name='reports',
            field=models.IntegerField(default=b'0'),
        ),
    ]
