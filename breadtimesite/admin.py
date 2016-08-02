# -*- coding: UTF-8 -*-
from django.contrib import admin
from breadtimesite.models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin): #Mostra os campos nas colunas
	list_display = ('nome', 'sobrenome', 'email', 'senha')

class PostAdmin(admin.ModelAdmin): # Cria o Filtro na página do administrador
	list_display = ('usuario', 'data','categoria')
	list_filter = ('data','usuario',)

#admin.site.register(UsuarioAdmin) #Autoriza mostrar as colunas
admin.site.register(Categoria)
admin.site.register(ViewsPost)
admin.site.register(Post)#Autoriza a criacao do filto