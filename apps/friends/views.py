from django.views.generic.edit import CreateView
#
from .models import FriendRequest, Friends


class FriendRequestView(CreateView):
    model = FriendRequest
    fields = "__all__"

class FriendsView(CreateView):
    model = Friends
    fields = "__all__"
