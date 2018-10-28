from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=5)
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=300)
    prize= models.FloatField(max_length=20)
    image = models.ImageField(upload_to="products",blank=True)
    

    def __str__(self):
        return self.name