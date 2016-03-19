from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    added_at = models.DateField(auto_now=True)
    rating = models.IntegerField()
    author = models.ManyToManyField(User)
    # likes = models.CharField(max_length=30)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
