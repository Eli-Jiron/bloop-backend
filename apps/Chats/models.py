from django.db import models

from apps.Users.models import Users

class Chat(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Chat #{self.id}"

# Tabla Integrantes (Integrantes del chat)
class Integrantes(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} in Chat #{self.chat.id}"

# Tabla Messages
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Message from {self.user.username} in Chat #{self.chat.id}"
