from django.db import models

class Activity(models.Model):
    activity_title = models.CharField(max_length=50)
    activity_time = models.IntegerField(default=0)
    
    def __str__(self):
        return self.activity_title
    