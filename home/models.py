from django.db import models
from authorization.models import User


class Record(models.Model):
    author = models.ForeignKey(User, related_name='records', on_delete=models.CASCADE)
    _file = models.FileField(upload_to = 'files/') 
    duration = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

class Assess(models.Model):
    record = models.ForeignKey(Record, related_name='assesses', on_delete=models.CASCADE)
    positive = models.IntegerField()
    negative = models.IntegerField()