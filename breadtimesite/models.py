# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=70)
    conteudo = models.TextField(max_length=1500)
    data = models.DateField()
    imagem = models.ImageField(upload_to='static/img/upload')
    status = models.BooleanField()
    contview = models.IntegerField()
    # caso Post seja rascunho ou postado
    usuario = models.ForeignKey(User)
    categoria = models.ForeignKey('CategoriaPost', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class CategoriaPost(models.Model):

    desc = models.CharField(max_length=50)

    def natural_key(self):
        return (self.desc)

    class Meta:
        unique_together = (('desc'),)

    def __str__(self):
        return self.desc


class Token(models.Model):
    token = models.CharField(max_length=200, unique=True)
