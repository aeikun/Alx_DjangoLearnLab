import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    for book in books:
        print(book.title)

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(librarian.name)

if __name__ == '__main__':
    # Example usage
    print("Books by Author 'J.K. Rowling':")
    query_books_by_author('J.K. Rowling')
    
    print("\nBooks in Library 'Central Library':")
    list_books_in_library('Central Library')
    
    print("\nLibrarian for Library 'Central Library':")
    retrieve_librarian_for_library('Central Library')
