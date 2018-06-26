from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=100,default='')
    content = models.CharField(max_length=300,default='')
    
    def __str__(self):
        return self.title