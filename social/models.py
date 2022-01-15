from django.db import models
from authentication.models import User
from django.utils.timezone import now

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=now)


class Post(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, related_name="posts")
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=now)
    comments = models.ManyToManyField(Comment, default=[])
    likes = models.ManyToManyField("authentication.User",blank=True,related_name='like')