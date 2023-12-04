from django.urls import path
from .views import CommentListView, CommentReplyCreateView, CommentCreateView

urlpatterns = [
    path('', CommentListView.as_view(), name='comment_list'),
    path(
        'add-comment/',
        CommentCreateView.as_view(),
        name='add_comment'
    ),
    path(
        'add-comment/<int:parent_comment_id>/',
        CommentReplyCreateView.as_view(),
        name='add_comment_reply'
    ),
]
