import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print(f"Author with name {author_name} does not exist.")

# List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"Library with name {library_name} does not exist.")

# Retrieve the librarian for a library
def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library with name {library_name} does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")

# Example usage
if __name__ == "__main__":
    query_books_by_author('J.K. Rowling')
    list_books_in_library('Central Library')
    retrieve_librarian_for_library('Central Library')
