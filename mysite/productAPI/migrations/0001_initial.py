# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('key', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('key', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('key', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('key', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Metal',
            fields=[
                ('key', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('baseid', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('collection', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('subcollection', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
                ('metal', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('theme', models.CharField(max_length=100)),
                ('stone', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('newest', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('myImg', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Stone',
            fields=[
                ('key', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategary',
            fields=[
                ('key', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('key', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
    ]
