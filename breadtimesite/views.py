# -*- coding: UTF-8 -*-
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from breadtimesite.models import *
from breadtimesite.models import Token
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    imagem = Post.objects.all()
    return render_to_response('index.html', {'imagem': imagem})


def exportarfeed(request):
    # Habilita os campos legiveis para aparecer no json
    # https://docs.djangoproject.com/ja/1.9/topics/db/queries/
    json = serializers.serialize(
        'json', list(Post.objects.filter(status=True)),
        indent=3, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(json, content_type="application/json")

@csrf_exempt
def salvatoken(request):
    if request.method == 'POST':
        tk = Token(request.POST.get('Token'))
        tk.save()
        return HttpResponse(tk)

    return render_to_response('token.html')    
