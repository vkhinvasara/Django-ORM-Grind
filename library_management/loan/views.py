from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Loan
from .serializers import LoanSerializer
from books.models import Books
from users.models import User

class LoanViewSet(viewsets.ModelViewSet):
	queryset = Loan.objects.all()
	serializer_class = LoanSerializer

	def create(self, request, *args, **kwargs):
		book_id = request.data.get('book')
		user_id = request.data.get('user')
		book = Books.objects.get(id=book_id)
		user = User.objects.get(id=user_id)

		if Loan.objects.filter(book=book, user=user).exists():
			return Response({'message': 'User has already borrowed this book'}, status=status.HTTP_400_BAD_REQUEST)
		
		if book.is_borrowed:
			return Response({'message': 'Book is already borrowed'}, status=status.HTTP_400_BAD_REQUEST)
		
		book.is_borrowed = True
		book.save()
		return super().create(request, *args, **kwargs)