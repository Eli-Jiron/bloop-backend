from django.views.generic.edit import CreateView
#
from apps.Users.models import Rol, UserRoles, Users


class RolView(CreateView):
    model = Rol
    fields = ['title', 'description']

class UserRolesView(CreateView):
    model = UserRoles
    fields = ['title', 'description']
    
class UsersView(CreateView):
    model = Users
    fields = ['title', 'description']