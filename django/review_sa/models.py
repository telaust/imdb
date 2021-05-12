from django.db import models

# Create your models here.
class Sentiment(models.Model):
    sentiment = models.TextField()
    # rating = models.IntegerField()
