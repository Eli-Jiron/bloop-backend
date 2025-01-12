from django.db import models
from apps.users.models import Users


# Tabla FriendRequest
class FriendRequest(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)  # Estado: pendiente, aceptada, rechazada, etc.
    sender = models.ForeignKey(Users, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Users, related_name='received_requests', on_delete=models.CASCADE)
    sendDate = models.DateField()

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username} ({self.estado})"

# Tabla Friends
class Friends(models.Model):
    id = models.AutoField(primary_key=True)
    friend1 = models.ForeignKey(Users, related_name='friend1', on_delete=models.CASCADE)
    friend2 = models.ForeignKey(Users, related_name='friend2', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.friend1.username} <-> {self.friend2.username}"
