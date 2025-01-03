from django.apps import AppConfig

class FriendsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Friends'
    
class ChatsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Chats'

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Users'

class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Post'
