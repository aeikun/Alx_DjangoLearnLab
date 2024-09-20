from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedViewSet
from .views import UserFeedView


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('posts.urls')),
    path('feed/', FeedViewSet.as_view({'get': 'list'})),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
]
