# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class UsuarioGerenciador(models.Manager):
    # Classe para definir um nome legivel no json
	#https://docs.djangoproject.com/en/1.9/topics/serialization/#id2
	def get_by_natural_key(self,nome):
		return self.get(nome=nome)

class Usuario(models.Model):
	objects = UsuarioGerenciador()

	nome = models.CharField(max_length = 50)
	sobrenome = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50)
	senha = models.CharField(max_length = 20)
	tipousuario = models.ForeignKey('TipoUsuario', on_delete=models.CASCADE)
	

	def natural_key(self):
		return (self.nome)

	class Meta:
		unique_together = (('nome'),)

	def __str__(self):
		return self.nome

class TipoUsuario(models.Model):

	desc = models.CharField(max_length = 50)

	def __str__(self):
		return self.desc

class CategoriaGerenciador(models.Manager): #Classe manager para mostrar nomes naturais no json
	#https://docs.djangoproject.com/en/1.9/topics/serialization/#id2
	def get_by_natural_key(self,desc):
		return self.get(desc=desc)

class Categoria(models.Model):
	objects = CategoriaGerenciador()
	desc = models.CharField(max_length = 50)
	
	def natural_key(self):
		return (self.desc)

	class Meta:
		unique_together = (('desc'),)
			

	def __str__(self):
		return self.desc

class ViewsPost(models.Model):

	contviews = models.DecimalField(max_digits = 10, decimal_places = 0)

	'''def __str__(self):
		return self.contviews'''  

class Post(models.Model):

	titulo = models.CharField(max_length = 80)
	conteudo = models.TextField(max_length = 1500)
	data = models.DateField()
	imagem = models.ImageField(upload_to = 'static/img/upload')
	status = models.BooleanField() # caso Post seja rascunho ou postado
	usuario = models.ForeignKey('Usuario', on_delete = models.CASCADE)
	categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)
	viewsPost = models.ForeignKey('ViewsPost', on_delete = models.CASCADE)

	def __str__(self):
		return self.titulo