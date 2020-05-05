from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField(max_length=200,unique=True)
    message = models.CharField(max_length=500,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)