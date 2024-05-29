from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Books

class BookViewSet(viewsets.ModelViewSet):
	queryset = Books.objects.all()
	serializer_class = BookSerializer

