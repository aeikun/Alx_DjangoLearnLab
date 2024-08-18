import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print(f"Author {author_name} does not exist.")

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(librarian.name)
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")
    except Librarian.DoesNotExist:
        print(f"Librarian for library {library_name} does not exist.")

if __name__ == "__main__":
    print("Books by Author 'John Doe':")
    query_books_by_author('John Doe')
    
    print("\nBooks in Library 'Central Library':")
    list_books_in_library('Central Library')
    
    print("\nLibrarian for Library 'Central Library':")
    retrieve_librarian_for_library('Central Library')
