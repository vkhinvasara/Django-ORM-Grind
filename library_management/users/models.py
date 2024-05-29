from django.db import models

class User(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)
	date_of_birth = models.DateField()
	MEMBERSHIP_STATUS = [
		('A', 'Active'),
		('I', 'Inactive'),
	]
	membership_status = models.CharField(
		max_length=1,
		choices=MEMBERSHIP_STATUS,
		default='A',
	)

	def __str__(self):
		return self.id

	class Meta:
		db_table = 'users'
		verbose_name = 'User'
		verbose_name_plural = 'Users'