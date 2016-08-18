from rest_framework import serializers

from breadtimesite.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('titulo', 'conteudo', 'data', 'imagem', 'status', 'contview', 'usuario', 'categoria',)
