from django.db import models
from django.urls import reverse

# Create your models here.
class CategoryModel(models.Model):
    category_name=models.CharField(max_length=150, unique=True)
    slug=models.SlugField(max_length=255,unique=True)
    description=models.TextField(max_length=255, blank=True)
    
    def __str__(self) -> str:
        return self.category_name
