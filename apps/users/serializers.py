from rest_framework.serializers import ModelSerializer
from utils.serializers import DynamicFieldsModelSerializer

from .models import Users


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ("username", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True},
            "displayname": {"required": False},
        }

    def create(self, validated_data):
        validated_data["displayname"] = validated_data["username"]
        password = validated_data.pop("password", None)
        user = self.Meta.model(**validated_data)

        if password is not None:
            user.set_password(password)

        user.save()
        return user


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
        }
