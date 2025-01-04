from django.urls import path
from apps.Chats.views import ChatsView, IntegrantesView, MessageView


urlpatterns = [
    path('', ChatsView.as_view(), name='chats'),
    path('integrantes/', IntegrantesView.as_view(), name='integrantes'),
    path('message/', MessageView.as_view(), name='message'),
]
