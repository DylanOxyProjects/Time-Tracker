from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    activity_title = models.CharField(max_length=50)
    activity_time = models.TimeField(auto_now_add=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.activity_title
    