# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0002_tu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tu',
            name='image',
            field=models.ImageField(upload_to=b'uploads', verbose_name='\u56fe\u7247'),
        ),
    ]
