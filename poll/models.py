from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=150)
    votes = models.IntegerField(default=0)
