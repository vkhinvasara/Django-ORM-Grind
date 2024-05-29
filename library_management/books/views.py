from .models import Books
from rest_framework import viewsets
from .serializers import BooksSerializer

class BooksViewSet(viewsets.ModelViewSet):
	queryset = Books.objects.all().order_by('book_id')
	serializer_class = BooksSerializer