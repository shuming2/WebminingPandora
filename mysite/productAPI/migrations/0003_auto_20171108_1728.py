# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productAPI', '0002_auto_20171108_0652'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubCategary',
            new_name='SubCategory',
        ),
        migrations.AlterField(
            model_name='product',
            name='theme',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
