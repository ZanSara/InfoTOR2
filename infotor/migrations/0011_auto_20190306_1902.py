# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-06 19:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import infotor.validators


class Migration(migrations.Migration):

    dependencies = [
        ('infotor', '0010_auto_20190306_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forra',
            name='acquaticita',
            field=models.DecimalField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], db_column='LIVH2O', decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)], verbose_name='Livello Acquaticità'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='ampiezza_bacino',
            field=models.DecimalField(blank=True, db_column='AMPBAC', decimal_places=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Ampiezza Bacino (km2)'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='bellezza',
            field=models.DecimalField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4)], db_column='LIVBEL', decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='Punteggio Bellezza'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='calata_massima',
            field=models.DecimalField(blank=True, db_column='CALMAX', decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Calata Massima'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='dislivello',
            field=models.DecimalField(blank=True, db_column='DISLIV', decimal_places=0, max_digits=2, verbose_name='Dislivello (m)'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='divertimento',
            field=models.DecimalField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4)], db_column='LIVDIV', decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='Punteggio Divertimento'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='grado_impegno',
            field=models.ForeignKey(blank=True, db_column='IMPTOR', on_delete=django.db.models.deletion.CASCADE, to='infotor.GradoImpegno', verbose_name='Grado Impegno'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='km_navetta',
            field=models.DecimalField(blank=True, db_column='KMNAV', decimal_places=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Kilometri Navetta'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='lunghezza_min_corda',
            field=models.DecimalField(blank=True, db_column='CORMIN', decimal_places=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Lunghezza minima corda singola'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='minuti_navetta',
            field=models.DecimalField(blank=True, db_column='MMNAV', decimal_places=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Minuti Navetta'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='numero_calate',
            field=models.DecimalField(blank=True, db_column='NUMC', decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Numero Calate'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='numero_min_corde',
            field=models.DecimalField(blank=True, db_column='MINCORDE', decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Numero minimo di corde'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='ore_avvicinamento',
            field=models.DecimalField(blank=True, db_column='HAVV', decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), infotor.validators.frac_min_validator], verbose_name='Ore Avvicinamento'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='ore_discesa',
            field=models.DecimalField(blank=True, db_column='HCAL', decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), infotor.validators.frac_min_validator], verbose_name='Ore Discesa'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='ore_rientro',
            field=models.DecimalField(blank=True, db_column='HRIE', decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), infotor.validators.frac_min_validator], verbose_name='Ore Rientro'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='verticalita',
            field=models.DecimalField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], db_column='LIVVER', decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)], verbose_name='Livello Verticalità'),
        ),
    ]
