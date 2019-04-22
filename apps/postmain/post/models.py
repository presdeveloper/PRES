from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

from apps.postmain.category.models import Category
from apps.postmain.textgenre.models import TextGenre

# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	textgenre = models.ForeignKey(TextGenre, on_delete=models.CASCADE)
	title = models.CharField(max_length=64)
	text = models.CharField(max_length=256)
	reference = models.CharField(max_length=64, blank=True)
	creation = models.DateField(default=datetime.now)
	is_banned = models.BooleanField(default=False)
	is_draft = models.BooleanField()



class PostImage(models.Model):
	image = models.ImageField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostReaction(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	value = models.IntegerField()
	creation = models.DateField(default=datetime.now)


class PostFlag(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	creation = models.DateField(default=datetime.now)


class PostVisualization(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	creation = models.DateField(default=datetime.now)
