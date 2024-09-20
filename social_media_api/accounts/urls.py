from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import FollowUserView, UnfollowUserView


router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('api/accounts/', include('accounts.urls')),
    path('', include(router.urls)),
     path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
