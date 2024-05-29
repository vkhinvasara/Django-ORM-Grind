from django.db import models
from books.models import Books
from users.models import User
from datetime import datetime, timedelta

class Loan(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Books, on_delete=models.CASCADE)
	borrow_date = models.DateField(auto_now_add=True)
	due_to_return_date = models.DateField(default=datetime.now() + timedelta(days=30))
	

