from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class User(AbstractUser):

    newschoices = (
        ('politics', 'Politics'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),
        ('health', 'Health'),
        ('entertainment', 'Entertainment'),
        ('weather', 'Weather'),
        ('business', 'Business'),
    )

    user = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    choice = models.CharField(max_length=100 ,choices=newschoices, null=True,blank=True, default=None)

    REQUIRED_FIELDS = []



class NewsCategory(models.Model):
    title  = models.CharField(max_length=100)

    
    def __str__(self):
        return self.title


class News(models.Model):
   
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    image = models.ImageField(upload_to='news', blank=True, null=True )
    catergory = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)   
    source = models.CharField(max_length=100, default='ary news')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=100)



class Notification(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    news= models.ForeignKey(News, on_delete=models.CASCADE)


class Help(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)

