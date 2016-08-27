from breadtimesite.models import *
from pyfcm import FCMNotification
import django.dispatch


def enviar_notificacao(sender, **kwargs):
    push_service = FCMNotification(api_key="AIzaSyDXv8_47S0_g64d5sHvwZWpH98gyJDUhtc")
    push_service.notify_topic_subscribers(topic_name="bread", message_body=kwargs['conteudo'])
