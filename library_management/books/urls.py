from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BooksViewSet

router = DefaultRouter()
router.register(r'books', BooksViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
