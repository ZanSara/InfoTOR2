"views per l'app di torrentismo del CAI"
import os, json
from collections import defaultdict
#from dbfread import DBF
from dbfpy3 import dbf

from django.shortcuts import render
from django.core.exceptions import ValidationError

from infotor.models import Forra, Percorso, LIVELLI, PUNTEGGI
#from infotor.models_dbf import ForraDBF, LIVELLI_DBF, PUNTEGGI_DBF
from infotor.forms import ForraForm


# TODO aggiungi pagine custom 500 e 404

PATH_TO_DBF = "{}/{}".format(os.path.dirname(os.path.realpath(__file__)), 'dbf')
PATH_TO_SEN_TRT = "{}/{}".format(PATH_TO_DBF, 'sen_trt.dbf')
PATH_TO_SEN_PERC = "{}/{}".format(PATH_TO_DBF, 'sen_perc.dbf')


def index(request):
    "Renderizza la pagina principale contenente l'elenco delle forre"

    #lista_forre = Forra.objects.values('id', 'nome', 'dislivello', 'ore_avvicinamento', 'ore_discesa', 'ore_rientro').order_by('nome')        
    forre = load_dbf_with_readable_colnames(PATH_TO_SEN_PERC)
    return render(request, 'infotor/index.html', {'forre' : forre})
    

def mostra_forra(request, id_forra):
    "Renderizza la pagina per visualizzare i dati di una forra"
    
    forre_records = load_dbf_with_readable_colnames(PATH_TO_SEN_PERC)    
    forra = [forra for forra in forre_records if forra["numero"]==id_forra][0]
    # forra = Forra.objects.get(id=id_forra)
    punteggi = 'x' * len(PUNTEGGI)
    livelli = 'x' * len(LIVELLI)

    context_dict = {
        'forra' : forra,
        'punteggi' : punteggi,
        'livelli' : livelli,
    }

    return render(request, 'infotor/forra.html', context_dict)

def modifica_forra(request, id_forra):
    "Renderizza la pagina per modificare i dati di una forra"
    
    # se il form è stato compilato e inviato al server, processalo
    if request.method == 'POST':
        form = ForraForm(data=request.POST, files=request.FILES, instance=forra) #FIXME
        # se il form è valido, salvalo e mostra la forra modificata
        if form.is_valid():
            form.save(commit=True)
            return mostra_forra(request, id_forra)
    
    else:
        forre_records = load_dbf_with_readable_colnames(PATH_TO_SEN_PERC)    
        forra = [forra for forra in forre_records if forra["numero"]==id_forra][0]
        form = ForraForm(initial=forra)
        return render(request, 'infotor/modifica_forra.html', {'forra' : forra, 'form' : form})
    
    
# TODO completare questo
# def nuova_forra(request):
#     "Renderizza la pagina per aggiungere una nuova forra"

#     if request.method == 'POST':
#         form = ForraForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
        # TODO completare
#     else:
#         form = ForraForm()

#     return render(request, 'infotor/modifica_forra.html', {'form' : form})





def load_dbf_with_readable_colnames(path_to_dbf_file):

    dbf_fields = []
    for field in Forra._meta.get_fields() + Percorso._meta.get_fields():
        try:
            dbf_fields.append( (field.name, field.db_column) )
        except AttributeError:
            pass

    for filepath in [PATH_TO_SEN_TRT, PATH_TO_SEN_PERC]:
        forre_records = dbf.Dbf(path_to_dbf_file)
        forre_list = []
        for forra_record in forre_records:
            forra = defaultdict(dict)
            for field in dbf_fields:
                key, value = field
                try:
                    forra[key] = forra_record[value]   
                except ValueError:
                    forra[key] = ""
            forre_list.append( forra )
        
    # print( json.dumps(forre_list, indent=4, default=str) )   
    return forre_list
