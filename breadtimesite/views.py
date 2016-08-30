# -*- coding: UTF-8 -*-
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from breadtimesite.models import *
from breadtimesite.models import Token
from django.views.decorators.csrf import csrf_exempt
from breadtimesite.serializers import PostSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.


def index(request):
    imagem = Post.objects.all()
    return render_to_response('index.html', {'imagem': imagem})


def exportar_feed(request):
    # Recupera os dados somente os que atende a condição
    posts = Post.objects.filter(status=True)
    # Passa da dados para a classe que serializa e limpa
    serializer = PostSerializer(posts, many=True)
    json_feed = JSONRenderer().render(serializer.data)
    return HttpResponse(json_feed)


@csrf_exempt
def salvar_token(request):
    t = Token()
    if request.method == 'POST':
        # Campo que vem junto com o Token.
        t.token = request.POST['Token']
        t.save()
        return HttpResponse(t.token)

    return render_to_response('token.html')
