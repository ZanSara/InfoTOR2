# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-05 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infotor', '0004_auto_20180805_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradoimpegno',
            name='codice',
            field=models.CharField(db_column='CODICE', max_length=3, primary_key=True, serialize=False, verbose_name='Codice'),
        ),
    ]
