from django.views.generic.edit import CreateView
from django import forms
from django.shortcuts import render
from apps.Chats.models import Chat, Integrantes, Message


class ChatsView(CreateView):
    model = Chat
    fields = "__all__"
    def mi_vista(request):
        objetos = Chat.objects.all()  # Obtener todos los objetos de MiModelo
        return render(request, 'mi_template.html', {'objetos': objetos})



class IntegrantesView(CreateView):
    model = Integrantes
    fields = "__all__"

class MessageView(CreateView):
    model = Message
    fields = "__all__"

