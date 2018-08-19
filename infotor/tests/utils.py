from infotor.models import Forra, GradoImpegno

def instanciate_forra():
    "Istanzia una forra con valori di default. Crea anche un istanza di GradoImpegno"
    return Forra(
        id=99,
        nome='test',
        grado_impegno=GradoImpegno.objects.create(codice='I', descrizione='< 2 ore'),
        verticalita=1,
        acquaticita=1,
        bellezza=1,
        divertimento=1,
        numero_calate=0,
        calata_massima=0,
        lunghezza_min_corda=0,
        numero_min_corde=0,
        dislivello=0,
        ampiezza_bacino=0,
        ore_avvicinamento=0,
        ore_discesa=0,
        ore_rientro=0,
        minuti_navetta=0,
        km_navetta=0,
    )
