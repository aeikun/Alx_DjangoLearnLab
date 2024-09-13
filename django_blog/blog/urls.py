from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment,
    edit_comment,
    delete_comment,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # Change this line to use 'update' instead of 'edit'
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # Other paths
     path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
]
