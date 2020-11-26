from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  like_contents = models.ManyToManyField('Content', blank=True, related_name='like_users')

  def __str__(self):
    return str(self.user)
    
class Content(models.Model):
  title = models.CharField(max_length=20)
  body = models.TextField()
  date = models.DateTimeField(default=timezone.now)
  writer = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
  image = models.ImageField(upload_to="images/", null=True, blank=True)

  like_count = models.PositiveIntegerField(default=0)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

  class Meta:
    ordering = ['-date',]

  def __str__(self):
    return str(self.title)

class Comment(models.Model):
  post = models.ForeignKey(Content, on_delete=models.CASCADE, null=True)
  body = models.TextField()
  date = models.DateTimeField(default=timezone.now)
  writer = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

  class Meta:
    ordering = ['-date',]

class Recomment(models.Model):
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
  body = models.TextField()
  date = models.DateTimeField(default=timezone.now)
  writer = models.ForeignKey('auth.user', on_delete=models.CASCADE, null=True)

  class Meta:
    ordering = ['-date',]