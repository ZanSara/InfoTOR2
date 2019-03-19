"Mappa gli url del sito"

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from infotor import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mappa/$', views.mappa, name='mappa'),
    url(r'^forra/(?P<id_forra>[0-9]+)/$', views.mostra_forra, name='mostra_forra'),
    url(r'^forra/(?P<id_forra>[0-9]+)/modifica/$', views.modifica_forra, name='modifica_forra'),
]

# urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = 'infotor.views.handler404'
handler500 = 'infotor.views.handler500'


