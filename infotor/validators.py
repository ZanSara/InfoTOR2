from math import modf

from django.core.exceptions import ValidationError

def frac_min_validator(value):
    frac, _ = modf(value)
    if frac >= 0.60:
        raise ValidationError("Formato della durata non corretto")
