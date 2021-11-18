from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    gender = models.CharField(default='Пол', max_length=10, null=True)
    city = models.CharField(default='Город Проживания', max_length=255, null=True)
    dialect = models.CharField(default='Диалект', max_length=255, null=True)

    def __str__(self):
        return self.username