from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
	type_of = models.IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	has_read = models.BooleanField(default=False)
