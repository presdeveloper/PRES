from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=32)
	creation = models.DateField(default=datetime.now)


class CategoryFollowed(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	creation = models.DateField(default=datetime.now)

