from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Content(models.Model):
  title = models.CharField(max_length=20)
  body = models.TextField()
  date = models.DateTimeField()

  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Content, on_delete=models.CASCADE, null=True)
  body = models.TextField()