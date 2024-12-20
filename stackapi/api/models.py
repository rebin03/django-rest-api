from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    phone = models.CharField(max_length=10, unique=True)

    
class Question(models.Model):
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='question_images', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Answer(models.Model):
    
    comment = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question_object = models.ForeignKey(Question, on_delete=models.CASCADE)
    up_vote = models.ManyToManyField(User, related_name='upvote')
    down_vote = models.ManyToManyField(User, related_name='downvote')