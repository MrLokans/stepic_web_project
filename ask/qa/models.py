from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
try:
    User = settings.AUTH_USER_MODEL
except ImportError:
    from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    added_at = models.DateField(auto_now=True)
    rating = models.IntegerField()
    author = models.ManyToManyField(User)

    def get_url(self):
        # TODO: where the hell is ID stored?
        return reverse('question-details', kwargs={'qid': self.id})

    def __str__(self):
        return self.title
    # likes = models.CharField(max_length=30)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
