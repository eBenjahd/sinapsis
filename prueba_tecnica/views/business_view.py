from rest_framework.generics import ListAPIView
from prueba_tecnica.serializers import BookSerializer, PopularAuthorsSerializer 
from prueba_tecnica.models import Book, Author
from django.db.models import Count


class AllLoanedBooksView(ListAPIView):

    serializer_class = BookSerializer

    def get_queryset(self):

        queryset = Book.objects.filter(loan__returned=False).distinct()
        print (queryset.query)

        # DEVUELVE TODOS LOS LIBROS QUE ESTAN ACTUALMENTE PRESTADOS
        return queryset
    

class TopAuthorsView(ListAPIView):

    TOP_AUTHORS = 3
    serializer_class = PopularAuthorsSerializer

    def get_queryset(self):

        queryset = Author.objects.annotate(
            top_authors = Count('books__loan__book_id')
            ).order_by('-top_authors')[:self.TOP_AUTHORS]

        print(queryset.query)
        return queryset