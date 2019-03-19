
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from infotor import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^infotor/', include('infotor.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'infotor.views.handler404'
handler500 = 'infotor.views.handler500'

