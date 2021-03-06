# -*- coding: UTF-8 -*-
from django.conf.urls import url
import breadtimesite.views

urlpatterns = [
    url(r'^$', breadtimesite.views.index),
    # Versão mais recente do django não suporta string
    url(r'^exportarfeed/$', breadtimesite.views.exportar_feed),
    #url(r'^salvatoken/(?P<tokens>[\w\S\-\_\\\/,/]+)/$', breadtimesite.views.sexportar_feed),
    url(r'^salvatoken/$', breadtimesite.views.salvar_token),
    url(r'^notificacao/$', breadtimesite.views.enviar_notificacao),

]
