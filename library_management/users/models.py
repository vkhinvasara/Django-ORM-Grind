from django.db import models

# Create your models here.

class User(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)
	date_of_birth = models.DateField()
	membership_status = models.BooleanField(default=False)

	def __str__(self):
		return self.id

	class Meta:
		db_table = 'users'
		verbose_name = 'User'
		verbose_name_plural = 'Users'