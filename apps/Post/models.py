from django.db import models
from apps.Users.models import Users

# Tabla Post
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Post by {self.user.username}"

# Tabla PostImage
class PostImage(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.URLField()  # O podría ser un campo FileField si quieres cargar imágenes

    def __str__(self):
        return f"Image for Post #{self.post.id}"

# Tabla BoxComments
class BoxComment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()

    def __str__(self):
        return self.text