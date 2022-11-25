from django.db import models
from django import forms

# Create your models here.
class account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
