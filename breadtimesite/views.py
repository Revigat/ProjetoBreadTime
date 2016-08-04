# -*- coding: UTF-8 -*-
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from breadtimesite.models import *
# Create your views here.


def index(request):
    imagem = Post.objects.all()
    return render_to_response('index.html', {'imagem': imagem})


def exportarfeed(request):
    # Habilita os campos legiveis para aparecer no json
    feed = serializers.serialize(
        'json', list(Post.objects.all()),
        indent=1, use_natural_foreign_keys=True, use_natural_primary_keys=True)

    return HttpResponse(feed, content_type="application/json")


def gerarjson(request, format=None):

    feed = serializers.serialize(
        'json', Post.objects.all(),
        use_natural_foreign_keys=True, use_natural_primary_keys=True)

    return JsonResponse({
        'titulo': feed,
        'conteudo': feed,
        'data': feed,
        'imagem': feed,
        'status': feed,
        'usuario': feed,
        'categoria': feed,
        'viewsPost': feed, })
# Return HttpResponse(feed, content_type="application/json")
