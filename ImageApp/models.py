from tkinter import Image
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    UserName=models.CharField(max_length=255)
    Email=models.EmailField()
    ContactNumber=models.CharField(max_length=255)
    Image=models.ImageField(default="default.jpg",blank=True,upload_to="image/", null=True)