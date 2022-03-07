from django.db import models


# Create your models here.
class Topic(models.Model):
    topicName = models.CharField(max_length=100, unique=True)


class DifficultyLevel(models.Model):
    diffLevel = models.CharField(max_length=50, unique=True)


class ProblemCreation(models.Model):
    author = models.CharField(max_length=50)
    topicID = models.ForeignKey(Topic, on_delete=models.PROTECT)
    diffID = models.ForeignKey(DifficultyLevel, on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    question = models.TextField()
    answer = models.TextField()
