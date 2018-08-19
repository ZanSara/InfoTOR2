# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-09 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infotor', '0007_auto_20180805_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forra',
            name='checkpoint1',
            field=models.ForeignKey(blank=True, db_column='CHECKP1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkpoint1', to='infotor.Checkpoint', verbose_name='Checkpoint 1'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='checkpoint2',
            field=models.ForeignKey(blank=True, db_column='CHECKP2', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkpoint2', to='infotor.Checkpoint', verbose_name='Checkpoint 2'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='descr_accesso_monte',
            field=models.TextField(blank=True, db_column='DESACCM', max_length=250, verbose_name='Descrizione accesso a monte'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='descr_accesso_valle',
            field=models.TextField(blank=True, db_column='DESACCV', max_length=250, verbose_name='Descrizione accesso a valle'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='descr_avvicinamento',
            field=models.TextField(blank=True, db_column='DESAVV', max_length=250, verbose_name='Descrizione avvicinamento'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='descr_percorso',
            field=models.TextField(blank=True, db_column='DESPERC', max_length=250, verbose_name='Descrizione percorso'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='descr_uscita',
            field=models.TextField(blank=True, db_column='DESUSC', max_length=250, verbose_name='Descrizione uscita'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='dislivello',
            field=models.DecimalField(db_column='DISLIV', decimal_places=0, max_digits=2, verbose_name='Dislivello (m)'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='litologia',
            field=models.ForeignKey(blank=True, db_column='LITOL', null=True, on_delete=django.db.models.deletion.CASCADE, to='infotor.Litologia', verbose_name='Litologia'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='note',
            field=models.TextField(blank=True, db_column='NOTE', max_length=250, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='opere_idrauliche',
            field=models.ForeignKey(blank=True, db_column='OPEIDR', null=True, on_delete=django.db.models.deletion.CASCADE, to='infotor.OperaIdraulica', verbose_name='Opere Idrauliche'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='origine_acqua',
            field=models.ForeignKey(blank=True, db_column='ORIGACQUA', null=True, on_delete=django.db.models.deletion.CASCADE, to='infotor.OrigineAcqua', verbose_name='Origine Acqua'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='presentazione_forra',
            field=models.TextField(blank=True, db_column='PRES', max_length=250, verbose_name='Presentazione forra'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='profilo',
            field=models.ImageField(blank=True, db_column='PROFILO', null=True, upload_to='profili/', verbose_name='Profilo Forra'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='stagionalita',
            field=models.ManyToManyField(blank=True, db_column='STAGIONE', null=True, to='infotor.Mese', verbose_name='Mesi ok'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='vincoli_ambientali',
            field=models.TextField(blank=True, db_column='VINCOLI', max_length=250, verbose_name='Vincoli ambientali'),
        ),
    ]
