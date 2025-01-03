from django.views.generic.edit import CreateView
#
from apps.Friends.models import FriendRequest, Friends


class FriendRequestView(CreateView):
    model = FriendRequest
    fields = ['title', 'description']

class FriendsView(CreateView):
    model = Friends
    fields = ['title', 'description']
