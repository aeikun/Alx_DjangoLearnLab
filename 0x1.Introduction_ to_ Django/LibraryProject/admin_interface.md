# Django Admin Interface Integration

## Registering the Book Model

In `bookshelf/admin.py`, the `Book` model was registered with the Django admin interface:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
