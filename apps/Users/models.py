from django.db import models

# Tabla User
class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    registered = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

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
    
    