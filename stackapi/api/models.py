from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    
    phone = models.CharField(max_length=10, unique=True)
    

class Profile(models.Model):
    
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True, default="profiles/default.png")

    
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
    
    
def create_profile(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(owner=instance)
        
post_save.connect(create_profile, User)