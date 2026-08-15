from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView
from prueba_tecnica.serializers import BookSerializer, LoanSimpleSerializer
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from prueba_tecnica.models import Book, Loan
from django.utils import timezone

class BookView(ListCreateAPIView):

    serializer_class = BookSerializer

    def get_queryset(self):

        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        title = self.request.query_params.get('title')

        if author:
            queryset = queryset.filter(author=author)

        if title:
            queryset = queryset.filter(title__icontains=title)
            

        return queryset


class BookDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()


class LoanBookView(CreateAPIView):

    serializer_class = LoanSimpleSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, id=self.kwargs['pk'])

        if book.copies_available == 0:
            raise ValidationError("No hay copias disponibles para este libro.")

        book.copies_available -= 1
        book.save()

        serializer.save(book=book)


from django.db import transaction 


class LoanBookReturnView(UpdateAPIView):

    serializer_class = LoanSimpleSerializer
    queryset = Loan.objects.all()

    def perform_update(self, serializer):

        with transaction.atomic():
            loan = serializer.instance

            if loan.returned:
                raise ValidationError(
                    "Libro ya fue devuelto, no existe préstamo pendiente."
                )

            book = loan.book
            book.copies_available += 1
            book.save()

            serializer.save(returned=True)
