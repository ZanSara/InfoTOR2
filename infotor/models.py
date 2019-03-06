from math import modf

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from infotor.validators import frac_min_validator

PUNTEGGI = ((1, 1), (2, 2), (3, 3), (4, 4))
LIVELLI = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7))

class Forra(models.Model):
    id = models.IntegerField(verbose_name='Id Forra', db_column='NUME', primary_key=True)

    nome = models.CharField(verbose_name='Nome Forra', db_column='TREK1', max_length=80)
    # id_percorso = models.ForeignKey('Percorso', verbose_name='Id Percorso', db_column='IDPERC')
    
    # TODO aggiungere i campi di collegamento che non mi sembrano tanto ok
    # id percorso
    # numero percorso
    # nome tratta

    grado_impegno = models.ForeignKey('GradoImpegno', verbose_name='Grado Impegno', db_column='IMPTOR', null=True, blank=True)

    verticalita = models.DecimalField(verbose_name='Livello Verticalità', db_column='LIVVER', choices=LIVELLI,
        max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(len(LIVELLI))], null=True, blank=True)
    acquaticita = models.DecimalField(verbose_name='Livello Acquaticità', db_column='LIVH2O', choices=LIVELLI,
        max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(len(LIVELLI))], null=True, blank=True)
    bellezza = models.DecimalField(verbose_name='Punteggio Bellezza', db_column='LIVBEL', choices=PUNTEGGI,
        max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(len(PUNTEGGI))], null=True, blank=True)
    divertimento = models.DecimalField(verbose_name='Punteggio Divertimento', db_column='LIVDIV', choices=PUNTEGGI,
        max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(len(PUNTEGGI))], null=True, blank=True)

    numero_calate = models.DecimalField(verbose_name='Numero Calate', db_column='NUMC',
        max_digits=1, decimal_places=0, validators=[MinValueValidator(0)], null=True, blank=True)
    calata_massima = models.DecimalField(verbose_name='Calata Massima', db_column='CALMAX',
        max_digits=1, decimal_places=0, validators=[MinValueValidator(0)], null=True, blank=True)
    lunghezza_min_corda = models.DecimalField(verbose_name='Lunghezza minima corda singola', db_column='CORMIN',
        max_digits=2, decimal_places=0, validators=[MinValueValidator(0)], null=True, blank=True)
    numero_min_corde = models.DecimalField(verbose_name='Numero minimo di corde', db_column='MINCORDE',
        max_digits=1, decimal_places=0, validators=[MinValueValidator(0)], null=True, blank=True)
    dislivello = models.DecimalField(verbose_name='Dislivello (m)', db_column='DISLIV',
        max_digits=2, decimal_places=0, null=True, blank=True)
    ampiezza_bacino = models.DecimalField(verbose_name='Ampiezza Bacino (km2)', db_column='AMPBAC',
        max_digits=4, decimal_places=0, validators=[MinValueValidator(0)], null=True, blank=True)

    origine_acqua = models.ForeignKey('OrigineAcqua', verbose_name='Origine Acqua', db_column='ORIGACQUA', null=True, blank=True)
    # TODO completare
    # quota partenza forra
    # quota arrivo forra
    ore_avvicinamento = models.DecimalField(verbose_name='Ore Avvicinamento', db_column='HAVV',
        max_digits=5, decimal_places=2, validators=[MinValueValidator(0), frac_min_validator], null=True, blank=True)
    ore_discesa = models.DecimalField(verbose_name='Ore Discesa', db_column='HCAL',
        max_digits=5, decimal_places=2, validators=[MinValueValidator(0), frac_min_validator], null=True, blank=True)
    ore_rientro = models.DecimalField(verbose_name='Ore Rientro', db_column='HRIE',
        max_digits=5, decimal_places=2, validators=[MinValueValidator(0), frac_min_validator], null=True, blank=True)

    minuti_navetta = models.DecimalField(verbose_name='Minuti Navetta', db_column='MMNAV',
        max_digits=3, decimal_places=0, validators=[MinValueValidator(0)], null=True, blank=True)
    km_navetta = models.DecimalField(verbose_name='Kilometri Navetta', db_column='KMNAV',
        max_digits=3, decimal_places=0, validators=[MinValueValidator(0)], null=True, blank=True)

    opere_idrauliche = models.ForeignKey('OperaIdraulica', verbose_name='Opere Idrauliche', db_column='OPEIDR', null=True, blank=True)
    litologia = models.ForeignKey('Litologia', verbose_name='Litologia', db_column='LITOL', null=True, blank=True)
    stagionalita = models.ManyToManyField('Mese', verbose_name='Mesi ok', db_column='STAGIONE', null=True, blank=True)

    # --- Checkpoints (foto) SONO FOREIGN KEY, c'è la tabella sotto
    checkpoint1 = models.ForeignKey('Checkpoint', verbose_name='Checkpoint 1', db_column='CHECKP1',
        related_name='checkpoint1', null=True, blank=True)
    checkpoint2 = models.ForeignKey('Checkpoint', verbose_name='Checkpoint 2', db_column='CHECKP2',
        related_name='checkpoint2', null=True, blank=True)

    # --- Informazioni (Memo / Testo libero) ---
    vincoli_ambientali = models.TextField(verbose_name='Vincoli ambientali', db_column='VINCOLI',
        max_length=250, null=True, blank=True)
    presentazione_forra = models.TextField(verbose_name='Presentazione forra', db_column='PRES',
        max_length=250, null=True, blank=True)
    descr_accesso_valle = models.TextField(verbose_name='Descrizione accesso a valle', db_column='DESACCV',
        max_length=250, null=True, blank=True)
    descr_accesso_monte = models.TextField(verbose_name='Descrizione accesso a monte', db_column='DESACCM',
        max_length=250, null=True, blank=True)
    descr_avvicinamento = models.TextField(verbose_name='Descrizione avvicinamento', db_column='DESAVV',
        max_length=250, null=True, blank=True)
    descr_percorso = models.TextField(verbose_name='Descrizione percorso', db_column='DESPERC',
        max_length=250, null=True, blank=True)
    descr_uscita = models.TextField(verbose_name='Descrizione uscita', db_column='DESUSC',
        max_length=250, null=True, blank=True)

    # --- Profilo forra ---
    profilo = models.ImageField(upload_to='profili/', verbose_name='Profilo Forra', db_column='PROFILO', null=True, blank=True)
    note = models.TextField(verbose_name='Note', db_column='NOTE', max_length=250, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Forre'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        Forra._validate_range(self.verticalita, 1, len(LIVELLI))
        Forra._validate_range(self.acquaticita, 1, len(LIVELLI))
        Forra._validate_range(self.bellezza, 1, len(PUNTEGGI))
        Forra._validate_range(self.divertimento, 1, len(PUNTEGGI))
        Forra._validate_non_negative(self.numero_calate)
        Forra._validate_non_negative(self.calata_massima)
        Forra._validate_non_negative(self.lunghezza_min_corda)
        Forra._validate_non_negative(self.numero_min_corde)
        Forra._validate_non_negative(self.ampiezza_bacino)
        Forra._validate_non_negative(self.minuti_navetta)
        Forra._validate_non_negative(self.km_navetta)
        Forra._validate_decimal_duration(self.ore_avvicinamento)
        Forra._validate_decimal_duration(self.ore_discesa)
        Forra._validate_decimal_duration(self.ore_rientro)
        super(Forra, self).save(*args, **kwargs)

    @staticmethod
    def _validate_range(value, min_value, max_value):
        if value is None or value == "":
            return
        value = int(value)
        if value < min_value or value > max_value:
            raise ValueError('Value not in range')

    @staticmethod
    def _validate_non_negative(value):
        if value is None or value == "":
            return
        if value < 0:
            raise ValueError('Value cannot be negative')

    @staticmethod
    def _validate_decimal_duration(value):
        if value is None or value == "":
            return
        Forra._validate_non_negative(value)
        frac, _ = modf(value)
        if frac >= 0.60:
            raise ValueError('Fraction representing minutes cannot exceed 60')


#______________________________________________________________________________

class Tratta(models.Model):
    id = models.IntegerField(verbose_name='Id Tratta', db_column='IDTRAT', primary_key=True)

    nome = models.CharField(verbose_name='Nome Tratta', db_column='TRTNAME', max_length=30, null=True)
    regione = models.CharField(verbose_name='Regione', db_column='REGIONE', max_length=2, null=True)
    provincia = models.CharField(verbose_name='Provincia', db_column='PROVINCIA', max_length=2, null=True)
    comune = models.CharField(verbose_name='Comune', db_column='COMUNE', max_length=6, null=True)

    gruppo_montuoso = models.CharField(verbose_name='Gruppo Montuoso', db_column='GRUMON', max_length=11, null=True)
    sezione = models.CharField(verbose_name='Sezione', db_column='SEZION', max_length=7, null=True)

    tipologia = models.ForeignKey('Tipologia', verbose_name='Tipologia', db_column='TIPOLOGIA')
    caratteristica = models.ForeignKey('Caratteristica', verbose_name='Caratteristica', db_column='CARATTER')

    lunghezza_piana = models.DecimalField(verbose_name='Lunghezza Piana', db_column='PERLUN',
        max_digits=5, decimal_places=0)
    lunghezza_inclinata = models.DecimalField(verbose_name='Lunghezza Inclinata', db_column='PERLUNF',
        max_digits=5, decimal_places=0)
    quota_inizio = models.DecimalField(verbose_name='Quota Inizio', db_column='PERQUO1',
        max_digits=4, decimal_places=0)
    quota_fine = models.DecimalField(verbose_name='Quota Fine', db_column='PERQUO2',
        max_digits=4, decimal_places=0)
    pendenza = models.DecimalField(verbose_name='Pendenza', db_column='PENDENZA',
        max_digits=5, decimal_places=2)
    # TODO controlla i seguenti NEWFIELD trovati nei dbf che suonano strani
    tempo_andata = models.DecimalField(verbose_name='Tempo di percorrenza andata', db_column='NEWFIELD1',
        max_digits=5, decimal_places=2)
    tempo_ritorno = models.DecimalField(verbose_name='Tempo di percorrenza ritorno', db_column='NEWFIELD2',
        max_digits=5, decimal_places=2)

    difficolta = models.ForeignKey('Difficolta', verbose_name='Difficoltà', db_column='PERDIF')
    segnaletica = models.ForeignKey('Segnaletica', verbose_name='Segnaletica', db_column='SEGNI')

    rilevatore = models.CharField(verbose_name='Rilevatore', db_column='RILEVATORE', max_length=50, null=True)
    # TODO aggiugere la tabella corrispondente
    # accuratezza = models.ForeignKey('Accuratezza', db_column='TIPO_RIL')
    ### campi non segnalati nel documento ma comparenti nel dbf
    gps = models.CharField(verbose_name='Data GPS', db_column='DATA_GPS', max_length=16, null=True)
    id_rilevatore = models.CharField(verbose_name='ID Rilevatore', db_column='ID_RIL', max_length=3, null=True)

    class Meta:
        verbose_name_plural = 'Tratte'

    def __str__(self):
        return self.nome

#______________________________________________________________________________

class Percorso(models.Model):
    id = models.IntegerField(verbose_name='Id Percorso', db_column='IDPERC', primary_key=True)

    numero = models.CharField(verbose_name='Numero Percorso', db_column='NUME', max_length=6)
    nome = models.CharField(verbose_name='Nome/Sigla/Logo Trekking', db_column='TREK1', max_length=80)
    percorribilita = models.ForeignKey('Condizioni', verbose_name='Percorribilità', db_column='PERCORR')
    descrizione = models.CharField(verbose_name='Descrizione', db_column='DENOMI', max_length=80, null=True)

    lunghezza_piana = models.DecimalField(verbose_name='Lunghezza Piana', db_column='PERLUN',
        max_digits=5, decimal_places=0)
    lunghezza_inclinata = models.DecimalField(verbose_name='Lunghezza Inclinata', db_column='PERLUNF',
        max_digits=5, decimal_places=0)
    quota_inizio = models.DecimalField(verbose_name='Quota Inizio', db_column='PERQUO1',
        max_digits=4, decimal_places=0)
    quota_fine = models.DecimalField(verbose_name='Quota Fine', db_column='PERQUO2',
        max_digits=4, decimal_places=0)
    pendenza = models.DecimalField(verbose_name='Pendenza', db_column='PENDENZA',
        max_digits=5, decimal_places=2)
    tempo_andata = models.DecimalField(verbose_name='Tempo di percorrenza andata', db_column='PERTEM1',
        max_digits=5, decimal_places=2)
    tempo_ritorno = models.DecimalField(verbose_name='Tempo di percorrenza ritorno', db_column='PERTEM2',
        max_digits=5, decimal_places=2)

    difficolta = models.ForeignKey('Difficolta', verbose_name='Difficoltà', db_column='PERDIF')
    segnaletica = models.ForeignKey('Segnaletica', verbose_name='Segnaletica', db_column='SEGNI')

    data_aggiornamento = models.DateField(verbose_name='Data Aggiornamento', db_column='DATARIL')
    # rete_regionale = models.ForeignKey('Rete', db_column='RETEREG', null=True) # TODO metti la tabella corrispondente
    codice_catasto = models.CharField(verbose_name='Codice Catasto Regionale', db_column='CODREG', max_length=12, null=True)

    operatore = models.CharField(verbose_name='Ente Manutentore', db_column='OPERATORE', max_length=80)

    #interesse_storico = models.ForeignKey('Valenza', db_column='STORICO', null=True) # TODO metti la tabella corrispondente
    #interesse_architettonico = models.ForeignKey('Valenza', db_column='ARCHITETT', null=True)
    #interesse_paesaggistico = models.ForeignKey('Valenza', db_column='PAESAGG', null=True)
    #interesse_naturalistco = models.ForeignKey('Valenza', db_column='NATURAL', null=True)

    link_CMS = models.CharField(verbose_name='Link CMS', db_column='LINK', max_length=16, null=True)
    aggiornatore = models.CharField(verbose_name='Aggiornatore', db_column='UTENTE', max_length=16, null=True)

    class Meta:
        verbose_name_plural = 'Percorsi'

    def __str__(self):
        return self.nome

#______________________________________________________________________________

class PercorsoTratta(models.Model):
    percorso = models.ForeignKey('Percorso', verbose_name='ID Percorso', db_column='ID_PERCORS')
    tratta = models.ForeignKey('Tratta', verbose_name='ID Tratta', db_column='ID_TRATTA')

#______________________________________________________________________________

class Tipologia(models.Model):
    codice = models.CharField(verbose_name='Codice', db_column='CODICE', max_length=3, primary_key=True)
    descrizione = models.CharField(verbose_name='Descrizione', db_column='DESCRIZION', max_length=50)


    class Meta:
        verbose_name_plural = 'Tipologie'

    def __str__(self):
        return self.descrizione

#______________________________________________________________________________

class Caratteristica(models.Model):
    codice = models.CharField(verbose_name='Codice', db_column='CODICE', max_length=3, primary_key=True)
    descrizione = models.CharField(verbose_name='Descrizione', db_column='DESCRIZION', max_length=50)

    class Meta:
        verbose_name_plural = 'Caratteristiche'

    def __str__(self):
        return self.descrizione

#______________________________________________________________________________

class Difficolta(models.Model):
    codice = models.CharField(verbose_name='Codice', db_column='CODICE', max_length=3, primary_key=True)
    descrizione = models.CharField(verbose_name='Descrizione', db_column='DESCRIZION', max_length=20)

    class Meta:
        verbose_name_plural = 'Difficoltà'

    def __str__(self):
        return self.descrizione

#______________________________________________________________________________

class Segnaletica(models.Model):
    codice = models.CharField(verbose_name='Codice', db_column='CODICE', max_length=3, primary_key=True)
    descrizione = models.CharField(verbose_name='Descrizione', db_column='DESCRIZION', max_length=20)

    class Meta:
        verbose_name_plural = 'Segnaletiche'

    def __str__(self):
        return self.descrizione

#______________________________________________________________________________

class Condizioni(models.Model):
    codice = models.CharField(verbose_name='Codice', db_column='CODICE', max_length=3, primary_key=True)
    descrizione = models.CharField(verbose_name='Descrizione', db_column='DESCRIZION', max_length=16)

    class Meta:
        verbose_name_plural = 'Condizioni'

    def __str__(self):
        return self.descrizione

#______________________________________________________________________________

class GradoImpegno(models.Model):
    codice = models.CharField(verbose_name='Codice', db_column='CODICE', max_length=3, primary_key=True)
    descrizione = models.CharField(verbose_name='Descrizione', db_column='DESCRIZION', max_length=20)

    class Meta:
        verbose_name_plural = 'Gradi Impegno'

    def __str__(self):
        return self.descrizione

#______________________________________________________________________________

class OrigineAcqua(models.Model):
    codice = models.DecimalField(verbose_name='Codice', db_column='CODICE', primary_key=True,
        max_digits=2, decimal_places=0)
    descrizione = models.CharField(verbose_name='Descrizione', db_column='DESCRIZION', max_length=20)

    class Meta:
        verbose_name_plural = 'Origini Acqua'
        ordering = ('descrizione', )

    def __str__(self):
        return self.descrizione

#______________________________________________________________________________

class Litologia(models.Model):
    codice = models.DecimalField(verbose_name='Codice', db_column='CODICE', primary_key=True,
        max_digits=2, decimal_places=0)
    descrizione = models.CharField(verbose_name='Descrizione', db_column='DESCRIZION', max_length=20)

    class Meta:
        verbose_name_plural = 'Litologie'
        ordering = ('descrizione', )

    def __str__(self):
        return self.descrizione

#______________________________________________________________________________

class OperaIdraulica(models.Model):
    codice = models.CharField(verbose_name='Codice', db_column='CODICE', max_length=2, primary_key=True)
    descrizione = models.CharField(verbose_name='Descrizione', db_column='DESCRIZION', max_length=20)

    class Meta:
        verbose_name_plural = 'Opere Idrauliche'
        ordering = ('descrizione', )

    def __str__(self):
        return self.descrizione

#______________________________________________________________________________

class Mese(models.Model):
    codice = models.DecimalField(verbose_name='Codice', db_column='CODICE', primary_key=True,
        max_digits=2, decimal_places=0)
    mese = models.CharField(verbose_name='Mese', db_column='MESE', max_length=10)

    class Meta:
        verbose_name_plural = 'Mesi'
        ordering = ('codice', )

    def __str__(self):
        return self.mese

#______________________________________________________________________________

class Checkpoint(models.Model):
    codice = models.DecimalField(verbose_name='Codice', db_column='CODICE', primary_key=True,
        max_digits=5, decimal_places=0)
    descrizione = models.TextField(verbose_name='Descrizione', db_column='DESCRIZION', max_length=250, null=True)
    immagine = models.ImageField(upload_to='checkpoints/', verbose_name='Immagine', db_column='IMMAGINE')



    def __str__(self):
        return str(self.immagine)
