# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='myImg',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='newest',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
