from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False,null=True,blank=True)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to= "images/")
    
    def __str__(self):
        return self.title
