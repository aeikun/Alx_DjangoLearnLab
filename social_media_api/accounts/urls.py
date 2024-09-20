from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import follow_user, unfollow_user


router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('api/accounts/', include('accounts.urls')),
    path('', include(router.urls)),
    # Follow a user
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    
    # Unfollow a user
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]
