"views per l'app di torrentismo del CAI"
import os, json
from collections import defaultdict

import os, json
from collections import defaultdict
from dbfread import DBF
import gdaltools

from django.http import Http404
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.fields.reverse_related import ManyToOneRel
from django.contrib.staticfiles.storage import staticfiles_storage

from infotor.models import Forra, Percorso, LIVELLI, PUNTEGGI
from infotor.forms import ForraForm, CheckpointForm


# TODO aggiungi pagine custom 500 e 404
PATH_TO_SEN_TRT = staticfiles_storage.path('dbf/sen_trt.dbf')
PATH_TO_SEN_PERC = staticfiles_storage.path('dbf/sen_perc.dbf')
PATH_TO_CON_DIF = staticfiles_storage.path('dbf/con_dif.dbf')


def index(request):
    "Renderizza la pagina principale contenente l'elenco delle forre"
    forre_dbf = read_dbf(PATH_TO_SEN_PERC, [Forra, Percorso])
    forre = []
    for forra in forre_dbf:
        try:
            forre.append( Forra.objects.get(id=int(forra["id"])) )
        except Forra.DoesNotExist:
            nuova_forra = create_forra(forra["id"])
            if nuova_forra is not None:
                forre.append(nuova_forra)
    return render(request, 'infotor/index.html', {'forre' : forre})
    
def mappa(request):

    ogr = gdaltools.ogr2ogr()
    ogr.set_encoding("UTF-8")
    ogr.set_input(staticfiles_storage.path('dbf/sen_trt.shp'))
    ogr.set_output(staticfiles_storage.path('gml/torrenti.gml'))
    ogr.execute()

    return render(request, 'infotor/mappa.html')



def mostra_forra(request, id_forra):
    "Renderizza la pagina per visualizzare i dati di una forra"
    forra = None
    try:
        forra = Forra.objects.get(id=id_forra)
    except Forra.DoesNotExist:
        raise Http404              
    finally:
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
    try:
        try:
            # fetch della forra dal db in base all'index. Può fallire
            forra = Forra.objects.get(id=id_forra)
        except Forra.DoesNotExist:
            raise Http404
        # se il form è stato compilato e inviato al server, processalo
        if request.method == 'POST':
            form = ForraForm(data=request.POST, files=request.FILES, instance=forra)
            checkpoint1_form = CheckpointForm(prefix='checkpoint1', data=request.POST, files=request.FILES, instance=forra.checkpoint1)
            checkpoint2_form = CheckpointForm(prefix='checkpoint2',data=request.POST, files=request.FILES, instance=forra.checkpoint2)
            
            # print(json.dumps(request.POST, indent=4))
            
            # se il form è valido, salvalo e mostra la forra modificata
            if form.is_valid() and checkpoint1_form.is_valid() and checkpoint2_form.is_valid():
                form.save(commit=True)
                nuovaforra = Forra.objects.get(id=id_forra)
                nuovaforra.checkpoint1 = checkpoint1_form.save(commit=True)
                nuovaforra.checkpoint2 = checkpoint2_form.save(commit=True)
                nuovaforra.save()
                
                return mostra_forra(request, id_forra)
        # se non è POST, allora l'utente vuole modificare la forra
        else:
            form = ForraForm(instance=forra)
            checkpoint1_form = CheckpointForm(prefix='checkpoint1', instance=forra.checkpoint1)
            checkpoint2_form = CheckpointForm(prefix='checkpoint2', instance=forra.checkpoint2)

    except Forra.DoesNotExist:
        form = None
        checkpoint1_form = None
        checkpoint2_form = None

    return render(request, 'infotor/modifica_forra.html', { 'form' : form, 
                                                            'forra' : forra, 
                                                            'checkpoint1_form': checkpoint1_form, 
                                                            'checkpoint2_form': checkpoint2_form
                                                          })
    
    
    
    
    
def read_dbf(path_to_dbf_file, models):
    dbf_fields = []
    fields_list = []
    for model in models:
        fields_list += model._meta.get_fields()
    
    for field in fields_list:
        try:
            if type(field) != ManyToOneRel:
                dbf_fields.append( (field.name, field.db_column) )
        except AttributeError:
            #print("[WARNING] Model field {} ({}) not found in this record of {}.".format(field.name, field.db_column, path_to_dbf_file) )
            pass

    for filepath in [PATH_TO_SEN_TRT, PATH_TO_SEN_PERC]:
        forre_list = []
        for forra_record in DBF(path_to_dbf_file):
            forra = defaultdict(dict)
            for field in dbf_fields:
                key, value = field
                try:
                    forra[key] = forra_record[value]
                    if type(forra[key]) == type(""):
                        forra[key] = forra[key].strip()
                except KeyError as e:
                    pass
                    #print("[WARNING] forra[{}] not found in this record of {}. [KeyError: {}]".format(value, path_to_dbf_file, e) )
                    #forra[key] = ""
                #except dbf.FieldMissingError:
                #    print("[WARNING] forra[{}] not found in this record of {}.".format(value, path_to_dbf_file) )
                #    forra[key] = ""
            forre_list.append( forra )
    #print( json.dumps(forre_list, indent=4, default=str) )   
    return forre_list
    

    
def create_forra(id_forra):
    forre_esistenti = read_dbf(PATH_TO_SEN_PERC, [Forra, Percorso])
    
    for forra in forre_esistenti:
        if int(forra['id']) == int(id_forra):
            #print(forra)
            
            nuovaforra = Forra.objects.create(id=id_forra, 
                nome=forra['nome'], 
                id_percorso=forra['numero'],
                quota_inizio = forra['quota_inizio'],
                quota_fine = forra['quota_fine'],
                tempo_andata = create_timestring(forra['tempo_andata']),
                tempo_ritorno = create_timestring(forra['tempo_ritorno']) )
            return Forra.objects.get(id=id_forra)
    return None
    
    
def create_timestring(value):
    if value is None:
        return None
    try:
        hours_int = int(value/60)
        minutes_int = int(value%60)
        if hours_int < 10:
            hours = "0{}".format(hours_int)
        else:
            hours = "{}".format(hours_int)
        if minutes_int < 10:
            minutes = "0{}".format(minutes_int)
        else:
            minutes = "{}".format(minutes_int)
    except:
        return None
    return "{}:{}".format(hours, minutes)
    
