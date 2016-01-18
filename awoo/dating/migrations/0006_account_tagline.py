# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0005_auto_20160118_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='tagline',
            field=models.CharField(max_length=140, blank=True),
        ),
    ]
