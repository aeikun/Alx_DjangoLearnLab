# relationship_app/urls.py
from django.urls import path
from . import views
from .views import list_books
from .views import UserLoginView, UserLogoutView, UserRegisterView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
