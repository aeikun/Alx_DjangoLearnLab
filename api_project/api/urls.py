from django.contrib import admin
from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve
    path('books/new/', BookCreateView.as_view(), name='book-create'),  # Create
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-update'),  # Update
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete
]
