from django.contrib import admin
from breadtimesite.models import *

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('nome', 'sobrenome', 'email', 'senha')

class PostAdmin(admin.ModelAdmin):
	list_display = ('usuario', 'data','categoria')
	list_filter = ('data','usuario',)

admin.site.register(Usuario, AuthorAdmin)
admin.site.register(TipoUsuario)
admin.site.register(Categoria,)
admin.site.register(ViewsPost)
admin.site.register(Post,PostAdmin)