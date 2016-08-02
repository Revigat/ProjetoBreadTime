# -*- coding: UTF-8 -*-
from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from breadtimesite.models import *

# Create your views here.

def index(request):
	imagem = Post.objects.all()
	return render_to_response('index.html', {'imagem' : imagem})


def exportarfeed(request):
	#Habilita os campos legiveis para aparecer no json
	feed = serializers.serialize('json', list(Post.objects.all()),indent=1,use_natural_foreign_keys=True, use_natural_primary_keys=True)
	return HttpResponse(feed, content_type="application/json")
