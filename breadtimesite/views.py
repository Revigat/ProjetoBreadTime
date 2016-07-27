# -*- coding: UTF-8 -*-
from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from django.core.serializers.json import DjangoJSONEncoder
from breadtimesite.models import *

# Create your views here.

def index(request):
	imagem = Post.objects.all()
	return render_to_response('index.html', {'imagem':imagem})


def exportarfeed(request):
	data = serializers.serialize('json', list(Post.objects.all()),indent=2,use_natural_foreign_keys=True, use_natural_primary_keys=True)
	#Habilita o nome legivel 
	return HttpResponse(data,content_type="application/json; charset=utf-8")