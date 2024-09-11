# api/filters.py
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework as filters
from .models import Book

# Make `OrderingFilter` and `SearchFilter` available as `filters.OrderingFilter` and `filters.SearchFilter`
class filters:
    OrderingFilter = OrderingFilter
    SearchFilter = SearchFilter

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    publication_year = filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
