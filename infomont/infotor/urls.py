"Mappa gli url del sito"

from django.conf.urls import url
from infotor import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^forra/(?P<id_forra>[0-9]+)/$', views.mostra_forra, name='mostra_forra'),
    url(r'^forra/(?P<id_forra>[0-9]+)/modifica/$', views.modifica_forra, name='modifica_forra'),
    url(r'^forra/nuova/$', views.nuova_forra, name='nuova_forra'),
]
