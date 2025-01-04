from django.views.generic.edit import CreateView
#
from apps.Friends.models import FriendRequest, Friends


class FriendRequestView(CreateView):
    model = FriendRequest
    fields = "__all__"

class FriendsView(CreateView):
    model = Friends
    fields = "__all__"
