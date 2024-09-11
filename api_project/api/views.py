from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, NumberFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import BasePermission
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    Read-only access is granted to any user.
    """

    def has_permission(self, request, view):
        # Allow read-only access for any user (GET, HEAD, OPTIONS requests)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Allow write access only for admin users (POST, PUT, DELETE requests)
        return request.user and request.user.is_staff
    
class IsEditorOrReadOnly(BasePermission):
    """
    Custom permission to allow only editors to edit objects.
    """

    def has_permission(self, request, view):
        # Allow read-only access for any user
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Allow write access only for users with the "editor" role
        return request.user and request.user.role == 'editor'

@api_view(['GET', 'POST'])
@permission_classes([IsAdminOrReadOnly])
def book_list(request):
    if request.method == 'GET':
        # Get book list logic here
        return Response({"message": "List of books"})
    elif request.method == 'POST':
        # Create book logic here
        return Response({"message": "Book created"})

# Define a filter set for the Book model
class BookFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')  # Filter books by title
    author = CharFilter(lookup_expr='icontains')  # Filter books by author
    publication_year = NumberFilter(lookup_expr='exact')  # Filter books by publication year

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
    permission_classes = [IsAuthenticatedOrReadOnly]

# List view for all books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, )  # Add other filters if necessary
    filterset_class = BookFilter
    search_fields = ['title', 'author']  # Ensure these fields are searchable
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users

# Detail view for a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users

# Create view for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users only

    def perform_create(self, serializer):
        # Additional custom logic before saving a book
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError("A book with this title already exists.")
        serializer.save()

# Update view for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users only

    def perform_update(self, serializer):
        # Additional custom logic before updating a book
        serializer.save()

# Delete view for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users only
