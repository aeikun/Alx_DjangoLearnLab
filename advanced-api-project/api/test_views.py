# api/test_views.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user and a book for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.book = Book.objects.create(title='Test Book', author='Test Author', publication_year=2024)
        self.book_url = '/api/books/'
        self.book_detail_url = f'{self.book_url}{self.book.id}/'
    
    def test_create_book(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2024}
        response = self.client.post(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_retrieve_book(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Updated Book'}
        response = self.client.patch(self.book_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, 'Updated Book')

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get(self.book_url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book')

    def test_search_books(self):
        response = self.client.get(self.book_url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book')

    def test_order_books(self):
        response = self.client.get(self.book_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book')

    def test_permissions(self):
        # Test that unauthenticated users cannot create books
        data = {'title': 'Unauthorized Book', 'author': 'Unauthorized Author', 'publication_year': 2024}
        response = self.client.post(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Test that authenticated users can create books
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
