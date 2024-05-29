from django.db import models

# Create your models here.
from django.db import models

class Books(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	book_name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	published_date = models.DateField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
