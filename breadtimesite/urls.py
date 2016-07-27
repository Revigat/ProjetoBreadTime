# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.contrib import admin
import breadtimesite.views

urlpatterns = [
	url(r'^$',breadtimesite.views.index), # versão mais recente do django não suporta string
	url(r'^exportarfeed/',breadtimesite.views.exportarfeed),
	
]
