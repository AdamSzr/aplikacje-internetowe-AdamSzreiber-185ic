from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model): # models.Model have default Id field. 
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return ' '.join([self.name,self.surname])





class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Moje-posty"

    def __str__(self):
        return self.title
