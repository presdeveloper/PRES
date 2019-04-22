from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

from apps.postmain.post.models import Post

# Create your models here.

class PostShare(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	creation = models.DateField(default=datetime.now)


class PostShareReaction(models.Model):
	postshare = models.ForeignKey(PostShare, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	value = models.IntegerField()
	creation = models.DateField(default=datetime.now)






