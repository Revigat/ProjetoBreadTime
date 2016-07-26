from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'breadtimesite.views.index'),
	#url(r'^exportarfeed/','breadtimesite.views.exportarfeed'),

]
