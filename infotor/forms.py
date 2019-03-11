from django import forms
from infotor.models import Forra, Checkpoint

class CheckpointForm(forms.ModelForm):
    
    class Meta:
        model = Checkpoint
        fields = [
            'immagine',
            'descrizione'
        ]
        

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
          
        #@staticmethod      
        #def generate_time_field(name):
        #    field = Forra._meta.get_field(name)
            

    numero_calate = Utils.generate_decimal_field('numero_calate')
    calata_massima = Utils.generate_decimal_field('calata_massima')
    lunghezza_min_corda = Utils.generate_decimal_field('lunghezza_min_corda')
    numero_min_corde = Utils.generate_decimal_field('numero_min_corde')
    dislivello = Utils.generate_decimal_field('dislivello', False)
    ampiezza_bacino = Utils.generate_decimal_field('ampiezza_bacino')
    km_navetta = Utils.generate_decimal_field('km_navetta')
    
    #tempo_andata = Utils.generate_time_field('tempo_andata')
    #ore_discesa = Utils.generate_time_field('ore_discesa')
    #tempo_ritorno = Utils.generate_time_field('tempo_ritorno')
    #minuti_navetta = Utils.generate_time_field('minuti_navetta')
    
    #ore_avvicinamento = Utils.generate_decimal_field('tempo_andata')

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
            'tempo_andata', #'ore_avvicinamento',
            'ore_discesa',
            'tempo_ritorno', #'ore_rientro',
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
    
    def clean_tempo_andata(self):
        return self.clean_minutes(self.cleaned_data['tempo_andata'])
    def clean_ore_discesa(self):
        return self.clean_minutes(self.cleaned_data['ore_discesa'])
    def clean_tempo_ritorno(self):
        return self.clean_minutes(self.cleaned_data['tempo_ritorno'])
    def clean_minuti_navetta(self):
        return self.clean_minutes(self.cleaned_data['minuti_navetta'])
    
    def clean_minutes(self, value_to_clean):
        if value_to_clean is None:
            print("D")
            return None
        #try:
        hours, minutes = value_to_clean.split(":")
        if len(hours) > 2 or len(hours) < 1:
            print("A")
            return None
        else:
            if len(hours) == 1:
                hours = "0{}".format(hours)
        if len(minutes) > 2 or len(minutes) < 1:
            print("B")
            return None
        else:
            if len(minutes) == 1:
                minutes = "{}0".format(minutes)
        return "{}:{}".format(hours, minutes)
        #except:
        #    print("C")
        #    return None
        return None
