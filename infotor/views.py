"views per l'app di torrentismo del CAI"

from django.shortcuts import render

from infotor.models import Forra, LIVELLI, PUNTEGGI
from infotor.forms import ForraForm

# TODO aggiungi pagine custom 500 e 404

def index(request):
    "Renderizza la pagina principale contenente l'elenco delle forre"

    lista_forre = Forra.objects.values('id', 'nome', 'dislivello', 'ore_avvicinamento', 'ore_discesa', 'ore_rientro').order_by('nome')
    return render(request, 'infotor/index.html', {'forre' : lista_forre})

def mostra_forra(request, id_forra):
    "Renderizza la pagina per visualizzare i dati di una forra"
    try:
        forra = Forra.objects.get(id=id_forra)
    except Forra.DoesNotExist:
        forra = None
    finally:
        punteggi = 'x' * len(PUNTEGGI)
        livelli = 'x' * len(LIVELLI)

        context_dict = {
            'forra' : forra,
            'punteggi' : punteggi,
            'livelli' : livelli,
        }

    return render(request, 'infotor/forra.html', context_dict)

# TODO completare questo
def nuova_forra(request):
    "Renderizza la pagina per aggiungere una nuova forra"

    if request.method == 'POST':
        form = ForraForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        # TODO completare
    else:
        form = ForraForm()

    return render(request, 'infotor/modifica_forra.html', {'form' : form})

def modifica_forra(request, id_forra):
    "Renderizza la pagina per modificare i dati di una forra"

    try:
        # fetch della forra dal db in base all'index. Può fallire
        forra = Forra.objects.get(id=id_forra)
        # se il form è stato compilato e inviato al server, processalo
        if request.method == 'POST':
            form = ForraForm(data=request.POST, files=request.FILES, instance=forra)
            # se il form è valido, salvalo e mostra la forra modificata
            if form.is_valid():
                form.save(commit=True)
                return mostra_forra(request, id_forra)

        # se non è POST, allora l'utente vuole modificare la forra
        else:
            form = ForraForm(instance=forra)

    except Forra.DoesNotExist:
        form = None

    return render(request, 'infotor/modifica_forra.html', {'form' : form, 'forra' : forra})
