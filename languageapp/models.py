from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
