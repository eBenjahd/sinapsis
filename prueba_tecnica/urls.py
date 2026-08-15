from django.urls import path
from prueba_tecnica.views import (
    BookView, 
    BookDetailView, 
    LoanBookReturnView, 
    AllLoanedBooksView,
    TopAuthorsView,
    LoanBookView
)

urlpatterns = [
    path('books/',BookView.as_view(), name='books'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/return-loan/', LoanBookReturnView.as_view(), name='book-returned'),
    path('books/<int:pk>/loan/', LoanBookView.as_view(), name='book-loan'),
    path('loaned/', AllLoanedBooksView.as_view(), name='loaned'),
    path('authors/top/', TopAuthorsView.as_view(), name='top-authors'),
] 