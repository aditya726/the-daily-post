from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000000)
    Dates = models.DateTimeField(default=timezone.now, blank=True)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blogImages/', null=True, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
