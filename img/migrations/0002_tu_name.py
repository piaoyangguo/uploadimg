# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tu',
            name='name',
            field=models.CharField(default=1, max_length=200, verbose_name='\u540d\u5b57'),
            preserve_default=False,
        ),
    ]
