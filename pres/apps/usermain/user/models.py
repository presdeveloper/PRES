from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(blank=True)
	name = models.CharField(max_length=32)
	key = models.CharField(max_length=16)
	is_banned = models.BooleanField(default=False)
	has_checked_email = models.BooleanField(default=False)


class UserFollowed(models.Model):
	user_followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_followed')
	#conflito com o user_from de UserVisualization: por isso esse related_name escroto.
	user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_from_followed')
	creation = models.DateField(default=datetime.now)

class UserVisualization(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_from_visualization')
	creation = models.DateField(default=datetime.now)

