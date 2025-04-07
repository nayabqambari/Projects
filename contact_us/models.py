from django.db import models

class ContactUs(models.Model):
    message = models.CharField(max_length=1500)
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100) 
