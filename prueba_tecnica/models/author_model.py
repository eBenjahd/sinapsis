from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name