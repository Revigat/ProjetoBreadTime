# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from pyfcm import FCMNotification

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=70)
    conteudo = models.TextField(max_length=1500)
    # Pega a Data do dia
    data = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='static/img/uploads')
    status = models.BooleanField()
    contview = models.IntegerField()
    usuario = models.ForeignKey(User)
    categoria = models.ForeignKey('CategoriaPost', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# ----- Inicio signals ----- #
'''Aqui defino o método de notificação, recebe sender(Post),
instanciando o modelo com (INSTANCE) recuperando os dados que foram enviados'''


def enviar_notificacao(sender, instance, **kwargs):
    # Instância da classe FCMNotification com parâmetro da API
    push_service = FCMNotification(api_key="AIzaSyDXv8_47S0_g64d5sHvwZWpH98gyJDUhtc")
    # Método que passa os parâmetros de configuração do alerta do push
    # Recebe o que vem da categoria e passa para a função de envio, obs: Tiramos o uso do IF
    push_service.notify_topic_subscribers(topic_name='%s' % instance.categoria.desc,
                                            sound=True,
                                            color=None,
                                            message_body=instance.titulo,
                                            #condition=topic_condition
                                            )


# Chamando a função do signals que invoca o método para enviar a notificação
post_save.connect(enviar_notificacao, sender=Post)
# ----- Fim signals ----- #


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
