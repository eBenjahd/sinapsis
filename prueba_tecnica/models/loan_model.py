from django.db import models
from .book_model import Book

class Loan(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loan')
    borrower_name = models.CharField(max_length=100)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.book.title