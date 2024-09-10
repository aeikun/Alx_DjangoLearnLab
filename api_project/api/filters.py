# api/filters.py
from rest_framework.filters import OrderingFilter, SearchFilter

# Make `OrderingFilter` and `SearchFilter` available as `filters.OrderingFilter` and `filters.SearchFilter`
class filters:
    OrderingFilter = OrderingFilter
    SearchFilter = SearchFilter
