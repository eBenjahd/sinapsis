from django.db import models
from .author_model import Author

class Book(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=255, unique=True)
    published_date = models.DateField(null= True)
    copies_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.author} - {self.title}"