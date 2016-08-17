# -*- coding: UTF-8 -*-
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from breadtimesite.models import *
from breadtimesite.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import json
from django.core.serializers.python import Serializer

# Create your views here.


def index(request):
    imagem = Post.objects.all()
    return render_to_response('index.html', {'imagem': imagem})


def exportar_feed(request):
    # Habilita os campos legiveis para aparecer no json
    # https://docs.djangoproject.com/ja/1.9/topics/db/queries/

    class MySerialiser(Serializer):
        def end_object(self, obj):
            self._current['id'] = obj._get_pk_val()
            self.objects.append(self._current)

 # Views.py
    serializer = MySerialiser()

    json = serializer.serialize(Post.objects.filter(status=True),
        indent=3, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(json, content_type="application/json; charset=utf-8")


@csrf_exempt
def salvar_token(request):
    t = Token()
    if request.method == 'POST':
        # Campo que vem junto com o Token.
        t.token = request.POST['Token']
        t.save()
        return HttpResponse(t.token)

    return render_to_response('token.html')
