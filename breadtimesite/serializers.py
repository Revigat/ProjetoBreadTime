# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from django.contrib.auth.models import User
from breadtimesite.models import Post


# Serializo para pode usar os atributos da classe
class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


class PostSerializer(serializers.ModelSerializer):
    ''' Slug serializers.SlugRelatedField mostra o nome do campo ao invés de ID
    Slug_field='first_name' = Campo da tabela ralcionada
    https://codedump.io/share/v1fGXkfilQXi/1/django-python-39customer39-object-is-not-iterable '''
    # usuario = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    categoria = serializers.SlugRelatedField(slug_field='desc', read_only=True)
    # Faço a instancia da classe e digo qual campo do modelo ele se refere
    nome_completo = UsuarioSerializer(source='usuario')

    class Meta:
        model = Post
        fields = ('titulo', 'conteudo', 'data', 'imagem', 'status', 'contview', 'nome_completo', 'categoria')
