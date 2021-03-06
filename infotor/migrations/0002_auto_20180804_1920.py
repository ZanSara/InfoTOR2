# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-04 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infotor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Percorso_Tratta',
            new_name='PercorsoTratta',
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='descrizione',
            field=models.TextField(db_column='DESCRIZION', max_length=250, null=True, verbose_name='Descrizione'),
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='immagine',
            field=models.ImageField(db_column='IMMAGINE', upload_to='checkpoints/', verbose_name='Immagine'),
        ),
    ]
