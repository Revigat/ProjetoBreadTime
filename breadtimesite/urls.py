# -*- coding: UTF-8 -*-
from django.conf.urls import url
import breadtimesite.views

urlpatterns = [
    url(r'^$', breadtimesite.views.index),
    # Versão mais recente do django não suporta string
    url(r'^exportarfeed/$', breadtimesite.views.exportarfeed),
    url(r'^salvatoken/(?P<tokens>[\w\S\-\_\\\/,/]+)/$', breadtimesite.views.salvatoken),


]
