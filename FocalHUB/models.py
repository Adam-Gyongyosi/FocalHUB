import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to="images")
    upload_date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    uploader = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length = 100,blank=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)