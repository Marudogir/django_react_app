from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=150)
    memo = models.TextField(blank=True)
    #установить текушее время
    created = models.DateTimeField(auto_now_add=True)
    completed = models.TextField(blank=True)
    #пользователь что разместил
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
