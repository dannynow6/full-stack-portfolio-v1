from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from django.db.models.signals import post_save 

# Users app models 

class Profile(models.Model):
    """A profile extending Django's build in User model"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, blank=True) 
    interest = models.CharField(max_length=200, blank=True) 
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance) 
    
    @receiver(post_save, sender=User) 
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save() 
    
    def __str__(self):
        return f"{self.bio}"
