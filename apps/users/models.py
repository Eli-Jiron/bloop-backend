import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Tabla User
class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    displayname = models.CharField(max_length=50, blank=True)
    username = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex="^[A-Za-z0-9._]+$",
                message="Username can only contain letters, numbers, dots, and underscores.",
            )
        ],
    )
    email = models.EmailField(unique=True)
    last_login = None
    first_name = None
    last_name = None
    is_superuser = None
    is_staff = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password", "username"]


# Tabla Rol
class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


# Tabla UserRoles
class UserRoles(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.rol.name}"
