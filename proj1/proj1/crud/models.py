from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.title,self.description
