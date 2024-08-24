# bookshelf/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from .models import Book
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_create', raise_exception=True)
def book_list(request):
    """View to list all books."""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_delete', raise_exception=True)
def raise_exception(request):
    """View to raise a PermissionDenied exception."""
    raise PermissionDenied("You do not have permission to access this page.")

def book_list(request):
    """View to list all books."""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def raise_exception(request):
    """View to raise a PermissionDenied exception."""
    raise PermissionDenied("You do not have permission to access this page.")

def books(request):
    """Another view for handling books (can be customized as needed)."""
    return HttpResponse("This is the books view.")
