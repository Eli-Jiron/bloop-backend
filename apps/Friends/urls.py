from django.urls import path
from apps.Friends.views import FriendRequestView, FriendsView


urlpatterns = [
    path('', FriendsView.as_view(), name='friends'),
    path('friendRequest/', FriendRequestView.as_view(), name='friend_request'),
]

