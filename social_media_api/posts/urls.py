from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedViewSet
from .views import UserFeedView
from .views import like_post, unlike_post, get_notifications


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('posts.urls')),
    path('feed/', FeedViewSet.as_view({'get': 'list'})),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
    path('notifications/', get_notifications, name='get-notifications'),
    path('posts/', include('posts.urls')),
    path('notifications/', include('notifications.urls')),
]
