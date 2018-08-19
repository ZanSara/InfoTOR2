from unittest import skip
from django.test import TestCase
from . import utils

class ForraTests(TestCase):
    "Testa tutti i campi della forra"

    def test_default_instance_valid(self):
        "Assicura che l'instanza di default si possa salvare senza errori"
        try:
            forra = utils.instanciate_forra()
            forra.save()
        except:
            self.fail("Impossibile salvare l'istanza di default")

    def test_rating_not_in_range(self):
        "Assicura che i punteggi siano nel giusto intervallo"
        forra = utils.instanciate_forra()
        forra.divertimento = 0
        self.assertRaises(ValueError, forra.save)

    def test_value_not_int(self):
        "Assicura che i punteggi siano interi decimali"
        forra = utils.instanciate_forra()
        forra.bellezza = 'ciao'
        self.assertRaises(ValueError, forra.save)

    def test_non_negative_values(self):
        "Assicura che i campi specificati non possano essere negativi"
        forra = utils.instanciate_forra()
        forra.numero_calate = -5
        self.assertRaises(ValueError, forra.save)
        forra.numero_calate = 4
        forra.save()

    def test_durations(self):
        "Controlla che i campi che indicano durate siano corretti"
        forra = utils.instanciate_forra()
        forra.ore_discesa = 0.89
        self.assertRaises(ValueError, forra.save)
        forra.ore_discesa = 89.55
        forra.save()
