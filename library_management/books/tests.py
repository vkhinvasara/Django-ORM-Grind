from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Books
from .serializers import BooksSerializer

class BookModelTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.book_data = {
			'book_id': 1,
			'book_name': 'Python Programming',
			'author_name': 'John Doe',
			'published_date': '2021-01-01',
			'ISBN': '978-3-16-148410-0',
			'pages': 300,
			'cover_image': 'covers/python.jpg'
		}

	def test_create_and_retrieve_book(self):
		""""Test the creation and retrieval of a book object."""
		response = self.client.post(
			reverse('books-list'),
			self.book_data,
			format='json'
		)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		book = Books.objects.get(book_id=1)
		serializer = BooksSerializer(book)
		self.assertEqual(response.data, serializer.data)

	def test_delete_book(self):
		""""Test the deletion of a book object."""
		book = Books.objects.get()
		response = self.client.delete(
			reverse('books-detail', kwargs={'pk': book.book_id}),
			format = 'json',
			follow = True
		)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertEqual(Books.objects.count(), 0)
	
	def test_update_book(self):
		"""Test the update of a book object."""
		book = Books.objects.get()
		new_data = {
			'book_name': 'Python Programming for Beginners'
		}
		response = self.client.patch(
			reverse('books-detail', kwargs={'pk': book.book_id}),
			new_data,
			format = 'json'
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['book_name'], 'Python Programming for Beginners')
