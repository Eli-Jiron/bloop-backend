from django.views.generic.edit import CreateView
#
from apps.Post.models import BoxComment, Post, PostImage


class BoxCommentView(CreateView):
    model = BoxComment
    fields = ['title', 'description']

class PostView(CreateView):
    model = Post
    fields = ['title', 'description']
    
class PostImageView(CreateView):
    model = PostImage
    fields = ['title', 'description']