from django.db import models

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)