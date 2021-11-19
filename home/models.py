from django.db import models
from authorization.models import User
from datetime import datetime


class Text(models.Model):
    text = models.CharField(max_length=500)


class Record(models.Model):
    author = models.ForeignKey(User, related_name='records', on_delete=models.CASCADE)
    _file = models.FileField(upload_to = 'files/') 
    text = models.ForeignKey(Text, related_name='records', on_delete=True)
    duration = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now, auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.author.username

class Assess(models.Model):
    record = models.ForeignKey(Record, related_name='assesses', on_delete=models.CASCADE)
    who = models.ForeignKey(User, related_name='assesses', on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, auto_now_add=True)
