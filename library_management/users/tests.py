from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserApiTest(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.user = User.objects.create(
			id = 1,
			name = 'Test User',
			email = 'testuser@example.com',
			date_of_birth = '1990-01-01',
			membership_status = 'A'
		)

	def test_list_users(self):
			response = self.client.get(reverse('user-list'))
			self.assertEqual(response.status_code, status.HTTP_200_OK)
			self.assertEqual(len(response.data), 1)
		
	def test_retireve_user(self):
			response = self.client.get(reverse('user-detail', args=[self.user.id]))
			self.assertEqual(response.status_code, status.HTTP_200_OK)
			self.assertEqual(response.data['name'], self.user.name)
			self.assertEqual(response.data['email'], self.user.email)
			self.assertEqual(response.data['date_of_birth'], self.user.date_of_birth)
			self.assertEqual(response.data['membership_status'], self.user.membership_status)

	def test_update_user(self):
			new_data = {"name": "Updated User"}
			response = self.client.patch(reverse('user-detail', kwargs={'pk': self.user.pk}), new_data)
			self.assertEqual(response.status_code, status.HTTP_200_OK)
			self.assertEqual(response.data['name'], 'Updated User')
	def test_delete_user(self):
				response = self.client.delete(reverse('user-detail', kwargs={'pk': self.user.pk}))
				self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
				self.assertEqual(User.objects.count(), 0)