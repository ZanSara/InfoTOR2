from math import modf

from django.core.exceptions import ValidationError

def frac_min_validator(value):
    frac, _ = modf(value)
    if frac >= 0.60:
        raise ValidationError("Formato della durata non corretto")
             
def timespan_validator(value):
    if value is None or value == "":
        return
    if value.count(":") != 1:
        raise ValidationError("Esprimere la durata in ore:minuti (per esempio, 01:20)")
    hours, minutes = value.split(":")
    if len(hours) <=0 or len(minutes) <=1:
        raise ValidationError("Esprimere la durata in ore:minuti (per esempio, 00:30)")
    try:
        hours = int(hours)
        minutes = int(minutes)
    except:
        raise ValidationError("Esprimere la durata in ore:minuti (per esempio, 01:15)")
    if hours < 0 or minutes < 0 or minutes >= 60:
        raise ValidationError("Esprimere la durata in ore:minuti (per esempio, 02:05)")
