from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    college_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.BigIntegerField()
    message=models.TextField()