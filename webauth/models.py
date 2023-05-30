from django.db import models
from django.contrib import admin
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[('0','featured'), ('1','normal')])
    fram = models.CharField(max_length=50, choices=[('0','django'), ('1','flask'),('2','featured')])
    thumbnail = models.ImageField(upload_to='media')
    body = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title