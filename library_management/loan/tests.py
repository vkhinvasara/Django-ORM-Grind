from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Books, Loan, User
from django.urls import reverse

class LoanModelTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(id = 1, name='testuser', email = 'xyz@example.com', date_of_birth = '1990-01-01', membership_status = 'A')
        self.book = Books.objects.create(book_id = 1, book_name = 'testbook', author_name = 'testauthor', published_date = '2021-01-01', ISBN = '1234567890123', pages = 100, cover_image = 'covers/test.jpg', is_borrowed = False)
        self.loan = Loan.objects.create(book=self.book, user=self.user)
    
    def test_loan_creation(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'book': self.book.book_id,
            'user': self.user.id
        }
        response = self.client.post(reverse('loan-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Loan.objects.count(), 2)
        self.assertEqual(Books.objects.get(book_id=self.book.book_id).is_borrowed, True)
        new_loan = Loan.objects.get(id=response.data['id'])
        self.assertEqual(new_loan.book, self.book)
        self.assertEqual(new_loan.user, self.user)