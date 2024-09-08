# bookshelf/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Replace with your success URL
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

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

# Unsafe (potential SQL injection)
books = Book.objects.raw('SELECT * FROM bookshelf_book WHERE title = "%s"' % title)

# Safe
books = Book.objects.filter(title=title)