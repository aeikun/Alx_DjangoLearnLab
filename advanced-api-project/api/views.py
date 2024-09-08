from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import filters_OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, NumberFilter
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

# Define a filter set for Book model
class BookFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')  # Filter books by title
    author = CharFilter(lookup_expr='icontains')  # Filter books by author
    publication_year = NumberFilter(lookup_expr='exact')  # Filter books by publication year

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# List view for all books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, filters_OrderingFilter, SearchFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
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

# Update view for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users only

# Delete view for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users only
