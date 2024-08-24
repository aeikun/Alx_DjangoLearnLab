# delete.md

## Deleting a Book Instance

```python
from bookshelf.models import Book
# Delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Confirm deletion
all_books = Book.objects.all()
print(all_books)  # Should show an empty list if deletion was successful
