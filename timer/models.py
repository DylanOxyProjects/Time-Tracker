from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    activity_title = models.CharField(max_length=50)
    #activity_time = models.TimeField(auto_now_add=False)
    activity_time = models.CharField(max_length=50, default="0000:00:00.000")
    activity_level = models.IntegerField(default=1)
    activity_image = models.ImageField(blank=True, null=True, upload_to='documents/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.activity_title