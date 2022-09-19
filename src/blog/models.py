from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # author
    # tags
    #category
    created = models.DateTimeField(default=timezone.now)




class Category(models.Model):
    category_name = models.CharField(max_length=50)
