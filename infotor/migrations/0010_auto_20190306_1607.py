# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-06 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infotor', '0009_auto_20190306_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forra',
            name='id',
            field=models.IntegerField(db_column='NUME', primary_key=True, serialize=False, verbose_name='Id Forra'),
        ),
    ]