from django.views.generic.edit import CreateView
#
from apps.Chats.models import Chat, Integrantes, Message


class ChatsView(CreateView):
    model = Chat
    fields = ['title', 'description']

class IntegrantesView(CreateView):
    model = Integrantes
    fields = ['title', 'description']

class MessageView(CreateView):
    model = Message
    fields = ['title', 'description']

