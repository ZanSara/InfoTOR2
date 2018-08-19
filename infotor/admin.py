"Sezione di amministrazione"

from django.contrib import admin

from infotor.models import Forra, Checkpoint, GradoImpegno, OperaIdraulica, Litologia, OrigineAcqua, Mese
# Register your models here.
admin.site.register(Forra)
admin.site.register(Checkpoint)
admin.site.register(GradoImpegno)
admin.site.register(OperaIdraulica)
admin.site.register(Litologia)
admin.site.register(OrigineAcqua)
admin.site.register(Mese)
