from django.views.generic.edit import CreateView
#
from .models import BoxComment, Post, PostImage


class BoxCommentView(CreateView):
    model = BoxComment
    fields = "__all__"

class PostView(CreateView):
    model = Post
    fields = "__all__"
    
class PostImageView(CreateView):
    model = PostImage
    fields = "__all__"