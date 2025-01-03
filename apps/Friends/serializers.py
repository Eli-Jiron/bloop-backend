from rest_framework import serializers
from apps.Friends.models import FriendRequest, Friends


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__' 
        
class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__' 