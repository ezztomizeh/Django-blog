from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(default='Untitled',max_length=100)
    content = models.TextField(null=False)
    date_posted = models.DateField(default=datetime.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'