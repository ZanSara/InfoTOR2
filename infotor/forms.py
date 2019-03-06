from django import forms
from infotor.models import Forra

class ForraForm(forms.ModelForm):

    class Utils:
        "Contain static functions that can be called in the main class body"
        @staticmethod
        def generate_decimal_field(name, positive=True):
            field = Forra._meta.get_field(name)
            max_val = 10 ** (field.max_digits - field.decimal_places) - 1
            if positive:
                return forms.DecimalField(max_value=max_val, min_value=0, decimal_places=field.decimal_places, required=False)
            else:
                return forms.DecimalField(max_value=max_val, decimal_places=field.decimal_places, required=False)

    numero_calate = Utils.generate_decimal_field('numero_calate')
    calata_massima = Utils.generate_decimal_field('calata_massima')
    lunghezza_min_corda = Utils.generate_decimal_field('lunghezza_min_corda')
    numero_min_corde = Utils.generate_decimal_field('numero_min_corde')
    dislivello = Utils.generate_decimal_field('dislivello', False)
    ampiezza_bacino = Utils.generate_decimal_field('ampiezza_bacino')
    minuti_navetta = Utils.generate_decimal_field('minuti_navetta')
    km_navetta = Utils.generate_decimal_field('km_navetta')
    ore_avvicinamento = Utils.generate_decimal_field('ore_avvicinamento')

    class Meta:
        model = Forra
        fields = [
            'id',
            'nome',
            'grado_impegno',
            'verticalita',
            'acquaticita',
            'bellezza',
            'divertimento',
            'numero_calate',
            'calata_massima',
            'lunghezza_min_corda',
            'numero_min_corde',
            'dislivello',
            'ampiezza_bacino',
            'origine_acqua',
            'ore_avvicinamento',
            'ore_discesa',
            'ore_rientro',
            'minuti_navetta',
            'km_navetta',
            'opere_idrauliche',
            'litologia',
            'stagionalita',
            'checkpoint1',
            'checkpoint2',
            'vincoli_ambientali',
            'presentazione_forra',
            'descr_accesso_monte',
            'descr_accesso_valle',
            'descr_avvicinamento',
            'descr_percorso',
            'descr_uscita',
            'profilo',
            'note',
        ]

        widgets = {
            'stagionalita': forms.CheckboxSelectMultiple,
        }
