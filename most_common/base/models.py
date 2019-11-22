from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=20)
    prepop = models.CharField(max_length=1)

    def __str__(self):
        return self.word
