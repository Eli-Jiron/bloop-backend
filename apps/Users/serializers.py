from rest_framework import serializers
from apps.Users.models import Rol, UserRoles, Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        
class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

        