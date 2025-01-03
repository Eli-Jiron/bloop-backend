from rest_framework import serializers
from apps.Chats.models import Integrantes, Chat, Message


class IntegrantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrantes
        fields = '__all__' 

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

