from django.views.generic.edit import CreateView
#
from apps.Users.models import Rol, UserRoles, Users


class RolView(CreateView):
    model = Rol
    fields = "__all__"

class UserRolesView(CreateView):
    model = UserRoles
    fields = "__all__"
    
class UsersView(CreateView):
    model = Users
    fields = "__all__"