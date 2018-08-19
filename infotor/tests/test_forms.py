from django.test import TestCase
from django.forms import model_to_dict
from infotor.forms import ForraForm
from . import utils

class ForraFormTests(TestCase):

    def test_validation(self):
        "Controlla che il form generato con i dati dell'istanza di default sia valido"
        data = model_to_dict(utils.instanciate_forra())
        form = ForraForm(data=data)
        self.assertTrue(form.is_valid())

    def test_non_negative_values(self):
        "Controlla che il form con valori negativi non sia valido"
        data = model_to_dict(utils.instanciate_forra())
        data['numero_calate'] = -1
        data['calata_massima'] = -2
        data['numero_min_corde'] = -3
        data['dislivello'] = -4 # allowed
        data['km_navetta'] = -5
        data['ampiezza_bacino'] = 6
        form = ForraForm(data=data)
        # the form should contain exactly four errors
        self.assertEqual(len(form.errors), 4)

    def test_ratings_ranges(self):
        "Controlla che i punteggi del form siano nei giusti intervalli"
        data = model_to_dict(utils.instanciate_forra())
        data['verticalita'] = 9 # not ok
        data['bellezza'] = 0 # not ok
        data['acquaticita'] = 3 # ok
        data['divertimento'] = 1.4 # not ok
        form = ForraForm(data=data)
        # the form should contain exactly three errors
        self.assertEqual(len(form.errors), 3)

    def test_durations(self):
        "Controlla che i campi che indicano durate siano corretti"
        data = model_to_dict(utils.instanciate_forra())
        data['ore_avvicinamento'] = 1.7
        data['ore_discesa'] = -2.1
        data['ore_rientro'] = 1.23
        form = ForraForm(data=data)
        self.assertEqual(len(form.errors), 2)
