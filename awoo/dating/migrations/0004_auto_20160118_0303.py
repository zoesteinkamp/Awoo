# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0003_auto_20160118_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='active',
            field=models.NullBooleanField(),
        ),
    ]
