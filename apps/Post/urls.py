from django.urls import path
from apps.Post.views import BoxCommentView, PostImageView, PostView


urlpatterns = [
    path('', PostView.as_view(), name='post_view'),
    path('postImage/', PostImageView.as_view(), name='post_image_view'),
    path('boxComment/', BoxCommentView.as_view(), name='box_comment_view'),
]
