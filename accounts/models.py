from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.

class Accounts(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=150, blank=True) 
    body = models.TextField(blank=True)
    image = models.ImageField(
    upload_to='images/', default= "../profile_kqgeo6.jpg"
    )
    # CHANGE THE DEFAULT PROFILE IMAGE

    class Meta: 
        ordering = ["-created"] 

    def __str__(self):
        return f"{self.owner}'s account"

def create_account(sender, instance, created, **kwargs):
    if created:
        Accounts.objects.create(owner=instance)

post_save.connect(create_account, sender=User)