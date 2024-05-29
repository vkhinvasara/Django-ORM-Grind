from django.db import models

class Books(models.Model):
	book_id = models.PositiveIntegerField(primary_key=True)
	book_name = models.CharField(max_length=100)
	author_name = models.CharField(max_length=100)
	published_date = models.DateField()
	ISBN = models.CharField(max_length=100, unique=True)
	pages = models.PositiveIntegerField()
	cover_image = models.ImageField(upload_to='covers/')

	def __str__(self) -> str:
		return self.book_id
	
	class Meta:
		db_table = 'books'
		verbose_name = 'Book'
		verbose_name_plural = 'Books'