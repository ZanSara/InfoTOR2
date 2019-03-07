# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-07 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infotor', '0013_forra_id_percorso'),
    ]

    operations = [
        migrations.AddField(
            model_name='forra',
            name='aggiornatore',
            field=models.CharField(blank=True, db_column='UTENTE', max_length=16, null=True, verbose_name='Aggiornatore'),
        ),
        migrations.AddField(
            model_name='forra',
            name='codice_catasto',
            field=models.CharField(blank=True, db_column='CODREG', max_length=12, null=True, verbose_name='Codice Catasto Regionale'),
        ),
        migrations.AddField(
            model_name='forra',
            name='data_aggiornamento',
            field=models.DateField(blank=True, db_column='DATARIL', null=True, verbose_name='Data Aggiornamento'),
        ),
        migrations.AddField(
            model_name='forra',
            name='descrizione',
            field=models.CharField(blank=True, db_column='DENOMI', max_length=80, null=True, verbose_name='Descrizione'),
        ),
        migrations.AddField(
            model_name='forra',
            name='difficolta',
            field=models.ForeignKey(blank=True, db_column='PERDIF', null=True, on_delete=django.db.models.deletion.CASCADE, to='infotor.Difficolta', verbose_name='Difficoltà'),
        ),
        migrations.AddField(
            model_name='forra',
            name='link_CMS',
            field=models.CharField(blank=True, db_column='LINK', max_length=16, null=True, verbose_name='Link CMS'),
        ),
        migrations.AddField(
            model_name='forra',
            name='lunghezza_inclinata',
            field=models.DecimalField(blank=True, db_column='PERLUNF', decimal_places=0, max_digits=5, null=True, verbose_name='Lunghezza Inclinata'),
        ),
        migrations.AddField(
            model_name='forra',
            name='lunghezza_piana',
            field=models.DecimalField(blank=True, db_column='PERLUN', decimal_places=0, max_digits=5, null=True, verbose_name='Lunghezza Piana'),
        ),
        migrations.AddField(
            model_name='forra',
            name='operatore',
            field=models.CharField(blank=True, db_column='OPERATORE', max_length=80, null=True, verbose_name='Ente Manutentore'),
        ),
        migrations.AddField(
            model_name='forra',
            name='pendenza',
            field=models.DecimalField(blank=True, db_column='PENDENZA', decimal_places=2, max_digits=5, null=True, verbose_name='Pendenza'),
        ),
        migrations.AddField(
            model_name='forra',
            name='percorribilita',
            field=models.ForeignKey(blank=True, db_column='PERCORR', null=True, on_delete=django.db.models.deletion.CASCADE, to='infotor.Condizioni', verbose_name='Percorribilità'),
        ),
        migrations.AddField(
            model_name='forra',
            name='quota_fine',
            field=models.DecimalField(blank=True, db_column='PERQUO2', decimal_places=0, max_digits=4, null=True, verbose_name='Quota Fine'),
        ),
        migrations.AddField(
            model_name='forra',
            name='quota_inizio',
            field=models.DecimalField(blank=True, db_column='PERQUO1', decimal_places=0, max_digits=4, null=True, verbose_name='Quota Inizio'),
        ),
        migrations.AddField(
            model_name='forra',
            name='segnaletica',
            field=models.ForeignKey(blank=True, db_column='SEGNI', null=True, on_delete=django.db.models.deletion.CASCADE, to='infotor.Segnaletica', verbose_name='Segnaletica'),
        ),
        migrations.AddField(
            model_name='forra',
            name='tempo_andata',
            field=models.DecimalField(blank=True, db_column='PERTEM1', decimal_places=2, max_digits=5, null=True, verbose_name='Tempo di percorrenza andata'),
        ),
        migrations.AddField(
            model_name='forra',
            name='tempo_ritorno',
            field=models.DecimalField(blank=True, db_column='PERTEM2', decimal_places=2, max_digits=5, null=True, verbose_name='Tempo di percorrenza ritorno'),
        ),
        migrations.AlterField(
            model_name='forra',
            name='id_percorso',
            field=models.IntegerField(db_column='IDPERC', verbose_name='Id Percorso'),
        ),
    ]